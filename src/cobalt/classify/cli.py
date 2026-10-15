"""`cobalt classify` — the JEV trial's commands.

    cobalt classify discover --out scratch/openrouter-models-<YYYYMMDD>.json

`discover` is KEYLESS: two public GETs, no credential — his id's per-model
endpoints record first (the authority, desk R46), then the general list
(only to record other matching ids). It verifies HIS model id
(`trial.yaml` `model_id`, R42) and writes, guarded, inside `scratch/`:
`<out>` = the endpoints record, ONLY the other matching entries, the
general list's count and `ruled_id_listed: true`; `<out stem>.endpoints.json`
= the endpoints response body byte for byte (the fixture's source, L45).

    cobalt classify probe [--set FLOOR|S1] --out scratch/probe-[s1-]<YYYYMMDDTHHMMSS>.json

`probe` is KEYED and METERED: ONE call through the System One door, and
ONE metered call per set per branch. `FLOOR` (the default) asks its one
Noul — which by the schema carries no probabilities / confidence; build
`31` ran it. `S1` (JEV fix r3, his R89) asks a choice and a score, the
answer types that carry them; `--out` must be `scratch/probe-s1-….json`.
Run only through `ops/run_classify_trial.sh` (desk R42).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import route, trial
from .collector import ClassifyError, OpenRouterClassifier
from .config import REPO_ROOT, SET_NAMES, load_trial_config


def _scratch_out(cfg, raw: str) -> Path:
    """`--out` must land inside the configured scratch results dir."""
    p = Path(raw)
    p = (p if p.is_absolute() else REPO_ROOT / p).resolve()
    root = cfg.results_path()
    if p != root and root not in p.parents:
        raise ClassifyError(f"--out {raw!r} resolves outside {root} — refused")
    return p


def cmd_discover(args: argparse.Namespace) -> None:
    cfg = load_trial_config()
    clf = OpenRouterClassifier(cfg)
    out = _scratch_out(cfg, args.out)
    d = clf.discover_detail()
    artifact = d.artifact(cfg.model_id)
    clf._guard_stored(artifact)
    clf._guard_stored(d.raw_record.decode("utf-8"))
    raw_out = out.with_name(f"{out.stem}.endpoints.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(artifact, indent=2, ensure_ascii=False) + "\n")
    raw_out.write_bytes(d.raw_record)
    others = ", ".join(m.id for m in d.others) or "none"
    print(
        f"DISCOVER ruled={cfg.model_id} ruled_listed=yes (per-model endpoints) "
        f"models_listed={d.total} others={others} wrote={out} raw={raw_out}"
    )


def _present(rec, field: str) -> str:
    return "present" if any(getattr(a, field) is not None for a in rec.answers) else "absent"


#: The sets a probe may ask, and the `--out` name prefix of each. FLOOR's
#: glob `probe-*.json` also sees every S1 file; S1's sees only its own.
PROBE_SETS = {"FLOOR": "probe-", "S1": "probe-s1-"}


def cmd_probe(args: argparse.Namespace) -> None:
    """ONE metered call of `--set` (FLOOR by default, or S1) through
    `classify()` — the same guards, ledger check and ledger record as
    every trial call. One probe per set per branch: an existing
    `scratch/<prefix>*.json` refuses the run.

    Writes `<out>` (the guarded CallRecord) and `<out stem>.raw.json` (the
    guarded raw body, byte for byte). Prints EXACTLY one `PROBE …` line.
    A body the stored guard refuses is not written; the error names the
    KIND of hit, never the text."""
    name = getattr(args, "set", "FLOOR")
    if name not in PROBE_SETS:
        raise ClassifyError(f"--set {name!r}: a probe asks {' or '.join(PROBE_SETS)} only — refused")
    prefix = PROBE_SETS[name]
    cfg = load_trial_config()
    out = _scratch_out(cfg, args.out)
    if not (out.name.startswith(prefix) and out.suffix == ".json"):
        raise ClassifyError(
            f"--out {args.out!r} must be scratch/{prefix}<YYYYMMDDTHHMMSS>.json — refused"
        )
    existing = sorted(p.name for p in cfg.results_path().glob(f"{prefix}*.json"))
    if existing:
        raise ClassifyError(
            f"a {name} probe already ran on this branch ({', '.join(existing)}) — one metered "
            "probe per set per branch; refused, zero calls"
        )
    clf = OpenRouterClassifier(cfg)
    qset, items = cfg.resolve(name)
    guard = clf.literal_guard_state()
    rec, raw = clf._classify(qset, items[0], overrun_check=False)

    raw_out = out.with_name(f"{out.stem}.raw.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(rec.model_dump_json(indent=2) + "\n")
    raw_out.write_bytes(raw)
    print(
        f"PROBE status={rec.http_status} model={rec.model_returned} "
        f"provider={rec.provider_returned or 'none'} latency_ms={rec.latency_ms:.1f} "
        f"http_ms={rec.http_ms:.1f} cost_usd={rec.cost_usd} cost_source={rec.cost_source} "
        f"probabilities={_present(rec, 'probabilities')} confidence={_present(rec, 'confidence')} "
        f"ledger_usd={clf.ledger.spent()} cap_usd={cfg.spend_cap_usd:g} guard_literals={guard}"
    )
    if rec.cost_usd is not None:
        clf.ledger.check_cost(returned=rec.cost_usd, projected=rec.projected_usd)
    if rec.status != "ok":
        raise ClassifyError(f"probe status {rec.status}: {rec.error}")


def cmd_trial(args: argparse.Namespace) -> None:
    """`--dry-run` renders, guards and projects every call — ZERO network.
    `--run` is KEYED and METERED (never run by build `28`)."""
    cfg = load_trial_config()
    clf = OpenRouterClassifier(cfg)
    p = trial.plan(cfg, clf, args.set, reps=args.reps, mode=args.mode,
                   questions=args.questions, reverse=args.reverse)
    if args.dry_run:
        print(trial.dry_run(p, clf))
        return
    _, summary = trial.run(p, clf, tag=args.tag or "untagged")
    print(summary)


def add_parser(sub) -> None:
    p = sub.add_parser("classify", help="Typed-classifier trial (JEV, 2026-09-23).")
    csub = p.add_subparsers(dest="command", required=True)

    d = csub.add_parser("discover", help="KEYLESS: verify the ruled model id on OpenRouter's public list.")
    d.add_argument("--out", required=True, help="scratch/openrouter-models-<YYYYMMDD>.json")
    d.set_defaults(func=cmd_discover)

    pr = csub.add_parser("probe", help="KEYED, METERED: one call of one set, once per set per branch (via the wrapper).")
    pr.add_argument("--set", choices=tuple(PROBE_SETS), default="FLOOR")
    pr.add_argument("--out", required=True, help="scratch/probe-[s1-]<YYYYMMDDTHHMMSS>.json")
    pr.set_defaults(func=cmd_probe)

    t = csub.add_parser("trial", help="Run one trial set: --dry-run (nothing sent) or --run (KEYED, METERED).")
    t.add_argument("--set", required=True, choices=SET_NAMES)
    t.add_argument("--reps", type=int, default=1)
    t.add_argument("--mode", choices=trial.MODES, default="single")
    t.add_argument("--questions", type=int, default=None, help="the first n questions (plan M2)")
    t.add_argument("--reverse", action="store_true", help="the question map reversed (plan M6)")
    how = t.add_mutually_exclusive_group(required=True)
    how.add_argument("--dry-run", dest="dry_run", action="store_true")
    how.add_argument("--run", action="store_true")
    t.add_argument("--tag", default=None)
    t.set_defaults(func=cmd_trial)

    # card 591: the JEV shadow router (`route`) and its weekly read (`route-read`)
    route.add_route_parsers(csub)


__all__ = ["add_parser"]
