"""`vault restore`, per write — the two defects closed on 2026-09-09.

Both were ESCALATE items 1 and 2 of the ADR-0008 report, and both had
the same shape: `restore` knew one way to put a note back, and it was
too coarse to be used.

1. **Section-wide.** A unit write was rolled back by replacing the WHOLE
   section from `vault_writes.before`, so every sibling unit written
   after it went with it. The daily note carries `rules` (05:15) and
   `heartbeat` (every 15 min) inside one section: undoing a bad
   heartbeat write took the morning's rules block with it. A rollback
   that cannot be used on any note with two units is not a rollback.

2. **No frontmatter undo.** `upsert_region` — the one marker-less write
   path — writes into a span located by a callable. `restore` looked for
   a section MARKER, and frontmatter cannot carry one (an HTML comment
   above the opening `---` stops it being frontmatter; one inside stops
   it being YAML). 102 of the ADR-0008 sprint's writes were frontmatter,
   and a restic snapshot was their only rollback.

Same ground as `test_vaultwrite.py`: the DEV vault, the DEV database,
one rolled-back transaction per test.
"""

import os
import shutil
from pathlib import Path

import pytest

from cobalt.vaultwrite import VaultWriteError, VaultWriter, VaultWriteStore
from cobalt.vaultwrite.frontmatter import frontmatter_span

DEV_VAULT = Path.home() / "dev-vault-cobalt"
DB_NAME = "cobalt_dev"

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("COBALT_DB_USER")),
    reason="Postgres env settings not available",
)
requires_dev_vault = pytest.mark.skipif(
    not DEV_VAULT.is_dir(), reason=f"dev vault {DEV_VAULT} not present"
)

pytestmark = [requires_db, requires_dev_vault, pytest.mark.usefixtures("dev_db_tx")]

SECTION = "cobalt-status"
UNIT_A = "rules"
UNIT_B = "heartbeat"


def _purge(prefix: str) -> None:
    s = VaultWriteStore(DB_NAME)
    s.ensure_schema()
    with s._connect() as conn:
        conn.execute("DELETE FROM vault_overrides WHERE note LIKE %s", (prefix + "%",))
        conn.execute("DELETE FROM vault_writes WHERE note LIKE %s", (prefix + "%",))


@pytest.fixture
def dev_dir(request):
    path = DEV_VAULT / "_l28-tests" / request.node.name.replace("/", "_")[:80]
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)
    _purge(str(path))
    yield path
    _purge(str(path))
    shutil.rmtree(path, ignore_errors=True)


@pytest.fixture
def store():
    s = VaultWriteStore(DB_NAME)
    s.ensure_schema()
    return s


@pytest.fixture
def writer(store):
    return VaultWriter("test.restore", store=store)


# =====================================================================
# DEFECT 1 — a unit write is restored on its own
# =====================================================================


class TestAUnitRestoreLeavesItsSiblingsAlone:
    """THE CASE THAT ACTUALLY HAPPENS, reproduced: two units, one
    section, written in order. Rolling the first one back must not touch
    the second."""

    @pytest.fixture
    def note(self, writer, dev_dir):
        path = dev_dir / "2026-09-09.md"
        writer.create_if_absent(path, "# 2026-09-09\n\nHis own first line.\n")
        return path

    def test_restoring_unit_one_keeps_unit_two(self, writer, note):
        writer.upsert_unit(note, SECTION, UNIT_A, "rules v1")
        second = writer.upsert_unit(note, SECTION, UNIT_A, "rules v2")
        writer.upsert_unit(note, SECTION, UNIT_B, "beat GREEN 08:19")

        result = writer.restore(second.write_id)

        assert result.action == "restored"
        text = note.read_text()
        assert "rules v1" in text, "the rolled-back unit is back at its old body"
        assert "rules v2" not in text
        assert "beat GREEN 08:19" in text, (
            "THE DEFECT: the sibling unit was written AFTER the one being rolled "
            "back and must survive it"
        )
        assert "His own first line." in text

    def test_the_human_text_between_the_units_survives(self, writer, note):
        writer.upsert_unit(note, SECTION, UNIT_A, "rules v1")
        second = writer.upsert_unit(note, SECTION, UNIT_A, "rules v2")
        # A line he typed inside the section, outside every unit.
        text = note.read_text().replace(
            "<!-- /cobalt:unit rules -->",
            "<!-- /cobalt:unit rules -->\n\nMy note to self: watch the open.",
        )
        note.write_text(text)

        writer.restore(second.write_id)
        assert "My note to self: watch the open." in note.read_text()

    def test_the_restore_row_records_the_unit_not_the_section(self, writer, note, store):
        writer.upsert_unit(note, SECTION, UNIT_A, "rules v1")
        second = writer.upsert_unit(note, SECTION, UNIT_A, "rules v2")
        result = writer.restore(second.write_id)

        row = store.get_write(result.write_id)
        assert row["unit"] == UNIT_A
        assert row["unit_after"] == "rules v1", (
            "the restored body is the next merge's baseline — otherwise the next "
            "ordinary write merges against the version it just undid"
        )

    def test_a_write_that_CREATED_the_unit_removes_it_again(self, writer, note):
        """Restoring a create is a delete. Putting back an empty body
        would leave a Cobalt marker pair the before-state never had."""
        writer.upsert_unit(note, SECTION, UNIT_A, "rules v1")
        created = writer.upsert_unit(note, SECTION, UNIT_B, "beat GREEN")
        assert "cobalt:unit heartbeat" in note.read_text()

        writer.restore(created.write_id)

        text = note.read_text()
        assert "cobalt:unit heartbeat" not in text, "the unit it created is gone"
        assert "beat GREEN" not in text
        assert "rules v1" in text, "its sibling is untouched"
        assert f"<!-- cobalt:section {SECTION} -->" in text, "the section stays"

    def test_a_missing_unit_is_a_LOUD_refusal(self, writer, note):
        """Refusals stay loud: the unit is gone, and guessing where to
        put the text back is exactly what this module never does."""
        writer.upsert_unit(note, SECTION, UNIT_A, "rules v1")
        second = writer.upsert_unit(note, SECTION, UNIT_A, "rules v2")
        stripped = "\n".join(
            line
            for line in note.read_text().split("\n")
            if "cobalt:unit" not in line and "rules v" not in line
        )
        note.write_text(stripped)

        with pytest.raises(VaultWriteError) as exc:
            writer.restore(second.write_id)
        assert "not in section" in str(exc.value)
        assert UNIT_A in str(exc.value)

    def test_a_missing_section_is_still_a_loud_refusal(self, writer, note):
        writer.upsert_unit(note, SECTION, UNIT_A, "rules v1")
        second = writer.upsert_unit(note, SECTION, UNIT_A, "rules v2")
        note.write_text("# 2026-09-09\n\nnothing left but prose.\n")
        with pytest.raises(VaultWriteError):
            writer.restore(second.write_id)

    def test_dry_run_shows_the_diff_and_writes_nothing(self, store, note, dev_dir):
        w = VaultWriter("test.restore", store=store)
        w.upsert_unit(note, SECTION, UNIT_A, "rules v1")
        second = w.upsert_unit(note, SECTION, UNIT_A, "rules v2")
        w.upsert_unit(note, SECTION, UNIT_B, "beat GREEN")
        before = note.read_bytes()

        dry = VaultWriter("test.restore", store=store, dry_run=True)
        result = dry.restore(second.write_id)

        assert result.dry_run and result.diff
        assert "-rules v2" in result.diff and "+rules v1" in result.diff
        changed = [
            line for line in result.diff.split("\n")
            if (line.startswith("-") or line.startswith("+"))
            and not line.startswith(("---", "+++"))
        ]
        assert not any("beat GREEN" in line for line in changed), (
            f"the sibling must appear only as unchanged context, never as a "
            f"+/- line. Changed lines: {changed}"
        )
        assert note.read_bytes() == before, "a dry run writes nothing"


# =====================================================================
# DEFECT 2 — a frontmatter write can be undone
# =====================================================================


FM_SECTION = "frontmatter"
FM_REGION = "frontmatter"

ORIGINAL = """---
trade_def: example-trade
working_timeframe: 2m
status: draft
---

# The note body, every byte his.

Some prose he wrote.
"""


class TestAFrontmatterWriteCanBeUndone:
    @pytest.fixture
    def note(self, writer, dev_dir):
        path = dev_dir / "trade.md"
        writer.create_if_absent(path, ORIGINAL)
        return path

    def test_restore_puts_the_file_back_byte_for_byte(self, writer, note):
        before = note.read_bytes()

        result = writer.upsert_region(
            note,
            FM_SECTION,
            FM_REGION,
            "---\ntrade_def: example-trade\nworking_timeframe: 5m\nstatus: def\n---",
            locate=frontmatter_span,
        )
        assert result.action == "updated"
        assert b"working_timeframe: 5m" in note.read_bytes()

        restored = writer.restore(result.write_id)

        assert restored.action == "restored"
        assert note.read_bytes() == before, (
            "THE DEFECT: 102 of the sprint's writes were frontmatter and a restic "
            "snapshot was their only rollback"
        )

    def test_it_never_looked_for_a_section_marker(self, writer, note):
        """Frontmatter cannot carry one — see vaultwrite/frontmatter.py.
        This is the exact refusal that used to happen."""
        result = writer.upsert_region(
            note, FM_SECTION, FM_REGION,
            "---\ntrade_def: example-trade\nstatus: def\n---",
            locate=frontmatter_span,
        )
        assert "cobalt:section" not in note.read_text()
        writer.restore(result.write_id)  # would have raised before today

    def test_the_body_below_the_frontmatter_is_untouched(self, writer, note):
        result = writer.upsert_region(
            note, FM_SECTION, FM_REGION,
            "---\ntrade_def: example-trade\nstatus: def\n---",
            locate=frontmatter_span,
        )
        note.write_text(note.read_text() + "\nA line he added after the write.\n")
        writer.restore(result.write_id)
        text = note.read_text()
        assert "A line he added after the write." in text
        assert "Some prose he wrote." in text
        assert "status: draft" in text, "the frontmatter itself is back"

    def test_a_region_rewritten_since_is_a_LOUD_refusal(self, writer, note):
        """Zero anchors. Restoring over whatever replaced it would delete
        work nobody asked to lose."""
        result = writer.upsert_region(
            note, FM_SECTION, FM_REGION,
            "---\ntrade_def: example-trade\nstatus: def\n---",
            locate=frontmatter_span,
        )
        note.write_text(note.read_text().replace("status: def", "status: HIS OWN EDIT"))

        with pytest.raises(VaultWriteError) as exc:
            writer.restore(result.write_id)
        assert "no longer on disk as it was written" in str(exc.value)

    def test_an_ambiguous_anchor_is_a_LOUD_refusal(self, writer, dev_dir, store):
        """Two identical copies of the written text and nothing to tell
        them apart. A marker-less region has no other anchor."""
        path = dev_dir / "seat-usage.md"
        w = VaultWriter("test.restore", store=store)
        w.create_if_absent(path, "# report\n\nold one\nold two\n\nfiller\n")

        def locate(lines):
            return (2, 4)

        result = w.upsert_region(path, "cells", "cells", "AAA\nBBB", locate=locate)
        assert result.write_id is not None
        # A second, identical copy appears elsewhere in the note — now
        # the written text is not a unique anchor any more.
        path.write_text(path.read_text() + "\nAAA\nBBB\n")

        with pytest.raises(VaultWriteError) as exc:
            w.restore(result.write_id)
        assert "ambiguous" in str(exc.value)

    def test_a_non_frontmatter_region_is_restored_by_content(self, writer, dev_dir, store):
        """The seat-usage report's human cells use their own locator, not
        `frontmatter_span`. `unit_after` is the durable evidence of where
        the region was, so no registry of locators has to be kept."""
        path = dev_dir / "report.md"
        w = VaultWriter("test.restore", store=store)
        w.create_if_absent(path, "# report\n\nweekly_pct_open:\nweekly_pct_close:\n\ntail\n")

        def locate(lines):
            return (2, 4)

        result = w.upsert_region(
            path, "cells", "cells", "weekly_pct_open: 61\nweekly_pct_close: 55",
            locate=locate,
        )
        assert "weekly_pct_open: 61" in path.read_text()

        w.restore(result.write_id)
        text = path.read_text()
        assert "weekly_pct_open:\n" in text and "61" not in text
        assert "tail" in text


# =====================================================================
# The legacy path is unchanged
# =====================================================================


class TestLegacyRowsKeepTheOldBehaviour:
    """A row with no `unit`, or one written before `unit_before` was
    recorded, has nothing to locate a unit by. The honest thing to do
    with it is what was always done — replace the whole section."""

    def test_a_row_with_a_null_unit_before_restores_the_whole_section(
        self, writer, dev_dir, store
    ):
        path = dev_dir / "legacy.md"
        writer.create_if_absent(path, "# legacy\n\nprose\n")
        writer.upsert_unit(path, SECTION, UNIT_A, "rules v1")
        second = writer.upsert_unit(path, SECTION, UNIT_A, "rules v2")
        writer.upsert_unit(path, SECTION, UNIT_B, "beat GREEN")

        # Blank the column the new path keys on, exactly as a pre-2026-09
        # row would have it.
        with store._connect() as conn:
            conn.execute(
                "UPDATE vault_writes SET unit_before = NULL WHERE id = %s",
                (second.write_id,),
            )

        writer.restore(second.write_id)

        text = path.read_text()
        assert "rules v1" in text
        assert "beat GREEN" not in text, (
            "the OLD behaviour, on purpose: a row with no unit baseline can only "
            "be put back section-wide, and that is what it does"
        )
        assert "prose" in text, "everything outside the section is still untouched"


# =====================================================================
# D — a SYNC REVERT is not a human override
# =====================================================================


class TestSyncRevertIsNotAHumanOverride:
    """Today's shape, replayed.

    2026-09-09: the daily note's `heartbeat` unit was stuck on the 05:54
    GREEN block from 06:25 to 08:05. The 06:09 and 06:24 beats wrote RED;
    at 06:25:54 Obsidian Sync carried a stale copy up from another device
    and put the 05:54 text back. Every beat after that read on-disk !=
    baseline as "a human edited this", let the human win, and recorded
    overrides 30-34 — for an hour and forty minutes, and with an audit
    trail that said a person had insisted on it five times.

    A human edit is NEW text; a sync revert is OLD text coming back, and
    the difference was already in `vault_writes` and simply never
    consulted.
    """

    @pytest.fixture
    def note(self, writer, dev_dir):
        path = dev_dir / "2026-09-09.md"
        writer.create_if_absent(path, "# 2026-09-09\n\nHis own journal line.\n")
        return path

    def test_the_0909_shape_end_to_end(self, writer, note, store):
        # A = 05:54 GREEN, B = 06:09 RED, then the sync puts A back,
        # then C = the next beat.
        a = writer.upsert_unit(note, SECTION, UNIT_B, "beat GREEN 05:54")
        a_after = store.get_write(a.write_id)["unit_after"]
        writer.upsert_unit(note, SECTION, UNIT_B, "beat RED 06:09")

        # 06:25:54 — Obsidian Sync writes A's text back over B's.
        note.write_text(note.read_text().replace("beat RED 06:09", a_after))
        assert "beat GREEN 05:54" in note.read_text()

        c = writer.upsert_unit(note, SECTION, UNIT_B, "beat RED 06:39")

        row = store.get_write(c.write_id)
        assert row["sync_revert_of"] == a.write_id, (
            "the write row must name WHICH earlier write came back — the forensic "
            "question gets a row id, not a guess"
        )
        assert not c.overrides, "a sync revert is not a human override"
        assert store.overrides_for(str(note)) == [], "and no override row is written"
        assert "beat RED 06:39" in note.read_text(), (
            "THE DEFECT: Cobalt's new text must win cleanly — this is what did not "
            "happen between 06:25 and 08:05"
        )
        assert "beat GREEN 05:54" not in note.read_text()

    def test_the_result_names_the_matched_write_and_its_timestamp(
        self, writer, note, store
    ):
        a = writer.upsert_unit(note, SECTION, UNIT_B, "beat GREEN 05:54")
        a_row = store.get_write(a.write_id)
        writer.upsert_unit(note, SECTION, UNIT_B, "beat RED 06:09")
        note.write_text(note.read_text().replace("beat RED 06:09", a_row["unit_after"]))

        c = writer.upsert_unit(note, SECTION, UNIT_B, "beat RED 06:39")

        joined = " ".join(c.notes)
        assert "SYNC REVERT" in joined
        assert str(a.write_id) in joined
        assert f"{a_row['ts']:%Y-%m-%d %H:%M:%S}" in joined

    def test_a_REAL_human_edit_still_produces_an_override(self, writer, note, store):
        """The regression that matters. Recognising sync reverts must not
        cost the thing the override machinery exists for."""
        writer.upsert_unit(note, SECTION, UNIT_B, "beat GREEN 05:54")
        writer.upsert_unit(note, SECTION, UNIT_B, "beat RED 06:09")

        # Text Cobalt has never written into this unit.
        note.write_text(
            note.read_text().replace("beat RED 06:09", "I checked — this was my fault")
        )

        c = writer.upsert_unit(note, SECTION, UNIT_B, "beat RED 06:39")

        assert c.overrides, "a human edit is still an override"
        rows = store.overrides_for(str(note))
        assert rows and rows[-1]["human_text"] == "I checked — this was my fault"
        assert store.get_write(c.write_id)["sync_revert_of"] is None
        assert "I checked — this was my fault" in note.read_text(), "human wins (L28.2)"

    def test_an_ordinary_write_records_no_revert(self, writer, note, store):
        writer.upsert_unit(note, SECTION, UNIT_B, "beat GREEN 05:54")
        second = writer.upsert_unit(note, SECTION, UNIT_B, "beat RED 06:09")
        assert store.get_write(second.write_id)["sync_revert_of"] is None
        assert not second.notes or not any("SYNC REVERT" in n for n in second.notes)

    def test_the_window_is_bounded(self, writer, note, store):
        """`recent_afters` is a recognition window, not a history search.
        A body older than the window is not silently assumed to be
        Cobalt's own — it is treated as a human edit, which is the safe
        direction."""
        first = writer.upsert_unit(note, SECTION, UNIT_B, "beat v0")
        first_after = store.get_write(first.write_id)["unit_after"]
        for i in range(1, VaultWriter.SYNC_REVERT_WINDOW + 2):
            writer.upsert_unit(note, SECTION, UNIT_B, f"beat v{i}")

        note.write_text(
            note.read_text().replace(
                f"beat v{VaultWriter.SYNC_REVERT_WINDOW + 1}", first_after
            )
        )
        result = writer.upsert_unit(note, SECTION, UNIT_B, "beat vNEXT")
        assert store.get_write(result.write_id)["sync_revert_of"] is None
        assert result.overrides, "outside the window it is treated as a human edit"

    def test_recent_afters_is_newest_first_and_bounded(self, writer, note, store):
        ids = [
            writer.upsert_unit(note, SECTION, UNIT_B, f"beat v{i}").write_id
            for i in range(5)
        ]
        rows = store.recent_afters(str(note), SECTION, UNIT_B, limit=3)
        assert [r[0] for r in rows] == list(reversed(ids))[:3]
        assert rows[0][1] == "beat v4"


class TestTheRegionPathUsesTheSameHelper:
    """One helper, both write paths. The frontmatter carve-out gets the
    same protection — and it is the path where a sync revert is most
    likely, because frontmatter is what other devices' Templater runs
    rewrite."""

    def test_a_reverted_frontmatter_is_not_an_override(self, writer, dev_dir, store):
        path = dev_dir / "trade.md"
        writer.create_if_absent(path, ORIGINAL)

        a = writer.upsert_region(
            path, FM_SECTION, FM_REGION,
            "---\ntrade_def: example-trade\nstatus: def\n---",
            locate=frontmatter_span,
        )
        a_after = store.get_write(a.write_id)["unit_after"]
        writer.upsert_region(
            path, FM_SECTION, FM_REGION,
            "---\ntrade_def: example-trade\nstatus: solidified\n---",
            locate=frontmatter_span,
        )

        # The other device's copy comes back.
        path.write_text(path.read_text().replace("status: solidified", "status: def"))
        assert a_after in path.read_text()

        c = writer.upsert_region(
            path, FM_SECTION, FM_REGION,
            "---\ntrade_def: example-trade\nstatus: retired\n---",
            locate=frontmatter_span,
        )

        assert store.get_write(c.write_id)["sync_revert_of"] == a.write_id
        assert not c.overrides
        assert "status: retired" in path.read_text()
        assert any("SYNC REVERT" in n for n in c.notes)


class TestTheRollbackScriptIsNeverRunByEnsureSchema:
    """`ensure_schema()` globs `migrations/*.sql`, and 0004 is the first
    vaultwrite migration to ship a reverse script beside its forward one.
    Without the exclusion the rollback would run on every boot, next to
    the migration it undoes."""

    def test_forward_migrations_excludes_rollback_scripts(self):
        from cobalt.vaultwrite.store import forward_migrations

        names = [p.name for p in forward_migrations()]
        assert "0004_vault_writes_sync_revert.sql" in names
        assert not any(n.endswith(".rollback.sql") for n in names), names

    def test_the_reverse_script_exists_beside_its_forward_one(self):
        from cobalt.vaultwrite.store import MIGRATIONS_DIR

        assert (MIGRATIONS_DIR / "0004_vault_writes_sync_revert.rollback.sql").exists(), (
            "the DATABASE rollback domain needs its own script — same convention "
            "as db_migrations/0002_move_tables.rollback.sql"
        )

    def test_the_column_is_nullable(self, store):
        """Null is the ordinary case; every pre-existing row has it."""
        with store._connect() as conn:
            row = conn.execute(
                "SELECT is_nullable FROM information_schema.columns "
                "WHERE table_schema = 'user' AND table_name = 'vault_writes' "
                "AND column_name = 'sync_revert_of'"
            ).fetchone()
        assert row is not None, "migration 0004 has not been applied"
        assert row[0] == "YES"
