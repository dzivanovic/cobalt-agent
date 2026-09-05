"""F7 card state machine — the states, the edges, and who may move them.

Charter §3 F7: "WATCH -> ARMED -> TRIGGERED -> FILLED -> CLOSED /
PASSED / EXPIRED / MISSED, every transition persisted with evidence;
trigger while unarmed = MISSED, counted not hidden. Test: DRC counts
match Postgres rows; no card exists without a state."

TWO LAWS ARE ENCODED HERE, and they are the whole point of the module:

1. **No card exists without a state.** A card row is created together
   with its genesis transition (`from_state` NULL -> WATCH); there is no
   moment at which a row is state-less, and `state` is NOT NULL.
2. **No state changes without a transition row.** `state` on the card is
   a cache of the last row in `card_transitions`; the store writes both
   in ONE transaction or neither.

THE EDGE TABLE IS DATA, IN ONE PLACE. `ALLOWED` below is the single
authority — the store, the sheet's button set, the tests and the DevDocs
page all read it rather than restating it. `edge_table_markdown()`
renders it, so the wiki page cannot drift from the code that enforces it
(the DevDoc is generated from this function, not typed by hand).

ILLEGAL EDGES ARE REFUSED, NEVER COERCED. There is no "closest legal
state" fallback and no silent no-op: `IllegalTransition` names the edge
it refused and lists what WAS legal from there. A card that reached a
wrong state quietly is a card whose DRC count is wrong, and F7's
acceptance test is precisely that those counts match Postgres.
"""

from __future__ import annotations

from enum import Enum


class CardState(str, Enum):
    """The eight states a card can be in. `str` mixin so a value stamps
    straight into a `text` column and compares equal to its own name in
    SQL — the same reason `Session` carries one."""

    WATCH = "WATCH"
    ARMED = "ARMED"
    TRIGGERED = "TRIGGERED"
    FILLED = "FILLED"
    CLOSED = "CLOSED"
    PASSED = "PASSED"
    EXPIRED = "EXPIRED"
    MISSED = "MISSED"

    def __str__(self) -> str:
        return self.value


class Origin(str, Enum):
    """Where a card came from. A property of the CARD, not of a move.

    F7's ONE-CLICK FILL (CTO review of S1-P2, 2026-09-04) is allowed on
    `manual` cards and refused on `radar` ones, and that is the whole
    reason this enum exists. A card Dejan wrote himself and then filled
    was armed and triggered in his head and in DAS — Cobalt was simply
    not asked to watch it happen, and making him tap three buttons to say
    so is bookkeeping, not evidence. A card the S2 RADAR proposed is the
    opposite case: the detector's whole claim is that it SAW the arm and
    the trigger, so a fill that skipped them is a hole in the detector's
    record, and it is refused rather than papered over.
    """

    MANUAL = "manual"
    RADAR = "radar"

    def __str__(self) -> str:
        return self.value


class Actor(str, Enum):
    """Who moved the card. Every transition row carries one.

    The distinction is not bookkeeping: Dejan's taps are the calibration
    set (Charter §1, "human rules the grade"), so a state Cobalt reached
    on its own and a state he chose must never be summed together.
    """

    COBALT = "cobalt"
    YOU = "you"

    def __str__(self) -> str:
        return self.value


#: THE edge table. `from -> {legal to}`. One table, in code, exported.
ALLOWED: dict[CardState, frozenset[CardState]] = {
    CardState.WATCH: frozenset(
        {CardState.ARMED, CardState.PASSED, CardState.EXPIRED, CardState.MISSED}
    ),
    # ARMED -> WATCH is `disarm`: the one edge that walks backwards, and
    # it is deliberate. Nothing to decide while armed except disarm
    # (card-spec §2.2), so the way out has to exist.
    CardState.ARMED: frozenset(
        {CardState.WATCH, CardState.TRIGGERED, CardState.EXPIRED}
    ),
    CardState.TRIGGERED: frozenset(
        {CardState.FILLED, CardState.PASSED, CardState.EXPIRED}
    ),
    CardState.FILLED: frozenset({CardState.CLOSED}),
    CardState.CLOSED: frozenset(),
    CardState.PASSED: frozenset(),
    CardState.EXPIRED: frozenset(),
    CardState.MISSED: frozenset(),
}

#: Terminal = no outgoing edge. Derived from ALLOWED, never listed twice
#: (one-path rule applied to a constant).
TERMINAL: frozenset[CardState] = frozenset(s for s, to in ALLOWED.items() if not to)

#: States in which the STOP is still the trader's to move (mock decision
#: 11: "stop is editable in WATCH and IN-TRADE; key is frozen once
#: armed"). IN-TRADE is FILLED here — the card is live and stops move
#: with structure.
STOP_EDITABLE: frozenset[CardState] = frozenset({CardState.WATCH, CardState.FILLED})

#: The KEY (grade) is frozen from ARMED onward — it is a risk
#: commitment, not a view (decision 11). Everything that is not WATCH is
#: at-or-past ARMED, including the terminal states, where nothing is
#: editable at all.
KEY_EDITABLE: frozenset[CardState] = frozenset({CardState.WATCH})

#: The state a one-click fill lands on, and the state it walks from.
#: `fill_path()` derives the route from the edge table, so the shortcut
#: is a CONVENIENCE OVER the table and never a new edge.
FILL_TARGET = CardState.FILLED

#: The one edge that means "the trigger fired but the card was never
#: armed". Charter §3 F7: counted, not hidden — so it is a real state
#: with a real transition row, and it requires a reason (store.py).
MISSED_EDGE = (CardState.WATCH, CardState.MISSED)


class IllegalTransition(RuntimeError):
    """A refused edge. Carries both ends so callers can render it."""

    def __init__(self, from_state: CardState, to_state: CardState, card_id: int | None = None):
        self.from_state = from_state
        self.to_state = to_state
        self.card_id = card_id
        legal = sorted(s.value for s in ALLOWED[from_state])
        where = f"card {card_id}: " if card_id is not None else ""
        if from_state in TERMINAL:
            detail = (
                f"{from_state.value} is TERMINAL — a card that reached it is "
                "finished, and reopening one would silently change a count "
                "the DRC has already reported"
            )
        else:
            detail = f"legal from {from_state.value}: {', '.join(legal)}"
        super().__init__(
            f"REFUSED {where}{from_state.value} -> {to_state.value} is not a legal "
            f"card transition. {detail}. The edge is not coerced to the nearest "
            "legal state and it is not silently dropped (F7: no state changes "
            "without a transition row, and no transition row without a legal edge)."
        )


def is_legal(from_state: CardState, to_state: CardState) -> bool:
    return to_state in ALLOWED[from_state]


def assert_edge(
    from_state: CardState, to_state: CardState, *, card_id: int | None = None
) -> None:
    """Refuse, loudly and by name, or return. The ONE gate."""
    if not is_legal(from_state, to_state):
        raise IllegalTransition(from_state, to_state, card_id)


def fill_path(from_state: CardState) -> list[CardState]:
    """The shortest LEGAL route from `from_state` to FILLED.

    Breadth-first over `ALLOWED`, so the shortcut cannot invent an edge:
    every state it returns is one the edge table already permits, and
    every hop becomes a real `card_transitions` row. Returns `[]` when
    FILLED is unreachable (a terminal card, a PASSED card) — the caller
    refuses; it does not coerce.

    Today WATCH -> [ARMED, TRIGGERED, FILLED] and ARMED -> [TRIGGERED,
    FILLED]. Neither list is written down here. Add an edge to the table
    and this follows it.
    """
    if from_state is FILL_TARGET:
        return []
    queue: list[tuple[CardState, list[CardState]]] = [(from_state, [])]
    seen = {from_state}
    while queue:
        state, path = queue.pop(0)
        for nxt in sorted(ALLOWED[state], key=lambda s: s.value):
            if nxt in seen:
                continue
            route = [*path, nxt]
            if nxt is FILL_TARGET:
                return route
            seen.add(nxt)
            queue.append((nxt, route))
    return []


def edge_table_markdown() -> str:
    """The edge table as a markdown table, for the DevDocs page.

    Generated, not transcribed: `docs/40 - DevDocs` renders THIS, so the
    wiki and the enforcement cannot disagree. `cobalt cards edges` prints
    it too.
    """
    lines = [
        "| From | Legal `to` states | Terminal |",
        "|---|---|---|",
    ]
    for state in CardState:
        to = sorted(s.value for s in ALLOWED[state])
        lines.append(
            f"| `{state.value}` | {', '.join(f'`{t}`' for t in to) or '— (none)'} "
            f"| {'yes' if state in TERMINAL else 'no'} |"
        )
    return "\n".join(lines)


__all__ = [
    "ALLOWED",
    "Actor",
    "FILL_TARGET",
    "CardState",
    "IllegalTransition",
    "KEY_EDITABLE",
    "MISSED_EDGE",
    "STOP_EDITABLE",
    "TERMINAL",
    "assert_edge",
    "Origin",
    "edge_table_markdown",
    "fill_path",
    "is_legal",
]
