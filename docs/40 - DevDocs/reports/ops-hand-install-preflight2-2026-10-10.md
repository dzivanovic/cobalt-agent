# ops-hand install card 306 — re-preflight after amend, 2026-10-10 (read-only)

Read against `HEAD` `a780d176`; card `BASE` `936c9b1e`. `git diff 936c9b1e HEAD --stat` over `OPS-HAND.md`, `STANDING-LIST.md`, `ops`, `tests` → empty: every file the rows touch is the same at `BASE` and `HEAD`. Every check of the first preflight (`307` `Checks:`) was re-run against the card as it stands; checks 1-4 and 6-13, 16-24 carry from the first report unchanged (card text for those rows was not edited by the amend), re-verified below where the amend touched them.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <306 card>` | empty (committed, clean) | OK |
| 2 | `grep -n "«FILL" <card>`; `grep -n -E "^(RULINGS\|BASE\|TIP\|CHECK REPORT\|HOUSE B):"` | no `«FILL`; `BASE: 936c9b1e` filled; `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty as CARD.md marks them | OK |
| 3 | RULINGS form | `RULINGS: 2026-10-10 R969, 2026-10-10 R971`: comma form, each item `<date> R<n>`, no space form | OK |
| 4 | rows: `grep -n -E "^\| (R969\|R971) " reports/cto-2026-10-10.md` | `:10` R971 and `:12` R969, both `HIS RULING · APPROVED`; `git diff HEAD` of the report empty (committed) | OK |
| 5 (re-proof of FAIL 5) | `grep -n -E "cto-2026-10-10.md.{0,12}:[0-9]+" <card>` | no output: no line cite remains. Card cites by id (`LADDER`, WHY, I1, READ `rows R969, R971`, RECORDS: "Rows are cited by id, never by line") | OK |
| 6 | H4 anchors `desk-launch.sh` `:628`, `:633-634`, `:636-638`, `:663-673`, `:704-705` | unchanged since `BASE` (diff empty); as proved in the first report | OK |
| 7 | H4 title read | only the `«INSTALL` token grep; NEW title holds no `«` | OK |
| 8 | `authorize.sh` `:148`, `:173-183` | unchanged; names no `OPS-HAND` | OK |
| 9 | I1 OLD/NEW vs `OPS-HAND.md` | unchanged text; `wc -l OPS-HAND.md` → 22; `grep -c "^claude --bg "` → 1 | OK |
| 10 | I1 reds by hand: `grep -c -F -e "«INSTALL" OPS-HAND.md` | BASE 1 (line 1); NEW line holds none → 0 after. `HIS RULING · APPROVED 2026-10-10 R969` → 0 on BASE, 1 on NEW line (card `:32`) | OK |
| 11 | I2 vs `OPS-HAND.md:20`, strings | I2 text unchanged by the amend; 4 allow, 17 deny, mode, model, names as proved in first report | OK |
| 12 | I2 block line count | 13 lines (blank, heading, blank, para, blank, 6 table, blank, Deny) | OK |
| 13 | STANDING-LIST anchors | `wc -l` → 220; unchanged since `BASE` | OK |
| 14 (re-proof of FAIL 14) | by hand on the NEW I2 text: `grep -c -F -e '`Bash(sudo *)`' STANDING-LIST.md` | BASE 0 (run); NEW Deny line (card `:50`) writes `` `Bash(sudo *)` `` in backticks → 1 after. `grep -c -F -e '## 8. `OPS-HAND.md`'` BASE 0 (run); NEW heading `:39` → 1. `grep -c -F -e '--permission-mode default'` BASE 0 (run); NEW `:39` → ≥ 1. Red-first 0 → 1 holds | OK |
| 15 (re-proof of NOTE 15) | `wc -l STANDING-LIST.md`; card wording | 220 on BASE (run); card says "220 on `BASE`, 233 after the row" (220 + 13) | OK |
| 16 | brain test `:497-501` | `## 8.` adds none of `claude-opus-5-5`, `claude-fable-5-1`, `the only variable` (checked in card `:39-50`); stays green | OK |
| 17 | I3 trace `:296-300`, `:303-315` | I3 text unchanged by the amend; as traced in first report | OK |
| 18 | readers of `STANDING-LIST`/`OPS-HAND` in tests, ops | tests/ops unchanged since `BASE`; first report's list stands | OK |
| 19 | rows touch only `OPS-HAND.md`, `STANDING-LIST.md`, the one test | yes; I3 is the one non-docs edit | OK |
| 20 | no new command (R411, R412) | `NOT IN THIS JOB` last bullet; every string is an existing allow string | OK |
| 21 | house | RECORDS last bullet: house A Grok, `HOUSE B: as needed`, never OpenAI (R920) | OK |
| 22 | collision with card 284 | 284 K3 inserts one line after `STANDING-LIST.md:148`; I2 appends `:221-233` after `:220`. Different lines | OK |
| 23 | other anchors (`bare-guard.py:1122`, `231` lines 24, 27, words `:12-13`) | unchanged; ops/ and the first report's proofs stand | OK |
| 24 | drafter decisions 1-2 (amend report) | 1: cites by id, no other row touched; 2: `RULINGS` carries R971 as its own item. Rows consistent with both | OK |
| 25 | single-quoted backtick grep | card I2 red and RECORDS use `'…'` for both backtick patterns (`:20`, `:80`); no backtick inside double quotes in a typed command | OK |

## ISSUES
- NOTE: row lines moved again while the card was in flight (R971 `:10`, R969 `:12` at `HEAD` `a780d176`); the card cites ids, so no effect.
- NOTE: `BASE` `936c9b1e` is behind `HEAD` `a780d176`; the files the rows touch are the same at both, so the desk's re-write at launch changes nothing.
- NOTE: `uv run pytest` and `uv run cobalt jobs restarts` not run (read-only seat); the I3 trace is by reading.

PREFLIGHT DONE · card: ops-hand-install-1010 · checks: 25 · fails: 0 · ready: YES
