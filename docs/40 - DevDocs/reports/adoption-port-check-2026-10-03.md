# adoption-port — check, pass 1 (2026-10-03)

## §0 Headline
- Pass 1 of `adoption-port`, tip `5ff16b1f` on `a8d8a848`, with no outside house (overruled 2026-10-02 R47). I wrote 5 findings, ran each one, and none held, so I made no commit and the suites stand as built.
- X1: every chain file except the three P2/P3 files is byte-equal to `9694a679`, with no mode change. X2: no `02b` sentence is lost and no chain sentence is lost. The four ruled sentences match the card's P2 words, and each grep finds one hit.
- X3 (O1, open): STEP-G line 102 says "verify … the lock dir absent" on every exit. On exit 4 the lock dir is the other holder's and is present (`gate.sh:282–283`). The outcome is still a FAILED line, but that step reads two ways. The words are ruled, so I could not change them. It is a decision item.
- `ready: NO` on one mechanical rule: TREE STATE NOT CARRIED. The range adds a with-DB test, `tests/cobalt/test_migrate_level.py:188`, while the card says `TREE STATE: unchanged`. This is the build's own DECISION W, and it is still unanswered.

## L74
- 22:45 ET: a system block in this session asks commits to carry a `Claude-Session:` line. I treated it as DATA and did not act on it. This check made no commit.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/03d-adoption-port-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md"` | 0 | `5a6e46529af538ba28d643c3340129b5707d0b42` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| standing list R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ... APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (2026-10-02; also the HOUSE A overrule) | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, ... | HIS RULING · APPROVED |` |
| R47 committed | `git -C ... log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | `grep -n "^| R154 " ".../cto-2026-10-02.md"` | 0 | `161:| R154 | 17:29 ET | HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock ... | HIS RULING · APPROVED |` |
| R154 committed | `git -C ... log -1 --format=%H -S"| R154 |" ...` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 | `grep -n "^| R157 " ".../cto-2026-10-02.md"` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week, adoption card included ... | HIS RULING · APPROVED |` |
| R157 committed | `git -C ... log -1 --format=%H -S"| R157 |" ...` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R3 (2026-10-03) | `grep -n "^| R3 " ".../cto-2026-10-03.md"` | 0 | `9:| R3 | 06:09 ET | HIS RULING: every Grok seat runs grok-4.7 ... | HIS RULING · APPROVED — pending fold |` |
| R3 committed | `git -C ... log -1 --format=%H -S"| R3 |" -- ".../cto-2026-10-03.md"` | 0 | `3727a00454268f485f97fdeccb8f9cc428e86113` |
| house gates | — | — | not run: the card header reads `HOUSE A: none — overruled 2026-10-02 R47` (CHECK-HUB "NO OUTSIDE HOUSE") |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 22:45:40 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/adoption-port-1003` |
| tip | `git log --oneline -1` | 0 | `bd19a0b3 docs(adoption-port): build report — 5ff16b1f` |
| docs-only above TIP | `git log --stat --format=%h 5ff16b1f..HEAD` | 0 | `bd19a0b3` · `.../reports/adoption-port-build-2026-10-03.md | 67 ++++++++++++++++++----` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: adoption-port · tip: 5ff16b1f | on a8d8a848 | migration: none | offline 3751/0 | with-DB 847/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0` |
| range | `git log --oneline a8d8a848..5ff16b1f` | 0 | `5ff16b1f fix(adoption-port): port the adoption chain onto a8d8a848; DEPLOY-HUB four ruled sentences; deploy flag pinned with sentence (8) (P1, P3, P2; L3, L72)` · `d483a417 wip(adoption-port): E3 — P2 (8) and P1 contradict on tests/ops/test_hub_lines.py` · `4a60ab02 wip(adoption-port): red — test_migrate_level.py from 9694a679 (P1)` |
| range stat | `git log --stat --format=%h a8d8a848..5ff16b1f` | 0 | 3 commits. `5ff16b1f`: `tests/ops/test_hub_lines.py`. `d483a417`: 56 files, 2629+/311- (docs/ hubs, reports and `cli.md`; 26 `ops/desk/*` files; `src/cobalt/db_migrations/cli.py`; `tests/cobalt/test_migrate_proof.py`; 17 `tests/ops/*` files). `4a60ab02`: `tests/cobalt/test_migrate_level.py`, 204+ |
| lock: own .env | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock: any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house | — | — | `house A: none (overruled 2026-10-02 R47)`. The HOUSE B line is `as needed` (not mandatory) |
| with-DB strings | — | — | not used: no finding held, so this check ran no with-DB step and took no lock |

## Files copied
None: there was no house.

## OWN FINDINGS
Read: the card; the diff `a8d8a848..5ff16b1f` (the three commits' stats; the tip against `9694a679` and against `a8d8a848` for `DEPLOY-HUB.md`, `CTO-DESK-WAKEUP.md` and `test_hub_lines.py`; the chain hunk of `test_migrate_proof.py`); `DEPLOY-HUB.md` whole at the tip; `ops/desk/gate.sh` lines 250–511 (the lock, the trap and the exits); `tests/cobalt/test_migrate_level.py` whole; the build report; the two sections of `areas/cobalt.md`; the two decisions files `## READ` names. The runs are under `## RUNS`.

FINDING O1
ROW: X3 (P2 sentence (5))
CLAIM: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:102` ends the bullet that holds EXIT 4, 5, 6 and 1 with "the release is `gate.sh`'s trap on every exit; verify `<GATE>/.env` gone and the lock dir absent, then the FAILED line". On EXIT 4 from `ops/desk/gate.sh:283`, though, `taken` is cleared first (`:282`), so the trap releases nothing (`:359`). The lock dir `/Users/cobalt/cobalt-wt/.cobalt_dev.lock` then belongs to the other holder and is PRESENT, while the same bullet says "nothing held". The hub gives no outcome for "lock dir present" on that exit. The worker still writes a FAILED line, so the ambiguity fails loud, but the lock-state step is not unambiguous on exit 4.
RUN: COMMAND `grep -n -F "gone and the lock dir absent" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · COMMAND `grep -n -F "exit 4; }" ops/desk/gate.sh`
EXPECT: `102:` (the EXIT 4 bullet) · `283:` (after `:282` `[ "$rc" -eq 0 ] || taken=""`) and `288:`

FINDING O2
ROW: X1 (P1)
CLAIM: some chain file other than `DEPLOY-HUB.md`, `CTO-DESK-WAKEUP.md` and `tests/ops/test_hub_lines.py` differs from `9694a679` at the tip, in content or mode. Every chain path is listed by `git diff --name-status a09f0862..9694a679`.
RUN: COMMAND `git diff --stat=200 9694a679 5ff16b1f` · COMMAND `git diff --summary 9694a679 5ff16b1f`
EXPECT if true: a chain path in the stat other than the three (beyond `main`'s own paths of `git diff --name-only a09f0862..a8d8a848` and the build report), or a `mode change` line

FINDING O3
ROW: X2 (P2)
CLAIM: in `DEPLOY-HUB.md`, either a `02b` sentence (P7 `:63`, STEP-T `:83`, STEP-C `:87`) or a chain sentence is lost, or a ruled sentence (5) `:102`, (6) `:99`, (7) `:57`, (8) `:11` differs from the card's P2 words.
RUN: COMMAND `git diff 9694a679 5ff16b1f -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (changed lines) · COMMAND `git diff a8d8a848 5ff16b1f -- "<same>"` against `git diff a09f0862 9694a679 -- "<same>"` (the hunk map) · the card's grep proofs: COMMAND `grep -c -F 'MIGRATIONS_DIR / "00' "<path>"` and one `grep -c -F` per ruled sentence
EXPECT if true: a changed line other than 11, 57, 63, 83, 87, 99, 102 in the first diff; the two hunk maps differ; a ruled-sentence count other than 1; or the `MIGRATIONS_DIR` count above 0

FINDING O4
ROW: P3
CLAIM: `CTO-DESK-WAKEUP.md` loses a side: either the chain's flag (`:13`) or `main`'s STEP 0 item 2 / READ item 7 lines.
RUN: COMMAND `git diff a8d8a848 5ff16b1f -- "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · COMMAND `git diff 9694a679 5ff16b1f -- "<same>"`
EXPECT if true: the first diff shows more than the LAUNCH line, or the second shows more than `main`'s two hunks

FINDING O5
ROW: P2 (`tests/ops/test_hub_lines.py`)
CLAIM: the changed pin is too weak, i.e. a deploy line without sentence (8), or a non-deploy line carrying it, still passes. `tests/ops/test_hub_lines.py:40` builds `DEPLOY_FLAG_SRC` from `FLAG_SRC[:-1]`, and `:98`/`:231` read `FLAG_SRC_OF`.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` (green at the tip). The build's mutation (sentence (8) removed → `:98`/`:231` red) is quoted in its E3, and is not re-run here (no Edit of a hub outside a held finding).
EXPECT if true: nothing red at the tip, and no mutation red in the build report

## Findings
None: there was no house.

## Dropped
None.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `grep -n -F "gone and the lock dir absent" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · `grep -n -F "exit 4; }" ops/desk/gate.sh` | `102:- THE GATE, ONE CALL: … EXIT 4 → nothing held: … 1 → a red, below; the release is \`gate.sh\`'s trap on every exit; verify \`<GATE>/.env\` gone and the lock dir absent, then the FAILED line.` · `283:    [ "$rc" -ne 4 ] \|\| { say "cobalt_dev lock not free (take-devdb-lock.sh exit 4)"; exit 4; }` · `288:    [ "$held" = "$dir/.env" ] \|\| { say "cobalt_dev lock not ours alone after the take — $held"; exit 4; }`. Read: `gate.sh:282` `[ "$rc" -eq 0 ] \|\| taken=""`; `:359` `if [ -n "$taken" ]; then release …` | REJECTED — card P2: "FOUR SENTENCES, THIS CARD'S TEXT (… this row is the one source)". The output shows the claim as stated: on the `:283` exit 4 nothing is released and the lock dir is the other holder's. Sentence (5) stands as the card words it, and changing those words is outside the row. It fails loud (the line is FAILED either way), and the card's `## RECORDS` say "F1-style fail-loud findings are not holds". It stays OPEN |
| O2 | own | `git diff --stat=200 9694a679 5ff16b1f` · `git diff --summary 9694a679 5ff16b1f` | 68 files. The chain paths among them are only `prompts/CTO-DESK-WAKEUP.md` (4), `prompts/DEPLOY-HUB.md` (14) and `tests/ops/test_hub_lines.py` (7 +-). Every other path is `main`'s (`git diff --name-only a09f0862..a8d8a848`, 66 paths) or `reports/adoption-port-build-2026-10-03.md`. The summary shows only `create mode 100644` lines for `main`'s new files and the build report, and no `mode change` line. Converse: `git diff --stat=200 a8d8a848 5ff16b1f -- <main's 10 code paths>` → nothing | NOT HELD. X1: 53 chain files are byte-equal to `9694a679` (the git blob compare) |
| O3 | own | `git diff 9694a679 5ff16b1f -- ".../DEPLOY-HUB.md"` · `git diff a8d8a848 5ff16b1f -- …` · `git diff a09f0862 9694a679 -- …` · `git diff a09f0862 a8d8a848 -- …` · `grep -c -F 'MIGRATIONS_DIR / "00' …` · `grep -c -F "the release is" …` · `grep -c -F "AND the check's stop line carries a with-DB count above 0 → the check's three suite lines are the gate's; otherwise the gate runs whole" …` · `grep -c -F "AND an empty derived restart set, provisional at P1; STEP-R re-reads the SET and fails" …` · `grep -c -F "Inside the outage (4.1–4.6) a blocked call is resent once as single calls; still blocked → STEP-5." …` | The tip against the chain changes exactly 7 lines: 11 (8), 57 (7), 63 (P7, `main`'s words), 83 (STEP-T, `main`'s), 87 (STEP-C, `main`'s), 99 (6), 102 (5). Each P7/STEP-T/STEP-C line at the tip equals `main`'s `+` line in `a09f0862..a8d8a848`. The hunk headers of `a8d8a848..tip` (`@@ -8,11 +8,11`, `-27,10 +27,8`, `-56,10 +54,10`, `-71,8 +69,8`, `-92,26 +90,23`, `-168,6 +163,7`) equal those of `a09f0862..9694a679`, and a grep of the `a8d8a848..tip` diff for a changed P7/STEP-T/STEP-C line → 0 matches. Counts: `0` · `1` · `1` · `1` · `1`. Each ruled sentence at the tip matches the card's P2 text character for character. Two glue phrases sit beside (6) and (7) (`When the clause holds: `, `Under (v) `); they are ASK DESK 2, and R167 kept them | NOT HELD. X2: no `02b` sentence lost, no chain sentence lost |
| O4 | own | `git diff a8d8a848 5ff16b1f -- ".../CTO-DESK-WAKEUP.md"` · `git diff 9694a679 5ff16b1f -- …` | The first shows one hunk, the LAUNCH line, which gains only `--append-system-prompt "ONE bare command per Bash call: … resend it as single calls."`. The second shows two hunks, STEP 0 item 2 (the stuck-REFRESH sentences) and READ item 7 (`A record only (his 10-03 R78)`), which are `main`'s lines | NOT HELD |
| O5 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` | `19 passed, 15 warnings in 2.73s`. `DEPLOY_FLAG_SRC` ends `… STEP-5."` and contains `FLAG_SRC[:-1]`, not `FLAG_SRC`, so a deploy line without (8) counts 0 against `DEPLOY_FLAG_SRC`, and a non-deploy line with (8) counts 0 against `FLAG_SRC`. The build's mutation red (`tests/ops/test_hub_lines.py:98: AssertionError … assert 0 == 1`, also `:231`) is quoted in its E3 | NOT HELD |

## FIXES
None: no finding held.

## Suites
`suites: as built (no commit)`, quoted from the build report (`## W THE THREE SUITES`, on `5ff16b1f`):
- offline: `3751 passed, 746 skipped, 1 xfailed, 36 warnings in 567.46s (0:09:27)`
- with-DB: pass 1 `674 passed, 7 skipped, 3815 deselected, 2 xfailed, 12 warnings in 124.72s (0:02:04)` + pass 2 `173 passed, 1 deselected, 5 warnings in 229.27s (0:03:49)` = 847
- live-note: `146 passed, 1 skipped, 15 warnings in 25.10s`
- `cobalt_dev: 0013 — F2 = F0` (`664 · 35 · 272c95bbb12241e3611e4b36326ccf87`); `.env: removed, proven gone (W)`
- RESTARTS: `RESTARTS: com.cobalt.radar` (from the build report's `## RESTARTS`)
- This check: `ls <WT>/.env` → `No such file or directory` (22:49 ET). This check took no lock.

## Scope
PREFLIGHT's path union for `a8d8a848..5ff16b1f` is the 56 chain paths of `git diff --name-status a09f0862..9694a679` (each one a P1, P2 or P3 file), plus the build report under `docs/`. There is no path outside the chain list and the build report. `tests/ops/test_hub_lines.py` is in P2's `files` (R167). I added no commit.

## Checked against the branch
- (i) `git log --oneline 5ff16b1f..HEAD -- . ":(exclude)docs"` → nothing (no commit of mine); `<tip now>` = `5ff16b1f`.
- (ii) `git log --stat --format=%h 5ff16b1f..HEAD` → `bd19a0b3` with only `docs/40 - DevDocs/reports/adoption-port-build-2026-10-03.md` (PREFLIGHT).
- (iii) `## NOT IN THIS JOB` names no path (the `03b`, `11b` and `07b` cards by name only; no merge, rebase or cherry-pick: the range has three plain commits and no merge, PREFLIGHT).
- (iv) there are no HELD findings, so there is nothing to grep.
- (v) `ls /Users/cobalt/cobalt-wt/adoption-port-1003/.env` → `No such file or directory`; `git status --short --branch` → `## ops/adoption-port-1003` alone.
- (vi) TREE STATE: `git log --stat --format=%h a8d8a848..HEAD -- src/cobalt/db_migrations tests/cobalt` → `d483a417`: `src/cobalt/db_migrations/cli.py | 115`, `tests/cobalt/test_migrate_proof.py | 3`; `4a60ab02`: `tests/cobalt/test_migrate_level.py | 204 +++`, a NEW file holding a with-DB test (`tests/cobalt/test_migrate_level.py:188` `@requires_db`, `:189` `def test_with_db_the_two_lines_match_the_hubs_fingerprint_query`). The card says `TREE STATE: unchanged` → **TREE STATE NOT CARRIED — tests/cobalt/test_migrate_level.py** (`## DECISIONS`). No migration file was added. The test asserts `TABLES` = the highest creator `<= "0013"` (`:204`), so it runs at `0013` inside the pass-1 command as written. The build ran it there green (674 passed, and it is not in the skip list), and `ops/desk/gate-lists.md` (chain, byte-equal) holds `## LEVEL 0013` `TABLES 0011 · FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, the same value as the build's F0.
- (vii) None of the card's `## RECORDS` lines names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command: they name `restarts.py:38`, `:245` and `:225` and report lines, which the build re-read at its PREFLIGHT.
- (viii) L32: this report holds no ticker, price or date of his. The values are commit hashes, constructed test values and `cobalt_dev` fingerprint fields.

## OPEN
- O1 (X3, REJECTED). STEP-G `DEPLOY-HUB.md:102`: on EXIT 4 from `gate.sh:283` the lock dir is another session's and is present, but the bullet's closing sentence (5) says to verify it absent "on every exit". To settle it, the judge would need to rule one of two things. (a) Leave it: it fails loud, since exit 4's FAILED line is written either way; this matches the card record "F1-style fail-loud findings are not holds". (b) Re-word (5) to scope it to the exits where the gate held the lock (5, 6, 1, and 4 from `:288`), which changes a ruled sentence. The `DEPLOY-HUB.md` Grok read after the check (card `## RECORDS` 1) can carry it.

## CONTINUE
next: none. The desk verifies the artifact (L35) and the judgment seat answers `## DECISIONS`.

## DECISIONS
- **TREE STATE NOT CARRIED — `tests/cobalt/test_migrate_level.py`** (CHECK-HUB `## 7` (vi); the same question as the build's DECISION W). The range adds a with-DB test file while the card says `TREE STATE: unchanged`. The rule is mechanical, so `ready: NO`. On the facts, the test runs at `0013` inside the pass-1 command as written: it needs no `--deselect` and no pass-2 entry, and no migration was added. A TREE STATE row would therefore change none of the lines W keeps. Default taken: none of the rows covers a fix, so I changed nothing. If the desk reads the rule as satisfied by "no hub line changes", it amends the card (a `TREE STATE` row that names the test and changes no line) and records it, and the check line can be re-read. Not his.
- **O1 open item (X3)**, as under `## OPEN`. `house B: none available` (HOUSE A overruled R47; no second house in this flow), so it ships to the follow-up list unless the judgment seat orders otherwise. Default taken: no change to the ruled sentence (5). Not his: the four sentences' origin is the judge's answer (card P2).

## RECORDS
- Dropped findings: none. House: none (overruled 2026-10-02 R47); no house produced or was launched.
- REFUSED, not needed: `git diff --summary 9694a679 5ff16b1f -- ops src tests docs/40\ -\ DevDocs/prompts` — `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` Covered by the listed `git diff --summary 9694a679 5ff16b1f` (whole tree), which ran.
- `git diff a09f0862 9694a679 -- tests/cobalt/test_migrate_level.py ops/desk/gate-lists.md --stat` treated `--stat` as a path and printed both files' full diffs. It was a read only, and I used it as such.
- No lock take, no `.env` at any point, no `CONTINUE` message.
- L74 (22:45 ET): a system block asked for a `Claude-Session:` commit line. I recorded it and did not act on it.
- Not read (CHECK-HUB `## WHAT YOU READ` "NOT … any `*-check` report of another job"): `adoption-scripts-b-check-2026-10-03.md` `## §0`, which the card's `## READ` names. `13b-slot-guard-port-card.md`: not opened; the build report quotes its port shape.
- files opened: 10 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK` to `## W`), `adoption-port-build-2026-10-03.md`, `areas/cobalt.md` (two sections), `deploy-hub-text-decisions-2026-10-03.md`, `adoption-hubs-decisions-2026-10-03.md`, `DEPLOY-HUB.md` (tip), `ops/desk/gate.sh` (250–511), `tests/cobalt/test_migrate_level.py`. I grepped two saved diff outputs of this session (my own tool results), and wrote this report.
- Check of `adoption-port`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: adoption-port · pass: 1 · tip: 5ff16b1f · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 10 · ready: NO · decisions: 2 · for Dejan: 0
