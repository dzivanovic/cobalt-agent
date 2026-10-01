JOB: aset-interim-close
LADDER: OFF-LADDER — cto-2026-10-01.md 2026-10-01 R13
BRANCH: s3/aset-interim-close-1001
WORKTREE: aset-interim-close-1001
BASE: bce3cfa8
TIP:
REPORT: /Users/cobalt/cobalt-wt/aset-interim-close-1001/docs/40 - DevDocs/reports/aset-interim-close-build-2026-10-01.md
CHECK REPORT:
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-01 R13

## ROWS

| row | what | red first | files |
|---|---|---|---|
| S1 | RUN — asserts nothing. The page jumps to the top while he fills the new-card form at the bottom of `/` (R13, his words). Find every path that reloads or re-renders `/` while he moves from field to field: every `fetch`, `addEventListener`, `onchange`, `blur`, form submit and `location` use in the page script (`src/cobalt/aset/web.py` ~190-310, the `/api/prefill` caller, the voice widget's own script), and what each does to the page and to scroll. Quote each with `file:line` and say which one moves the page to the top. A cause you cannot find from code is `## DECISIONS`, UNPROVEN (L70); never guessed | — (tool output quoted in the report) | none (read only) |
| S2 | On `/`, NO card of any kind is above the new-card form: the whole open-cards block (`open_cards_html`: open cards, each card's controls and in-trade block, today's closed cards and estimated legs) renders BELOW the `/size` form, and `{banner}` / `{result}` stay where they are. Today it is rendered above it (`web.py` ~405, built by `_open_cards_block` ~758). Every response that renders `/` (GET, and the POST results of `/size`, `/fill`, `/card/{id}/move`, `/card/{id}/stop`, `/attest`, settings) keeps that order | test in `tests/cobalt/test_aset_web.py`: render `/` with one WATCH card and one FILLED card; asserts the index of `action="/size"` is LESS than the index of the open-cards label `Open cards (F7)`, in the GET and in the POST result of `/card/{id}/move`. RED on `BASE`: the label comes first | `src/cobalt/aset/web.py`, `tests/cobalt/test_aset_web.py` |
| S3 | The CLOSE button on `/` closes a FILLED card with nothing typed. `POST /card/{id}/move` with `to=CLOSED` (today refused, `web.py` ~1382-1391) now writes ONE flat exit leg for every share still running, at the card's entry fill price, through the one leg writer (`cards.legs.record_exit`, flat preset; its `_close_if_zero` closes the card), actor YOU, evidence `via=aset.sheet`, and a price source that marks it estimated (`sheet_close_at_entry`, never a broker fill: L57, L35). The page asks for no price, share count or reason; a card with a typed price is not a case of this route. The C2 rule is unchanged everywhere else: no other route and no other state reaches CLOSED without a zero-running leg. Radar cards listed on `/` close the same way from `/`. The CLOSE button is drawn only on a FILLED card (it is already the only legal edge) | tests in `tests/cobalt/test_aset_web.py`: (a) a FILLED manual card of 12 shares at 64.10 → POST CLOSE with no other field → card CLOSED, one leg of 12 shares at 64.10 with the estimated price source, running 0, no banner `FAILED`; (b) the same on a radar-origin FILLED card; (c) a card already at running 0 or a WATCH card → refused loud, nothing written; (d) `to=FILLED` and every other refusal at `~1370-1380` unchanged. RED on `BASE`: (a) answers `REFUSED card …: CLOSED — this route never closes` | `src/cobalt/aset/web.py`, `tests/cobalt/test_aset_web.py` (the C2 test that pins the refusal is changed to pin the new rule; name it in the report) |
| S4 | Whatever S1 finds moves the page to the top while he fills the form is fixed so a field change, a ticker lookup or a refresh of the voice box never scrolls or re-renders the form out from under him. If S1 finds a full-page reload, the lookup fills the fields in place instead. If S1 finds nothing in code, S4 is a `## DECISIONS` item with the evidence and no change | test: the specific path S1 names, pinned by a test that fails on `BASE` for that reason, named in the report | `src/cobalt/aset/web.py`, `tests/cobalt/test_aset_web.py` (and `src/cobalt/voice/web.py` only if S1 names it) |

## NOT IN THIS JOB
- `/radar` and everything under `src/cobalt/radar/` and `radar_panel.py`: unchanged (his R13: "Not on the radar. On this form only").
- Removing or hiding the old sheet; adding any control to `/radar`.
- The voice peers config (`configs/cobalt/voice.yaml`) and the `/voice/status` 403: its own job.
- The width of the narrow boxes in the daily-settings row: its own job.
- `cards/legs.py` rules: S3 calls the existing flat exit and changes none of its rules; a change there is a `## DECISIONS` item.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-01-words.md` `## R13`.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/aset-sheet-survey-2026-10-01.md` §1 and §2.
- `src/cobalt/aset/web.py`: `_card_controls` (~640-720), `_sheet_in_trade` (~1925-1981), `card_move` (~1359-1420), the page template (~395-460) and its script (~190-310); `src/cobalt/cards/legs.py` `record_exit` (~381), `_close_if_zero` (~228).

## RECORDS
- A closed-at-entry leg stands for "he did not say the price"; the report states how the P&L, the trade note and the F22 note read an estimated leg, with `file:line`.

## DECISIONS ASKED
- DECISION S-A: the flat leg's price source. The card says an estimated source at the card's entry fill price; the builder names the existing source string that `legs.py` accepts, or the one new string it adds, and shows every reader of that field handles it.
