"""`cobalt cards shadow-report [--since YYYY-MM-DD]` (S2-P2 STEP-10).

The evidence half of the shadow-mode promotion law (L7). Every computed
dot runs in SHADOW through S2 (R6): the engine grades it, the card shows
it hollow, and his tap is recorded next to the engine grade that was on
screen (`"user".card_dot_taps.engine_grade_at_tap`). This report reads
`"user".shadow_agreement_v` — one row per factor × ET trading day with
every |tap − engine| delta — and, per factor, compares

    sessions (trading days with ≥1 pair) ≥ bar.sessions
    pairs                                 ≥ bar.pairs
    median |Δ| over ALL pairs             ≤ bar.median_max
    share of pairs with |Δ| ≤ 2           ≥ bar.within2_min

against `card.shadow_promotion_bar` in `"user".trader_settings` (09-14
group-2 ruling: 10 / 30 / 1 / 0.90), printing GATE MET or GATE NOT MET
with the misses named.

IT NEVER FLIPS ANYTHING. A met gate is evidence for the curve tribunal
and the HITL decision, not the decision: this module reads one view and
one setting and prints. There is no write in it.

No bar loaded → refuse loud; the bar is his setting, never defaulted.
"""

            f"{f.factor}: sessions {f.sessions} · pairs {f.pairs} · median |Δ| {_fmt(f.median_abs_delta)} · "
            f"within-2 {_fmt(f.within2_share)} · {status}"
        )
    return "\n".join(lines)


def cmd_shadow_report(args: argparse.Namespace) -> None:
    bar = CardSettingsReader().current().shadow_promotion_bar
    if bar is None:
        raise SystemExit(
            "card.shadow_promotion_bar is not set in \"user\".trader_settings — the bar is his setting and is "
            "never defaulted; load it with `cobalt settings load --card <file> --sha256 <hash> --apply`"
        )
    since = date.fromisoformat(args.since) if args.since else None
    rows = CardStore().shadow_agreement(since)
    print(render_report(shadow_report(rows, bar=bar, since=since)))


__all__ = ["AgreementRow", "FactorAgreement", "ShadowReport", "ShadowReportError", "cmd_shadow_report",
