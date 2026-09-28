# Shrink pre-apply checks — P1 · X9 · X3b · X11 (2026-09-28)

## §0 Headline
- Run 07:10–07:40 EDT on `F/` as measured 07:3x (the desk edited `F/CTO-DESK-WAKEUP.md` and `F/cto-desk-contract.md` at 07:30 and the live contract moved 16,384 → 16,709 B; every figure below is dated). Live files, DB, git and vault untouched; writes only under `scratch/shrink-checks/` and this file.
- P1 7/10 groups hold, 3 BROKEN (readers of moved contract text) · X9a 97/97 real links resolve (LAWS 79 · contract 11 · wake-up 6 · INDEX 1 · cobalt 0; APPLY says 96) · X9b 4/5 houses answered on one route (Opus, Astra, Grok, qwen; every named path exists), agy HARNESS x2 · X3b **FAIL** on READ 5 alone (iii), PASS with READ 3 in context; a one-sentence fix is proven on scratch · X11 PASS 23/23 cut points, 18/18 files, 4/4 created paths gone.
- Forced changes: 5 (READ 5 wording; APPLY.md figures; three prompt readers). ESCALATE: 4.

## P1
Scope: every prompt in `prompts/2026-09-25/` (45), `2026-09-27/` (13), `2026-09-28/` (5) — grepped for `cto-desk-contract`, `CTO-DESK-WAKEUP`, `### prompts and cards`, `- R3 `, `### L`, `LAWS.md`, `UNATTENDED-LAUNCH`, `SESSION-CLOSE`, `CLAUDE.md`, and every distinct quoted `grep` pattern (435 distinct). The queued ones (`34`, `36`/`37`/`09`, `99-close`) were read for their literals.

| # | reader (prompt:line) | literal | after apply (`F/` file:line) | verdict |
|---|---|---|---|---|
| 1 | `2026-09-27/51-review-deploy-hotfix.md:21` (executed: `reports/deploy-hotfix-read-2026-09-27.md`) | `grep -n -F "- R3 "` on `Memory/topics/cto-desk-contract.md` | `F/cto-desk-checklist.md:61` (`## reads`); `F/cto-desk-contract.md`: 0 lines | **BROKEN** — path |
| 2 | `2026-09-25/31-draft-stacked-deploy.md:9` (consumed by `32`) | heading `### prompts and cards`, K10 | `F/cto-desk-checklist.md:79` `## prompts`, K10 `:90` | **BROKEN** — heading renamed |
| 3 | `2026-09-25/38-draft-stack-seam-build.md:21` (consumed by `39`) | `### prompts and cards`, K16 / K17 | `F/cto-desk-checklist.md:96`, `:97` under `## prompts` | **BROKEN** — heading renamed |
| 3b | same line, `UNATTENDED-LAUNCH.md` §1 and §5 | `§1`, `§5` | `F/UNATTENDED-LAUNCH.md:3` `## 1. Before launch`, `:24` `## 5. Facts` | HOLDS |
| 4 | `^### L<n> ` greps: `2026-09-25/29, 33, 40, 41, 45`; `2026-09-27/46, 49` | L1 L19 L35 L42 L43 L45 L48 L54 L61 L62 L63 L66 L67 L68 L70 L71 L72 L76 | `F/LAWS.md`: every `^### L<n> ` for n = 1…77 prints exactly 1 line (loop, 0 exceptions); no prompt cites n > 77 | HOLDS |
| 5 | "`LAWS.md` … in full" — 39 prompts in `2026-09-25/` and `2026-09-27/` | file + `L59` | `F/LAWS.md` exists; `### L59 Worker law-reading` at `:307` reads Preamble + Index + named entries | HOLDS as a path; "IN FULL" is stricter than L59 now (a cost, not a break) |
| 6 | desk-row greps `^| R<n> ` in `cto-2026-09-2x.md`: R17 R19 (`cto-2026-09-24.md:35`, `:37`), R64 (`cto-2026-09-25.md:73`), R4 R9 R11 R15 R23 (both 09-25 and 09-27), R74, R109 | row literals | apply writes no report; row shape untouched | HOLDS |
| 7 | desk-written literals: `STACKED DEPLOY 2026-09-25 APPROVED`, `no other house hub is running`, `FILL AT LAUNCH`, `R_[_]` | — | the first three live in no contract, checklist, wake-up or LAWS file (live and `F/`, grep) — the desk writes them into launch rows and prompts; `R_[_]` is a rule in live contract line 53 and moves unchanged to `F/cto-desk-checklist.md:29` | HOLDS (X3, the row → `-words.md` migration, is not this run) |
| 8 | `2026-09-27/99-close.md` (queued) | `SESSION-CLOSE.md` steps 1, 2, 2a, 4a, 5, 6 (3, 4 desk-owned); the `awk '/^## NOW/…/^## What Cobalt is/'` range | `F/SESSION-CLOSE.md` table rows 1, 2, 2a, 3, 4, 4a, 5, 6, 7; `F/cobalt.md:11` `## NOW`, `:14` `## What Cobalt is` | HOLDS |
| 9 | prose "the CLAUDE.md rule" / "CLAUDE.md's absolute boundary": `2026-09-25/02:106, 05:25, 16:3, 17:4, 18:4, 21:92, 24:3, 25:4, 26:4, 36:111, 39:137` | not greps | CLAUDE.md becomes a 126 B stub; boundary at `F/cobalt.md:16`, DevDocs rule at `:29` | HOLDS as pointers (see ESCALATE 5) |
| 10 | `2026-09-25/34`, `36`, `37`, `09`; `2026-09-27/48–50, 52–53`; `2026-09-28/01–05` | code / log / vault-note greps; `53` and `19-draft` read the wake-up whole (no literal) | — | HOLDS |

P1: **7 of 10** reader groups hold; BROKEN 3 (rows 1–3). Exact edits are under `## FORCED CHANGES`.

## X9a
`grep -c -x -F "## <target>"` / `"### <target>"` on the target file in `F/`, each must print exactly 1. Two passes (07:2x on the first build, 07:3x after the desk's 07:30 edits): identical.

| file | links | resolved (exactly 1 line) |
|---|---|---|
| `F/LAWS.md` | 79 (77 `### L<n>` + `Reading` + `Fold at session close — …`) | 79 |
| `F/cto-desk-contract.md` | 11 (all `cto-desk-checklist#…`: handover replies rulings launch watch×2 commit reads prompts memory close) | 11 |
| `F/CTO-DESK-WAKEUP.md` | 6 (handover×2 rulings launch watch close) | 6 |
| `F/INDEX.md` | 1 (`LAWS#Index`) | 1 |
| `F/cobalt.md` | 0 real links — `:8` holds `[[name#heading]]` as a grammar example, not a link | — |

Total 97 / 97; 0 misses. APPLY's "78 + 11 + 6 + 1 = 96" is stale: LAWS gained L77 (its `## Index` line) after the derive.

## X9b
Candidate tree `scratch/shrink-checks/tree/`: the live memory folder (`Memory/`, 828 KB) and the repo start files (`repo/`) copied, then every `F/` file copied over its live name per `APPLY.md` (rows 4–9b, 14–16; `_retired/cobalt.md`, `_retired/writing-rules.md`; `cobalt.md` with the LIVE `## NOW` line pasted over the `«snapshot …»` line = 5,687 B, as APPLY estimates). Deviations, both mine: (a) the absolute paths inside the copies (`/Users/cobalt/Vault/Think/6 - Permanent/Memory`, `/Users/cobalt/cobalt/`) were rewritten by `sed` to the tree's paths, so a house cannot wander into the live files; (b) the tree sits inside the `agy-trial` worktree, whose root carries the OLD `CLAUDE.md` (16,590 B), `AGENTS.md`, `QWEN.md`: Claude ran with `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1`, Codex with `-c project_doc_max_bytes=0`; Grok had no such switch found (its answer shows no old-tree content), qwen ran with `--bare` (no implicit context-file discovery), agy never got that far. The wake-up copied into the tree is the 07:2x build, not the 07:30 one — no house's path touches it.

Question (one fixed sentence, start file = the named file in the tree): "Starting only from <start file>, which files and line ranges do you open to learn (1) the current state, (2) the laws that bind a hub launch, (3) the desk's launch checklist? List each path and range; open nothing else."

| house | start file | command (flags after the prompt) | result | every named path exists in `tree/`? |
|---|---|---|---|---|
| Opus 5.5 | `repo/CLAUDE.md` | `claude -p --model claude-opus-5-5 "<q>" --allowedTools Read Grep Glob --add-dir <tree>` (`--bare` failed: "Not logged in") | answered | yes (5/5); ranges checked: `## Start here` 6–10, `## NOW` 11–13, INDEX `## start` 7–12, LAWS `## Reading` 90, checklist `## launch` 21–40 |
| Astra | `repo/AGENTS.md` | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only -C <tree>/repo -c project_doc_max_bytes=0 "<q>"` | answered | yes (8/8) |
| Grok | `repo/AGENTS.md` | `grok --sandbox cobalt-job -p "<q>"` (cwd `tree/repo`) | answered | yes (3/3 + the chain it names) |
| agy | `repo/AGENTS.md` | `agy --print="<q>" --model gemini-3.1-pro-low --mode plan --sandbox --print-timeout 7m --add-dir <tree>`, twice | **HARNESS**: no output, a `command` tool auto-denied in headless mode (no allow-rule for the tree in `~/.gemini/antigravity-cli/settings.json`, which is not mine to edit) — recorded, not a defect (L70) | n/a |
| qwen | `repo/QWEN.md` | qwen --bare --auth-type openai --openai-base-url http://localhost:1234/v1 --openai-api-key lmstudio -m mainframe (cwd tree/repo, --approval-mode plan, --add-dir tree); first try without those auth flags: exit 1, No auth type is selected | answered after about 20 min (plan mode refused one shell loop, then answered from earlier reads) | yes (5/5 files; ranges match the tree: 6-10, 11-13, 7-12, 1-89, 229-231, 313-324, 21-40) |

Same route in all four answers: start file → `areas/cobalt.md` `## Start here` → `INDEX.md` `## start` → `LAWS.md` Preamble + Index (1–89) plus named entries (all four name L36, L61, L62, L63; Opus also L29 L33 L34 L47 L55; Astra reads nine LAWS ranges) → `topics/cto-desk-checklist.md` `## launch` 21–40. Read whole: `cobalt.md` 1–55 (Astra), `INDEX.md` 1–33 (Astra, Grok), `LAWS.md` 1–102 (Astra) — against `F/MEASURE.md`.

Answers verbatim:

**Opus 5.5** (`x9b/claude.out`)

~~~~
I read only CLAUDE.md, the files it points to in a chain, and heading lists found with grep. I haven't opened anything below yet; each range runs from a heading to the line before the next one.

**The route from CLAUDE.md:**
- `repo/CLAUDE.md` 1–3 → sends you to `areas/cobalt.md` `## Start here`
- `Memory/areas/cobalt.md` 6–10 (`## Start here`) → says to read `## NOW`, then follow INDEX `## start`
- `Memory/INDEX.md` 7–12 (`## start`) → points to LAWS Preamble + Index; lines 15–17 list `cto-desk-checklist` under "retrieve when the task asks"

**(1) Current state**
- `Memory/areas/cobalt.md` **11–13** (`## NOW`): ALL STOP is still in effect until the startup redesign is applied, and it's waiting on Dejan's single approval. The live deploy is `3349466f` and main is `8c3049db`.

**(2) Laws that bind a hub launch** (`Memory/LAWS.md`)
- **1–89**: title, Preamble and Index. Every house must read these first.
- **90–102** `## Reading`: how an entry binds. Read it before citing law.
- The entries a hub launch touches:
  - **200–205** L29 Model rule: write-path sessions run on the top model, never in auto mode.
  - **218–221** L33 Roles, not flags: fixed launcher profiles.
  - **222–225** L34 Every spawn is a job row.
  - **229–231** L36 No worker spawns workers: the desk starts hubs.
  - **266–269** L47 The meter is not the router: check the meter before launch.
  - **293–295** L55 Push, no bypass: never use `bypassPermissions`.
  - **313–315** L61 Desk launches, deploy permissions: hubs start in the background.
  - **316–321** L62 Unattended launch: grant every permission before start.
  - **322–324** L63 No dialogs, ever: every launch line denies the dialog tools.

**(3) The desk's launch checklist**
- `Memory/topics/cto-desk-checklist.md` **21–40** (`## launch`)

If you're working as the CTO desk, INDEX line 12 also makes `cto-desk-contract` required reading at startup. I haven't found or opened that file.
~~~~

**Astra** (`x9b/codex.out`)

~~~~
Paths below are relative to `/Users/cobalt/cobalt-wt/agy-trial/scratch/shrink-checks/tree/`.

| Purpose | Path | Lines opened |
|---|---|---|
| Starting instructions | `repo/AGENTS.md` | 1–3 |
| Navigation and current state | `Memory/areas/cobalt.md` | 1–55; **NOW: 11–12** |
| Required reading route | `Memory/INDEX.md` | 1–33 |
| Required preferences | `Memory/preferences.md` | 1–13 |
| Required profile | `Memory/profile.md` | 1–11 |
| Law preamble, index, interpretation | `Memory/LAWS.md` | 1–102 |
| Laws relevant to hub launch | `Memory/LAWS.md` | 164–167, 200–205, 218–231, 245–247, 254–257, 266–269, 293–295, 307–327, 355–365 |
| Desk’s launch checklist | `Memory/topics/cto-desk-checklist.md` | **21–40**; also scanned heading lines to locate it |

No other file contents were opened.
~~~~

**Grok** (`x9b/grok.out`)

~~~~
I'll start from `AGENTS.md` and follow only the references it names for current state, hub-launch law, and the desk launch checklist.**(1) Current state.** `/Users/cobalt/cobalt-wt/agy-trial/scratch/shrink-checks/tree/Memory/areas/cobalt.md` lines 11–12 (`## NOW`).

**(2) Laws that bind a hub launch.** `/Users/cobalt/cobalt-wt/agy-trial/scratch/shrink-checks/tree/Memory/LAWS.md` lines 1–89 (through the Index, stopping before `## Reading`), then the entries that cover starting a hub and the launch line:

- L36, lines 229–230
- L61, lines 313–314
- L62, lines 316–320
- L63, lines 322–323

**(3) Desk's launch checklist.** `/Users/cobalt/cobalt-wt/agy-trial/scratch/shrink-checks/tree/Memory/topics/cto-desk-checklist.md` lines 21–40 (`## launch`).

Reached only through `AGENTS.md` lines 1–2, `cobalt.md` lines 6–9 (`## Start here`), and `INDEX.md` lines 1–33 (read once; `## start` is 7–12, and the checklist pointer is line 17). Nothing else.
~~~~

**agy** (`x9b/agy.err`, identical on both tries)

~~~~
jetski: no output produced — a tool required the "command" permission that headless mode cannot prompt for, so it was auto-denied. Add an allow-rule under permissions.allow in settings.json (e.g. command(<target>)). Alternatively, re-run with --dangerously-skip-permissions to auto-approve all tools.
exit 0
~~~~

**qwen** (`x9b/qwen.out` / `qwen.err`)

~~~~
<think>The `for` loop with `wc -c` was flagged as potentially non-read-only (probably because of the loop/printf construct). Let me use a simpler read-only approach. Actually, I already have enough information from the earlier reads to determine the ranges. Let me just use sed (which is read-only) without the for loop.

Actually, I've already confirmed:
- L36 = 229–231 (heading + 1 body line + blank)
- L61 = 313–315 (heading at 313, next heading L62 at 316)
- L62 = 316–321 (heading at 316, next heading L63 at 322)
- L63 = 322–324 (heading at 322, next heading L64 at 325)

The exact blank-line positions within don't change the ranges I'll report — I'll report each entry as "heading line through the line before the next heading." That's the standard way to express it, and it matches LAWS.md's own instruction: "read through its body, stopping before the next heading of equal or higher level."

So:
- L36 = 229–231 (stops before L37 at 232)
- L61 = 313–315 (stops before L62 at 316)
- L62 = 316–321 (stops before L63 at 322)
- L63 = 322–324 (stops before L64 at 325)

I have everything I need. Let me not run more commands — I have all the line numbers confirmed:

**LAWS.md:**
- `## Preamble` = 5, `## Index` = 8, `## Reading` = 90
- Top down to `## Reading` = lines 1–89
- L36 = 229, L37 = 232 → L36 entry = 229–231
- L61 = 313, L62 = 316 → L61 entry = 313–315
- L62 = 316, L63 = 322 → L62 entry = 316–321
- L63 = 322, L64 = 325 → L63 entry = 322–324

**cobalt.md:**
- `## Start here` = 6, `## NOW` = 11 → Start here = 6–10
- `## NOW` = 11, `## What Cobalt is` = 14 → NOW = 11–13

**INDEX.md:**
- `## start` = 7, `## before writing` = 13 → start section = 7–12
- cto-desk-contract pointer = line 12 (in start section)
- `## retrieve when the task asks` = 15, cto-desk-checklist pointer = line 17

**cto-desk-checklist.md:**
- `## launch` = 21, `## watch` = 41 → launch section = 21–40

**QWEN.md:**
- 3 lines total (1–3)

Now let me compose the final answer. This is a plan-mode / read-only investigation task, and the user asked me to "List each path and range; open nothing else." So my deliverable is the list. I should present it clearly, grouped by goal, with the shared read path noted.

Let me reconsider whether I should present this as a "plan" via exit_plan_mode, or just answer directly. The user's question is a direct question: "which files and line ranges do you open... List each path and range." This is asking for an answer, not a plan to execute. Since I'm in plan mode and this is purely informational (no changes to make), I should just answer the question directly with the list.

Wait — but plan mode says "Present your plan by calling the exit_plan_mode tool." However, this task isn't really a "plan to execute changes" — it's a question about what I would read. There are no code changes to make. The user is testing my ability to trace the read path and identify minimal ranges.

Hmm, let me reconsider. The plan mode instructions say I'm "pair-planning with the user" and should present a plan via exit_plan_mode. But this particular task is a read-only investigation question with a definitive answer (a list of files/ranges). There's nothing to "execute" — the answer IS the deliverable.

I think the right move is to just answer the question directly with the list, since:
1. The task is purely informational (identify files/ranges)
2. There are no changes to make or execute
3. The user explicitly asked me to "List each path and range"

Calling exit_plan_mode would imply there's a plan of actions to execute, which doesn't fit here. The answer is the list itself.

Actually, let me reconsider once more. In plan mode, I'm not supposed to make edits or run state-modifying tools. Answering a question with text is fine — it's not an edit or a state change. So I can just provide the answer as text.

But wait — is providing the "list of files I would open" itself a kind of plan? The user asked "which files and line ranges do you open to learn X?" — this is asking me to identify/report, not to actually go open them (I've already opened them for investigation). So my answer is a report of the minimal read set.

I'll provide the answer directly as text, clearly structured. I won't call exit_plan_mode because there's no execution plan — the deliverable is the list itself, which I'm providing now.

Hmm, but actually, let me reconsider whether the system wants me to use exit_plan_mode. The plan mode reminder is quite insistent: "Present your plan by calling the exit_plan_mode tool, which will prompt the user to confirm the plan."

But that's for when there's an implementation plan. Here, the "task" is to identify and list files/ranges — which I've done through investigation. The answer is complete. There's no subsequent execution step that needs user confirmation.

I think the cleanest interpretation: this is a research/identification question, and I should answer it directly. The "plan" in plan mode is about what changes to make; here there are no changes, just an answer. I'll provide the list directly.

Let me reconsider — maybe I'm overthinking the plan mode aspect. The user gave a specific, answerable question. I've done the investigation. Let me just give a clear, well-structured answer with the file paths and line ranges, grouped by the three goals plus the shared read path.

Let me write the final answer. I'll be precise and concise, matching the CLI tone. I'll use absolute paths as required.

Let me structure it:

**Read path (shared, opened in order):**
1. `/Users/cobalt/.../repo/QWEN.md` — 1–3 (whole file; sole pointer → cobalt.md `## Start here`)
2. `/Users/cobalt/.../Memory/areas/cobalt.md` — 6–10 (`## Start here`; directs to `## NOW`, then INDEX.md `## start`)
3. `/Users/cobalt/.../Memory/INDEX.md` — 7–12 (`## start`; read order; line 8 → LAWS#Index for laws)

Wait, let me get the exact line of the LAWS pointer in INDEX.md's start section. From my read:
```
## start — read in this order        (line 7)
- [[cobalt]] — follow its `## Start here`.   (line 8)
- [[preferences]] — how he works with agents  (line 9)
- [[profile]] — who he is   (line 10)
- [[LAWS#Index]] — ...   (line 11)
- [[cto-desk-contract]] — read only if you are the CTO desk...  (line 12)
```

So:
- Line 7: `## start — read in this order`
- Line 8: `- [[cobalt]] ...`
- Line 9: `- [[preferences]] ...`
- Line 10: `- [[profile]] ...`
- Line 11: `- [[LAWS#Index]] ...`
- Line 12: `- [[cto-desk-contract]] ...`

So the LAWS#Index pointer is on line 11, and cto-desk-contract is on line 12. The start section = lines 7–12.

And the retrieve section:
- Line 15: `## retrieve when the task asks`
- Line 16: `- [[LAWS-HISTORY]] — superseded law`
- Line 17: `- [[cto-desk-checklist]] — the desk's checklist, one section per trigger`

So cto-desk-checklist pointer = line 17. ✓ (confirmed by grep)

Now let me finalize the answer:

**Shared read path (in order):**
1. `repo/QWEN.md` — lines 1–3 (whole file)
2. `Memory/areas/cobalt.md` — lines 6–10 (`## Start here`)
3. `Memory/INDEX.md` — lines 7–12 (`## start`)

**Goal 1 — current state:**
4. `Memory/areas/cobalt.md` — lines 11–13 (`## NOW`)

**Goal 2 — laws that bind a hub launch:**
5. `Memory/INDEX.md` — line 11 (`[[LAWS#Index]]` pointer) [within the start section]
6. `Memory/LAWS.md` — lines 1–89 (top → just before `## Reading`: Preamble + Index)
7. `Memory/LAWS.md` — lines 229–231 (L36 No worker spawns workers)
8. `Memory/LAWS.md` — lines 313–324 (L61 Desk launches · L62 Unattended launch · L63 No dialogs, ever)

**Goal 3 — desk's launch checklist:**
9. `Memory/INDEX.md` — line 17 (`[[cto-desk-checklist]]` pointer)
10. `Memory/topics/cto-desk-checklist.md` — lines 21–40 (`## launch`, L1–L17)

That's the complete minimal set. Let me present this clearly with full absolute paths.

Let me reconsider goal 2's range for LAWS.md "top down to ## Reading". The INDEX says "`LAWS.md` from its top down to `## Reading`: the Preamble and the Index." So it's lines 1–89 (line 90 is `## Reading`, which we stop before). Actually "down to ## Reading" — does it include the `## Reading` heading line (90) or stop before it? The phrasing "from its top down to `## Reading`: the Preamble and the Index" clarifies that it's "the Preamble and the Index" — so it's lines 1–89 (Preamble at 5-7, Index at 8-89), stopping before `## Reading` (line 90). I'll say lines 1–89.

Now, one more consideration: should I present L61/L62/L63 as separate ranges or combined? They're contiguous (313–324). I'll present them as one range 313–324 but label the three laws, since they form the launch cluster. Actually, for precision and to match "each path and range," I'll give:
- L36: 229–231
- L61–L63 (contiguous launch cluster): 313–324

Or I could break L61/L62/L63 into 313–315, 316–321, 322–324. I think giving the combined contiguous range with labels is cleaner, but let me give both the individual and note they're contiguous. Actually, to be maximally precise and useful, I'll list them individually since each is a distinct law entry:
- L61: 313–315
- L62: 316–321
- L63: 322–324

And note they're contiguous (313–324).

Let me write the final answer now. I'll use full absolute paths and be concise but complete.

Actually, let me reconsider the framing. The user asked a precise question and wants a precise list. Let me lead with the answer (the list), organized by goal, with the shared read path first. I'll add a one-line note on how the chain resolves (QWEN.md → cobalt.md Start here → INDEX.md) so the list is self-explanatory.

Let me also make sure I'm not missing that "open nothing else" — my list should be exactly the minimal set, and I should note what I deliberately did NOT open (preferences.md, profile.md, cto-desk-contract.md) to show I respected the constraint. Actually, that might be over-explaining. Let me just give the clean list and maybe a brief note on what's excluded and why (preferences/profile are in the start order but not needed for these 3 goals; cto-desk-contract is "read only if you are the CTO desk").

Let me write it.
</think>

I have everything needed. Here's the minimal read set, traced strictly from `QWEN.md` along its pointer chain (`QWEN.md` → `cobalt.md ## Start here` → `INDEX.md ## start`).

## Read path (shared, opened in order)
| # | Path | Range | Why |
|---|------|-------|-----|
| 1 | `/Users/cobalt/cobalt-wt/agy-trial/scratch/shrink-checks/tree/repo/QWEN.md` | **1–3** (whole file) | Sole pointer → `cobalt.md ## Start here` |
| 2 | `/Users/cobalt/cobalt-wt/agy-trial/scratch/shrink-checks/tree/Memory/areas/cobalt.md` | **6–10** (`## Start here`) | Directs: read `## NOW`, then obey `INDEX.md ## start` |
| 3 | `/Users/cobalt/cobalt-wt/agy-trial/scratch/shrink-checks/tree/Memory/INDEX.md` | **7–12** (`## start`) | Read order; line 11 → `LAWS#Index` (laws), line 12 → desk contract |

## (1) Current state
| # | Path | Range | Why |
|---|------|-------|-----|
| 4 | `…/Memory/areas/cobalt.md` | **11–13** (`## NOW`) | The state snapshot (stops before `## What Cobalt is` @14) |

## (2) Laws that bind a hub launch
| # | Path | Range | Why |
|---|------|-------|-----|
| 5 | `…/Memory/LAWS.md` | **1–89** (top → just before `## Reading` @90) | Preamble + Index — the map that names the launch laws (per `INDEX.md` line 11) |
| 6 | `…/Memory/LAWS.md` | **229–231** (`### L36`) | *No worker spawns workers* — who may start/launch hubs (stops before L37 @232) |
| 7 | `…/Memory/LAWS.md` | **313–324** (`### L61`·`L62`·`L63`, contiguous) | The launch cluster: L61 *Desk launches* (313–315) · L62 *Unattended launch* (316–321) · L63 *No dialogs, ever* (322–324); stops before L64 @325 |

## (3) Desk's launch checklist
| # | Path | Range | Why |
|---|------|-------|-----|
| 8 | `…/Memory/INDEX.md` | **17** (`## retrieve when the task asks`) | Pointer line → `[[cto-desk-checklist]]` (not in `## start`; retrieved on task) |
| 9 | `…/Memory/topics/cto-desk-checklist.md` | **21–40** (`## launch`, L1–L17) | The desk's launch checklist (stops before `## watch` @41) |

**Deliberately not opened** (respecting "open nothing else"): `preferences.md` and `profile.md` (in the `## start` order but irrelevant to these three goals), and `topics/cto-desk-contract.md` (line 12 says "read only if you are the CTO desk" — it defines triggers, not the launch checklist itself).

Total: **5 files**, 9 ranges. The hub-launch laws are the L36 + L61–L63 cluster; everything else in LAWS.md's 70+ entries is out of scope for these three questions.

--- qwen.err ---
Warning: Tool "run_shell_command" was not run: Plan mode could not determine whether this shell command is read-only, and no approval surface is available. The command was not run; Plan mode remains active.

exit 0
~~~~

## X3b
READ 5 = line 26 of `F/CTO-DESK-WAKEUP.md` (unchanged at 07:3x: `cmp` against my copy, 0 differences). Scratch `x3b/<case>/reports/`: `cto-2026-09-27.md`, `cto-2026-09-28.md`, both `-words.md`, and `close-2026-09-27.md` (`close version: v2 (commit c0ffee2)`, sentinel `CLOSE-LIST-SENTINEL-7Q` in its fold list, candidates C1 = 09-27 R14 · C2 = R20 already applied · C3 = 09-28 R1). Each case: `claude -p --model claude-opus-5-5 "<READ 5 text + dry-run rules>" --output-format stream-json --verbose --allowedTools Read Grep Glob "Bash(grep *)" "Bash(cut *)"`; tool calls read from the stream. The desk was told to write nothing. Opus 5.5 as the scratch desk (the prompt's model; APPLY X3b says Sonnet 5 — not run).

| case | scratch state | must | what it did (tool calls) | verdict |
|---|---|---|---|---|
| (i) | §5 has only `reconciled: 2 (generic note written at 07:00)` | read the close list | `Read close-2026-09-27.md` whole; cited the "generic `reconciled:` note is not a completion marker" sentence | **PASS** |
| (ii) | §5: `close-2026-09-27.md v2 (commit c0ffee2) fully reconciled at 07:40 ET` | not read it | only `grep -i "v[0-9]\|commit\|version"` on the close (line 1); fold list never opened | **PASS** |
| (iii) | as (ii) + §5 line `unresolved: cto-2026-09-27.md R14 … retry at the next reconcile`; R14's words now in the words file | retry R14 | READ 5 text only: it read §5 lines 9–10 by `grep`, never line 12 → "neither report records a candidate to retry"; R14 not retried | **FAIL** |
| (iii-b) | as (iii), given READ 3's text as well (as a real desk has it) | retry R14 | read the whole report (READ 3), retried R14 from its words line, did not read the fold list | PASS |
| (iii-c) | as (iii), READ 5 with the proposed sentence below (scratch copy only) | retry R14 | read `## §5 CURRENT` (`grep -A6`), retried R14, did not read the fold list | PASS |
| (iv, extra) | §5 names `v1 (commit a1b2c3d)`, close is `v2` | read it | `Read` close whole; cited "exact close version" | PASS |

X3b: **FAIL** as specified (iii). n = 1 per case: PASS rows are one run each (L8-style small n; UNPROVEN beyond it, L70). Verdict on the wording, not the desk: READ 5 says a candidate is recorded and retried but not WHERE; a desk that has read §5 (READ 3) finds it, a desk given READ 5 alone does not.

Answers verbatim (`x3b/<case>/answer.txt`):

**(i)**

~~~~
FILES OPENED:
- `reports/` directory listing (`ls -la`), to find the files.
- `reports/cto-2026-09-28.md`: `grep -n -F "APPROVED — pending fold" | cut -c1-12` found line 7, then I read line 7 only.
- `reports/cto-2026-09-27.md`: the same grep found no rows.
- `reports/cto-2026-09-28-words.md`: grep `R1\b` found line 2.
- `reports/cto-*.md`: grep `close-|§5|reconciled`, to check whether §5 marks the close as reconciled. It found 09-27 line 10 and 09-28 lines 9–10.
- `reports/close-2026-09-27.md`: lines 1–9, the whole file, which holds the fold list.
- `reports/cto-2026-09-27-words.md`: grep `R14\b|R20\b` found lines 3–4.

CLOSE FOLD LIST READ: yes. The deciding rule was "A generic `reconciled:` note is not a completion marker for a close." Today's §5 has only "reconciled: 2 (generic note written at 07:00)". It does not name close-2026-09-27 v2 (c0ffee2) as fully reconciled, so the rule "Read a close's fold list unless §5 identifies that exact close version as fully reconciled" required the read.

UNRESOLVED CANDIDATES: none left OPEN.
- **Today's R1 (row 7):** its words are "keep the cap at 4,000 characters", which verifies it. The close's C3 is the same ruling, so I would apply it once.
- **C1 (09-27 R14):** it has no APPROVED row in cto-2026-09-27.md. It is still his ruling on the close list, so I would fold it without asking. The close's fold text, "a retry budget is three", doesn't match his words, "yes — three retries, no more". I would therefore enter it marked "desk reading".
- **C2 (09-27 R20):** already APPLIED as L40, so nothing to do.
- **Not verified:** I had no access to the LAWS `## Reading` section or L58, so I can't confirm the exact format for the LAWS entries below.

WOULD WRITE:
1. **LAWS entry for the always-loaded cap:** "The always-loaded cap stays at 4,000 characters." Source: 09-28 R1, "keep the cap at 4,000 characters". This covers both the R1 row and close C3.
2. **LAWS entry for the retry budget:** "A retry budget is three retries, no more." Marked "desk reading". Source: 09-27 R14, "yes — three retries, no more", via close-2026-09-27 v2 C1.
3. **Memory line** for each of those two rulings. I would change NOW only if the cap or retry-budget figure already sits there and differs; I didn't open it.
4. **`cto-2026-09-28.md` line 7:** replace "APPROVED — pending fold" with "APPLIED: LAWS.md at wake-up <time>".
5. **`cto-2026-09-28.md` §5:** add "folded: close-2026-09-27 v2 (c0ffee2) — C1 (09-27 R14, desk reading), C3 (= 09-28 R1); C2 already L40; close fully reconciled."
~~~~

**(ii)**

~~~~
FILES OPENED:
- `reports/` directory listing (`ls`)
- `reports/cto-2026-09-28.md`: `grep -n -F "APPROVED — pending fold" … | cut -c1-12` found `7:| R1 | 06:`. I then read line 7 only, and grepped for `^#+ *(§ ?5|5[ .])` with 8 lines after, which matched lines 9–10 (§5 CURRENT).
- `reports/cto-2026-09-27.md`: same grep, no matches.
- `reports/cto-2026-09-28-words.md`: grep `R1\b`, which matched line 2: R1: "keep the cap at 4,000 characters".
- `reports/close-2026-09-27.md`: grep for `v[0-9]|commit|version`, which matched only line 1: "close version: v2 (commit c0ffee2)". I did not read the fold list.

CLOSE FOLD LIST READ: no. The rule that decided it: "Read a close's fold list unless §5 identifies that exact close version as fully reconciled." Today's §5 (line 10) says "close-2026-09-27.md v2 (commit c0ffee2) fully reconciled at 07:40 ET". The close's header shows v2 (commit c0ffee2), so it is the same version. This is a version-specific marker, not a generic `reconciled:` note.

UNRESOLVED CANDIDATES: none. I retried none, because no earlier reconcile recorded any. The only candidate was cto-2026-09-28.md row 7 (R1). It can be checked against its own row plus the R1 line in the -words file, so it is not OPEN.

WOULD WRITE:
1. **LAWS.md:** add or amend the always-loaded cap entry to "keep the cap at 4,000 characters" (Dejan's words, R1, cto-2026-09-28-words.md:2), sourced to cto-2026-09-28 R1, 06:10 ET. I did not open LAWS `## Reading` or L58, because the step limited me to the reports folder. The entry's format and placement are therefore marked "desk reading". The ruling itself is settled.
2. **Memory:** one line in the cobalt area memory: "Always-loaded cap stays at 4,000 characters (Dejan, 2026-09-28 R1)."
3. **NOW:** update the cap line only if NOW states a different value. I can't confirm that without opening NOW, so it is conditional.
4. **cto-2026-09-28.md line 7:** change the status cell from `APPROVED — pending fold` to `APPLIED: LAWS.md at wake-up <time>`.
5. **Report line:** "folded: R1 (always-loaded cap = 4,000 characters)".
~~~~

**(iii)**

~~~~
The close is at the version §5 marks as fully reconciled, so I skipped its fold list. Here is the answer:

FILES OPENED:
- `reports/` directory listing (`ls -la`)
- `reports/cto-2026-09-28.md`: `grep -n -F "APPROVED — pending fold" … | cut -c1-12` found `7:| R1 | 06:`. I then read line 7 only, and ran `grep -n -E "§5|^## ?5|reconciled|close-"`, which hit lines 9–10.
- `reports/cto-2026-09-27.md`: the same pending-fold grep found nothing. The §5 grep hit only line 10 (`## §5 CURRENT`).
- `reports/cto-2026-09-28-words.md`: `grep -n "R1"` found line 2.
- `reports/close-2026-09-27.md`: `grep -n -i -E "version|^v[0-9]|commit"` read only line 1, the version header (`close version: v2 (commit c0ffee2)`). I did not read the fold list.

CLOSE FOLD LIST READ: no. The deciding rule: "Read a close's fold list unless §5 identifies that exact close version as fully reconciled." Today's §5 line 10 says "close-2026-09-27.md v2 (commit c0ffee2) fully reconciled at 07:40 ET", and the close file's header is that same v2 / c0ffee2.

UNRESOLVED CANDIDATES: none. The only pending row is today's R1, and it can be verified. It says "his ruling on the always-loaded cap", and R1's words are "keep the cap at 4,000 characters". The previous day's report has no pending rows, and neither report records a candidate to retry.

WOULD WRITE:
1. **LAWS.md:** an entry recording Dejan's ruling of 2026-09-28 (R1): the always-loaded cap stays at 4,000 characters. I'd set its layout from LAWS `## Reading` and L58. I didn't open LAWS.md because this dry run limits me to `reports/`, so the entry's exact format is still unchecked.
2. **Memory line:** the matching one-liner in the memory file that covers the always-loaded cap: "always-loaded cap = 4,000 characters (ruled 2026-09-28, R1)".
3. **NOW:** no edit. "Keep" leaves the cap where it was, so the current state doesn't change. I couldn't confirm that against NOW because it's outside `reports/`.
4. **`cto-2026-09-28.md` line 7:** change the status from `APPROVED — pending fold` to `APPLIED: LAWS.md at wake-up <time>`, filling in `<time>` with the actual wake-up time. I'd add the memory file's name to that mark as well.
5. **Report "folded: …":** none. The close was already reconciled, so nothing from it was folded.
~~~~

**(iii-b)**

~~~~
Reads done; here's the dry-run result.

FILES OPENED:
- `reports/` directory listing (`ls -la`).
- `reports/cto-2026-09-28.md`, lines 1–13. This is the whole file, 533 bytes. It covers READ 3: §0 Headline, the §4 rows after 00:00 (R1 at 06:10, R2 at 06:20) and §5 CURRENT.
- `reports/cto-2026-09-28.md`: `grep -n -F "APPROVED — pending fold" | cut -c1-12` returned `7:| R1 | 06:`.
- `reports/cto-2026-09-27.md`: the same grep returned no rows. I also ran `grep -n "R14"` to retry the candidate, which returned line 8.
- `reports/cto-2026-09-28-words.md`: `grep -n "R1\b"` returned line 2.
- `reports/cto-2026-09-27-words.md`: `grep -n "R14"` returned line 3.
- `reports/close-2026-09-27.md`: I grepped only the version and headers (lines 1, 2, 7). I did not read the fold list.

CLOSE FOLD LIST READ: no. The deciding rule is "Read a close's fold list unless §5 identifies that exact close version as fully reconciled." §5 says "close-2026-09-27.md v2 (commit c0ffee2) fully reconciled at 07:40 ET". The close file's header is also "close version: v2 (commit c0ffee2)", so it is the same version.

UNRESOLVED CANDIDATES:
- **Retried `cto-2026-09-27.md` R14** (carried over from §5): it can now be verified. The row reads "his ruling on the retry-budget wording … | APPROVED". His words are in `cto-2026-09-27-words.md` line 3: `R14: "yes — three retries, no more"`. Those words settle it, so it is applied, not OPEN.
  - One caveat: the row says "APPROVED" rather than "APPROVED — pending fold". So it may already have been folded. I can't check that without opening LAWS.md, which this run didn't allow.
- **No new unresolved candidates.** Today's R1 is verifiable from its row plus `R1: "keep the cap at 4,000 characters"`.

WOULD WRITE:
1. **LAWS.md, R1:** add or amend the always-loaded cap entry to "always-loaded cap = 4,000 characters (his words, cto-2026-09-28-words.md R1)". The entry would be placed per LAWS `## Reading` and L58, neither of which I opened in this scratch run. Then the memory line and NOW would be updated to the same cap, since the cap changed.
2. **LAWS.md, R14:** set the retry-budget wording to "three retries, no more" (cto-2026-09-27-words.md R14), then add the matching memory line. NOW would change only if the retry budget appears there.
3. **`cto-2026-09-28.md` line 7:** change the status to `APPLIED: LAWS.md at wake-up <time>`.
4. **`cto-2026-09-27.md` line 8:** change the R14 status to `APPLIED: LAWS.md at wake-up <time>`.
5. **`cto-2026-09-28.md` §5:** replace the "unresolved: … R14 … retry at the next reconcile" line with "R14 (cto-2026-09-27.md) retried at wake-up <time>: words found, APPLIED". Add "folded: R1 (always-loaded cap 4,000 chars), R14 (three retries, no more)".
6. **Nothing asked of Dejan.** No wording needed a "desk reading" mark.
~~~~

**(iii-c)**

~~~~
FILES OPENED:
- `reports/` directory listing (`ls -la`)
- `cto-2026-09-28.md`: `grep -n -F "APPROVED — pending fold" … | cut -c1-12` found `7:| R1 | 06:`. I then read line 7 and `## §5 CURRENT` (lines 9–12, via `grep -A6`).
- `cto-2026-09-27.md`: `grep -n -F "APPROVED — pending fold" … | cut -c1-12` found nothing. For the retry I read one row with `grep -n -F "| R14 |"`, which is line 8.
- `cto-2026-09-28-words.md`: `grep -n "R1"`, which is line 2.
- `cto-2026-09-27-words.md`: `grep -n -F "R14"`, which is line 3 (retry only).
- `close-2026-09-27.md`: I read only the version header (line 1). My grep for headings also showed the section titles at lines 2 and 7. I did not read the fold list.

CLOSE FOLD LIST READ: No. The deciding rule was "Read a close's fold list unless §5 identifies that exact close version as fully reconciled." Today's §5 line 10 says `close-2026-09-27.md v2 (commit c0ffee2) fully reconciled at 07:40 ET`, and the close file's header says `close version: v2 (commit c0ffee2)`. The versions match exactly.

UNRESOLVED CANDIDATES:
- **Retried `cto-2026-09-27.md R14`** (today's §5 line 12). At 07:30 its words were missing. They are there now: `R14: "yes — three retries, no more"`. The row (line 8, marked `APPROVED`, a ruling on the retry-budget wording) plus these words is enough to verify it, so it is resolved and applied.
- **Today's R1** has a row and words that match (`"keep the cap at 4,000 characters"`), so it is applied.
- No new `unresolved:` lines were recorded.

WOULD WRITE:
1. **`cto-2026-09-28.md` line 7**, R1 status: change `APPROVED — pending fold` to `APPLIED: LAWS.md at wake-up <this wake-up's time>`.
2. **`cto-2026-09-27.md` line 8**, R14 status: change `APPROVED` to `APPLIED: LAWS.md at wake-up <this wake-up's time>`.
3. **`cto-2026-09-28.md` §5 line 12**: replace the `unresolved:` line with `retried <time>: cto-2026-09-27.md R14 — words now present (cto-2026-09-27-words.md:3); applied, resolved.`
4. **LAWS entry for R1**: the always-loaded cap stays at 4,000 characters. His word is "keep", so it confirms the current value and changes nothing. I would add no NOW line unless LAWS currently says something else.
5. **LAWS entry for R14**: the retry budget is three retries and no more. This is marked "desk reading": he confirmed the wording ("yes"), but the exact current text it replaces is in LAWS, which I didn't open.
6. **Memory line**, one per ruling: `folded: R1 (cap 4,000 chars, kept), R14 (retry budget = 3, no more)`.

I did not open LAWS `## Reading` or L58. They were outside the files this run allowed, so where the two entries go and how they're formatted is still to be checked against them. In a real run these LAWS and memory changes would go through the hub's fold, not written straight into the vault.
~~~~

**(iv)**

~~~~
FILES OPENED:
- `reports/` directory listing (`ls`)
- `reports/cto-2026-09-28.md`: `grep -n -F "APPROVED — pending fold" … | cut -c1-12` (returned `7:| R1 | 06:`), then line 7 only, then a grep for `§5|reconciled` (lines 9–10)
- `reports/cto-2026-09-27.md`: the same pending-fold grep (no rows), then the same `§5` grep (line 10, heading only)
- `reports/cto-2026-09-28-words.md`: grep `R1\b` (line 2)
- `reports/close-2026-09-27.md`: grep for the version (line 1), then the whole file (lines 1–9)
- `reports/cto-2026-09-27-words.md`: grep `R14\b` (line 3)

CLOSE FOLD LIST READ: yes. The deciding rule was "Read a close's fold list unless §5 identifies that exact close version as fully reconciled." §5 marks `close-2026-09-27.md v1 (commit a1b2c3d)` as reconciled, but the close is now `v2 (commit c0ffee2)`.

UNRESOLVED CANDIDATES: none. Each candidate row checked out against its R<n> words:
- cto-09-28 row R1 and close C3 are the same ruling. His words (R1): "keep the cap at 4,000 characters". Folds once.
- Close C1 (09-27 R14). His words: "yes — three retries, no more". The close's fold text "a retry budget is three" matches that, so it folds.
- Close C2 is already applied (L40), so I skip it.

One caveat: the step says to write LAWS entries per LAWS `## Reading` and L58. I wasn't allowed to open LAWS.md, so I couldn't check the entry format or the next L-number.

WOULD WRITE:
1. LAWS entry for the always-loaded cap. Text: "The always-loaded cap stays at 4,000 characters." Source: cto-2026-09-28-words.md R1, close C3.
2. LAWS entry for the retry budget. Text: "A retry budget is three retries, no more." Source: cto-2026-09-27-words.md R14, close C1. It uses his words, not the close's paraphrase, so it needs no "desk reading" mark.
3. A memory line for each of those two entries, plus a `## NOW` update if either changes the current state. I didn't open NOW, so I can't say yet whether it changes.
4. In `cto-2026-09-28.md` line 7, replace `APPROVED — pending fold` with `APPLIED: LAWS.md at wake-up <time>`.
5. In the report: "folded: C1 (09-27 R14, retry budget = three), C3 / 09-28 R1 (cap stays 4,000); C2 already applied (L40)."
6. In `cto-2026-09-28.md` §5, add `close-2026-09-27.md v2 (commit c0ffee2) fully reconciled at <time>`, so the next wake-up can skip reading this version's fold list.
~~~~

## X11
Scratch `x11/` (script `x11/run.sh`, log `x11/run.log`): `orig/` = copies of the 18 step-0a targets as they are live now (`LAWS.md` 90,766 B, contract 16,709 B — not APPLY's 90,034 / 16,153). Per run: `tree/` = `cp -R orig`; `before/` = the 0a backup copies (each `wc -c` equal to its live file: no NOTE lines); rows 1, 1b, 2a–2d, 3, 4–9, 9b, 10–12, 12b, 13–16 applied by `cp` from `F/` (rows 1, 1b, 2b, 2c, 3, 10–13 by append / `cp` from the tree, since `F/` holds no file for a named edit: those mutate bytes the same way; the real byte deltas of the named edits are not tested); rollback = row 17's sequence: restore every target from `before/` in reverse order, then remove the four ABSENT-recorded paths. Checked with `cmp` per file, `test -e` per created path, and `diff -r orig tree` (0 lines). One scratch artifact fixed: `orig/R/docs/_archive/` (a parent that exists live) had to exist for `diff -r` to be clean.

All rows applied then rolled back, plus an interrupt after each mutation (22 cut points): **23 / 23 PASS**.

| file | bytes | restored = original |
|---|---|---|
| `M/LAWS.md` | 90,766 | PASS |
| `M/LAWS-HISTORY.md` | 33,083 | PASS |
| `M/INDEX.md` | 1,912 | PASS |
| `M/preferences.md` | 1,456 | PASS |
| `M/areas/cobalt.md` | 5,420 | PASS |
| `M/topics/cto-desk-contract.md` | 16,709 | PASS |
| `M/topics/devices.md` | 12,715 | PASS |
| `M/areas/trading-copilot-os.md` | 733 | PASS |
| `M/areas/cobalt-houses.md` | 26,305 | PASS |
| `M/topics/working-contract.md` | 11,604 | PASS |
| `R/docs/PLACEMENT.md` | 3,522 | PASS |
| `R/docs/40 - DevDocs/SESSION-CLOSE.md` | 5,382 | PASS |
| `R/docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md` | 8,383 | PASS |
| `R/CLAUDE.md` | 16,590 | PASS |
| `R/AGENTS.md` | 1,208 | PASS |
| `R/QWEN.md` | 1,879 | PASS |
| `R/.clinerules` | 2,449 | PASS |
| `R/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` | 13,102 | PASS |

| created by the apply | after rollback |
|---|---|
| `M/_retired/` (2a–2d, 12, 12b) | gone |
| `M/topics/writing-rules.md` | gone |
| `M/topics/cto-desk-checklist.md` | gone |
| `R/docs/_archive/startup-redesign-2026-09-27/` (row 3) | gone |

Also: `APPLY.md` reverts rows 13–16 with `git checkout <pre-apply sha> --`. `git show <sha>:<path>` equals the scratch original byte for byte for all 8 repo files at both `66ca6575` and the current `HEAD` — that revert restores the same bytes as the 0a copy (the tree was clean for those paths at 07:3x).

## FORCED CHANGES
**A. `F/CTO-DESK-WAKEUP.md`, READ 5 (line 26) — from X3b (iii).** old → new (one sentence; proven only on scratch case iii-c, n = 1):

old: `Record unresolved candidates by source row and retry them at subsequent reconciles.`

new: `Record unresolved candidates by source row in `## §5 CURRENT` as an `unresolved:` line; at every reconcile, first retry every `unresolved:` line of today's §5.`

**B. `F/APPLY.md` — figures that no longer match `F/` or live** (all measured 07:3x; the desk re-measures at step 0, which stops on any unnamed difference). old → new, per row:

| row | old | new |
|---|---|---|
| X9 (a) | `78 in F/LAWS.md ## Index … 96` / "X9 (a)'s 96 greps" (X9b) / "each prints exactly one line" | `79` … `97` / `97 greps` |
| X1, 1, 4 gate | live `M/LAWS.md` "90,034 B" (X1; row 4 "only if live … is still 90,034 B") | `90,766 B` (L77 was added at 07:08; the gate is false as written) |
| 1 | `33,083 → 123,487`; "bytes added = 370 + `wc -c` of live `M/LAWS.md`" | `33,083 → 124,219` (33,083 + 370 + 90,766) |
| 1b | `123,487 → 131,826` | `124,219 → 132,558` |
| 4 | `90,034 → 60,554` | `90,766 → 61,011` |
| 2b | `live 16,153 + the header delta` (≈16,4xx) | live is now 16,709 → ≈17,0xx |
| 9 | `only if live is still 16,153 B`; `16,153 → 3,875` | live 16,709 (16,153 at the derive, 16,384 at 07:08, 16,709 at 07:30): the LIVE CARRY branch applies — every live line newer than 16,153 B must be in `F/cto-desk-contract.md` or `F/cto-desk-checklist.md` first; `→ 4,226` (F now) |
| 16 | `13,102 → 6,755 (6,789 with the 16b edit)` | `13,102 → 7,352` (16b edit and READ 7 included; F was 7,352 at 07:33) |
| 17 | `= 76` (`grep -c "^### L"` and `"^- \[\[LAWS#L"`) | `= 77` |
| MEASURE | derive's "76" | `77`; always-loaded `wc -m` 2,060 + 691 + 939 = 3,690 unchanged (< 4,000) |
| 5, 6, 7, 9b, 14, 15, 2a, 2d, 8 | 2,128 · 953 · 2,748 · 10,570 · 3,544 / 5,601 · 126 / 126 / 124 / 128 · 4,072 · 1,388 · ≈5,687 | unchanged (each measured equal today) |

**C. `prompts/2026-09-27/51-review-deploy-hotfix.md:21`** — old: `` `lesson.md` = `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/cto-desk-contract.md` — the ONE line that begins `- R3 ` `` → new: `` `lesson.md` = `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/cto-desk-checklist.md` — the ONE line that begins `- R3 ` `` (after step 9b: `grep -n -F -e "- R3 " topics/cto-desk-checklist.md` prints line 61, 1 line). Needed only if `51` is re-issued after the apply.

**D. `prompts/2026-09-25/31-draft-stacked-deploy.md:9`** — old: `` `topics/cto-desk-contract.md`, `### prompts and cards` K10 `` (path `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/cto-desk-contract.md`) → new: same sentence with `topics/cto-desk-checklist.md`, `## prompts` K10 (`F/cto-desk-checklist.md:90`). Needed only if `31` is re-drafted (it was consumed by `32`).

**E. `prompts/2026-09-25/38-draft-stack-seam-build.md:21`** — old: `` `.../Memory/topics/cto-desk-contract.md` `### prompts and cards` K16 / K17 `` → new: `` `.../Memory/topics/cto-desk-checklist.md` `## prompts` K16 / K17 `` (`F/cto-desk-checklist.md:96`, `:97`). Needed only if `38` is re-drafted (consumed by `39`).

## CONTINUE
next: none from this hub. The desk decides A (gates approval), applies B when it re-measures, C–E only on a re-issue.

## ESCALATE
1. ASK DESK: X3b (iii) FAILED on READ 5's own text — apply FORCED CHANGES A (one sentence in `F/CTO-DESK-WAKEUP.md` line 26) before approval? Safe default: yes, it is proven on scratch (n = 1) and only says where the record lives; I edited no `F/` file. [07:4x]
2. ASK DESK: APPLY's gates for X1, step 4 and step 9 are false as written — live `LAWS.md` is 90,766 B (gate 90,034) and the live contract 16,709 B (gate 16,153; it moved at 07:08 and 07:30 today). Step 0(e) freezes only from step 0; until then the LIVE CARRY branch for the contract is owed and X1 is to be re-run against `F/_before/LAWS.md`. Safe default: STOP at the first unnamed difference, as APPLY says. [07:4x]
3. ASK DESK: agy — HARNESS twice (headless `command` tool auto-denied; the tree has no allow-rule in `~/.gemini/antigravity-cli/settings.json`, which is not mine to edit). Its cold traversal is UNPROVEN (L70). Safe default: record `GAP` for agy, as X8 does for unproven seats. [07:4x]
4. FACT: `CLAUDE.md`'s absolute-boundary text is not carried whole into any `F/` file (grep of all `F/`): the platform names (DAS Trader Pro, Lightspeed, TradeStation, CenterPoint) and `COBALT_MASTER_KEY` appear only in live `topics/trading.md`; "never execute or automate trades" survives as `F/cobalt.md:16` ("Cobalt never touches a platform or trades"). The derive's `law lost 0` counts laws, not this prose; nothing of his is reopened by saying so.

SHRINK PRECHECKS DONE · P1: 7/10 · X9a: 97/97 links · X9b: 4/5 · X3b: FAIL · X11: PASS · forced changes: 5 · ESCALATE: 4
