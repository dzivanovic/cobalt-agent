"""The DRC's reused unit helpers (Slice 2, item 4 → DRC D3).

THE 15:40 PREFILL IS RETIRED (DRC D3, v2 §8 `[F-22]`): the note is created
by ONE function, the input-driven DRC build (`cobalt.drc.build.
run_drc_build`), from HIS template (`5 - Templates/DRC.md`) — never the
repo template `drc.md.j2` (deleted), never a create-then-return (L1). What
stays here is what the build REUSES (v2 §8 `[F-26]`), each the one copy:

    format_risk_parameters        the sheet-mode risk line (drc-risk/risk_parameters)
    format_card_reconcile_block   the cards with no trade (in drc-rules/rules_check)
    format_rules_check_block      his checkboxes + the card reconcile
    RISK_PLACEMENT / TRADES_PLACEMENT / RULES_PLACEMENT   first-landing anchors

`format_tickers_block` (cards → the build's per-trade blocks from the
trading log), `parse_fill_updates` and `find_trade_note_for_card` (the fill
columns and the trade-note seam) left the DRC path with it (v2 §8).

COUNTS (L28 step 3): "cards written" and "trades taken" are two numbers,
shown as two — the build's summary carries both.
"""

import re
from typing import Optional

from cobalt.aset.models import Grade
from cobalt.session.clock import ET
from cobalt.vaultwrite import Placement, after_pattern

_PNL_HEADING_RE = re.compile(r"^###\s*PnL on the day.*$")
_RISK_PARAMS_LINE_RE = re.compile(r"^Risk Parameters:.*$")
_TRADES_HEADING_RE = re.compile(r"^###\s*Catalyst \+ Set Up \+ Trades\s*$")


def format_card_reconcile_block(cards: list[dict]) -> str:
    """A card is a written plan; a card the build matched to a trade was
    taken. Every other card is a pass, a phantom, or premarket
    exploration — and Cobalt does not guess which. One checklist line per
    card with no trade; Dejan answers taken / passed / discarded by hand."""
    lines = [
        f"- [ ] {c['created_at'].astimezone(ET):%H:%M:%S} {c['ticker']} "
        f"({c['grade']} {str(c['direction']).upper()}) — taken / passed / discarded?"
        for c in cards
    ]
    if not lines:
        return "(every card today matched a trade — nothing to reconcile)\n"
    return "\n".join(lines) + "\n"


def format_risk_parameters(cards: list[dict], sheet_modes_cfg) -> str:
    modes_used = sorted({c["sheet_mode"] for c in cards if c.get("sheet_mode")})
    if not modes_used:
        return "no sheet-mode cards today (configs/cobalt/aset.yaml has the ladder)"
    parts = []
    for mode in modes_used:
        grade_parts = ", ".join(
            f"{g.value}:${sheet_modes_cfg.dollars_for(mode, g)}"
            for g in Grade
            if sheet_modes_cfg.is_enabled(g)
        )
        parts.append(f"{mode.upper()} — {grade_parts}")
    return "; ".join(parts)


def risk_parameters_line(cards: list[dict]) -> str:
    """The `drc-risk/risk_parameters` body's value for the DRC build: the
    sheet-mode dollars of today's cards (the sheet config, as before)."""
    from cobalt.aset.config import load_sheet_modes_config

    return format_risk_parameters(cards, load_sheet_modes_config())


def rules_checkbox_block() -> str:
    """The DRC build's rules checkboxes: Rules.md re-parsed (inside the
    resident that runs the build, F41), mode-aware exactly as the morning
    note shows them (`daily.format_rules_checkbox_block`)."""
    from cobalt.aset.config import load_sheet_modes_config

    from .daily import apply_mode_aware_sizing, format_rules_checkbox_block
    from .rules_gen import regenerate_rules_config

    return format_rules_checkbox_block(
        apply_mode_aware_sizing(regenerate_rules_config().rules, load_sheet_modes_config())
    )


def format_rules_check_block(context: dict) -> str:
    return "\n".join(
        [
            "**Rules (copied from the morning note's checklist — Rules.md is the source):**",
            context["rules_checkbox_block"].rstrip("\n"),
            "",
            "**Card reconcile (cards with no trade — taken / passed / discarded?):**",
            context["card_reconcile_block"].rstrip("\n"),
        ]
    )


# ---------------------------------------------------------------------------
# Placement of each section the first time it lands in an existing note
# ---------------------------------------------------------------------------


def _risk_span(lines: list[str]) -> Optional[tuple[int, int]]:
    """Insert AFTER `Risk Parameters: ...` (or under the PnL heading).

    An earlier draft WRAPPED that line so Cobalt's computed figures
    would replace it. That was wrong and the 09-03 production dry-run
    caught it: in a Templater-created DRC the line reads
    `Risk Parameters: A:5R, B:1R, C:0.5R` — Dejan's own text, which
    Cobalt cannot prove it wrote. L28.2 is absolute about that: text it
    did not write is preserved verbatim, in position. So the section is
    inserted BELOW it and his line stands. A stale-looking duplicate is
    the correct price; silently rewriting his line is not.
    """
    for i, line in enumerate(lines):
        if _RISK_PARAMS_LINE_RE.match(line):
            return (i + 1, i + 1)
    for i, line in enumerate(lines):
        if _PNL_HEADING_RE.match(line):
            return (i + 1, i + 1)
    return None


RISK_PLACEMENT = Placement("below the 'Risk Parameters:' line (or under '### PnL on the day')", _risk_span)
TRADES_PLACEMENT = after_pattern(_TRADES_HEADING_RE, "under '### Catalyst + Set Up + Trades'")
# No anchor: the rules check is the last thing in the DRC by design, and
# L28's default placement (end of note, nothing above touched) is exactly
# where it belongs.
RULES_PLACEMENT = None
