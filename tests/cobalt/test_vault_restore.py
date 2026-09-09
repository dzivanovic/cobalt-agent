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
