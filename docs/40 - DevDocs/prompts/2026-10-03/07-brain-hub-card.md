JOB: brain-hub
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/brain-hub-1003
WORKTREE: brain-hub-1003
BASE: a09f0862
TIP: bb930cac
REPORT: /Users/cobalt/cobalt-wt/brain-hub-1003/docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/brain-hub-check-2026-10-03.md
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R157, 2026-10-02 R54

## ROWS

WHY: today a brain is a one-off prompt file (`prompts/2026-10-02/03-brain-unattended.md`, `23-brain-judge.md`), written by hand each time, and each successor restates the same reading set and the same write fence. His A on FOR DEJAN 13: a standing `BRAIN-HUB.md`, so a brain opens on a message and its handover is one short file. The brain is a read-only prompt kind (`## THE STANDARD` 13): it writes answer files, cards and the direction file, nothing else.

| row | what | red first | files |
|---|---|---|---|
| B1 | `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, the standing text, in the shape of `23-brain-judge.md`: `## LAUNCH` (one line, `desk-launch.sh brain "<handover>"`, model `claude-fable-5-1`, `--permission-mode auto`, `--remote-control brain --name brain`, the allow list of `23`'s line exactly, `--add-dir` the three roots); `## WHO YOU ARE` (judge seat under an order, his reasoning seat; L78: he asks nothing per step, you ask nothing per step); `## READ AT START` (the handover file named on the launch line; the current direction file it names; the `## §0` and `## THE STANDARD` of the standing design report it names; `tail -n 30` of the day's desk report; nothing else); `## WRITE FENCE` (answer files `reports/<job>-decisions-<date>.md` and `reports/<topic>-answer-<date>.md`, cards under `prompts/<date>/`, edits of the direction file the handover names; no memory, LAWS, fixed-file, script, code or desk-report edit; no launch; no commit; L74); `## HOW YOU ANSWER A JUDGE REQUEST` (the five lines of `23`); `## MEASURE` (250,000 → handover; the handover file is `prompts/<date>/<nn>-brain-handover.md`, written by the brain in the shape of `## HANDOVER SHAPE` below); `## HANDOVER SHAPE` (ten lines at most: seat, predecessor id and size, the direction file, precedents as one-line rules with their card numbers, state at handover with its time, what is owed, first reply). The hub carries NO precedent of a day: those live in the handover file | RUN — asserts nothing: `grep -c "^claude --bg " docs/40 - DevDocs/prompts/BRAIN-HUB.md` → `1`; `grep -c -F "«INSTALL" …` → `1` (the title token until his row) | `docs/40 - DevDocs/prompts/BRAIN-HUB.md` |
| B2 | `desk-launch.sh brain "<handover>"`: a kind beside `prompt`: refuses a handover not under `docs/40 - DevDocs/prompts/<date>/` or holding a fill token (the opening guillemet followed by the word FILL, as `desk-launch.sh` already greps it for cards); refuses while a session named `brain` is live (his R76: a brain is stopped only on his word; the desk's `desk-done.sh brain` is run on his word first); otherwise prints and runs the `BRAIN-HUB.md` line with `<handover>` filled. `STANDING-LIST.md` gains `## 7. BRAIN-HUB.md`: the line's strings, none NEW (every string stands on `23`'s line, approved by his 10-02 R131) | `tests/ops/test_desk_launch_brain.py`, `DESK_LAUNCH_DRY=1`, stub `claude` and a stub `desk-list.sh` answering a live `brain`: the good case prints the filled line; a live `brain` → `REFUSED`; a token → `REFUSED`; a path outside `prompts/` → `REFUSED`. RED on `BASE`: `REFUSED: kind 'brain' is none of …` | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_brain.py`, `docs/40 - DevDocs/prompts/STANDING-LIST.md` |
| B3 | The first handover file in the new shape: `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`, written from `23-brain-judge.md` and the direction's state at your `BASE` time, every fact re-read (the desk report's tail at build time; the direction's `## TOMORROW`). It is the file the desk launches the next brain on, after his word | RUN — asserts nothing: `wc -l` of the file ≤ 40; a `grep -c` for the fill token (the pattern `desk-launch.sh` uses for it; never spell the token in the card) → `0` | `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md` |
| B4 | THE BRAIN'S WRITE STRINGS. On the `BRAIN-HUB.md` launch line the bare `"Write"` and `"Edit"` are replaced by `"Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/**)"` and `"Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/prompts/20*/**)"` (an Edit rule governs Write on the same glob, `BUILD-HUB.md` line 14; the fixed files at `prompts/` root are outside the second glob by construction). Every other string of `23`'s line stands byte for byte. `STANDING-LIST.md` `## 7` marks the two as the replacements of `23`'s bare pair, judge 10-03 (brain-hub build DECISION 3), on his veto list | `tests/ops/test_desk_launch_brain.py`: the dry-run line holds the two scoped strings and neither bare `"Write"` nor bare `"Edit"`; a tmp `BRAIN-HUB.md` with the bare pair → the test fails. RED on `BASE`: the bare pair | `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `tests/ops/test_desk_launch_brain.py` |
| B5 | ADDED 10-03 after the check (judge, desk row 2026-10-03 R84; check O1, route (a)). `desk-launch.sh prompt "<file>"` REFUSES a launch line that names `--name brain` or `--remote-control brain`, before anything runs: `REFUSED: a brain seat launches by desk-launch.sh brain <handover>` (one path, L3). The `prompt` header's "a brain tab" use is struck. `tests/ops/test_desk_size_guard.py`'s `04-brain-prompt.md` fixture moves off the brain names (a plain seat name) so its size-guard case still runs | `tests/ops/test_desk_launch_brain.py`: drop the strict xfail marker on the check's `test_o1_…`, which then passes; a `prompt` file whose line holds `--remote-control brain` → `REFUSED: a brain seat launches by desk-launch.sh brain <handover>`; `tests/ops/test_desk_size_guard.py` green. RED on the tip `18c26c70`: the `prompt` kind runs the brain line | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_brain.py`, `tests/ops/test_desk_size_guard.py` |

## NOT IN THIS JOB
- The brain's allow list beyond row B4: no string added; B4 narrows two.
- Any law, memory or NOW edit; `JUDGE-HUB.md` and `JUDGE-CARD.md` (the judge card kind stands beside; the brain is a seat, not a card job).
- Launching a brain: his word, then the desk.

## READ
- `prompts/2026-10-02/23-brain-judge.md` whole (the shape and the line); `prompts/2026-10-02/03-brain-unattended.md` lines 1–20 (the first brain's reading set).
- `reports/brain-direction-2026-10-02.md` `## RULED AFTER THE FIRST WRITE` (FOR DEJAN 13 = A) and `## TOMORROW`.
- `reports/brain-unattended-2026-10-02.md` `## THE STANDARD` 8, 13; `## FOR DEJAN` item 13.
- `ops/desk/desk-launch.sh` the `prompt` kind (its write-path refusal is the shape B2 follows).
- `docs/40 - DevDocs/prompts/JUDGE-HUB.md` title and `## LAUNCH`: the seat this file sits beside, so the two never contradict.

## CHECK ASKS
- X1 Can a brain launched on this file write anything outside its fence (a tool it is allowed that reaches a law file, a script, a settings file)? Read the allow list string by string.
- X2 Does the hub text ask a fresh brain to read anything the handover does not name, or repeat a precedent that will go stale?
- X3 Does `desk-launch.sh brain` ever launch while a `brain` is live?

## RECORDS
- `DB: none`: every file is under `docs/` or `ops/`, `tests/ops/`.
- His R76 (09-30) and R131 (10-02) bind the seat: stopped only on his word; the successor prompt `23` is the approved shape and line.
- The install token: the hub's title carries `«INSTALL` until his row names it; `install-fixed.sh` replaces it (card `17`).
- FOR THE CHECK: Build decisions 1–6 answered by the judge: D3 fixed by row B4 (scoped write strings, his veto list); D1, D2, D4, D5, D6 KEEP; the unknown-kind text is not edited by this card or by 03.
- JUDGE 10-03 (desk row 2026-10-03 R84), check O2: the brain line's `git -C … diff*` string stays as is; the narrowing is the Sunday guard's (card `10`: deny `--output=` on any `git`, `-i` / `w` on `sed`, every seat), on his VETO LIST with the B4 narrowing. After `07` is on `main` the brain changes `00-brain-handover.md`'s launch line to the `brain` kind.
