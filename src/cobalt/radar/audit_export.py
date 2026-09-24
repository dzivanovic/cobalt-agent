"""`cobalt radar audit-export` — the frozen L52-d bundle (S2-P2 STEP-11; R11).

    cobalt radar audit-export --run <radar_score_run id> --out <dir>
    cobalt radar audit-export --replay <YYYY-MM-DD> --out <dir> [--trade-def <slug>]

WHY. L52 bar (d): whatever computes the score must be auditable by a house
other than the one producing it. The OpenAI house recomputes `card_score`
and every dot from this bundle, network off, with its own checker
(|Δ| ≤ 1e-6 on intermediates, exact integers and labels); a mismatch
blocks enable. This module produces the bundle and nothing else.

WHAT IS IN IT (one JSON file each, canonical: sorted keys, 2-space indent):

    bars.json         per member: the closed i1 rows consumed, daily rows, RVOL
    settings.json     the card settings (curves, bands) + today's enabled keys
    tunables.json     every tunable row read + the taxonomy defaults
    ast.json          every def's predicates: expr, parsed AST, required atoms
    definitions.json  the definitions as evaluated (quality factors included)
    cards.json        the published card rows (--run) / candidate rows (--replay)
    seam.json         the system-side run + score rows (--run) / replay counts
    receipts.json     the stored receipt chain, verbatim (--run only)
    formulas.json     the formulas in words + per-file source hashes
    manifest.json     sha256 of every file above, the bundle sha256, the run's
                      stored hashes re-derived, and Cobalt's own self-check

FROM STORED INPUTS ONLY (L57). `--run` reads the run's receipt chain —
never current `card_dots`, current settings or upserted bars — and
re-derives the run's `tunables_sha256`, `settings_sha256` and
`cohort_sha256` from the receipt's values; any mismatch refuses. It then
replays the receipt with `evaluate.replay_receipt` and refuses when
Cobalt's own recompute disagrees with what it published: a bundle Cobalt
itself cannot reproduce is not sent to another house to discover that.

`--replay` WRITES NOTHING to any store. It runs the same writes-nothing
day replay as `cobalt radar evaluate --replay` and bundles each first-seen
formation as a CANDIDATE row (dots against the current card curves, no
taps, so conviction and card_score are null), labelled as not published.

FROZEN. The out directory must not exist or be empty; nothing is
overwritten. Every refusal happens before the first file is written.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections.abc import Callable, Mapping
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any, Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict

from cobalt.cards.scoring import score_card
from cobalt.settings.card import CardSettings
from cobalt.taxonomy.defaults import TaxonomyDefaults
from cobalt.taxonomy.trade_def import TradeDef

from .evaluate import (
    _SRC,
    ET,
    EVALUATOR_VERSION,
    FORMULA_FILES,
    LoadedDef,
    MemberInput,
    ReplayError,
    _resolve_snapshot,
    bar_row,
    canonical_sha256,
    card_dots,
    daily_row,
    evaluate_member,
    formula_sha256,
    rebuild_members,
    replay_receipt,
)


class AuditExportError(RuntimeError):
    """The bundle cannot be produced faithfully — refuse before writing."""


class BundleManifest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    mode: Literal["run", "replay"]
    source: dict[str, Any]
    generated_at: AwareDatetime
    evaluator_version: str
    files: dict[str, str]
    bundle_sha256: str
    hashes: dict[str, dict[str, Any]]
    self_check: dict[str, Any] | None
    notes: list[str]


FORMULAS_IN_WORDS = {
    "card_score": (
        "card_score = round(conviction × proximity × 100), half-up, computed from the 6-dp stored conviction and "
        "proximity; null when conviction is null or score_suppressed is set"
    ),
    "conviction": "mean(trader_grade of the tapped dots) ÷ 10, half-up to 6 dp; no taps → null; shadow grades never count",
    "proximity": (
        "clamp(1 − |last − trigger| ÷ (3 × |trigger − stop|), 0, 1), half-up to 6 dp; trigger/stop are the card's live "
        "entry/stop; last is the close of the last closed i1 bar"
    ),
    "dot_grade": (
        "piecewise-linear through card.curves[factor] anchors (x ascending), flat beyond the end anchors, clipped to "
        "1–10, rounded half-up once; no anchors → na_reason curve_unset"
    ),
    "suppression": "a computed dot (source cobalt*, tier deterministic, not a desk factor) that is N/A and untapped suppresses card_score",
    "proposed_key": (
        "the highest card.proposed_key band the conviction meets (a_plus_min, a_min, b_min, c_min), snapped DOWN to "
        "an enabled key; null conviction → none"
    ),
    "desk_dots": "catalyst → DESK_NA; market_alignment, sector_alignment → DEFAULT_UNRULED (S2, plan §8 item 4)",
}


def _json_bytes(payload: Any) -> bytes:
    return (json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False, default=str) + "\n").encode("utf-8")


def _ast_json(node: Any) -> Any:
    if isinstance(node, BaseModel):
        return {"node": type(node).__name__, **{name: _ast_json(getattr(node, name)) for name in type(node).model_fields}}
    if isinstance(node, (list, tuple)):
        return [_ast_json(item) for item in node]
    if isinstance(node, (Decimal, datetime, date)):
        return str(node)
    return node


def ast_payload(defs: list[LoadedDef]) -> dict[str, Any]:
    out = []
    for ld in sorted(defs, key=lambda d: d.slug):
        td = ld.definition

        def predicates(items):
            return [
                {"expr": p.expr, "text": p.text, "ast": _ast_json(p.ast) if p.ast is not None else None,
                 "required_atoms": sorted(p.required_atoms)}
                for p in items
            ]

        out.append({
            "slug": ld.slug, "md5": ld.md5, "preconditions": predicates(td.preconditions),
            "avoid": predicates(td.avoid), "radar_watch": predicates(td.radar_watch),
            "quality_factors": [q.model_dump(mode="json") for q in td.quality_factors],
        })
    return {"defs": out}


def formulas_payload(*, run_formula_sha256: str | None) -> dict[str, Any]:
    current = formula_sha256()
    files = {
        path.relative_to(_SRC.parent).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(FORMULA_FILES, key=lambda p: p.relative_to(_SRC.parent).as_posix())
    }
    payload = {"evaluator_version": EVALUATOR_VERSION, "formula_sha256": current, "files": files, **FORMULAS_IN_WORDS}
    if run_formula_sha256 is not None:
        payload["run_formula_sha256"] = run_formula_sha256
        payload["run_formula_matches_current_code"] = run_formula_sha256 == current
    return payload


def _member_payload(member: MemberInput) -> dict[str, Any]:
    return {
        "membership_id": member.membership_id, "ticker": member.ticker, "trade_date": member.trade_date.isoformat(),
        "as_of": member.as_of.isoformat(), "departed": member.departed, "pool_position": member.pool_position,
        "i1": [bar_row(b) for b in member.bars if b.ts + timedelta(minutes=1) <= member.as_of],
        "daily": [daily_row(b) for b in member.daily.bars] if member.daily else None,
        "daily_status": member.daily_status,
        "rvol": member.rvol.model_dump(mode="json") if member.rvol else None,
    }


def _write_bundle(out: Path, payloads: dict[str, Any], manifest_fields: dict[str, Any]) -> BundleManifest:
    out = Path(out)
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise AuditExportError(f"{out} exists and is not empty — a bundle is frozen, never overwritten")
    blobs = {name: _json_bytes(payload) for name, payload in sorted(payloads.items())}
    files = {name: hashlib.sha256(blob).hexdigest() for name, blob in blobs.items()}
    manifest = BundleManifest(
        files=files,
        bundle_sha256=hashlib.sha256(json.dumps(files, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        evaluator_version=EVALUATOR_VERSION,
        **manifest_fields,
    )
    out.mkdir(parents=True, exist_ok=True)
    for name, blob in blobs.items():
        (out / name).write_bytes(blob)
    (out / "manifest.json").write_bytes(_json_bytes(manifest.model_dump(mode="json")))
    return manifest


# ---------------------------------------------------------------------
# --run
# ---------------------------------------------------------------------


def export_run(run_id: int, *, radar_store, card_store, out: Path, clock, generated_at: datetime) -> BundleManifest:
    """`radar_store` (SYSTEM): score_run, scores_for_run.
    `card_store` (USER): receipt_for_run, receipts_chain."""
    run = radar_store.score_run(run_id)
    if run is None:
        raise AuditExportError(f"no radar_score_run {run_id}")
    if run["status"] != "complete":
        raise AuditExportError(f"radar_score_run {run_id} is {run['status']!r}, not complete — it published nothing")
    receipt_id = card_store.receipt_for_run(run_id)
    if receipt_id is None:
        raise AuditExportError(f"radar_score_run {run_id} has no receipt — its numbers have no stored inputs (L57)")
    chain = card_store.receipts_chain(receipt_id)
    index = len(chain) - 1
    try:
        tunables = _resolve_snapshot(chain, "tunables_snapshot", index)
        settings = _resolve_snapshot(chain, "settings_snapshot", index)
        definitions = _resolve_snapshot(chain, "definitions_snapshot", index)
        pool_unit = _resolve_snapshot(chain, "pool_unit", index)
        members = rebuild_members(chain)
    except ReplayError as e:
        raise AuditExportError(f"receipt chain for run {run_id} does not verify: {e}") from e
    target = chain[index]

    derived = {
        "tunables_sha256": canonical_sha256(tunables),
        "settings_sha256": CardSettings.from_rows(settings["card"]).sha256(),
        "cohort_sha256": canonical_sha256(target["ordered_cohort"]),
        "pool_unit_sha256": canonical_sha256(pool_unit),
    }
    stored = {
        "tunables_sha256": run["tunables_sha256"], "settings_sha256": run["settings_sha256"],
        "cohort_sha256": run["cohort_sha256"], "pool_unit_sha256": target["pool_unit_sha256"],
    }
    hashes = {
        key: {"stored": stored[key], "derived": derived[key], "matches": stored[key] == derived[key]}
        for key in derived
    }
    broken = [key for key, value in hashes.items() if not value["matches"]]
    if broken:
        raise AuditExportError(f"run {run_id}: stored hash(es) {broken} do not match the receipt's retained values")

    try:
        evaluations, replayed = replay_receipt(chain, clock=clock)
    except ReplayError as e:
        raise AuditExportError(f"run {run_id}: Cobalt's own replay failed: {e}") from e
    differing = [r.card_id for r in replayed if r.recomputed != r.published]
    scores = radar_store.scores_for_run(run_id)
    by_key = {(ev.membership_id, ev.md5): ev.evaluation for ev in evaluations}
    label_diff = [
        (s["membership_id"], s["trade_def_md5"]) for s in scores
        if by_key.get((s["membership_id"], s["trade_def_md5"])) != s["evaluation"]
    ]
    if differing or label_diff:
        raise AuditExportError(
            f"run {run_id}: Cobalt's replay disagrees with what it published — cards {differing}, "
            f"seam evaluations {label_diff}; no bundle is written"
        )

    defs = [
        LoadedDef(slug=d["slug"], md5=d["md5"], definition=TradeDef.model_validate(d["definition"]))
        for d in definitions["defs"]
    ]
    cards = target["tap_versions"]["cards"]
    payloads = {
        "bars.json": {"members": [_member_payload(m) for m in members]},
        "settings.json": settings,
        "tunables.json": tunables,
        "ast.json": ast_payload(defs),
        "definitions.json": definitions,
        "cards.json": {
            "published": True, "cards_enabled": bool(run["cards_enabled"]), "cards": cards,
            "note": (
                "published card numbers as the run stored them in its receipt" if cards
                else ("dark run (radar.cards_enabled=false): seam rows and receipt only, no card rows"
                      if not run["cards_enabled"] else "no radar card was open or created in this run")
            ),
        },
        "seam.json": {"run": run, "scores": scores, "pool_unit": pool_unit},
        "receipts.json": {"chain": chain},
        "formulas.json": formulas_payload(run_formula_sha256=run["formula_sha256"]),
    }
    notes = []
    if not payloads["formulas.json"]["run_formula_matches_current_code"]:
        notes.append("the formula source changed since this run; the self-check replayed with the current code and agreed")
    return _write_bundle(out, payloads, {
        "mode": "run", "source": {"run_id": run_id}, "generated_at": generated_at, "hashes": hashes,
        "self_check": {"cards": len(replayed), "evaluations": len(scores), "all_equal": True}, "notes": notes,
    })


# ---------------------------------------------------------------------
# --replay
# ---------------------------------------------------------------------


def export_replay(
    day: date,
    *,
    pool_key: str,
    slug_filter: str | None,
    radar_store,
    defs_source: Callable[[], tuple[list[LoadedDef], dict]],
    daily_source,
    tunables: Mapping[str, Any],
    defaults: TaxonomyDefaults,
    settings_values: Mapping[str, Any],
    clock,
    out: Path,
    generated_at: datetime,
) -> BundleManifest:
    from cobalt.taxonomy.loader import merge_tunables

    from .evaluate_cli import _select, replay_formations

    card_settings = CardSettings.from_rows(dict(settings_values))
    report = replay_formations(
        day, pool_key=pool_key, slug_filter=slug_filter, radar_store=radar_store, defs_source=defs_source,
        daily_source=daily_source, tunables=tunables, defaults=defaults, clock=clock, out=lambda _line: None,
    )
    defs, user_rows = defs_source()
    defs = _select(defs, slug_filter)
    rows = merge_tunables(dict(tunables), user_rows)
    scan_interval = int(rows["radar.scan_interval"].value)
    by_slug = {d.slug: d for d in defs}
    admitted = [m for m in radar_store.members_for_day(pool_key, day) if m.get("entered_at") is not None]
    start = datetime.combine(day, datetime.min.time(), ET).astimezone(timezone.utc)
    bars: dict[str, list] = {}
    daily: dict[str, Any] = {}
    members_payload = []
    for member in sorted(admitted, key=lambda m: m["id"]):
        ticker = member["ticker"]
        if ticker not in bars:
            bars[ticker] = radar_store.i1_bars(ticker, start, start + timedelta(days=1))
            try:
                daily[ticker] = (daily_source(ticker, day), "cache-hit")
            except Exception as e:  # recorded, not hidden: the replay evaluated without it too
                daily[ticker] = (None, f"absent: {type(e).__name__}: {e}")
        series, status = daily[ticker]
        members_payload.append({
            "membership_id": member["id"], "ticker": ticker, "trade_date": day.isoformat(),
            "entered_at": str(member.get("entered_at")), "left_at": str(member.get("left_at")),
            "pool_position": member.get("last_rank"), "i1": [bar_row(b) for b in bars[ticker]],
            "daily": [daily_row(b) for b in series.bars] if series else None, "daily_status": status, "rvol": None,
        })

    candidates = []
    for formation in report.formations:
        member = next(m for m in sorted(admitted, key=lambda m: m["id"]) if m["ticker"] == formation.ticker)
        ld = by_slug[formation.slug]
        series, status = daily[formation.ticker]
        inp = MemberInput(
            membership_id=member["id"], ticker=formation.ticker, trade_date=day, as_of=formation.seen_at,
            bars=tuple(b for b in bars[formation.ticker] if b.ts < formation.seen_at), daily=series,
            daily_status=status, rvol=None, pool_position=member.get("last_rank"),
        )
        ev = evaluate_member(ld, inp, tunables=rows, defaults=defaults, scan_interval=scan_interval, clock=clock)
        if ev.evaluation != "formed" or ev.formation is None:
            raise AuditExportError(f"{formation.ticker} {formation.slug}: re-evaluation at {formation.seen_at} did not form")
        trigger, stop = ev.formation.trigger.price, ev.formation.stop.price
        dots = card_dots(ld, ev, card_settings, formation.seen_at, ev.formation.assumed_keys)
        score = score_card(dots, last=ev.last_price if ev.last_price is not None else trigger, trigger=trigger,
                           stop=stop, bands=card_settings.proposed_key, enabled=[])
        candidates.append({
            "ticker": formation.ticker, "slug": ld.slug, "md5": ld.md5, "membership_id": member["id"],
            "direction": ev.formation.trade_direction, "seen_at": formation.seen_at.isoformat(),
            "formed_bar_ts": ev.formation.formed_bar_ts.isoformat(), "trigger": str(trigger), "stop": str(stop),
            "last_price": None if ev.last_price is None else str(ev.last_price),
            "detail": ev.detail.model_dump(mode="json"),
            "observations": {k: v.model_dump(mode="json") for k, v in sorted(ev.observations.items())},
            "candidate": {
                "proximity": str(score.proximity), "conviction": None, "card_score": score.card_score,
                "score_suppressed": score.score_suppressed,
                "dots": [d.model_dump(mode="json") for d in dots],
            },
        })

    tunables_payload = {
        "rows": {k: row.model_dump(mode="json") for k, row in sorted(rows.items())},
        "defaults": defaults.model_dump(mode="json"),
    }
    definitions = {"defs": [
        {"slug": d.slug, "md5": d.md5, "definition": d.definition.model_dump(mode="json", by_alias=True)}
        for d in sorted(defs, key=lambda d: d.slug)
    ]}
    settings_payload = {
        "card": card_settings.rows(),
        "note": "replay: the current card settings; no taps, so no conviction and no proposed key",
    }
    payloads = {
        "bars.json": {"members": members_payload},
        "settings.json": settings_payload,
        "tunables.json": tunables_payload,
        "ast.json": ast_payload(defs),
        "definitions.json": definitions,
        "cards.json": {
            "published": False, "cards": candidates,
            "note": "replay writes nothing: candidate rows for each first-seen formation, never published cards",
        },
        "seam.json": {
            "scans": report.scans, "counts": report.counts, "not_evaluable": report.not_evaluable,
            "path_b_only": report.path_b_only, "formations": len(report.formations),
        },
        "formulas.json": formulas_payload(run_formula_sha256=None),
    }
    hashes = {
        "tunables_sha256": {"derived": canonical_sha256(tunables_payload)},
        "settings_sha256": {"derived": card_settings.sha256()},
        "definitions_sha256": {"derived": canonical_sha256(definitions)},
    }
    return _write_bundle(out, payloads, {
        "mode": "replay", "source": {"replay": day.isoformat()}, "generated_at": generated_at, "hashes": hashes,
        "self_check": None, "notes": ["replay mode: nothing was published, so there is nothing to self-check against"],
    })


# ---------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------


def add_arguments(parser: argparse.ArgumentParser) -> None:
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--run", type=int, metavar="RUN_ID", help="A complete radar_score_run id.")
    source.add_argument("--replay", metavar="YYYY-MM-DD", help="Replay a day (writes nothing to any store).")
    parser.add_argument("--out", required=True, help="Bundle directory (must not exist or be empty).")
    parser.add_argument("--trade-def", dest="trade_def", metavar="SLUG", help="--replay only: one def.")


def command(args: argparse.Namespace) -> None:
    from cobalt.cards.store import CardStore
    from cobalt.session import session_clock
    from cobalt.session.clock import now_utc
    from cobalt.settings.store import TraderSettingsStore
    from cobalt.taxonomy.loader import load_defaults, load_tunables
    from cobalt.taxonomy.store import TradeDefStore

    from .config import load_config
    from .evaluate_cli import CachedDailyBars
    from .store import RadarStore

    clock = session_clock()
    if args.run is not None:
        if args.trade_def:
            raise SystemExit("--trade-def applies to --replay only; a run bundle carries every def the run evaluated")
        manifest = export_run(args.run, radar_store=RadarStore(), card_store=CardStore(), out=Path(args.out),
                              clock=clock, generated_at=now_utc())
    else:
        config = load_config()
        manifest = export_replay(
            date.fromisoformat(args.replay), pool_key=config.pool_key, slug_filter=args.trade_def,
            radar_store=RadarStore(), defs_source=TradeDefStore().loaded_for_evaluation,
            daily_source=CachedDailyBars(Path(config.cache.dir)).load, tunables=load_tunables().by_key,
            defaults=load_defaults(), settings_values=TraderSettingsStore().values(), clock=clock,
            out=Path(args.out), generated_at=now_utc(),
        )
    print(f"audit bundle ({manifest.mode}) written to {args.out}")
    for name, digest in sorted(manifest.files.items()):
        print(f"  {digest}  {name}")
    print(f"  bundle sha256 {manifest.bundle_sha256}")
    for note in manifest.notes:
        print(f"  NOTE: {note}")


__all__ = ["AuditExportError", "BundleManifest", "FORMULAS_IN_WORDS", "add_arguments", "ast_payload", "command",
           "export_replay", "export_run", "formulas_payload"]
