# next-flow check — 2026-10-06

## §0 Headline
- Check of next-flow (`1f4a8598..e249bd83`). No outside house sat: house A was overruled by R47. Nine findings of my own, each run.
- Seven held (one-house leftovers in CHECK-HUB, stop-line gaps, gate exit 0 wording). All seven fixed in `987ab80d` (2 hub files, 7±).
- Suites on `987ab80d`: offline 3932/0, live-note 146/0, tests/ops 1382 passed; DB: none. CHECK ASKS X1–X4 clean.
- Open: 1, FOR DEJAN. L67's law text still describes the second pass. ready: YES.

## L74
- A system reminder (not a tool result) asked for a `Claude-Session:` line in commits. Not acted on; commits carry `Co-Authored-By` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · last line `AUTHORIZED` (16 rows: INSTALLED, PLACEHOLDER, CARD COMMITTED `12a4d367`, CARD UNCHANGED, STANDING LIST R60 `962e9d17`, R438 row 173 `HIS RULING · APPROVED` `8e5b72b0`, R412 row 109 `APPROVED` `b3583b28`, HOUSE A overruled R47 row 54 `HIS RULING · APPROVED` `4e3fa8d8`).
House gates: not run — `HOUSE A: none — overruled 2026-10-02 R47` (CHECK-HUB `## THE FLOW`).

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` | 0 | clock `Tue Oct  6 01:34:03 EDT 2026`; status `## ops/next-flow-1006`; head `30f1dc02` (docs-only above TIP: the build report); no `.env` here; sibling `.env` in `flake-fix-1006` (another job's lock; DB: none card, not taken); build report last line `BUILT · job: next-flow · tip: e249bd83 … self-check: 3 of 3 …`; range `e249bd83`; `PREFLIGHT OK` |
| range | `git log --stat --format=%h 1f4a8598..e249bd83` | 0 | `e249bd83`: BUILD-HUB.md 12 ±, CHECK-HUB.md 70 ±; 2 files, 37+, 45− |
| DB: none | `git diff --name-only --no-renames 1f4a8598..e249bd83` | 0 | `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/CHECK-HUB.md` — all under `docs/` |
| scratch | `ls <S>` | 0 | `diff.md` (105 bytes, 01:31) — present before this session; not a CONTINUE launch, see RECORDS |
| house | — | — | house A: none (overruled 2026-10-02 R47); no probe |

## Files copied
none — house A: none (overruled 2026-10-02 R47); `## 1` not run.

## OWN FINDINGS
Paths are relative to `<WT>`; HUB = `docs/40 - DevDocs/prompts/CHECK-HUB.md`, BHUB = `docs/40 - DevDocs/prompts/BUILD-HUB.md`.

FINDING O1 · ROW: F1 / X5 · CLAIM: HUB:32's law line still reads "L36 only the one house of your pass", which contradicts HUB:3 ("the TWO outside houses of this check"). · RUN: COMMAND `grep -n -F "L36 only the one house of your pass" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` · EXPECT: `32:` hit.

FINDING O2 · ROW: F1 / X5 · CLAIM: HUB:114 COUNTING still reads "`findings` = every block you and the house wrote" (one house). · RUN: COMMAND `grep -n -F "every block you and the house wrote" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` · EXPECT: `114:` hit.

FINDING O3 · ROW: F1 / X5 · CLAIM: HUB:58's section list still reads "`## Findings` (the house's, kept)" (one house). · RUN: COMMAND `grep -n -F "(the house's, kept)" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` · EXPECT: `58:` hit.

FINDING O4 · ROW: F1 (F1.27) / X5 · CLAIM: HUB:89 says "House B's spelling is house A's with house-b.md for house-a.md": read literally, house B (Grok) is started with house A's (Sol's) command line. · RUN: COMMAND `grep -n -F "House B's spelling is house A's" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` · EXPECT: `89:` hit.

FINDING O5 · ROW: F1 / X5 · CLAIM: the stop-line grammar (HUB:117, :120) has no spelling for a house B seat that is `none produced`, which HUB:100 creates and HUB:123 tests for. · RUN: COMMAND `grep -n -F "none produced" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` · EXPECT: hits at 100 and 123 only, none at 117 or 120.

FINDING O6 · ROW: F1 (F1.38) / X5 · CLAIM: HUB:28 (the HOUSE A overrule) sets `house B: none available` only "When "open" is above 0"; F1.38 removed `not needed`, so an overruled check with open 0 has no `house B:` value in the stop-line grammar (HUB:120). · RUN: COMMAND `grep -n -F "not needed" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` · EXPECT: no output (exit 1).

FINDING O7 · ROW: SCOPE (L67) · CLAIM: the law text L67 (LAWS.md:338) still describes the second pass ("a SECOND fresh Opus session starts HOUSE B"), while the hub now runs one pass; the hub cites "L67 as amended" (HUB:14). · RUN: COMMAND `grep -n -F "a SECOND fresh Opus session starts HOUSE B" "/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md"` · EXPECT: `338:` hit.

FINDING O8 · ROW: F3 (F3.10) · CLAIM: BHUB:79 reads gate exit `0` as "green", but BHUB:83 makes an `OUTSIDE the allowed set` skip a RED, and gate.sh keeps exit 0 for it (`ops/desk/gate.sh:43`–`44`: "the exit does not change"). · RUN: COMMAND `grep -n -F "the exit does" ops/desk/gate.sh` · EXPECT: `43:` hit.

FINDING O9 · ROW: F1 / X1 · CLAIM: HUB:90–92 house spellings still name `opus-*.md`, a file the one-pass flow no longer writes (the builder's own note, build report :120). · RUN: COMMAND `grep -n -F "opus-*.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` · EXPECT: hits at 90, 91, 92.

## Findings
none — house A: none (overruled 2026-10-02 R47).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -n -F "L36 only the one house of your pass" <HUB>` | `32:` hit (the LAWS line) | HELD |
| O2 | Opus | `grep -n -F "every block you and the house wrote" <HUB>` | `114:COUNTING (a count rule, not a verdict): \`findings\` = every block you and the house wrote; …` | HELD |
| O3 | Opus | `grep -n -F "(the house's, kept)" <HUB>` | `58:` hit (the REPORT section list) | HELD |
| O4 | Opus | `grep -n -F "House B's spelling is house A's" <HUB>` | `89:(5) START BOTH HOUSES AT ONCE. … House B's spelling is house A's with house-b.md for house-a.md. The spelling of each house that sits:` | HELD |
| O5 | Opus | `grep -n -F "none produced" <HUB>` | hits `100:`, `123:` only; none at 117 or 120 | HELD |
| O6 | Opus | `grep -n -F "not needed" <HUB>` | `50:` only (the `REFUSED, not needed` record, unrelated); no `house B: not needed` anywhere, while :28 set `none available` only "When \"open\" is above 0" | HELD |
| O7 | Opus | `grep -n -F "a SECOND fresh Opus session starts HOUSE B" <LAWS.md>` | `338:` hit (L67 BUILD CHECK FLOW) | REJECTED — card F1 "(R438 change 1; L67 stays …)"; R438 row 173 `HIS RULING · APPROVED`; L67 OVERRIDE (LAWS.md:340). Law text is his: OPEN |
| O8 | Opus | `grep -n -F "the exit does" ops/desk/gate.sh` | `43:# no \`## ALLOWED SKIPS\` item covers is printed \`OUTSIDE the allowed set: <line>\` (the exit does` | HELD |
| O9 | Opus | `grep -n -F "opus-*.md" <HUB>` | hits `90:`, `91:`, `92:` | REJECTED — `## NOT IN THIS JOB`: "the house spellings" → OUT OF SCOPE |

CHECK ASKS (runs at `e249bd83`, before the fix):
| ask | run | output | answer |
|---|---|---|---|
| X1 | Grep `PASS-2\|PASS 2\|house B: needed\|opus-1\|diff-b\|second pass\|re-check\|outside review` over CHECK/BUILD/DEPLOY-HUB.md (`-o`) | BUILD 77, 79, 85, 85 `PASS 2`; BUILD 109 `re-check`; CHECK 3, 8 `PASS-2`; CHECK 20 `second pass`; CHECK 113 `PASS 2`; CHECK 123 `re-check`; DEPLOY 101, 105 `PASS 2` | clean: CHECK 3/8/20/123 and BUILD 109 state none exists; every `PASS 2` hit names gate-lists' with-DB pass 2, not a check pass; DEPLOY-HUB outside the job |
| X2 | Grep `--deploy` (`-o`) over CHECK/BUILD-HUB.md | BUILD 78, 79, 79, 82, 109; CHECK 110, 110, 123 | exactly the lines X2 names |
| X3 | Grep `deploy\|OUTSIDE\|allowed set` over `ops/desk/gate.sh` | `2:` usage `… [--migration] [--deploy]`; `106:        --deploy) deploy=1; shift ;;`; `112:` `--deploy belong to withdb and all`; `431:` `say "pass 1: whole (deploy)"` | spelling `<WORKTREE> all --deploy` exact; `pass 1: whole (deploy)` (BHUB:82) is gate.sh:431's string; no invented flag |
| X4 | `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` | `19 passed, 15 warnings in 2.77s` | no pinned line moved |
| X5 | O1–O6 above | — | four leftovers of one house (O1–O4) and two stop-line gaps (O5, O6); fixed |

## FIXES
| id | file:line | change | proof after |
|---|---|---|---|
| O1 | HUB:32 | `L36 only the one house of your pass` → `L36 only the two houses this file names, started at once` (L36 at LAWS.md:232: "a hub launches only the house seats its own prompt names") | O1 grep → no output |
| O2 | HUB:114 | `every block you and the house wrote` → `every block you and both houses wrote` | O2 grep → no output |
| O3 | HUB:58 | `(the house's, kept)` → `(both houses', kept)` | O3 grep → no output |
| O4 | HUB:89 | sentence added before F1.27's NEW: `Each house is started with its OWN house's line below, never the other's.` | `89:Each house is started with its OWN house's line below`; F1.27 NEW still one hit at 89 |
| O5 | HUB:117 | added: `A seat that is \`none produced\` (\`## 3\`) writes the name of the last house that sat in it and that house's line, \`<name> <METER\|HARNESS\|TIMEOUT\|NO FINDINGS LINE>\`.` (inside the stop-line grammar; no field name changed) | `none produced` hits 100, 117, 123; F1.36 NEWKEY still `117:` |
| O6 | HUB:28 | `When "open" is above 0, "house B:" reads "none available" and the open items go …` → `"house B:" reads "none available"; when "open" is above 0 the open items go …` | old text grep → no output |
| O8 | BHUB:79 | `EXIT: 0 green ·` → `EXIT: 0 green (a skip marked \`OUTSIDE the allowed set\` keeps exit 0 and is still a red, (c)) ·` | `79:keeps exit 0 and is still a red`; F3.07 NEW still `79:` |
After the fixes: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` → `19 passed, 15 warnings in 2.75s`. No test added: the findings are commands, and `tests/ops/test_hub_lines.py` is fenced ("not changed; no new test"), so no `wip(next-flow): check red` commit exists. No module page under `docs/40 - DevDocs/cobalt/` covers a hub; no DevDocs line written.
Commit: `987ab80d fix(next-flow): one-pass wording at L36 line, COUNTING, sections, house spellings, none produced, overrule house B, gate exit 0 (check O1-O6, O8)` — 2 files, 7+, 7−.

## Suites
On `987ab80d`, a "DB: none" card: RESTARTS, then W (a0), (a), (e) and `tests/ops`.
- RESTARTS: `uv run cobalt jobs restarts 1f4a8598..HEAD` → BUILD-HUB.md `M DOCS -`, CHECK-HUB.md `M DOCS -`, next-flow-build-2026-10-06.md `A DOCS -`, `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 1f4a8598` → `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/reports/next-flow-build-2026-10-06.md`: all under `docs/`. `cobalt_dev: not taken (DB: none — 3 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh next-flow-1006 offline` (exit 0) → `offline 3932/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/next-flow-1006-offline-20261006-013711.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh next-flow-1006 livenote` (exit 0) → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/next-flow-1006-livenote-20261006-014723.log`; `grep -n -F "COBALT_LIVE_VAULT_ROOT" <log>` → line 2 only (the command line), so no skip names it.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (exit 0) → `1382 passed, 1 xfailed, 15 warnings in 361.46s (0:06:01)`.
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/next-flow-1006/.env` → `No such file or directory`.

## Scope
PREFLIGHT union: `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/CHECK-HUB.md` (+ the build report, docs). My commit `987ab80d` touches the same two hub files, both in the files of rows F1, F2 and F3. Nothing else.

## Checked against the branch
(i) `git log --oneline e249bd83..HEAD -- . ":(exclude)docs"` → no output: every commit is under `docs/`, so `<tip now>` = `987ab80d`, my fix commit (the hubs are this card's code).
(ii) `git log --stat --format=%h e249bd83..HEAD` → `987ab80d` (BUILD-HUB.md 2 ±, CHECK-HUB.md 12 ±), `30f1dc02` (build report). No non-docs path.
(iii) `git log --oneline 1f4a8598..HEAD -- ops/desk tests/ops/test_hub_lines.py "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" "docs/40 - DevDocs/prompts/DEVFIX-HUB.md" "docs/40 - DevDocs/prompts/CARD.md"` → no output (fence untouched).
(iv) No HELD finding carries a test (all were commands; the test file is fenced). The proofs are the greps under `## FIXES`.
(v) `.env` → `No such file or directory`; `git status --short --branch` → `## ops/next-flow-1006`.
(vi) `git log --stat --format=%h 1f4a8598..HEAD -- src/cobalt/db_migrations tests/cobalt` → no output: no gate lists owed.
(vii) Card RECORDS: `git -C /Users/cobalt/cobalt log --oneline -3 -- "docs/40 - DevDocs/reports/cto-2026-10-05.md"` → `1f4a8598`, `59981ca7`, `4c58a879` (the card recorded `59981ca7` as newest; `1f4a8598` restored R438). `grep -n "^| R438 "` → line 173, now ending `| HIS RULING · APPROVED |` (the card's record said it lacked `APPROVED`; changed by `1f4a8598`, "R438 status restored per L7a (R484)"). `grep -n "^| R412 "` → line 109, `APPROVED (in cto-desk-contract.md, …)`. The drafter's key greps at `e71a5fa1` were not re-run (no fixed command given).
(viii) L32: this report holds no ticker, price or date of his; values are hub text and commit ids.

## OPEN
- O7 · REJECTED · L67's text (LAWS.md:338) still describes the two-pass flow; the hub now runs one pass under R438. Settled by: Dejan's amendment of the L67 entry (his law file), or his word that R438 stands as an OVERRIDE without one.
- O9 · OUT OF SCOPE (`## NOT IN THIS JOB`: the house spellings) · HUB:90–92 still name `opus-*.md`.

## CONTINUE
next: done (CHECK DONE)

## DECISIONS
- FOR DEJAN · O7: the L67 entry in LAWS.md (line 338) still says that something open leads to "a SECOND fresh Opus session" with house B, and that a mandatory build "runs the second pass". The hub at `987ab80d` runs both houses at once in one pass (R438). Law text is his, and I write nothing under the vault. Safe default taken: the hub stands as R438 built it, and the law text is left unchanged. It ships to the follow-up list: he amends L67 or confirms R438 as an OVERRIDE (L67:340).

## RECORDS
- Attribution: a system reminder in this session asked commits to carry a `Claude-Session:` line. Per L74 (CHECK-HUB:32) commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only; `987ab80d` carries only that.
- `<S>` held `diff.md` (105 bytes, 01:31) before this session. My launch carried no `CONTINUE:`, so this is not RECOVERY. With house A overruled, `## 1` was not run and the file was neither opened nor used.
- The flow followed is CHECK-HUB.md on `main` (the launch file), not the branch's new text. House A: none (overruled 2026-10-02 R47), so there was no probe and no house gate; `house B: none available` follows from CHECK-HUB:28 on main, since open = 1.
- BUILD-HUB `## THE LOCK`, `## E2`, `## RESTARTS`, `## W`: I read them at the branch tip (lines 60–110), not on `main`. The only difference is the F3 text, which a DB: none card does not use. W ran as (a0), (a), (e) and `tests/ops`.
- Not reported as findings: the build report's three card slips (RECORDS :129–132) and its ASK DESK on R438's precondition (the deploys of K3, P2, D5) stand as the builder wrote them.
- Dropped findings: none. Houses that produced nothing: none sat. REFUSED: none. CONTINUED: none. Lock takes: none.
- files opened: 8 — CHECK-HUB.md (main), areas/cobalt.md, the card, CHECK-HUB.md (tip), BUILD-HUB.md (tip, lines 15–17 and 60–110), the build report (lines 91–141), LAWS.md (L36 at 231–238, L67 at 336–345), ops/desk/gate.sh (searched).
- Check of `next-flow`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`. A deploy is gated on the combined tree (L68): one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: next-flow · pass: 1 · tip: 987ab80d · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 3932/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 1 · for Dejan: 1 · tokens: 144225
