"""The trader's radar-card settings — five `"user".trader_settings` keys
(S2-P2, rulings R7/R9, Astra R1-5).

    radar.cards_enabled         the dark-ship switch (R9)
    card.proposed_key           conviction bands -> proposed key (R7)
    card.curves                 per-factor piecewise-linear anchors (R7)
    card.alignment_default      with/flat/against grades + flat_pct
    card.shadow_promotion_bar   the shadow-report gate (STEP-10)

THE WRITE PATH IS HIS HAND. `cobalt settings load --card <file> --sha256
<hash> --apply` — the file he reviewed, byte-exact (the hash is of the
file's bytes, checked before anything parses), a per-key diff against the
database, ONE `put` (one transaction, deletes included) and a round-trip
read before success is claimed. `--dry-run` prints the diff and the hash
and writes nothing. A trader-run apply is exempt from the HITL token
(L28, amended 2026-09-15); its trace is the command, hash and time.

THE FILE FORMAT (STEP-D1/D2):

    card_settings:
      radar.cards_enabled: false
      card.proposed_key: {a_plus_min: 0.9, a_min: 0.8, b_min: 0.6, c_min: 0.4}
      card.curves:
        rvol: [[1, 1], [3, 6], [10, 10]]
      card.alignment_default: {with_grade: 8, flat_grade: 5, against_grade: 2, flat_pct: 0.15}
      card.shadow_promotion_bar: {sessions: 10, pairs: 30, median_max: 1, within2_min: 0.90}

The file is the WHOLE card-settings set: a key it omits is deleted from
the database. `radar.cards_enabled` is required; the other four are
dark-only-optional — absent is `None`, never a default — and
`radar.cards_enabled: true` refuses without `card.proposed_key` and
`card.curves`, because an enabled radar with no bands or curves would
publish cards whose keys and grades nobody set.

WHAT IS NOT HERE. `card.dot.*` and `card.health.*` are engine tunables
in `configs/cobalt/taxonomy/tunables.yaml` (L53) and are refused by name;
the seven sheet/day-mode keys have their own `--from`/`--from-git` path
and are refused too. Two authorities for one value is the one-path rule's
failure, so neither loader accepts the other's keys.

READ PER CYCLE. `CardSettingsReader.current()` reads the store on every
call. The S5 evaluate stage and the card routes call it per scan/request,
which is what lets a D2 apply take effect without a restart (plan §5).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from cobalt.session import assert_writable

from .models import SETTING_KEYS, TraderSettingsError
from .store import TraderSettingsStore

CARDS_ENABLED = "radar.cards_enabled"
PROPOSED_KEY = "card.proposed_key"
CURVES = "card.curves"
ALIGNMENT_DEFAULT = "card.alignment_default"
SHADOW_PROMOTION_BAR = "card.shadow_promotion_bar"

CARD_SETTING_KEYS = (CARDS_ENABLED, PROPOSED_KEY, CURVES, ALIGNMENT_DEFAULT, SHADOW_PROMOTION_BAR)

#: Engine tunables, never settings (L53).
TUNABLES_ONLY_PREFIXES = ("card.dot.", "card.health.")

FILE_ROOT = "card_settings"


class CardSettingsError(TraderSettingsError):
    """Card settings missing, malformed or unverified — refuse, never default."""


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class ProposedKeyBands(_Strict):
    """Conviction (0–1, the mean tap ÷ 10) at or above which a key is
    proposed. Strictly descending, so every conviction falls in one band."""

    a_plus_min: Decimal = Field(ge=0, le=1)
    a_min: Decimal = Field(ge=0, le=1)
    b_min: Decimal = Field(ge=0, le=1)
    c_min: Decimal = Field(ge=0, le=1)

    @model_validator(mode="after")
    def _descending(self) -> ProposedKeyBands:
        if not self.a_plus_min > self.a_min > self.b_min > self.c_min:
            raise ValueError(
                "card.proposed_key bands must strictly descend a_plus_min > a_min > b_min > c_min"
            )
        return self


class CurveAnchor(_Strict):
    x: Decimal
    grade: Decimal = Field(ge=1, le=10)


class Curve(_Strict):
    """Piecewise-linear anchors, strictly increasing in x, at least two."""

    anchors: tuple[CurveAnchor, ...] = Field(min_length=2)

    @model_validator(mode="before")
    @classmethod
    def _pairs(cls, data: Any) -> Any:
        if isinstance(data, (list, tuple)):
            anchors = []
            for item in data:
                if not isinstance(item, (list, tuple)) or len(item) != 2:
                    raise ValueError(f"a curve anchor is [x, grade], got {item!r}")
                anchors.append({"x": item[0], "grade": item[1]})
            return {"anchors": anchors}
        return data

    @model_validator(mode="after")
    def _increasing(self) -> Curve:
        xs = [a.x for a in self.anchors]
        if any(a >= b for a, b in zip(xs, xs[1:])):
            raise ValueError(f"curve anchors must be strictly increasing in x, got {xs}")
        return self

    def pairs(self) -> list[list[str]]:
        return [[str(a.x), str(a.grade)] for a in self.anchors]


class AlignmentDefault(_Strict):
    with_grade: int = Field(ge=1, le=10)
    flat_grade: int = Field(ge=1, le=10)
    against_grade: int = Field(ge=1, le=10)
    flat_pct: Decimal = Field(ge=0)


class ShadowPromotionBar(_Strict):
    sessions: int = Field(gt=0)
    pairs: int = Field(gt=0)
    median_max: Decimal = Field(ge=0)
    within2_min: Decimal = Field(ge=0, le=1)


class CardSettings(_Strict):
    cards_enabled: bool
    proposed_key: ProposedKeyBands | None = None
    curves: dict[str, Curve] | None = None
    alignment_default: AlignmentDefault | None = None
    shadow_promotion_bar: ShadowPromotionBar | None = None

    @model_validator(mode="after")
    def _enabled_needs_bands_and_curves(self) -> CardSettings:
        if self.cards_enabled:
            missing = [
                key for key, value in ((PROPOSED_KEY, self.proposed_key), (CURVES, self.curves))
                if value is None
            ]
            if missing:
                raise ValueError(
                    f"radar.cards_enabled=true requires {missing}: an enabled radar with no "
                    "bands or curves would publish keys and grades nobody set"
                )
        return self

    @classmethod
    def from_rows(cls, rows: dict[str, Any]) -> CardSettings:
        """The runtime reader. Other keys in `rows` are ignored (the
        sheet/day-mode rows share the table); a missing
        `radar.cards_enabled` is refused, never defaulted."""
        if CARDS_ENABLED not in rows:
            raise CardSettingsError(
                f'"user".trader_settings has no {CARDS_ENABLED!r} row — the radar does not '
                "guess whether cards are on. Load the reviewed card-settings file with "
                "`cobalt settings load --card <file> --sha256 <hash> --apply`."
            )
        try:
            return cls(
                cards_enabled=rows[CARDS_ENABLED],
                proposed_key=rows.get(PROPOSED_KEY),
                curves=rows.get(CURVES),
                alignment_default=rows.get(ALIGNMENT_DEFAULT),
                shadow_promotion_bar=rows.get(SHADOW_PROMOTION_BAR),
            )
        except ValidationError as e:
            # Name the ROW, not the Python field: the trader edits keys.
            lines = []
            for err in e.errors():
                loc = list(err["loc"])
                head = _KEY_BY_FIELD.get(str(loc[0]), str(loc[0])) if loc else "(settings)"
                rest = ".".join(str(part) for part in loc[1:])
                lines.append(f"  {head}{'.' + rest if rest else ''}: {err['msg']}")
            raise CardSettingsError("invalid card settings:\n" + "\n".join(lines)) from e

    def rows(self) -> dict[str, Any]:
        """The present keys as JSON-ready row values (the inverse of
        `from_rows`)."""
        out: dict[str, Any] = {CARDS_ENABLED: self.cards_enabled}
        if self.proposed_key is not None:
            out[PROPOSED_KEY] = self.proposed_key.model_dump(mode="json")
        if self.curves is not None:
            out[CURVES] = {name: curve.pairs() for name, curve in sorted(self.curves.items())}
        if self.alignment_default is not None:
            out[ALIGNMENT_DEFAULT] = self.alignment_default.model_dump(mode="json")
        if self.shadow_promotion_bar is not None:
            out[SHADOW_PROMOTION_BAR] = self.shadow_promotion_bar.model_dump(mode="json")
        return json.loads(json.dumps(out))

    def snapshot(self) -> dict[str, Any]:
        return self.rows()

    def sha256(self) -> str:
        return hashlib.sha256(
            json.dumps(self.snapshot(), sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()


_KEY_BY_FIELD = {
    "cards_enabled": CARDS_ENABLED,
    "proposed_key": PROPOSED_KEY,
    "curves": CURVES,
    "alignment_default": ALIGNMENT_DEFAULT,
    "shadow_promotion_bar": SHADOW_PROMOTION_BAR,
}


class CardSettingsReader:
    """Reads the store on EVERY `current()` — no cache (plan §5)."""

    def __init__(self, store: TraderSettingsStore | None = None):
        self.store = store or TraderSettingsStore()

    def current(self) -> CardSettings:
        return CardSettings.from_rows(self.store.values())


def load_card_file(path: Path, *, expected_sha256: str | None) -> tuple[CardSettings, str]:
    """Parse a reviewed card-settings file. With `expected_sha256` the
    file's bytes must hash to it before anything is parsed."""
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if expected_sha256 is not None and digest != expected_sha256.strip().lower():
        raise CardSettingsError(
            f"{path}: sha256 {digest} != reviewed {expected_sha256} — the file changed after "
            "review (or the wrong file was named). Nothing applied."
        )
    try:
        doc = yaml.safe_load(raw.decode("utf-8"))
    except (UnicodeDecodeError, yaml.YAMLError) as e:
        raise CardSettingsError(f"{path}: unreadable card-settings file: {e}") from e
    if not isinstance(doc, dict) or set(doc) != {FILE_ROOT} or not isinstance(doc[FILE_ROOT], dict):
        raise CardSettingsError(f"{path}: expected exactly one top-level mapping {FILE_ROOT!r}")
    body: dict[str, Any] = doc[FILE_ROOT]
    for key in body:
        if any(str(key).startswith(prefix) for prefix in TUNABLES_ONLY_PREFIXES):
            raise CardSettingsError(
                f"{path}: {key!r} is an engine tunable — it lives in tunables.yaml under its "
                "own validation and restart rules (L53), never in trader_settings"
            )
        if key in SETTING_KEYS:
            raise CardSettingsError(
                f"{path}: {key!r} is a sheet/day-mode setting — load it with "
                "`cobalt settings load --from/--from-git`, not the card file"
            )
        if key not in CARD_SETTING_KEYS:
            raise CardSettingsError(
                f"{path}: unknown card setting {key!r}; known: {list(CARD_SETTING_KEYS)}"
            )
    try:
        settings = CardSettings.from_rows(body)
    except CardSettingsError as e:
        raise CardSettingsError(f"{path}: {e}") from e
    return settings, digest


def cmd_load_card(args: argparse.Namespace) -> None:
    dry_run = bool(args.dry_run)
    if dry_run == bool(args.apply):
        raise SystemExit("cobalt settings load --card: pass exactly one of --dry-run or --apply.")
    if not dry_run and not args.sha256:
        raise SystemExit(
            "cobalt settings load --card --apply requires --sha256 <hash of the reviewed file>"
        )
    path = Path(args.card)
    incoming, digest = load_card_file(path, expected_sha256=args.sha256)
    store = TraderSettingsStore()
    store.ensure_schema()
    current = store.values()
    new_rows = incoming.rows()

    print(f"cobalt settings load --card — {'DRY RUN' if dry_run else 'APPLY'} {path}")
    print(f"sha256 {digest}\n")
    changed, deletes = 0, []
    for key in CARD_SETTING_KEYS:
        old, new = current.get(key), new_rows.get(key)
        if key not in new_rows:
            if key in current:
                deletes.append(key)
                changed += 1
                print(f"  - {key}\n      db  : {json.dumps(old, sort_keys=True)}\n      file: (absent — deleted)")
            continue
        if old == new:
            print(f"  = {key}")
            continue
        changed += 1
        print(f"  {'+' if key not in current else '~'} {key}")
        print(f"      db  : {json.dumps(old, sort_keys=True) if key in current else '(absent)'}")
        print(f"      file: {json.dumps(new, sort_keys=True)}")

    if not changed:
        print("\nno differences — the database already holds these card settings.")
        return
    if dry_run:
        print(f"\nDRY RUN — {changed} card setting(s) would change. Nothing written.")
        return

    assert_writable("settings.load.card", target='"user".trader_settings')
    outcome = store.put(new_rows, source=f"card:{path.name}@sha256:{digest}", delete=deletes)
    print(f"\napplied: {outcome}; deleted: {deletes}")
    reloaded = CardSettings.from_rows(store.values())
    if reloaded != incoming:
        raise SystemExit(
            "FAILED: what the database now returns differs from the reviewed file — "
            f"db {reloaded.rows()} vs file {new_rows}"
        )
    print("round trip: CardSettings.from_rows(db) == reviewed file — EQUAL.")


__all__ = [
    "ALIGNMENT_DEFAULT", "AlignmentDefault", "CARDS_ENABLED", "CARD_SETTING_KEYS", "CURVES",
    "CardSettings", "CardSettingsError", "CardSettingsReader", "Curve", "CurveAnchor",
    "PROPOSED_KEY", "ProposedKeyBands", "SHADOW_PROMOTION_BAR", "ShadowPromotionBar",
    "cmd_load_card", "load_card_file",
]
