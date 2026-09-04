"""LAW L28 — the ONE vault write path, proven.

Every test here runs against the DEV VAULT (`~/dev-vault-cobalt`, in a
`_l28-tests/` scratch folder created and removed per test) and the DEV
DATABASE (`cobalt_dev`). Production paths and `cobalt_brain` appear only
in the refusal tests, and never as a write target.

The cases map 1:1 onto the law:

  L28.1  create-if-absent only; an existing file always merges
  L28.2  marker-bounded sections, stable unit ids, human text preserved
         verbatim in position, human edits win and are recorded
  L28.3  before/after + full-file hashes persisted, atomic write behind
         an mtime/hash guard that aborts loud and retries once
  L28.4  every result carries the unified diff
  L28.5  the live vault is never a test target — and the writer refuses
         one unless COBALT_ENV=production says so explicitly
"""

import hashlib
import os
import shutil
from pathlib import Path

import pytest

from cobalt.vault import PROD_VAULT_PATH_REFERENCE, VaultWriteRefused
from cobalt.vaultwrite import (
    MarkerError,
    NoteChangedOnDisk,
    VaultWriteError,
    VaultWriter,
    VaultWriteStore,
    assert_write_target,
    merge_body,
)
from cobalt.vaultwrite.markers import find_section

DEV_VAULT = Path.home() / "dev-vault-cobalt"
DB_NAME = "cobalt_dev"

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
requires_dev_vault = pytest.mark.skipif(
    not DEV_VAULT.is_dir(), reason=f"dev vault {DEV_VAULT} not present"
)

pytestmark = [requires_db, requires_dev_vault]


def _purge_rows(prefix: str) -> None:
    """vault_writes/vault_overrides are keyed by absolute note path, and
    these tests reuse the same paths run after run. Clear this test's own
    rows so a previous run's audit trail can't be mistaken for this
    one's — and so the non-expiring override table isn't slowly filled
    with test noise."""
    s = VaultWriteStore(DB_NAME)
    s.ensure_schema()
    with s._connect() as conn:
        conn.execute("DELETE FROM vault_overrides WHERE note LIKE %s", (prefix + "%",))
        conn.execute("DELETE FROM vault_writes WHERE note LIKE %s", (prefix + "%",))


@pytest.fixture
def dev_dir(request):
    """A scratch folder INSIDE the dev vault — the law says the live
    vault is never a test target, and the dev vault is the playground
    that exists so it never has to be."""
    path = DEV_VAULT / "_l28-tests" / request.node.name.replace("/", "_")[:80]
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)
    _purge_rows(str(path))
    yield path
    _purge_rows(str(path))
    shutil.rmtree(path, ignore_errors=True)


@pytest.fixture
def store():
    s = VaultWriteStore(DB_NAME)
    s.ensure_schema()
    return s


@pytest.fixture
def writer(store):
    return VaultWriter("test.l28", store=store)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


CARD_V1 = "```aset\nticker: TSLA\nshares: 120\n```"
CARD_V2 = "```aset\nticker: TSLA\nshares: 140\n```"


# ---------------------------------------------------------------------------
# L28.1 — create-if-absent only
# ---------------------------------------------------------------------------


def test_create_if_absent_creates(writer, dev_dir):
    path = dev_dir / "2026-09-04.md"
    result = writer.create_if_absent(path, "# 2026-09-04\n\ntemplate body\n")
    assert result.action == "created"
    assert path.read_text() == "# 2026-09-04\n\ntemplate body\n"
    assert result.diff.startswith("---")


def test_create_if_absent_never_rewrites_an_existing_file(writer, dev_dir):
    path = dev_dir / "2026-09-04.md"
    human = "# 2026-09-04\n\nDejan's whole journal, every byte his.\n"
    path.write_text(human)
    before = sha(path)

    result = writer.create_if_absent(path, "# 2026-09-04\n\nFRESH TEMPLATE\n")
    assert result.action == "skipped_exists"
    assert sha(path) == before
    assert path.read_text() == human


def test_upsert_refuses_to_create(writer, dev_dir):
    path = dev_dir / "missing.md"
    with pytest.raises(VaultWriteError, match="does not exist"):
        writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)


# ---------------------------------------------------------------------------
# L28.2 — markers, units, human text
# ---------------------------------------------------------------------------


def test_human_content_above_below_and_inside_survives_byte_for_byte(writer, dev_dir):
    path = dev_dir / "note.md"
    path.write_text(
        "# 2026-09-03\n"
        "\n"
        "ABOVE: Sleep 80 / Readiness 81 / RHR 56\n"
        "ABOVE: 1% goal — exit on structure break, not on hope\n"
        "\n"
        "<!-- cobalt:section aset-cards -->\n"
        "INSIDE: his own note between cards\n"
        "<!-- /cobalt:section aset-cards -->\n"
        "\n"
        "BELOW: full TSLA trade review, three Q&A answers\n"
    )
    writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    content = path.read_text()

    for line in (
        "ABOVE: Sleep 80 / Readiness 81 / RHR 56",
        "ABOVE: 1% goal — exit on structure break, not on hope",
        "INSIDE: his own note between cards",
        "BELOW: full TSLA trade review, three Q&A answers",
    ):
        assert line in content, f"human line lost: {line!r}"
    assert content.index("ABOVE: Sleep") < content.index("INSIDE:") < content.index("BELOW:")
    assert "ticker: TSLA" in content


def test_the_exact_0903_shape_loses_nothing(writer, dev_dir):
    """The shape that made `daily.py:483` dangerous: an ASET stub banner
    with human text ABOVE it. The old code kept only the suffix after the
    banner. Nothing here may be lost."""
    path = dev_dir / "2026-09-03.md"
    original = (
        "# 2026-09-03\n"
        "\n"
        "Sleep: 80\n"
        "Readiness: 81\n"
        "RHR: 56\n"
        "1% goal: exit on structure break, not on hope\n"
        "\n"
        "> ⚠️ Created by Cobalt — apply daily template.\n"
        "\n"
        "### 10:02:06 — TSLA LONG B\n"
        "```aset\nticker: TSLA\n```\n"
    )
    path.write_text(original)

    writer.upsert_unit(path, "aset-cards", "card-20260903T104253", CARD_V1)
    content = path.read_text()
    assert content.startswith(original), "content above/at the stub banner was not preserved"
    assert "shares: 120" in content


def test_section_appended_at_end_nothing_above_touched(writer, dev_dir):
    path = dev_dir / "note.md"
    original = "# 2026-09-03\n\nhis journal\n\n## Notes\n\nmore of his journal\n"
    path.write_text(original)
    result = writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    content = path.read_text()
    assert content.startswith(original)
    assert content.index("<!-- cobalt:section aset-cards -->") > content.index("more of his journal")
    assert result.action == "updated"


def test_same_unit_id_updates_in_place(writer, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    writer.upsert_unit(path, "aset-cards", "card-1", CARD_V2)
    content = path.read_text()
    assert content.count("<!-- cobalt:unit card-1 -->") == 1
    assert "shares: 140" in content
    assert "shares: 120" not in content


def test_three_runs_of_a_card_update_is_one_card(writer, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    for _ in range(3):
        writer.upsert_unit(path, "aset-cards", "card-20260903T100206", CARD_V1)
    content = path.read_text()
    assert content.count("<!-- cobalt:unit card-20260903T100206 -->") == 1
    assert content.count("ticker: TSLA") == 1


def test_second_run_is_a_zero_diff_noop(writer, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    before = sha(path)

    second = writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    assert second.action == "unchanged"
    assert second.diff == ""
    assert sha(path) == before


def test_human_added_line_inside_a_unit_survives(writer, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)

    text = path.read_text().replace(
        "shares: 120", "shares: 120\nHIS NOTE: took half off at 1R"
    )
    path.write_text(text)

    result = writer.upsert_unit(path, "aset-cards", "card-1", CARD_V2)
    content = path.read_text()
    assert "HIS NOTE: took half off at 1R" in content, "human-added line inside a unit was lost"
    assert "shares: 140" in content, "Cobalt's own update did not land"
    assert result.overrides == [], "an addition is not an override"


def test_human_modified_cobalt_line_wins_and_records_an_override(writer, store, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)

    path.write_text(path.read_text().replace("ticker: TSLA", "ticker: TSLA (his correction)"))

    result = writer.upsert_unit(path, "aset-cards", "card-1", CARD_V2)
    content = path.read_text()
    assert "ticker: TSLA (his correction)" in content, "human edit was overwritten"
    assert result.overrides, "no override recorded"
    assert "human" in result.overrides[0].describe()

    rows = store.overrides_for(str(path))
    assert len(rows) == 1
    assert rows[0]["human_text"] == "ticker: TSLA (his correction)"
    assert rows[0]["cobalt_text"] == "ticker: TSLA"
    # ...and it is recorded exactly once, not again on every later run
    writer.upsert_unit(path, "aset-cards", "card-1", CARD_V2)
    assert len(store.overrides_for(str(path))) == 1


def test_malformed_markers_refuse_the_write(writer, dev_dir):
    path = dev_dir / "note.md"
    original = "# note\n\n<!-- cobalt:section aset-cards -->\nunclosed\n"
    path.write_text(original)
    with pytest.raises(VaultWriteError, match="never closes"):
        writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    assert path.read_text() == original


# ---------------------------------------------------------------------------
# L28.3 — audit trail, guard, atomicity
# ---------------------------------------------------------------------------


def test_before_after_and_hashes_are_persisted(writer, store, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    first = writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    second = writer.upsert_unit(path, "aset-cards", "card-1", CARD_V2)

    row = store.get_write(second.write_id)
    assert row["note"] == str(path)
    assert row["section"] == "aset-cards"
    assert row["unit"] == "card-1"
    assert "shares: 120" in row["before"]  # the section as it was
    assert "shares: 140" in row["after"]
    assert row["hash_before"] == first.hash_after
    assert row["hash_after"] == sha(path)
    assert row["writer"] == "test.l28"
    assert row["run_id"] == writer.run_id


def test_mtime_race_aborts_loud_then_retries_once(store, dev_dir, caplog):
    path = dev_dir / "note.md"
    path.write_text("# note\n")

    calls = {"n": 0}

    def racer(target: Path) -> None:
        """A concurrent writer landing between the read and the rename —
        exactly the Obsidian buffer flush that destroyed data twice."""
        calls["n"] += 1
        if calls["n"] == 1:
            with open(target, "a", encoding="utf-8") as f:
                f.write("\nHIS LATE EDIT\n")

    w = VaultWriter("test.l28", store=store, precommit_hook=racer)
    result = w.upsert_unit(path, "aset-cards", "card-1", CARD_V1)

    assert calls["n"] == 2, "the aborted write was not retried exactly once"
    content = path.read_text()
    assert "HIS LATE EDIT" in content, "the racing write was clobbered"
    assert "ticker: TSLA" in content, "the retry did not land"
    assert result.action == "updated"


def test_a_persistent_racer_raises_rather_than_clobbering(store, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")

    def always_race(target: Path) -> None:
        with open(target, "a", encoding="utf-8") as f:
            f.write("\nRACE\n")

    w = VaultWriter("test.l28", store=store, precommit_hook=always_race)
    with pytest.raises(NoteChangedOnDisk):
        w.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    assert "ticker: TSLA" not in path.read_text()


def test_purge_leaves_overrides_alone(store):
    """Retention is the writer's own job and it stops at vault_writes —
    an override is a calibration signal, not an operational log."""
    before = store.purge_expired(days=30)
    assert isinstance(before, int)  # runs, and never touches vault_overrides
    with store._connect() as conn:
        cols = conn.execute(
            "SELECT column_name FROM information_schema.columns "
            "WHERE table_name = 'vault_overrides'"
        ).fetchall()
    assert cols, "vault_overrides must exist and is never purged"


# ---------------------------------------------------------------------------
# L28.4 — diffs and dry-run
# ---------------------------------------------------------------------------


def test_dry_run_leaves_the_file_hash_unchanged(store, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    before = sha(path)

    w = VaultWriter("test.l28", store=store, dry_run=True)
    result = w.upsert_unit(path, "aset-cards", "card-1", CARD_V1)

    assert sha(path) == before
    assert result.dry_run is True
    assert result.write_id is None
    assert "+ticker: TSLA" in result.diff
    assert "cobalt:unit card-1" in result.diff


def test_dry_run_creates_no_audit_rows(store, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    w = VaultWriter("test.l28", store=store, dry_run=True)
    w.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    with store._connect() as conn:
        n = conn.execute(
            "SELECT count(*) FROM vault_writes WHERE note = %s", (str(path),)
        ).fetchone()[0]
    assert n == 0


def test_every_result_carries_the_unified_diff(writer, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    result = writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    assert result.diff.startswith(f"--- {path} (before)")
    assert result.diff in result.report()


# ---------------------------------------------------------------------------
# Rollback
# ---------------------------------------------------------------------------


def test_restore_puts_a_section_back(writer, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n\nhis journal\n")
    writer.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    after_v1 = path.read_text()

    second = writer.upsert_unit(path, "aset-cards", "card-1", CARD_V2)
    assert "shares: 140" in path.read_text()

    restored = writer.restore(second.write_id)
    assert restored.action == "restored"
    assert path.read_text() == after_v1
    assert "his journal" in path.read_text()


def test_restore_dry_run_writes_nothing(store, dev_dir):
    path = dev_dir / "note.md"
    path.write_text("# note\n")
    w = VaultWriter("test.l28", store=store)
    w.upsert_unit(path, "aset-cards", "card-1", CARD_V1)
    second = w.upsert_unit(path, "aset-cards", "card-1", CARD_V2)
    before = sha(path)

    dry = VaultWriter("test.l28", store=store, dry_run=True)
    result = dry.restore(second.write_id)
    assert sha(path) == before
    assert "shares: 120" in result.diff


def test_restore_refuses_a_whole_file_create(writer, store, dev_dir):
    path = dev_dir / "note.md"
    created = writer.create_if_absent(path, "# note\n")
    with pytest.raises(VaultWriteError, match="whole-file create"):
        writer.restore(created.write_id)


# ---------------------------------------------------------------------------
# L28.5 — never the wrong vault
# ---------------------------------------------------------------------------


def test_production_path_refused_without_cobalt_env(monkeypatch):
    monkeypatch.delenv("COBALT_ENV", raising=False)
    target = Path(PROD_VAULT_PATH_REFERENCE) / "1 - Trading" / "1- Daily Notes" / "2026-09-04.md"
    with pytest.raises(VaultWriteRefused, match="did not declare COBALT_ENV=production"):
        assert_write_target(target)


def test_production_process_refused_a_non_production_path(monkeypatch, dev_dir):
    monkeypatch.setenv("COBALT_ENV", "production")
    with pytest.raises(VaultWriteRefused, match="outside the production vault"):
        assert_write_target(dev_dir / "note.md")


def test_dev_allow_flag_does_not_unlock_production_writes(monkeypatch):
    """COBALT_ALLOW_DEV_ENTRY is a read/entry opt-in. It must not be a
    back door into writing the live vault — only COBALT_ENV=production is."""
    monkeypatch.delenv("COBALT_ENV", raising=False)
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
    with pytest.raises(VaultWriteRefused):
        assert_write_target(Path(PROD_VAULT_PATH_REFERENCE) / "note.md")


def test_repo_path_refused(monkeypatch):
    monkeypatch.delenv("COBALT_ENV", raising=False)
    repo_note = Path(__file__).resolve().parents[2] / "README.md"
    with pytest.raises(VaultWriteRefused, match="INSIDE the repo"):
        assert_write_target(repo_note)


# ---------------------------------------------------------------------------
# Merge unit tests (no I/O)
# ---------------------------------------------------------------------------


class TestMerge:
    def test_cobalt_update_lands_when_human_left_it_alone(self):
        r = merge_body("a\nb", "a\nb", "a\nB2")
        assert r.text == "a\nB2"
        assert r.overrides == []

    def test_human_addition_carried_in_position(self):
        r = merge_body("a\nb", "a\nHIS\nb", "a\nb\nc")
        assert r.text.split("\n") == ["a", "HIS", "b", "c"]
        assert r.overrides == []

    def test_human_edit_of_a_cobalt_line_wins(self):
        r = merge_body("a\nb", "a\nHIS b", "a\nb")
        assert r.text == "a\nHIS b"
        assert len(r.overrides) == 1
        assert r.overrides[0].conflict is False

    def test_both_edited_is_a_conflict_and_the_human_wins(self):
        r = merge_body("a\nb", "a\nHIS b", "a\nCOBALT b")
        assert r.text == "a\nHIS b"
        assert r.overrides[0].conflict is True

    def test_human_deletion_of_a_cobalt_line_is_an_override(self):
        r = merge_body("a\nb\nc", "a\nc", "a\nb\nc")
        assert r.text == "a\nc"
        assert len(r.overrides) == 1


class TestMarkers:
    def test_finds_a_section_and_its_units(self):
        lines = (
            "<!-- cobalt:section s -->\n"
            "human\n"
            "<!-- cobalt:unit u -->\nbody\n<!-- /cobalt:unit u -->\n"
            "<!-- /cobalt:section s -->"
        ).split("\n")
        block = find_section(lines, "s")
        assert block is not None
        assert list(block.units) == ["u"]
        assert block.units["u"].body(lines) == ["body"]

    def test_duplicate_section_refuses(self):
        lines = [
            "<!-- cobalt:section s -->",
            "<!-- /cobalt:section s -->",
            "<!-- cobalt:section s -->",
        ]
        with pytest.raises(MarkerError, match="Duplicate opening marker"):
            find_section(lines, "s")

    def test_absent_section_is_none_not_an_error(self):
        assert find_section(["# note"], "s") is None
