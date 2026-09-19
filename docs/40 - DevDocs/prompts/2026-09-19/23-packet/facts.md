# Facts — cards go-live settings file (Task 1, verbatim-sourced, read-only)

## 0. Headline fact — the file the desk was asked to build does NOT validate

`src/cobalt/settings/card.py:157-169` (`CardSettings._enabled_needs_bands_and_curves`)
requires **`card.proposed_key`** and **`card.curves`** — not `card.alignment_default` /
`card.shadow_promotion_bar` — non-null before `radar.cards_enabled: true` is accepted:

```
@model_validator(mode="after")
def _enabled_needs_bands_and_curves(self) -> CardSettings:
    if self.cards_enabled:
        missing = [
            key for key, value in ((PROPOSED_KEY, self.proposed_key), (CURVES, self.curves))
            if value is None
        ]
        if missing:
            raise ValueError(...)
```

Confirmed live against the real repo module (`.venv/bin/python3`, read-only, no DB/`uv run`/`cobalt`):
loading `23-packet/p2-live-settings.yaml` (`radar.cards_enabled: true` +
`card.shadow_promotion_bar` only) through `load_card_file()` raises:

```
invalid card settings:
  (settings): Value error, radar.cards_enabled=true requires ['card.proposed_key', 'card.curves']:
  an enabled radar with no bands or curves would publish keys and grades nobody set
```

`card.proposed_key` (conviction→key bands) and `card.curves` (per-factor piecewise anchors) have
**no ruled or recorded default anywhere in the record** — they are named explicitly as Dejan's own
values, never a hub's: `docs/40 - DevDocs/plans/plan-s2-p2-2026-09-15.md:272` ("Dejan sets
`card.proposed_key` bands and `card.curves` anchors and flips `radar.cards_enabled=true`"), `:288`
("**Dejan:** … values for `card.proposed_key` and `card.curves`"); `cto-2026-09-17.md:261`
("curves are HIS values → 09-19 values session"). No cto/deploy/ladder-audit report between
09-14 and 09-19 records him supplying either. **This — not `alignment_default`/
`shadow_promotion_bar` — is the actual remaining gate on Monday's switch-on**; ladder-audit-
2026-09-19.md §7(2) and today's task brief both name the wrong pair of "two required" keys.
`alignment_default`/`shadow_promotion_bar` ARE real, ARE dark-only-optional, and ARE also open
09-19-values-session items (`cto-2026-09-17.md:178,261,264`) — just not the ones the code's
`cards_enabled=true` gate itself checks.

## 1. Schema of the `--card` file (`src/cobalt/settings/card.py`)

File shape (`load_card_file`, card.py:242-278; format documented card.py:18-33):
```
card_settings:
  radar.cards_enabled: <bool>                    # REQUIRED always
  card.proposed_key: {a_plus_min, a_min, b_min, c_min}   # Decimal 0..1, strictly descending (card.py:85-100)
  card.curves: {<factor>: [[x, grade], ...]}             # ≥2 anchors, x strictly increasing, grade 1..10 (card.py:103-133)
  card.alignment_default: {with_grade 1-10, flat_grade 1-10, against_grade 1-10, flat_pct ≥0}  (card.py:136-140)
  card.shadow_promotion_bar: {sessions >0, pairs >0, median_max ≥0, within2_min 0..1}  (card.py:143-147)
```
- The file is the WHOLE card-settings set: a key it omits is DELETED from the DB (card.py:28-29,
  `store.py` `put(..., delete=...)`).
- `radar.cards_enabled` — required, no default, ever (`CardSettings.from_rows`, card.py:172-181:
  a missing row raises `CardSettingsError`, never guesses).
- `card.proposed_key`, `card.curves` — dark-only-optional; **required non-null when
  `cards_enabled: true`** (card.py:157-169, confirmed above).
- `card.alignment_default`, `card.shadow_promotion_bar` — dark-only-optional; **not checked by
  `CardSettings` at all when enabling** (no validator references them). `shadow_promotion_bar`
  IS required by a *different*, unrelated command: `cobalt cards shadow-report` refuses loud if
  it is `None` (`src/cobalt/cards/shadow_report.py:147-152`) — needed to compute the L7 agreement
  gate later, not to flip the switch.
- Unknown keys, `card.dot.*`/`card.health.*` (tunables, L53), and the 7 sheet/day-mode
  `SETTING_KEYS` are all refused by name (card.py:259-273).
- Extra/unknown fields inside each sub-object are refused (`ConfigDict(extra="forbid")`,
  card.py:81-82).

## 2. `card.alignment_default` — plain words

Controls the two "desk" dots that would otherwise need Dejan's own market/sector-alignment
judgment (`market_alignment`, `sector_alignment`) — a with/flat/against numeric grade map so the
engine can render *something* on those dots without him tapping every one, per
`plan-s2-p2-2026-09-15.md:204`. "N/A" on screen (S2's actual behaviour) means the dot shows
`DEFAULT_UNRULED`/no computed grade at all — hollow, unscored, exactly like an untapped judgment
dot; it does not mean a placeholder number is guessed.

**Current runtime reality: this setting is NOT read by the running code at all.**
`src/cobalt/radar/evaluate.py:683-691` (`desk_shadow()`) takes no settings argument and hardcodes:
```
return DeskShadow(
    catalyst=entry("DESK_NA"), market_alignment=entry("DEFAULT_UNRULED"),
    sector_alignment=entry("DEFAULT_UNRULED"),
)
```
So whatever value `card.alignment_default` holds in the database, market/sector alignment ship
`DEFAULT_UNRULED` (N/A) through S2 regardless. This matches the plan's own ruling, not an
oversight: `plan-s2-p2-2026-09-15.md:295` — **[tightened 2026-09-15 per Astra R2-6, BLOCKER]**:
"MERGED (the 09-14 analyst tribunal) explicitly rejects SPY-sign alignment, and the 10/6/4 ceiling
is the only numeric source on record and is itself rejected. STEP-5 renders explicit N/A until an
exact dated ruling authorizes the default-map mapping semantics … If no such ruling is found, this
stays OPEN for Dejan, not a hub judgment call, and STEP-5 ships N/A for `sector_alignment`/
`market_alignment` defaults through S2 rather than reviving 10/6/4 or SPY-sign." No later report
(09-16 through 09-19) records that ruling being supplied. **No default exists** — only `flat_pct:
0.15` was ever called "accepted" (`plan:204`, "09-14 group-2 A"), and the schema will not accept
`flat_pct` alone (all four sub-fields are required together, card.py:136-140).

**Choice made in the go-live file:** `card.alignment_default` is left **ABSENT** — matches the
plan's own designed fallback (ship N/A) exactly, and matches what the code does regardless. This
is not a silent pick: the alternative (writing a numeric with/flat/against triple, e.g. the
8/5/2/0.15 values used only as an illustrative test fixture in `tests/cobalt/test_card_settings.py:34`,
never as a ruling) would write an explicitly-rejected semantic into live `trader_settings` for no
runtime effect. **Flagged to Dejan, not decided by this desk:** if he wants the with/flat/against
mapping wired up for real (i.e., `desk_shadow()` changed to read it), that is a code change to
`radar/evaluate.py` plus the still-missing authorizing ruling — out of scope for Monday's switch.

## 3. `card.shadow_promotion_bar` — plain words + source

The L7 promotion gate for the three desk-graded dots, checked later (S3) by
`cobalt cards shadow-report` against `"user".shadow_agreement_v`
(`src/cobalt/cards/shadow_report.py`, `src/cobalt/db_migrations/0007_radar_cards.sql:245-258`):

| Sub-field | Plain words | 09-14 group-2 ruled value | Source |
|---|---|---|---|
| `sessions` | minimum distinct ET trading days with ≥1 tap/engine pair, per factor | 10 | `plan-s2-p2-2026-09-15.md:223`; `TAXONOMY-DRAFT-v0_8.md:69`; `shadow_report.py:15-16` |
| `pairs` | minimum total tap-vs-engine pairs across those sessions | 30 | same |
| `median_max` | the median of `|tap_grade − engine_grade_at_tap|` over ALL pairs must be ≤ this | 1 | same |
| `within2_min` | share of pairs with `|Δ| ≤ 2` must be ≥ this | 0.90 | same |

`cobalt cards shadow-report` prints GATE MET/NOT MET and "never flips anything" (`plan:223`,
`shadow_report.py:19-21`) — it is read-only evidence for the later L7/L8 promotion decision, not
itself a trading-logic change. **Choice made:** these four values are set exactly as ruled — this
is a recorded ruling, not a pick.

## 4. What loading writes, restart, market-reset gate, rollback

- **Write target:** `"user".trader_settings` (Side.USER — trader-private data, L32), one row per
  key: `(user_id, key, value jsonb, source, updated_at)`, one transaction, upsert + delete atomic
  (`src/cobalt/settings/store.py:60-116`, `TraderSettingsStore.put`).
- **20:00-21:00 ET refusal:** `assert_writable("settings.load.card", …)` (card.py:322) →
  `src/cobalt/session/guard.py:123-150`: refuses only when `session_clock().session(now) is
  Session.MARKET_RESET`. **Keyed to trading days, confirmed by direct read**:
  `src/cobalt/session/clock.py:196-200` — `windows_for(day)` returns `[]` when
  `not self.calendar.is_trading_day(day)`, and `session()` (clock.py:222-228) falls through to
  `Session.OVERNIGHT` when no window matches. So the 20:00-21:00 block **cannot fire on a
  weekend**, regardless of wall clock — resolves the "not verified" note in
  `ladder-audit-2026-09-19.md:187-190`.
- **Restart needed:** **No.** `CardSettingsReader.current()` re-reads the store on every call, no
  cache (card.py:232-239, docstring lines 41-43); proven directly in the real test file at
  `tests/cobalt/test_card_settings.py:194-201` (`test_settings_are_re_read_on_every_call_not_cached`
  — not `s2-p2-build-opus-B-2026-09-16.md:53` as cited in the ladder audit; verified against the
  actual `tests/` tree on `main`, same assertion). S5 evaluate and the card routes call it per
  scan/request.
- **`--apply` prints:** per-key diff (`db`/`file` values or `(absent)`), `applied: {...}; deleted:
  [...]`, then a round-trip check — `CardSettings.from_rows(store.values()) == incoming` — and
  "round trip: CardSettings.from_rows(db) == reviewed file — EQUAL." (card.py:294-331). A mismatch
  raises `SystemExit("FAILED: ...")` before ever claiming success.
- **Rollback:** re-run `cobalt settings load --card
  data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml --sha256
  945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca --apply`. File CONFIRMED still
  present, bytes unchanged, hash reverified this session:
  `shasum -a 256 data/backups/pre-s2-p2-2026-09-17/p2-dark-settings.yaml` →
  `945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca` (matches
  `cto-2026-09-17.md:178` exactly). Note: this directory (`data/`) is gitignored
  (`.gitignore:6`) — it is a local file on this host only, not in git; that is by design (L32/data
  policy) but means the rollback file's survival depends on this host's `data/` tree, not git
  history.

## 5. What he sees Monday 04:00+ ET, what's recorded, what could page/alert/write

- **Where:** `GET /radar` on the same ASET-sheet host (`src/cobalt/aset/web.py:845-853`,
  `build_radar_panel`/`render_radar_page`); linked from the sheet page itself
  (`web.py:387`, "Trade Radar"). Read-only page; `fetch` POST only for actions, no
  alert/confirm/prompt (`plan:217`, focus law).
- **A WATCH card shows:** setup→trade, trigger price, structural stop, `proposed_key` (from
  `card.proposed_key` bands — **absent in S2 until Dejan sets it**, so `proposed_key` renders none
  until he does), one dot per `quality_factors[]` entry + the 3 desk dots, `conviction`/
  `proximity`/`card_score` with scan id + formula/tunables/settings hashes (`plan:12`).
- **Hollow / his tap:** every judgment-role dot renders **hollow** (unfilled) on the card face
  regardless of what the engine computed for it — both the human-only dot (`trail_fit`, N/A/
  MANUAL) and, in S2, the three desk dots (`catalyst`=`DESK_NA`, alignment=`DEFAULT_UNRULED`) and
  the computable dots (`role=shadow` per R6, `plan:58`, `:203`). Tapping
  `POST /radar/card/{id}/dot/{factor} {grade 1-10}` is what fills a dot: appends
  `card_dot_taps`, sets `card_dots.trader_grade`, recomputes conviction (mean of tapped
  grades ÷ 10, null if none tapped — never a neutral 5) and `card_score = round(conviction ×
  proximity × 100)` (`plan:205`, `:212`). The engine's own shadow grade is never shown as the
  face value; it only appears mirrored into the dot's reason text as `desk shadow: n`
  (`plan:204`) and stored in `radar_score.desk_shadow` (system-side, no trade-specific prose,
  `plan:175`).
- **Recorded for the agreement numbers:** each tap writes a `"user".card_dot_taps` row
  (`grade`, `engine_grade_at_tap`, `factor`, `at`); `"user".shadow_agreement_v`
  (`db_migrations/0007_radar_cards.sql:245-258`) aggregates per `(user_id, factor, ET trading
  day)`: `pairs`, `median_abs_delta`, `within2_share`, `deltas[]`. Read via
  `CardStore.shadow_agreement()` (`cards/store.py:875-883`) → `cobalt cards shadow-report`.
- **Vault/page/alert side effects of THIS switch specifically:** `POST /radar/card/{id}/key
  {grade}` (the WATCH key tap, not the switch-on) writes a daily-note card block via the
  existing `save_card` path (`plan:210`) — this is the pre-existing sheet vault-write mechanism,
  unchanged by cards going live, and only fires on HIS tap, never on card formation itself. **No
  evidence found** of any new Mattermost DM, page, or alert being wired to card
  formation/evaluation in S2 — F18's heartbeat is the only alert channel on record and email was
  already retired (`ladder-audit-2026-09-19.md:29`); grep of `plan-s2-p2-2026-09-15.md` and
  `src/cobalt/notify/` for a card-triggered notification found none. **Not fully verified**:
  I did not exhaustively read every line of `notify/`; flagged rather than asserted absent.

## 6. Dry-run command (L10)

```
cobalt settings load --card "docs/40 - DevDocs/prompts/2026-09-19/23-packet/p2-live-settings.yaml" \
  --sha256 d77106fcb16e270e908a6cf39e5797baeed1d905a322c4b655ad9b4f1e0c4d81 --dry-run
```
(`--sha256` is optional on `--dry-run` per the arg parser — only required with `--apply`,
`settings/card.py:281-288` — but passing it lets the dry run also prove the file is byte-exact
before anything parses, same as the review packet's own hash.) **This dry run will print the
per-key diff and then, per §0 above, `load_card_file` will raise `CardSettingsError` before any
diff is printed at all** — the file does not parse into a valid `CardSettings` regardless of
`--dry-run`/`--apply`, since validation happens before the diff step (`card.py:290`,
`cmd_load_card`). A real dry run today would fail this exact way, not print "0 differences."
