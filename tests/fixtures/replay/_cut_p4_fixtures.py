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
blank for an ordinary stock, so the radar config's `not_equity.values:
[Exchange Traded Fund]` matches nothing; the report is the evidence for
rebuilding that rule. It is a decision aid, never a rule. Tickers live
in the scratch file only (L32) — stdout carries counts.

THIRD MODE, `movers` (AT-1 2.5). Re-cuts ONLY the two movers fixtures,
from the re-fetched raw exports above, and touches nothing else: the
no-argument mode still needs raw inputs that no longer all exist, so
re-cutting everything is not a way to fix one fixture. Same rules as the
other cuts (`_anonymize`, first `MOVERS_ROWS` rows) plus the guarantee
that at least one real row with a non-blank `Asset Type` is in the cut —
see `cut_movers`. The fixture is never hand-edited: a divergence is
fixed here and the mode re-run.
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
from collections import Counter
from collections.abc import Iterable, Sequence
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
    sizings = json.loads(_anonymize(json.dumps(day_cards)))

    trans_text = (SCRATCH / "card-transitions-day-raw.tsv").read_text()
    transitions = json.loads(_anonymize(json.dumps(_tsv_rows(trans_text))))

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


#: Data rows taken from the top of each movers export. Enough to carry
#: the day's real top of the tape without committing 11,000 rows.
MOVERS_ROWS = 60


def _one_row(header: str, line: str) -> dict:
    """One export line parsed against the export's own header."""
    row = next(csv.DictReader(io.StringIO(header + line)), None)
    if row is None:
        raise AssertionError("movers: a data line parsed to no row")
    return row


def _first_fund_row(header: str, data: list[str], taken: int) -> tuple[int, str] | None:
    """The first row BELOW the cut whose `Asset Type` is non-blank, or
    None if the cut already holds one — or the file holds none at all."""
    if any((_one_row(header, line).get(ASSET_TYPE_COL) or "").strip() for line in data[:taken]):
        return None
    for offset, line in enumerate(data[taken:], start=taken + 1):
        if (_one_row(header, line).get(ASSET_TYPE_COL) or "").strip():
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

    A real row with a non-blank `Asset Type` is guaranteed to be in the
    cut. Finviz fills that column only for funds, so a cut without one
    would leave every "reads Asset Type when present" claim untested. If
    the top rows hold none, the first one further down the file is
    APPENDED, out of rank order, and stdout says so; if the file holds
    none at all, the cut is what exists and stdout says that instead. A
    row is never invented.
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
        appended = _first_fund_row(header, data, MOVERS_ROWS)
        if appended is not None:
            trimmed = trimmed + [appended[1]]
        dest = HERE / f"movers-{side}.real-shape.csv"
        dest.write_text(_anonymize("".join([header] + trimmed)))

        funds = sum(
            1 for line in trimmed if (_one_row(header, line).get(ASSET_TYPE_COL) or "").strip()
        )
        note = (
            f"appended data row {appended[0]} for its non-blank {ASSET_TYPE_COL}"
            if appended is not None
            else f"no {ASSET_TYPE_COL} row appended"
        )
        if funds == 0:
            note = f"NO non-blank {ASSET_TYPE_COL} row exists in the raw export — cut what exists"
        print(
            f"wrote {dest} ({len(trimmed)} rows, {len(records[0])} columns, "
            f"{funds} with a non-blank {ASSET_TYPE_COL}; {note})"
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

ASSET_TYPE_COL = "Asset Type"
INDUSTRY_COL = "Industry"
TICKER_COL = "Ticker"
FUND_INDUSTRY = "Exchange Traded Fund"

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
    table_a: list[PairCount] = []
    table_b: list[AssetTypeCount] = []
    table_c_non_blank_not_fund: list[DisagreementRow] = []
    table_c_fund_blank_type: list[DisagreementRow] = []

    @property
    def table_c_total(self) -> int:
        return len(self.table_c_non_blank_not_fund) + len(self.table_c_fund_blank_type)


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
        f"table C total: {report.table_c_total}"
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
    else:
        raise SystemExit(f"unknown mode {mode!r}; expected no argument, 'evidence' or 'movers'")
