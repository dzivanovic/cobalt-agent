"""S2-P2 STEP-9 — taxonomy v0.8: the `catalyst` standard, the ONE review
file, and the batch apply bound by sha256 (ruling R10; Astra R1-17).

Every vault here is a throwaway `make_vault` built from the shipped
synthetic example note; the real vault is never read. Writes go through
the real `VaultWriter` merge path with an in-memory audit store.
"""

from __future__ import annotations

import hashlib
import os
from contextlib import contextmanager
from datetime import UTC, date, datetime
from pathlib import Path

import pytest

from cobalt.session.models import Session
from cobalt.taxonomy import catalyst as cat
from cobalt.taxonomy import trade_def as td_module
from cobalt.taxonomy.factor_lines import FactorLinesError, factor_block
from cobalt.taxonomy.trade_def import TradeDef, schema_gate
from cobalt.taxonomy.vault_loader import load_vault_trade_defs
from cobalt.vaultwrite import VaultWriter
from taxonomy_example import (
    EXAMPLE_NAME,
    EXAMPLE_SLUG,
    example_def_mapping,
    example_def_yaml,
    example_note_text,
    example_tunables_yaml,
    render_note,
)

TODAY = date(2026, 9, 16)
PROBE_SLUG = "example-catalyst-probe"
PROBE_NAME = "Example Catalyst Probe"
DRAFT_SLUG = "example-draft"


class MemoryWriteStore:
    def __init__(self):
        self.rows = []

    def purge_expired(self):
        return 0

    def last_after(self, note, section, unit):
        for row in reversed(self.rows):
            if (row["note"], row["section"], row["unit"]) == (note, section, unit):
                return row["unit_after"]
        return None

    def recent_afters(self, note, section, unit, limit=10):
        return [
            (i, row["unit_after"]) for i, row in reversed(list(enumerate(self.rows, start=1)))
            if (row["note"], row["section"], row["unit"]) == (note, section, unit)
        ][:limit]

    @contextmanager
    def pending_write(self, **row):
        self.rows.append(row)
        try:
            yield len(self.rows)
        except BaseException:
            self.rows.pop()
            raise


class OpenClock:
    def session(self, _now):
        return Session.RTH


@pytest.fixture
def writer(monkeypatch):
    monkeypatch.setenv("COBALT_ENV", "dev")  # RULING 7: declared, never inferred
    monkeypatch.setattr(VaultWriter, "_annotate_sync", lambda _self, _result: None)
    return VaultWriter("test.taxonomy.catalyst", store=MemoryWriteStore(), clock=OpenClock(),
                       now=lambda: datetime(2026, 9, 16, 22, 0, tzinfo=UTC))


def _probe_note() -> str:
    mapping = example_def_mapping()
    factors = list(mapping["quality_factors"])
    factors[1:1] = ["catalyst_grade", {"name": "catalyst_class", "source": "human", "tier": "judgment"}]
    return render_note(
        PROBE_SLUG, PROBE_NAME,
        def_yaml=example_def_yaml(slug=PROBE_SLUG, quality_factors=factors),
        tunables_yaml=example_tunables_yaml(PROBE_SLUG),
    )


@pytest.fixture
def vault(make_vault):
    return make_vault({
        EXAMPLE_NAME: example_note_text(),
        PROBE_NAME: _probe_note(),
        "Example Draft": render_note(DRAFT_SLUG, "Example Draft", def_yaml=None, status="draft"),
    })


def _note_bytes(vault: Path) -> dict[str, bytes]:
    return {p.name: p.read_bytes() for p in sorted((vault / "1 - Trading/4 - Strategies").glob("*.md"))}


def _review_file(tmp_path, vault, *, marks: dict[str, str] | None = None) -> tuple[Path, str]:
    review = cat.draft_review(vault, today=TODAY)
    text = cat.render_review(review)
    for slug, decision in (marks or {}).items():
        lines = text.split("\n")
        for i, line in enumerate(lines):
            if line.startswith("| ") and f"| {slug} |" in line:
                cells = line.split(" | ")
                cells[-1] = f"{decision} |"
                lines[i] = " | ".join(cells)
        text = "\n".join(lines)
    path = tmp_path / "catalyst-review.md"
    path.write_text(text, encoding="utf-8")
    return path, hashlib.sha256(path.read_bytes()).hexdigest()


# ---------------------------------------------------------------------
# the schema gate
# ---------------------------------------------------------------------


def test_schema_is_0_5_and_the_loader_gate_stays_0_4():
    assert td_module.SCHEMA_VERSION == "0.5"
    assert td_module.LOADER_SCHEMA_GATE == "0.4"
    assert td_module.active_schema() == "0.4"
    # a def without `catalyst` still loads under the gate
    TradeDef.from_unit(example_def_mapping(), slug=EXAMPLE_SLUG, name=EXAMPLE_NAME)


def test_at_0_5_a_def_without_catalyst_fails_loud(monkeypatch):
    with schema_gate("0.5"), pytest.raises(ValueError, match="catalyst"):
        TradeDef.from_unit(example_def_mapping(), slug=EXAMPLE_SLUG, name=EXAMPLE_NAME)
    monkeypatch.setattr(td_module, "LOADER_SCHEMA_GATE", "0.5")
    with pytest.raises(ValueError, match="missing standard factors at schema 0.5"):
        TradeDef.from_unit(example_def_mapping(), slug=EXAMPLE_SLUG, name=EXAMPLE_NAME)
    mapping = example_def_mapping()
    mapping["quality_factors"].append("catalyst")
    assert "catalyst" in TradeDef.from_unit(mapping, slug=EXAMPLE_SLUG, name=EXAMPLE_NAME).quality_factor_names


def test_the_override_is_scoped_and_an_unknown_schema_is_refused():
    with schema_gate("0.5"):
        assert td_module.active_schema() == "0.5"
    assert td_module.active_schema() == "0.4"
    with pytest.raises(ValueError, match="unknown taxonomy schema"), schema_gate("0.9"):
        pass


# ---------------------------------------------------------------------
# the one review file
# ---------------------------------------------------------------------


def test_review_file_lists_every_defined_note_with_its_existing_catalyst_factors(vault):
    review = cat.draft_review(vault, today=TODAY)
    rows = {r.slug: r for r in review.rows}
    assert set(rows) == {EXAMPLE_SLUG, PROBE_SLUG}  # the draft is not a defined note
    assert rows[PROBE_SLUG].existing == ["catalyst_grade", "catalyst_class"]
    assert rows[EXAMPLE_SLUG].existing == []
    assert all(r.proposed == "- catalyst" and r.drop == [] for r in rows.values())
    text = cat.render_review(review)
    assert text.count(cat.REVIEW_OPEN) == 1 and text.count(cat.REVIEW_CLOSE) == 1
    for row in rows.values():
        assert row.note_path in text and row.unit_sha256 in text
    assert "keep" in text and "drop" in text  # the instructions name both marks


def test_review_round_trips_and_parses_the_three_marks(tmp_path, vault):
    path, _ = _review_file(tmp_path, vault)
    assert cat.parse_review(path.read_text()) == cat.draft_review(vault, today=TODAY)
    for mark, expected in (("drop", ["catalyst_grade", "catalyst_class"]), ("drop: catalyst_class", ["catalyst_class"]),
                           ("keep", [])):
        marked, _ = _review_file(tmp_path, vault, marks={PROBE_SLUG: mark})
        rows = {r.slug: r for r in cat.parse_review(marked.read_text()).rows}
        assert rows[PROBE_SLUG].drop == expected


@pytest.mark.parametrize("mark", ["drop: catalyst_nope", "remove", "drop:"])
def test_a_bad_mark_is_refused(tmp_path, vault, mark):
    path, _ = _review_file(tmp_path, vault, marks={PROBE_SLUG: mark})
    with pytest.raises(cat.CatalystReviewError):
        cat.parse_review(path.read_text())


def test_the_review_command_refuses_to_overwrite_an_existing_file(tmp_path, vault):
    out = tmp_path / "review.md"
    cat.write_review(vault, out, today=TODAY)
    with pytest.raises(cat.CatalystReviewError, match="exists"):
        cat.write_review(vault, out, today=TODAY)


# ---------------------------------------------------------------------
# the batch apply
# ---------------------------------------------------------------------


def test_batch_apply_refuses_on_sha_mismatch_and_writes_nothing(tmp_path, vault, writer):
    path, digest = _review_file(tmp_path, vault)
    before = _note_bytes(vault)
    with pytest.raises(cat.CatalystReviewError, match="sha256"):
        cat.apply_review(vault, path, expected_sha256="0" * 64, writer=writer)
    path.write_text(path.read_text() + "\n")  # the reviewed bytes changed after hashing
    with pytest.raises(cat.CatalystReviewError, match="sha256"):
        cat.apply_review(vault, path, expected_sha256=digest, writer=writer)
    assert _note_bytes(vault) == before


def test_apply_adds_catalyst_everywhere_drops_only_marked_and_rereads_valid_at_0_5(tmp_path, vault, writer):
    path, digest = _review_file(tmp_path, vault, marks={PROBE_SLUG: "drop: catalyst_class"})
    report = cat.apply_review(vault, path, expected_sha256=digest, writer=writer)
    assert sorted(report.written) == sorted([EXAMPLE_SLUG, PROBE_SLUG]) and report.already_applied == []
    assert report.gate_ready and all(r.diff for r in report.results)
    defs = {d.slug: d.definition for d in load_vault_trade_defs(vault_root=vault).defs}
    assert "catalyst" in defs[EXAMPLE_SLUG].quality_factor_names
    probe = defs[PROBE_SLUG].quality_factor_names
    assert "catalyst" in probe and "catalyst_grade" in probe and "catalyst_class" not in probe
    with schema_gate("0.5"):
        load_vault_trade_defs(vault_root=vault)


def test_apply_never_removes_an_unmarked_catalyst_factor(tmp_path, vault, writer):
    path, digest = _review_file(tmp_path, vault)  # every row left at `keep`
    cat.apply_review(vault, path, expected_sha256=digest, writer=writer)
    probe = {d.slug: d for d in load_vault_trade_defs(vault_root=vault).defs}[PROBE_SLUG]
    assert {"catalyst_grade", "catalyst_class", "catalyst"} <= set(probe.definition.quality_factor_names)


def test_every_other_byte_of_the_note_is_untouched(tmp_path, vault, writer):
    note = vault / "1 - Trading/4 - Strategies" / f"{EXAMPLE_NAME}.md"
    before = note.read_text().split("\n")
    path, digest = _review_file(tmp_path, vault)
    cat.apply_review(vault, path, expected_sha256=digest, writer=writer)
    after = note.read_text().split("\n")
    added = [line for line in after if line not in before]
    assert added == ["    - catalyst"]
    assert [line for line in after if line != "    - catalyst"] == before


def test_a_unit_that_drifted_since_the_review_refuses_the_whole_batch_before_any_write(tmp_path, vault, writer):
    path, digest = _review_file(tmp_path, vault)
    note = vault / "1 - Trading/4 - Strategies" / f"{PROBE_NAME}.md"
    note.write_text(note.read_text().replace("- range_duration", "- range_duration  # his edit"))
    before = _note_bytes(vault)
    with pytest.raises(cat.CatalystReviewError, match="drifted"):
        cat.apply_review(vault, path, expected_sha256=digest, writer=writer)
    assert _note_bytes(vault) == before


def test_an_interrupted_batch_resumes_and_keeps_what_was_applied(tmp_path, vault, writer, monkeypatch):
    path, digest = _review_file(tmp_path, vault)
    real = writer.upsert_unit
    calls = []

    def dies_second(*args, **kwargs):
        calls.append(args[2])
        if len(calls) == 2:
            raise RuntimeError("process killed mid-batch")
        return real(*args, **kwargs)

    monkeypatch.setattr(writer, "upsert_unit", dies_second)
    with pytest.raises(cat.CatalystReviewError, match="applied so far") as info:
        cat.apply_review(vault, path, expected_sha256=digest, writer=writer)
    assert "1 of 2" in str(info.value)
    monkeypatch.setattr(writer, "upsert_unit", real)
    report = cat.apply_review(vault, path, expected_sha256=digest, writer=writer)
    assert len(report.already_applied) == 1 and len(report.written) == 1 and report.gate_ready
    again = cat.apply_review(vault, path, expected_sha256=digest, writer=writer)
    assert again.written == [] and len(again.already_applied) == 2 and again.gate_ready


def test_a_human_edit_mid_batch_stops_the_batch_loudly(tmp_path, vault, writer, monkeypatch):
    path, digest = _review_file(tmp_path, vault)
    notes = sorted((vault / "1 - Trading/4 - Strategies").glob("Example [CR]*.md"))
    real = writer.upsert_unit
    written = []

    def write_then_he_types(note_path, *args, **kwargs):
        result = real(note_path, *args, **kwargs)
        written.append(Path(note_path))
        for other in notes:
            if other not in written:
                other.write_text(other.read_text().replace("- range_duration", "- range_duration  # typed mid-batch"))
        return result

    monkeypatch.setattr(writer, "upsert_unit", write_then_he_types)
    with pytest.raises(cat.CatalystReviewError, match="drifted.*applied so far: 1 of 2"):
        cat.apply_review(vault, path, expected_sha256=digest, writer=writer)
    untouched = next(n for n in notes if n not in written)
    assert "# typed mid-batch" in untouched.read_text() and "- catalyst\n" not in untouched.read_text()
    assert "- catalyst" in written[0].read_text()


def test_a_note_defined_after_the_review_refuses_the_batch(tmp_path, make_vault, vault, writer):
    path, digest = _review_file(tmp_path, vault)
    extra = render_note("example-late", "Example Late", def_yaml=example_def_yaml(slug="example-late"),
                        tunables_yaml=example_tunables_yaml("example-late"))
    make_vault({"Example Late": extra}, root=vault)
    with pytest.raises(cat.CatalystReviewError, match="example-late"):
        cat.apply_review(vault, path, expected_sha256=digest, writer=writer)


def test_default_review_path_is_under_inflight_and_gitignored():
    """The review carries note paths and factor names (user data, L32) — its
    default landing spot must be the gitignored `docs/_inflight` folder, not
    a committed DevDocs path. Desk ruling, S2-P2 chunk C ESCALATE 3."""
    import subprocess

    from cobalt.vault import REPO_ROOT

    path = cat.default_review_path(date(2026, 9, 16))
    assert path == REPO_ROOT / "docs" / "_inflight" / "catalyst-review-2026-09-16.md"
    result = subprocess.run(["git", "check-ignore", "-q", str(path)], cwd=REPO_ROOT)
    assert result.returncode == 0, "docs/_inflight/*.md must be gitignored (PLACEMENT.md's _inflight rule)"


def test_dry_run_writes_nothing_and_says_the_gate_is_unproven(tmp_path, vault, monkeypatch):
    monkeypatch.setenv("COBALT_ENV", "dev")
    monkeypatch.setattr(VaultWriter, "_annotate_sync", lambda _self, _result: None)
    dry = VaultWriter("test.taxonomy.catalyst", store=MemoryWriteStore(), clock=OpenClock(), dry_run=True,
                      now=lambda: datetime(2026, 9, 16, 22, 0, tzinfo=UTC))
    path, digest = _review_file(tmp_path, vault)
    before = _note_bytes(vault)
    report = cat.apply_review(vault, path, expected_sha256=digest, writer=dry)
    assert _note_bytes(vault) == before and report.gate_ready is False and len(report.results) == 2


# ---------------------------------------------------------------------
# the line editor
# ---------------------------------------------------------------------


def test_factor_block_reads_both_indent_styles_and_mapping_items():
    example = example_note_text().split("\n")
    names = factor_block(example).names
    assert names[:3] == ["range_duration", "range_height_vs_day_range", "break_bar_volume_vs_prior"]
    assert "tape_absorption_at_bound" in names
    probe = _probe_note().split("\n")
    assert factor_block(probe).names[1:3] == ["catalyst_grade", "catalyst_class"]


def test_flow_style_quality_factors_is_refused():
    body = ["```yaml", "trade_def:", "  quality_factors: [a, b]", "```"]
    with pytest.raises(FactorLinesError, match="flow-style"):
        factor_block(body)


# ---------------------------------------------------------------------
# requires_vault — the live notes, read in place, never written (hub-run)
# ---------------------------------------------------------------------

LIVE_VAULT_ENV = "COBALT_LIVE_VAULT_ROOT"
requires_vault = pytest.mark.skipif(
    not os.getenv(LIVE_VAULT_ENV),
    reason=f"{LIVE_VAULT_ENV} not set — the hub runs the live catalyst review draft",
)


@requires_vault
def test_live_review_lists_every_defined_note_and_its_catalyst_factors_and_writes_nothing(capsys):
    root = Path(os.environ[LIVE_VAULT_ENV])
    strategies = sorted((root / "1 - Trading/4 - Strategies").glob("*.md"))
    before = {p: p.stat().st_mtime_ns for p in strategies}
    defined = load_vault_trade_defs(vault_root=root).defs
    review = cat.draft_review(root, today=TODAY)
    assert {r.slug for r in review.rows} == {d.slug for d in defined} and len(review.rows) >= 13
    assert sum(bool(r.existing) for r in review.rows) >= 5  # plan F6: notes already grading catalyst_*
    assert all(r.proposed == cat.PROPOSED_LINE and r.drop == [] for r in review.rows)
    assert cat.parse_review(cat.render_review(review)) == review
    plans = cat.plan_apply(root, review)  # preflight only: every unit's target validates at 0.5
    assert {p.action for p in plans} == {"write"}
    with capsys.disabled():
        for row in review.rows:
            print(f"{row.slug}: existing {row.existing or '—'}")
    assert {p: p.stat().st_mtime_ns for p in strategies} == before
