"""F23 §2.1: the playbook data — setups from the vault, cards from one SELECT.

Setups are the validated defs `load_vault_trade_defs` returns (the one
loader, L3); a def's `family` list says which decks it is on, so a def with
two families is on both. Cards are the radar cards (`origin = 'radar'`),
whose `trade_def_slug` is the one deterministic link to a family.

`group()` is pure: rows in, decks out. NOTHING IS DROPPED (L1): a card whose
slug is not a loaded def goes to `unfiled` with its reason (`draft` when the
slug is a draft note, else `no note`); a null `formed_at` is shown, last.
ORDER IS TIME ONLY (L52): `formed_at DESC NULLS LAST, id DESC` — never
`card_score`, `conviction` or `proximity`, which are shown as stored and
never sorted, filtered or tie-broken on.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any, Iterable, Optional

from cobalt.taxonomy.trade_def import Family
from cobalt.taxonomy.vault_loader import VaultTradeDefs

FAMILIES: tuple[str, ...] = tuple(f.value for f in Family)
UNFILED = "unfiled"
#: Every run writes exactly these six decks (FINAL [F-09]).
DECK_NAMES: tuple[str, ...] = FAMILIES + (UNFILED,)
REASON_DRAFT = "draft"
REASON_NO_NOTE = "no note"

#: THE one read of cards. USER side; no ORDER BY here — `newest_first` is
#: the one order, applied after grouping.
CARDS_SQL = (
    "SELECT id, ticker, direction, state, trade_def_slug, formed_at, sized_grade, tapped_grade, "
    "trigger_price, structural_stop, entry, stop, card_score, why "
    'FROM "user".aset_sizings WHERE origin = %s'
)


@dataclass(frozen=True)
class Card:
    id: int
    ticker: str
    slug: str
    direction: str
    state: str
    formed_at: Optional[datetime]
    #: `sized_grade`, else `tapped_grade` (FINAL §2.2.3).
    grade: Optional[str]
    trigger_price: Optional[Decimal]
    structural_stop: Optional[Decimal]
    entry: Optional[Decimal]
    stop: Optional[Decimal]
    card_score: Optional[int]
    why: Optional[str]
    #: The setup's display name; None on an unfiled card.
    setup_name: Optional[str] = None
    #: The def's families; empty on an unfiled card.
    families: tuple[str, ...] = ()
    #: `draft` / `no note` on an unfiled card; None on a filed one.
    reason: Optional[str] = None


@dataclass(frozen=True)
class Setup:
    slug: str
    name: str
    note_path: str
    trade_class: str
    families: tuple[str, ...]
    #: Its cards on this deck.
    cards: int


@dataclass(frozen=True)
class Deck:
    name: str
    setups: tuple[Setup, ...]
    #: The cards shown, newest first.
    cards: tuple[Card, ...]
    #: Every card of this family before `latest_per_family`.
    in_family: int
    #: K: cards on this deck whose def lists another family (FINAL [F-15]).
    also_elsewhere: int

    @property
    def is_unfiled(self) -> bool:
        return self.name == UNFILED


@dataclass(frozen=True)
class Playbook:
    decks: tuple[Deck, ...]
    #: Draft slugs: listed on stdout, never in a deck.
    drafts: tuple[str, ...]

    def deck(self, name: str) -> Deck:
        for deck in self.decks:
            if deck.name == name:
                return deck
        raise KeyError(f"no deck {name!r}; the decks are {', '.join(DECK_NAMES)}")


def newest_first(cards: Iterable[Card]) -> list[Card]:
    """`formed_at DESC NULLS LAST, id DESC` — the only order."""
    return sorted(
        cards,
        key=lambda c: (c.formed_at is None, -c.formed_at.timestamp() if c.formed_at else 0.0, -c.id),
    )


def _card(row: dict[str, Any], **extra: Any) -> Card:
    return Card(
        id=int(row["id"]), ticker=row["ticker"], slug=row["trade_def_slug"], direction=row["direction"],
        state=row["state"], formed_at=row["formed_at"], grade=row["sized_grade"] or row["tapped_grade"],
        trigger_price=row["trigger_price"], structural_stop=row["structural_stop"], entry=row["entry"],
        stop=row["stop"], card_score=row["card_score"], why=row["why"], **extra,
    )


def group(defs: VaultTradeDefs, rows: Iterable[dict[str, Any]], *, latest_per_family: Optional[int]) -> Playbook:
    """The six decks from one loader read and one SELECT's rows."""
    by_slug = {d.slug: d for d in defs.defs}
    families_of = {d.slug: tuple(dict.fromkeys(f.value for f in d.definition.family)) for d in defs.defs}
    drafts = tuple(d.slug for d in defs.drafts)
    filed: dict[str, list[Card]] = {f: [] for f in FAMILIES}
    unfiled: list[Card] = []
    for row in rows:
        slug = row["trade_def_slug"]
        loaded = by_slug.get(slug)
        if loaded is None:
            unfiled.append(_card(row, reason=REASON_DRAFT if slug in drafts else REASON_NO_NOTE))
            continue
        card = _card(row, setup_name=loaded.name, families=families_of[slug])
        for family in card.families:
            filed[family].append(card)

    decks = []
    for family in FAMILIES:
        ordered = newest_first(filed[family])
        shown = ordered if latest_per_family is None else ordered[:latest_per_family]
        setups = tuple(
            Setup(slug=d.slug, name=d.name, note_path=d.note_path, trade_class=d.definition.trade_class.value,
                  families=families_of[d.slug], cards=sum(1 for c in shown if c.slug == d.slug))
            for d in defs.defs if family in families_of[d.slug]
        )
        decks.append(Deck(name=family, setups=setups, cards=tuple(shown), in_family=len(ordered),
                          also_elsewhere=sum(1 for c in shown if len(c.families) > 1)))
    decks.append(Deck(name=UNFILED, setups=(), cards=tuple(newest_first(unfiled)), in_family=len(unfiled),
                      also_elsewhere=0))
    return Playbook(decks=tuple(decks), drafts=drafts)


def fetch_radar_rows(dbname: str) -> list[dict[str, Any]]:
    """THE one SELECT (USER side, read only). A dead database raises (L1)."""
    from cobalt import db

    with db.connect(dbname, side=db.Side.USER) as conn:
        cur = conn.execute(CARDS_SQL, ("radar",))
        columns = [d.name for d in cur.description]
        return [dict(zip(columns, r)) for r in cur.fetchall()]


def load_playbook(latest_per_family: Optional[int]) -> Playbook:
    """The vault's defs (`COBALT_VAULT_PATH` / the mode's vault) and this
    mode's database, grouped. Every failure propagates (L1)."""
    from cobalt import env
    from cobalt.taxonomy.vault_loader import load_vault_trade_defs

    defs = load_vault_trade_defs()
    return group(defs, fetch_radar_rows(env.resolve_db_name()), latest_per_family=latest_per_family)


__all__ = [
    "CARDS_SQL", "DECK_NAMES", "FAMILIES", "REASON_DRAFT", "REASON_NO_NOTE", "UNFILED",
    "Card", "Deck", "Playbook", "Setup", "fetch_radar_rows", "group", "load_playbook", "newest_first",
]
