"""Deterministic, re-runnable cut of the S2-P4 replay/picks fixtures
(plan STEP-1, L45 real-shape rule) from production reads saved under the
hub's scratch directory. Never reads the live DB/Finviz itself, never
invents a row.

Anchor day: real STEP-0 day (see the hub's report `## STEP-0 facts` for
the exact date), aset_sizings ids 302-312: CRWD/MU/INTC. Confirmed
against system.bars i1 that CRWD 302/303/304/305 and MU 308/309 crossed
their WATCH entry level without ever arming or triggering — genuine
"missed" cards (the case F13's miss line exists for) — while CRWD 306,
MU 307/310, INTC 311/312 armed, triggered, filled and closed. No
PASSED-state card exists anywhere in the aset_sizings read window since
the STEP-0 query's start date (card_transitions checked for all 29
rows) — recorded as a real gap, never invented. Shifted to synthetic
2026-02-10 (the leak scan in plan STEP-1 row 4 requires no literal real
anchor-month date string survive under tests/fixtures/ — this docstring
therefore never spells it out either).

ANONYMIZATION is spec-01 §3's three transforms for the cards cut, and
all three are implemented here: the date shift (`_shift_dates`), the
`@<hex>` suffix scrub (`_anonymize`), and — key-level, so not reachable
from either text pass — `user_id` → 1 with free-text reasons →
`"<reason>"` (`strip_personal`, wired into `cut_cards_day`). The raw
reads this script consumes select neither of those last two columns, so
the committed cut is unchanged by them; they exist so that the
guarantee does not depend on the column list of whatever read comes
next. The tickers and card ids ARE the fixture spec-01:249 commissions
and are inherent to it (L45 real-shape), not an anonymization gap.

Inputs, all raw production-read output, none queried by this script:
  scratch/step0-sizings.json           aset_sizings, `--format json`
                                        (desk-staged per the CTO desk's
                                        report §4 R4 — see the hub's
                                        report for the exact timestamp)
  scratch/card-transitions-day-raw.tsv card_transitions cards 302-312,
                                        `--format table`
  RAW_BARS_SOURCE (below)              system.bars i1, CRWD/MU/INTC,
                                        anchor day 13:00-20:10 UTC (the
                                        window from first card creation
                                        through the 20:05 ET
                                        market_reset expiry — premarket
                                        bars before the first card
                                        existed play no role, same
                                        real-shape-trim rationale as
                                        P2's _cut_p2_fixtures.py daily
                                        window), `--format table`,
                                        persisted verbatim by the
                                        harness because of its size;
                                        copied into scratch/ by this
                                        script as the L45 raw-output
                                        record before transforming
  RAW_MEMBERSHIP_SOURCE (below)        system.radar_membership, full
                                        anchor day, `--format table`,
                                        same persist-then-copy handling
  scratch/pool-metrics-raw.csv         one cached Finviz screen CSV,
                                        `cp` from data/radar-cache/
  scratch/movers-{gainers,losers}-raw.csv
                                        live Finviz /export/screener
                                        o=-change / o=change, unfiltered,
                                        no filter param. RE-FETCHED by
                                        the hub at the radar's real
                                        column set (`v` and `c` from
                                        configs/cobalt/radar.yaml), 151
                                        columns incl. `Asset Type`,
                                        11,640 rows per side — the shape
                                        the collector actually receives.
                                        The first cut used a v=152
                                        default view (21 columns, no
                                        `Asset Type`), which is why the
                                        `movers` mode below exists.

Outputs:
  tests/fixtures/replay/cards-day.real-shape.json
  tests/fixtures/replay/bars-day.real-shape.json
  tests/fixtures/replay/membership-day.real-shape.json
  tests/fixtures/replay/movers-gainers.real-shape.csv
  tests/fixtures/replay/movers-losers.real-shape.csv
  tests/fixtures/radar/pool-metrics.real-shape.csv

SECOND MODE, `evidence` (AT-0). With no CLI argument the script does
exactly what it did before. With `evidence` it cuts nothing at all: it
reads every cached Finviz export it can find and writes ONE scratch
report comparing the `Asset Type` column against `Industry =
Exchange Traded Fund`. Read-only — no network, no DB, no fixture
written, nothing written anywhere but `scratch/asset-type-evidence.md`.
It exists because Finviz fills `Asset Type` only for funds and leaves it
blank for an ordinary stock, so the radar config's former one-column
rule (`not_equity.values: [Exchange Traded Fund]`) matched nothing; the
report was the evidence for rebuilding it (R16 "C", now `is_not_equity`).
It is a decision aid, never a rule. Tickers live
in the scratch file only (L32) — stdout carries counts.

THIRD MODE, `movers` (AT-1 2.5). Re-cuts ONLY the two movers fixtures,
from the re-fetched raw exports above, and touches nothing else: the
no-argument mode still needs raw inputs that no longer all exist, so
re-cutting everything is not a way to fix one fixture. Same rules as the
other cuts (`_anonymize`, first `MOVERS_ROWS` rows) plus a guaranteed
real row for every class in `GUARANTEED_ROW_CLASSES` — a non-blank
`Asset Type`, and a fund named by `Industry` alone with the `Asset Type`
cell left blank — see `cut_movers`. The fixture is never hand-edited: a
divergence is fixed here and the mode re-run.

FOURTH MODE, `movers-blank <raw-export-path>` (S2 smoke fix F1-FX). Cuts
ONE new fixture, `movers-gainers-blank-change.real-shape.csv`, from the
raw export named on the command line — READ ONLY, run on the retained
gainers export whose parse failed the 2026-09-22 replay (`Change ''`).
The committed movers fixtures are the export's TOP rows, so the tail
where Finviz lists never-traded listings with an EMPTY `Change` cell was
cut away and no test could see the shape that failed. This cut keeps the
raw header byte for byte, the first `BLANK_TOP_ROWS` data rows, and EVERY
data row whose `Change` cell is empty, in export order, each through
`_anonymize`. A raw export holding no such row FAILS the mode loud. The
other modes are untouched. Stdout carries counts only (L32) — never a
ticker, same posture as the `evidence` mode.
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
from collections import Counter
from collections.abc import Callable, Iterable, Sequence
from datetime import date, timedelta
from pathlib import Path

from pydantic import BaseModel

HERE = Path(__file__).parent  # tests/fixtures/replay/
RADAR_DIR = HERE.parent / "radar"
SCRATCH = Path(__file__).resolve().parents[3] / "scratch"

REAL_ANCHOR = date(2026, 9, 14)
SYNTH_ANCHOR = date(2026, 2, 10)
DELTA_DAYS = (SYNTH_ANCHOR - REAL_ANCHOR).days

_DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
_HEX_SUFFIX_RE = re.compile(r"@[0-9a-f]{12}")

# Exact stdout of the two approved `cobalt db query --prod --format
# table` reads (plan STEP-1 rows 2 and 2m), persisted verbatim by the
# harness under its own tool-output store because of their size. Real
# production-read output, not invented; copied into scratch/ below.
RAW_BARS_SOURCE = Path(
    "/Users/cobalt/.claude/projects/-Users-cobalt-cobalt-wt-s2-p4/"
    "4f911896-df95-4888-9f12-6038117d288e/tool-results/b9h4bhyxf.txt"
)
RAW_MEMBERSHIP_SOURCE = Path(
    "/Users/cobalt/.claude/projects/-Users-cobalt-cobalt-wt-s2-p4/"
    "4f911896-df95-4888-9f12-6038117d288e/tool-results/boetnggei.txt"
)

_INT_FIELDS = {
    "id",
    "card_id",
    "volume",
    "rank_at_entry",
    "last_rank",
    "below_cap_streak",
    "opened_scan_id",
    "last_scan_id",
    "closed_scan_id",
}


def _shift_dates(text: str) -> str:
    def repl(m: re.Match) -> str:
        d = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        if d.year == REAL_ANCHOR.year and d.month == REAL_ANCHOR.month:
            return (d + timedelta(days=DELTA_DAYS)).isoformat()
        return m.group(0)

    return _DATE_RE.sub(repl, text)


def _anonymize(text: str) -> str:
    return _HEX_SUFFIX_RE.sub("@000000000000", _shift_dates(text))


#: spec-01 §3 (`spec-01:249`), the two transforms `_anonymize` does not
#: do — it is a hex-suffix scrub plus the date shift, both text-level.
#: These are key-level and so run over the parsed rows instead.
#:
#: Today's raw reads select neither column (`step0-sizings.json` and
#: card-transitions carry `created_at, direction, entry, id, state, stop,
#: ticker` and `at, card_id, from_state, to_state`), so these change
#: nothing about the committed cut. They are here because "the read
#: happens to omit it" is not a transform: the next read taken with a
#: wider column list would otherwise carry an owner id or a line of the
#: trader's own writing into a committed file (L32).
PERSONAL_ID_FIELDS = frozenset({"user_id", "trader_id"})
FREE_TEXT_FIELDS = frozenset({"reason", "note", "comment", "rationale", "thesis"})
REASON_PLACEHOLDER = "<reason>"


def strip_personal(rows: Sequence[dict]) -> list[dict]:
    """`user_id` → 1, free-text reasons → `"<reason>"`, nothing else.

    A NULL free-text cell stays NULL: a missing note is not free text,
    and the real shape includes its nullability. Rows are copied, never
    mutated in place, so a caller's raw read is left as it was read.
    """
    out: list[dict] = []
    for row in rows:
        clean = dict(row)
        for field in PERSONAL_ID_FIELDS & clean.keys():
            clean[field] = 1
        for field in FREE_TEXT_FIELDS & clean.keys():
            if clean[field] is not None:
                clean[field] = REASON_PLACEHOLDER
        out.append(clean)
    return out


def _cast_row(row: dict) -> dict:
    out = {}
    for k, v in row.items():
        if v == "":
            out[k] = None
        elif k in _INT_FIELDS:
            out[k] = int(v)
        else:
            out[k] = v
    return out


def _tsv_rows(text: str) -> list[dict]:
    return [_cast_row(r) for r in csv.DictReader(io.StringIO(text), delimiter="\t")]


def cut_cards_day() -> None:
    sizings_raw = json.loads((SCRATCH / "step0-sizings.json").read_text())
    day_cards = [r for r in sizings_raw if r["created_at"].startswith(str(REAL_ANCHOR))]
    assert day_cards, "no sizings for the anchor day"
    sizings = json.loads(_anonymize(json.dumps(strip_personal(day_cards))))

    trans_text = (SCRATCH / "card-transitions-day-raw.tsv").read_text()
    transitions = json.loads(_anonymize(json.dumps(strip_personal(_tsv_rows(trans_text)))))

    dest = HERE / "cards-day.real-shape.json"
    dest.write_text(
        json.dumps({"sizings": sizings, "transitions": transitions}, indent=2, sort_keys=True) + "\n"
    )
    print(f"wrote {dest} ({len(sizings)} sizings, {len(transitions)} transitions)")


def cut_bars_day() -> None:
    raw_text = RAW_BARS_SOURCE.read_text()
    (SCRATCH / "bars-day-raw.tsv").write_text(raw_text)
    rows = _tsv_rows(raw_text)
    assert rows, "expected bars rows"
    anonymized = json.loads(_anonymize(json.dumps(rows)))
    dest = HERE / "bars-day.real-shape.json"
    dest.write_text(json.dumps(anonymized, indent=2, sort_keys=True) + "\n")
    print(f"wrote {dest} ({len(anonymized)} bars)")


def cut_membership_day() -> None:
    raw_text = RAW_MEMBERSHIP_SOURCE.read_text()
    (SCRATCH / "membership-day-raw.tsv").write_text(raw_text)
    rows = _tsv_rows(raw_text)
    assert rows, "expected membership rows"
    anonymized_rows = json.loads(_anonymize(json.dumps(rows)))

    # Synthesized PoolRow-shaped status block, matching the top-level
    # "pool" key of tests/fixtures/radar/panel-pool.real-shape.json
    # (P3). Not a derived production value — a plausible end-of-day
    # snapshot shape for STEP-2's PoolRow tests; the substantive data
    # for rank_metric/rank_value tests is the real "membership" list.
    pool_block = {
        "budget": {"planned_rpm": 36.6},
        "cap": 50,
        "degraded": False,
        "degraded_sources": [],
        "failed_detail": None,
        "failed_stage": None,
        "last_poll_at": None,
        "last_scan_at": f"{SYNTH_ANCHOR.isoformat()} 20:05:03.002850+00:00",
        "last_scan_id": 1000000000000,
        "last_scan_ms": 85,
        "members": 50,
        "poll_failures": [],
        "pool_key": "primary",
        "session": "close",
        "sources": [],
        "state": "scanning",
        "updated_at": f"{SYNTH_ANCHOR.isoformat()} 20:05:03.002850+00:00",
    }
    dest = HERE / "membership-day.real-shape.json"
    dest.write_text(
        json.dumps({"membership": anonymized_rows, "pool": pool_block}, indent=2, sort_keys=True) + "\n"
    )
    print(f"wrote {dest} ({len(anonymized_rows)} episodes)")


def cut_pool_metrics() -> None:
    raw_text = (SCRATCH / "pool-metrics-raw.csv").read_text()
    anonymized = _anonymize(raw_text)
    lines = anonymized.splitlines(keepends=True)
    trimmed = lines[:21]  # header + 20 rows
    dest = RADAR_DIR / "pool-metrics.real-shape.csv"
    dest.write_text("".join(trimmed))
    print(f"wrote {dest} ({len(trimmed) - 1} rows)")


#: Finviz column names and the one `Industry` value that names a fund.
#: Read by BOTH the movers cut (its guaranteed row classes) and the
#: read-only `evidence` mode below — one definition, never a second copy.
ASSET_TYPE_COL = "Asset Type"
INDUSTRY_COL = "Industry"
TICKER_COL = "Ticker"
FUND_INDUSTRY = "Exchange Traded Fund"

#: Data rows taken from the top of each movers export. Enough to carry
#: the day's real top of the tape without committing 11,000 rows.
MOVERS_ROWS = 60


def _one_row(header: str, line: str) -> dict:
    """One export line parsed against the export's own header."""
    row = next(csv.DictReader(io.StringIO(header + line)), None)
    if row is None:
        raise AssertionError("movers: a data line parsed to no row")
    return row


def _has_asset_type(row: dict) -> bool:
    """A fund Finviz named in the `Asset Type` column."""
    return bool((row.get(ASSET_TYPE_COL) or "").strip())


def _is_blank_type_fund(row: dict) -> bool:
    """A fund Finviz named in `Industry` ALONE, leaving `Asset Type`
    blank — the class table C(ii) counts, and the only rows that tell a
    `not_equity` rule reading one column from a rule reading both."""
    return not _has_asset_type(row) and (row.get(INDUSTRY_COL) or "").strip() == FUND_INDUSTRY


#: Row classes at least one real example of which must be in every
#: movers cut, with the phrase stdout names each by. A cut missing one
#: leaves that branch of the not-equity question asserted against
#: nothing.
GUARANTEED_ROW_CLASSES = (
    (f"a non-blank {ASSET_TYPE_COL}", _has_asset_type),
    (f"a blank {ASSET_TYPE_COL} with {INDUSTRY_COL} = {FUND_INDUSTRY}", _is_blank_type_fund),
)


def _first_row_below(
    header: str, data: list[str], taken: int, matches: Callable[[dict], bool]
) -> tuple[int, str] | None:
    """The first row BELOW the cut that `matches`, or None if the cut
    already holds one — or the file holds none at all."""
    if any(matches(_one_row(header, line)) for line in data[:taken]):
        return None
    for offset, line in enumerate(data[taken:], start=taken + 1):
        if matches(_one_row(header, line)):
            return offset, line
    return None


def cut_movers() -> None:
    """Both unfiltered movers exports, cut to their top `MOVERS_ROWS` rows.

    The header row is the raw file's own, never rebuilt and never
    trimmed, and `_anonymize` must leave it byte for byte — a header the
    cutter edited is not the shape the collector receives (L45). Line
    endings are the one normalisation, applied by `read_text` to every
    fixture this script cuts, so the movers header matches the radar
    export fixture's exactly.

    Every class in `GUARANTEED_ROW_CLASSES` is guaranteed a real row in
    the cut: a non-blank `Asset Type` (Finviz fills that column only for
    funds, so a cut without one would leave every "reads Asset Type when
    present" claim untested) and a fund named by `Industry` alone with a
    blank `Asset Type` (the case a one-column rule misses). If the top
    rows hold none of a class, the first one further down the file is
    APPENDED and stdout says so; if the file holds none at all, the cut
    is what exists and stdout says that instead. A row is never invented.

    An appended row is a lower-ranked row of the same export, so it
    extends the tail in the export's own order and `parse_movers`' sort
    check still passes — but it sits at a rank the raw file never gave
    it, which is why appends are counted on stdout rather than silent.
    """
    for side in ("gainers", "losers"):
        raw_text = (SCRATCH / f"movers-{side}-raw.csv").read_text()
        lines = raw_text.splitlines(keepends=True)
        records = list(csv.reader(io.StringIO(raw_text)))
        assert len(records) == len(lines), (
            f"movers-{side}: {len(records)} CSV records over {len(lines)} lines — a field spans "
            "lines, so cutting by line would split a row"
        )
        header, data = lines[0], lines[1:]
        assert _anonymize(header) == header, f"movers-{side}: _anonymize rewrote the header row"

        trimmed = data[:MOVERS_ROWS]
        notes: list[str] = []
        appends: list[tuple[int, str]] = []
        for label, matches in GUARANTEED_ROW_CLASSES:
            found = _first_row_below(header, data, MOVERS_ROWS, matches)
            if found is not None:
                appends.append(found)
                notes.append(f"appended data row {found[0]} for {label}")
            elif any(matches(_one_row(header, line)) for line in trimmed):
                notes.append(f"{label}: already in the top rows")
            else:
                notes.append(f"NO row with {label} exists in the raw export — cut what exists")
        # Ranked order: an append taken from further down the file keeps
        # the export's own order only if the appends go back in file order.
        trimmed = trimmed + [line for _, line in sorted(appends)]
        dest = HERE / f"movers-{side}.real-shape.csv"
        dest.write_text(_anonymize("".join([header] + trimmed)))

        rows = [_one_row(header, line) for line in trimmed]
        funds = sum(1 for row in rows if _has_asset_type(row))
        blank_type_funds = sum(1 for row in rows if _is_blank_type_fund(row))
        print(
            f"wrote {dest} ({len(trimmed)} rows, {len(records[0])} columns, "
            f"{funds} with a non-blank {ASSET_TYPE_COL}, "
            f"{blank_type_funds} blank-{ASSET_TYPE_COL} {FUND_INDUSTRY}; "
            + "; ".join(notes)
            + ")"
        )


#: Data rows taken from the top of the export by the `movers-blank` cut —
#: enough ranked rows above any benchmark `top_n` a test asks for.
BLANK_TOP_ROWS = 25
CHANGE_COL = "Change"
BLANK_CHANGE_FIXTURE = HERE / "movers-gainers-blank-change.real-shape.csv"


def _has_blank_change(row: dict) -> bool:
    """EXACTLY the cell `parse_movers` leaves unranked: empty after strip."""
    return (row.get(CHANGE_COL) or "").strip() == ""


def cut_movers_blank(raw_path: Path) -> None:
    """The top `BLANK_TOP_ROWS` rows of one raw movers export plus every
    row whose `Change` cell is empty, in export order (L45).

    Rows are the `csv` module's records: the guard below proves one
    record per line before any line is kept, the same guard `cut_movers`
    uses, so a quoted field spanning lines can never split a row. The
    header is the raw file's own and `_anonymize` must leave it byte for
    byte. A blank row inside the top rows is kept once, where it sits.
    """
    raw_text = Path(raw_path).read_text()
    lines = raw_text.splitlines(keepends=True)
    records = list(csv.reader(io.StringIO(raw_text)))
    assert len(records) == len(lines), (
        f"movers-blank: {len(records)} CSV records over {len(lines)} lines — a field spans "
        "lines, so cutting by line would split a row"
    )
    header, data = lines[0], lines[1:]
    assert _anonymize(header) == header, "movers-blank: _anonymize rewrote the header row"
    assert CHANGE_COL in records[0], f"movers-blank: the raw export has no {CHANGE_COL} column"

    blank_at = [
        position for position, line in enumerate(data, start=1)
        if _has_blank_change(_one_row(header, line))
    ]
    if not blank_at:
        raise SystemExit(f"movers-blank: NO row with a blank {CHANGE_COL} exists in the raw export")
    keep = sorted(set(range(1, min(BLANK_TOP_ROWS, len(data)) + 1)) | set(blank_at))
    kept = [data[position - 1] for position in keep]
    BLANK_CHANGE_FIXTURE.write_text(_anonymize("".join([header] + kept)))
    print(
        f"wrote {BLANK_CHANGE_FIXTURE} ({len(kept)} rows kept of {len(data)} data rows, "
        f"{len(records[0])} columns; {len(blank_at)} with a blank {CHANGE_COL}, kept at export "
        f"positions {blank_at[0]}-{blank_at[-1]}; "
        f"top {min(BLANK_TOP_ROWS, len(data))} rows kept above them)"
    )


def main() -> None:
    HERE.mkdir(parents=True, exist_ok=True)
    cut_cards_day()
    cut_bars_day()
    cut_membership_day()
    cut_pool_metrics()
    cut_movers()


# =====================================================================
# `evidence` mode — READ-ONLY. Writes nothing but EVIDENCE_OUT.
# =====================================================================

#: The production radar's on-disk Finviz cache. Read only, recursively,
#: and only by this mode; the cutting functions above never look at it.
RADAR_CACHE_DIR = Path("/Users/cobalt/cobalt/data/radar-cache")

#: The two unfiltered movers exports the hub already staged in scratch/
#: for the STEP-1 cut. Included so the evidence covers the `v=152` shape
#: as well as the cache's own column lists.
EVIDENCE_SCRATCH_INPUTS = ("movers-gainers-raw.csv", "movers-losers-raw.csv")

EVIDENCE_OUT = SCRATCH / "asset-type-evidence.md"

#: Rendered in place of an empty `Asset Type` so a blank is never
#: invisible in a table.
BLANK = "<blank>"


class EvidenceError(RuntimeError):
    """A named input could not be read or parsed. Always carries the
    file's name — a cache file that is not a CSV is a loud failure, not
    a skipped row (L1)."""


class DisagreementRow(BaseModel):
    """One row where the two fund signals disagree."""

    file: str
    ticker: str
    asset_type: str
    industry: str


class PairCount(BaseModel):
    """Table A: a distinct (`Asset Type`, `Industry`) pair, with rows."""

    asset_type: str
    industry: str
    rows: int


class AssetTypeCount(BaseModel):
    """Table B: a distinct `Asset Type` value, with rows."""

    asset_type: str
    rows: int


class EvidenceReport(BaseModel):
    """Everything the report file renders. Pure data — building it never
    touches the filesystem beyond reading the inputs."""

    input_dirs: list[str] = []
    files_read: int = 0
    files_without_columns: list[str] = []
    rows_with_columns: int = 0
    rows_without_columns: int = 0
    distinct_fund_tickers: int = 0
    distinct_asset_types: int = 0
    #: Rows the candidate not-equity rule would drop: `Asset Type`
    #: non-blank OR `Industry` = the fund industry. The union of table A's
    #: rows and table B's rows, counted once per row.
    dropped_under_new_rule: int = 0
    table_a: list[PairCount] = []
    table_b: list[AssetTypeCount] = []
    table_c_non_blank_not_fund: list[DisagreementRow] = []
    table_c_fund_blank_type: list[DisagreementRow] = []

    @property
    def table_c_total(self) -> int:
        return len(self.table_c_non_blank_not_fund) + len(self.table_c_fund_blank_type)

    @property
    def stock_rows_hit(self) -> int:
        """Rows `dropped_under_new_rule` drops that are NOT funds by
        industry — table C(i). An ordinary stock the rule would throw
        away, which is the cost side of the decision."""
        return len(self.table_c_non_blank_not_fund)


def _read_csv(path: Path) -> tuple[list[str], list[dict]]:
    """Header + rows of one export. The header row is read, never
    assumed: every lookup downstream is by column name."""
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            fieldnames = reader.fieldnames
            rows = list(reader)
    except (csv.Error, UnicodeDecodeError, OSError) as exc:
        raise EvidenceError(f"{path.name}: cannot be read as CSV ({exc})") from exc
    if not fieldnames:
        raise EvidenceError(f"{path.name}: cannot be read as CSV (no header row)")
    return list(fieldnames), rows


def collect_evidence(
    paths: Iterable[Path], input_dirs: Sequence[str] = ()
) -> EvidenceReport:
    """Read every path and count how the two fund signals line up.

    A file whose header lacks either column is COUNTED and named, never
    skipped and never an error — the `v=152` movers exports are exactly
    that case, and their absence from the comparison is itself evidence.
    """
    files_without: list[str] = []
    rows_with = 0
    rows_without = 0
    pairs: Counter[tuple[str, str]] = Counter()
    fund_types: Counter[str] = Counter()
    fund_tickers: set[str] = set()
    asset_types: set[str] = set()
    non_blank_not_fund: list[DisagreementRow] = []
    fund_blank_type: list[DisagreementRow] = []
    files_read = 0
    dropped = 0

    for path in paths:
        files_read += 1
        fieldnames, rows = _read_csv(path)
        if ASSET_TYPE_COL not in fieldnames or INDUSTRY_COL not in fieldnames:
            files_without.append(path.name)
            rows_without += len(rows)
            continue
        rows_with += len(rows)
        for row in rows:
            asset_type = (row.get(ASSET_TYPE_COL) or "").strip()
            industry = (row.get(INDUSTRY_COL) or "").strip()
            ticker = (row.get(TICKER_COL) or "").strip()
            is_fund_industry = industry == FUND_INDUSTRY
            if asset_type:
                pairs[(asset_type, industry)] += 1
                asset_types.add(asset_type)
            if is_fund_industry:
                fund_types[asset_type or BLANK] += 1
            if not (asset_type or is_fund_industry):
                continue
            dropped += 1
            fund_tickers.add(ticker)
            if asset_type and not is_fund_industry:
                non_blank_not_fund.append(
                    DisagreementRow(
                        file=path.name,
                        ticker=ticker,
                        asset_type=asset_type,
                        industry=industry,
                    )
                )
            elif is_fund_industry and not asset_type:
                fund_blank_type.append(
                    DisagreementRow(
                        file=path.name,
                        ticker=ticker,
                        asset_type=BLANK,
                        industry=industry,
                    )
                )

    return EvidenceReport(
        input_dirs=list(input_dirs),
        files_read=files_read,
        files_without_columns=files_without,
        rows_with_columns=rows_with,
        rows_without_columns=rows_without,
        distinct_fund_tickers=len(fund_tickers),
        distinct_asset_types=len(asset_types),
        dropped_under_new_rule=dropped,
        table_a=[
            PairCount(asset_type=at, industry=ind, rows=n)
            for (at, ind), n in sorted(pairs.items())
        ],
        table_b=[
            AssetTypeCount(asset_type=at, rows=n) for at, n in sorted(fund_types.items())
        ],
        table_c_non_blank_not_fund=non_blank_not_fund,
        table_c_fund_blank_type=fund_blank_type,
    )


def _table(header: Sequence[str], rows: Sequence[Sequence[object]]) -> list[str]:
    if not rows:
        return ["(none)"]
    lines = [
        "| " + " | ".join(header) + " |",
        "|" + "|".join(["---"] * len(header)) + "|",
    ]
    lines += ["| " + " | ".join(str(cell) for cell in row) + " |" for row in rows]
    return lines


def render_evidence(report: EvidenceReport) -> str:
    """The scratch report. Tickers appear HERE and nowhere else."""
    without = report.files_without_columns
    out: list[str] = [
        "# Asset Type vs Industry — evidence",
        "",
        "Read-only evidence for the S2-P4 `not_equity` decision, produced by",
        "`tests/fixtures/replay/_cut_p4_fixtures.py evidence`. A decision aid,",
        "not a rule. Contains user data (tickers) — scratch only, never committed.",
        "",
        "## 1. Read",
        "",
        f"- files read: {report.files_read}",
        f"- rows read (files with both columns): {report.rows_with_columns}",
        f"- rows read (files without the columns): {report.rows_without_columns}",
        f"- files without the columns ({len(without)}): "
        + (", ".join(without) if without else "(none)"),
        "- input dirs: " + (", ".join(report.input_dirs) if report.input_dirs else "(none)"),
        "",
        "## 2. Distinct counts",
        "",
        f"- distinct fund tickers (a row in table A or table B): {report.distinct_fund_tickers}",
        f"- distinct non-blank `Asset Type` values: {report.distinct_asset_types}",
        "",
        "## 2a. The candidate rule",
        "",
        f"- rows dropped under the new rule (non-blank `Asset Type` OR `Industry` = "
        f"{FUND_INDUSTRY}): {report.dropped_under_new_rule}",
        f"- of those, stock rows hit (table C(i), a non-fund `Industry`): "
        f"{report.stock_rows_hit}",
        "",
        "## 3. Table A — (`Asset Type`, `Industry`) pairs, `Asset Type` non-blank",
        "",
    ]
    out += _table(
        ["Asset Type", "Industry", "rows"],
        [(r.asset_type, r.industry, r.rows) for r in report.table_a],
    )
    out += [
        "",
        f"## 4. Table B — `Asset Type` values where `Industry` = {FUND_INDUSTRY}",
        "",
    ]
    out += _table(
        ["Asset Type", "rows"], [(r.asset_type, r.rows) for r in report.table_b]
    )
    out += [
        "",
        "## 5. Table C — disagreement rows",
        "",
        "COUNTS",
        "",
        f"- (i) non-blank `Asset Type`, `Industry` != {FUND_INDUSTRY}: "
        f"{len(report.table_c_non_blank_not_fund)}",
        f"- (ii) `Industry` = {FUND_INDUSTRY}, blank `Asset Type`: "
        f"{len(report.table_c_fund_blank_type)}",
        f"- total: {report.table_c_total}",
        "",
        f"### (i) non-blank `Asset Type`, `Industry` != {FUND_INDUSTRY}",
        "",
    ]
    out += _table(
        ["file", "ticker", "Asset Type", "Industry"],
        [(r.file, r.ticker, r.asset_type, r.industry) for r in report.table_c_non_blank_not_fund],
    )
    out += [
        "",
        f"### (ii) `Industry` = {FUND_INDUSTRY}, blank `Asset Type`",
        "",
    ]
    out += _table(
        ["file", "ticker", "Asset Type", "Industry"],
        [(r.file, r.ticker, r.asset_type, r.industry) for r in report.table_c_fund_blank_type],
    )
    return "\n".join(out) + "\n"


def summarize_evidence(report: EvidenceReport) -> str:
    """The one stdout line. Counts only — never a ticker (L32)."""
    return (
        f"files: {report.files_read} "
        f"(without the columns: {len(report.files_without_columns)}); "
        f"rows: {report.rows_with_columns} "
        f"(without the columns: {report.rows_without_columns}); "
        f"distinct fund tickers: {report.distinct_fund_tickers}; "
        f"distinct Asset Type values: {report.distinct_asset_types}; "
        f"table C total: {report.table_c_total}; "
        f"dropped under the new rule: {report.dropped_under_new_rule}; "
        f"stock rows hit: {report.stock_rows_hit}"
    )


def discover_evidence_inputs() -> tuple[list[Path], list[str]]:
    """Every `*.csv` under the radar cache, plus the two staged movers
    exports. A missing input is a loud failure, not an empty run (L1)."""
    if not RADAR_CACHE_DIR.is_dir():
        raise EvidenceError(f"radar cache directory not found: {RADAR_CACHE_DIR}")
    paths = sorted(RADAR_CACHE_DIR.rglob("*.csv"))
    for name in EVIDENCE_SCRATCH_INPUTS:
        staged = SCRATCH / name
        if not staged.is_file():
            raise EvidenceError(f"staged movers export not found: {staged}")
        paths.append(staged)
    return paths, [str(RADAR_CACHE_DIR), str(SCRATCH)]


def evidence_main() -> None:
    paths, input_dirs = discover_evidence_inputs()
    report = collect_evidence(paths, input_dirs=input_dirs)
    EVIDENCE_OUT.write_text(render_evidence(report), encoding="utf-8")
    print(summarize_evidence(report))
    print(f"wrote {EVIDENCE_OUT}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if not mode:
        main()
    elif mode == "evidence":
        evidence_main()
    elif mode == "movers":
        cut_movers()
    elif mode == "movers-blank":
        if len(sys.argv) != 3:
            raise SystemExit("movers-blank takes exactly one argument: the raw export's path")
        cut_movers_blank(Path(sys.argv[2]))
    else:
        raise SystemExit(
            f"unknown mode {mode!r}; expected no argument, 'evidence', 'movers' or 'movers-blank <path>'"
        )
