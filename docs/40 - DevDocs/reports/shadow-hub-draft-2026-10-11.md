# SHADOW-HUB card · draft · 2026-10-11

## §0 Headline
- Card `prompts/2026-10-11/324-shadow-hub-card.md` drafted: fixed files SHADOW-HUB and SPIKE-HUB, launcher kinds `shadow <card> --model <id>` and `spike <prompt>`, guard kinds, a results-table shape, and a RUN row for `seat()`. 11 rows.
- Arms per his R1019: Grok 4.7 (first, n=2 per band, plus drafter, preflight and judge trials), Sonnet 5.5, Terra. Opus and Sol are not measured; his word says they build every band. Gemini 4 is N/A.
- Four new command classes, each marked NEEDS HIS SIGN-OFF. The launcher refuses an unsigned model.
- `RULINGS: 2026-10-11 R1008` will be REFUSED by the launcher as it stands: R1008 carries no APPROVED (D-2).

## DECISIONS
- ASK DESK: the three builder strings and the spike line are NEW COMMAND CLASSES (R411). Default: each is in the card as `NEEDS HIS SIGN-OFF «SIGN: his row»`, with ONE sign-off for both kinds asked when the card is built and checked. S2 and P2 refuse until the row is signed. [06:21 EDT]
- ASK DESK: `RULINGS: 2026-10-11 R1008`, as the prompt orders. R1008 reads `HIS RULING` with no `APPROVED` (`cto-2026-10-11.md`, R1008 row), and `ruling_row` refuses that (`ops/desk/desk-launch.sh:268-270`). Default: kept as ordered; before the build launch the desk adds the APPROVED row or names R1009 (HIS RULING · APPROVED, "every build waiting on his word"). [06:21 EDT]
- ASK DESK: BASE is left `«FILL: main's code commit at the build launch»`. HEAD moved from `4f204e1b` to `8cc30dd5` during this draft. Default: the desk fills it at launch. [06:21 EDT]
- ASK DESK: the direction file `reports/model-bakeoff-redo-answer-2026-10-11.md` is untracked (`git status` `??`), and at 06:19:45 it did not yet carry R1019 at its head, despite the desk's message. The card cites it in `## READ`. Default: the desk adds R1019 to it and commits it before the build launch. [06:21 EDT]
- ASK DESK: can `codex exec -s workspace-write` (the Terra arm) run a shell command inside its sandbox? If it can, the flag does not hold "writes only". A Terra pass while `.env` is in the worktree could read it. Default: SHADOW-HUB runs no builder pass between a lock's take and its release, X3 asks the check, and the Terra arm waits for the first-gate X1 run on its line. `-C <wt>` is unproven too. [06:21 EDT]
- ASK DESK: the Sonnet line adds `--permission-mode dontAsk`, `--output-format json` (tokens per build) and `--disallowedTools "Bash" …` to the direction's string. Default: included, under the same sign-off. [06:21 EDT]
- ASK DESK: S3 (guard, kind `shadow`) and S4 (authorize, preflight and watch name the kind) go beyond FINAL §3's two artifacts. Without them, G7 (`bare-guard.py:1055-1059`) denies every builder call, and `authorize.sh`/`preflight.sh` refuse the kind. Default: included. The shadow fence is narrower than "its worktree": only `SHADOW-INSTRUCTIONS.md` and the report, since the gate seat never edits code. [06:21 EDT]
- ASK DESK: the 10-10 `seat()` follow-up row (R1021) was not found by my reads; `grep "follow-up"` over the 10-10 reports shows no `seat()` row. Default: P4 is a RUN row that quotes `seat()`'s kind for the brain, a drafter and the spike, and its output becomes a DECISION, not a guessed fix. I read that `:765-766` names any dated repo prompt `brain`, while the real brain reads `BRAIN-HUB.md`, which `HUBS` does not hold. [06:21 EDT]
- ASK DESK: Grok's extra card per band and the role-trial inputs (R1016) are the proposer's. Default: they are named on the desk's shadow cards, not in this card. [06:21 EDT]
- ASK DESK: the spike scratch dir is the literal `sdk-spike-1010` in SPIKE-HUB's line, so the line stays string for string prompt 330's and its READY YES preflight still applies. Default: a second spike with another dir is a later card. [06:21 EDT]

## RECORDS
- Ids (STEP 1), read 06:15:03-06:16:05 EDT:
  - `PROVEN gpt-5.6-sol` (`/Users/cobalt/.codex/models_cache.json:224`, `grep -n "\"slug\":"`), dropped from the card per R1019.
  - `PROVEN gpt-5.6-terra` (`models_cache.json:319`, same command).
  - `PROVEN grok-4.7` (`docs/40 - DevDocs/prompts/CHECK-HUB.md:91`, the Grok seat, his 10-03 R3; profile `ops/grok-sandbox.toml:5-14`).
  - `PROVEN claude-opus-5-5` (this session's environment model list), dropped per R1019.
  - `PROVEN claude-sonnet-5-5` (this session's environment model list).
  - `N/A — id not found` for Gemini 4: `CHECK-HUB.md:92` names `gemini-3.1-pro-high`; `UNATTENDED-LAUNCH.md` names no Gemini id; `grep -rn -o -i "gemini-4…"` over `prompts/`, `ops/` and `LAWS.md` found only prompt 323.
- HEAD proof: `git -C /Users/cobalt/cobalt status --short` over every cited file (`desk-launch.sh`, `bare-guard.py`, `restarts.py`, BUILD-HUB, CHECK-HUB, CARD, STANDING-LIST, FINAL, `grok-sandbox.toml`, `jobs.yaml`, `cto-2026-10-11.md`) printed nothing, 06:15:35 and 06:16:31 EDT, so every `file:line` was read equal to HEAD. The one exception, the untracked direction file, is in DECISIONS. `git show HEAD:` was used for card 231 (06:14). `git log --oneline -1` → `8cc30dd5`.
- Lines read: `desk-launch.sh` 180-329, 440-464, 600-799, 995-1019, 1250-1327 (1327 lines); `bare-guard.py` 18-97, 142, 748-775, 1040-1067; `BUILD-HUB.md` 1-92; `CHECK-HUB.md` 85-96; FINAL 60-288; `CARD.md` whole; `authorize.sh:42-47`; `preflight.sh:45-49`; `desk-watch.sh:27-39`; `stop-guard.py:155`; `restarts.py:38,225-232,246`; `STANDING-LIST.md:11,98`; `BRAIN-HUB.md:8`; prompt 330 `:1,7,15`; the spike preflight's last line.
- Desk messages, each verified against `reports/cto-2026-10-11.md` before it was folded in: R1014 (routing, not exclusion; 06:15:35), R1016 (Grok deepest and first; 06:17:06), R1019 (no Opus or Sol arm; 06:19:07), R1021 (spike kind in the same card; 06:19:51). The desk's row times (06:27-06:54 ET) are later than this session's `date` (06:15-06:21 EDT). Recorded only.
- Precedent copied: `prompts/2026-10-10/231-ops-hand-card.md` (fixed file plus launcher kind plus guard kind, `«INSTALL` gate, DECISIONS FOR HIM).
- RESTARTS: none expected. `ops/desk/` → operator script (`restarts.py:230-232`), `docs/` → DOCS (`:225-228`), `tests/ops/` → no resident (`:246`). Row S6 proves it.
- Card size: 76 lines, 17,789 bytes before the spike fold (`wc -c`). A new file, so no shrink rule applies.
- AMEND 06:23:04 EDT (desk message, brain direction L79), edit only; no other row touched:
  - The card at HEAD `850e1cd6` was committed by the desk with `RULINGS: 2026-10-11 R1009`. It stays (direction (1)). The DECISIONS item on R1008 is answered by that.
  - The redo file was re-read at the committed blob (`git show HEAD:…model-bakeoff-redo-answer-2026-10-11.md`, 06:22:40). R1016 is at `## PURPOSE` "His next words" (`:9`), and R1019 is at `:19` with "This SUPERSEDES" at `:20`. The DECISIONS item on the untracked file is answered by that.
  - S1 (d): the `.env` precondition replaces "no builder pass while `.env` is in the worktree". Any model's pass starts only after `ls -la <wt>/.env` → `No such file`; `.env` lives only inside the gate's with-DB step under the lock (L76); builder and gate passes never overlap; Terra's network is OFF (the `workspace-write` default), and X1 proves it before the Terra arm runs.
  - New row S7: the guard holds the precondition for kind `shadow` (a builder call is exit 2 while `<wt>/.env` exists, a symlink included). RED first: the route-line assertion on `BASE`, plus the file test for the `ls -la` step before every pass and Terra's `network: off`.
  - P4 stays a RUN row (direction (4)).

SHADOW-HUB CARD DRAFTED · decisions: 10
