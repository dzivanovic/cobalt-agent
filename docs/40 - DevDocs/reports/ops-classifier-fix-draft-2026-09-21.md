# ops-classifier-fix-draft — 2026-09-21

Seat `ops-classifier-fix-draft-0921` (Opus 5, drafting), 19:15–19:26 ET. Prompt: `prompts/2026-09-21/76-draft-ops-classifier-fix.md`.

## §0 Headline
- Drafted `77-ops-classifier-fix.md` (Sonnet 5 builder, offline, worktree `ops-0921`) and `78-ops-6a-check-r2.md` (Sonnet 5 hub, four checkers, reads the fix only). Nothing launched, nothing committed.
- **The rule is a `no_resident_reads` row in `configs/cobalt/jobs.yaml`, not an `if` in `restarts.py`.** This departs from the order's file list (ESCALATE 1, ASK DESK). A `restarts.py` edit would add a second path (L3), `cobalt jobs readers` would not see it, and it would derive a radar restart itself.
- **Two readers, not one.** The one-shot `com.cobalt.heartbeat` reads `backup.yaml` too (`heartbeat/probes.py:431`). This corrects the builder's claim. No resident reads the file.
- RULE PROOF: `77` vs `02` = 1/1 on all 19 strings and the triplet. `78` vs `69` = identical counts (4 strings count 2 in BOTH files, from prose). NEW approvals: none. ESCALATE: 3.

## L29 seat finding
**Sonnet 5 is eligible.** The fix touches no vault or DB write path, migration, delete, recovery or forensics.
- `src/cobalt/jobs/restarts.py` is a read-only classifier. Its only side effects:
  - `git` reads through `_git` (`restarts.py:58-64`: `diff --name-status`, `ls-files`)
  - AST parses (`:124` `read_text`)
  - `print` in `command` (`:261-272`)
- `grep -rn "open(\|write_text\|\.write(\|unlink\|mkdir"` on the file returns no hit.
- The new `no_resident_reads` row is read only at `restarts.py:205` and `jobs/cli.py:101` (the `cobalt jobs readers` print). `cobalt jobs register` saves only the `jobs:` rows (`jobs/cli.py:64-73`), never this table.
- `77` does not modify `restarts.py` at all. CLOSE requires `git diff f6aa4d0 -- src` to be empty.

## Readers of `configs/cobalt/backup.yaml` (file:line, on the branch `f6aa4d0`)
| caller | function | reached from | job | kind |
|---|---|---|---|---|
| `backup/config.py:19` / `:161` | `CONFIG_PATH` / `load_backup_config` (the one path, the one loader) | — | — | — |
| `backup/restic.py:164` | `snapshot` | `backup/cli.py:45` `_run` = `cobalt backup run` ← `ops/run_backup.sh:39` ← `ops/com.cobalt.backup.plist:63` | `com.cobalt.backup` | one-shot (`jobs.yaml:230-243`) |
| `backup/restic.py:248` | `latest_snapshot_age` | `backup/cli.py:70` (status); `heartbeat/probes.py:445` | (via the rows below/above) | — |
| `backup/restic.py:269` | `restore` | `backup/cli.py:75` `_restore` | operator command | no job |
| `backup/cli.py:59` | `_status` | `cobalt backup status` | operator command | no job |
| `heartbeat/probes.py:431` | `backup_freshness` | `heartbeat/runner.py:144` (`take_beat`) ← `cobalt heartbeat beat` ← `ops/com.cobalt.heartbeat.plist:30-43` | `com.cobalt.heartbeat` | one-shot (`jobs.yaml:245-256`) |

- **No resident reads it.**
  - No resident's `reads:` names the file (`jobs.yaml:67-69, 80, 95, 127, 158, 167-169`).
  - `grep -rln "dayopen\|cobalt.smoke"` over `src/cobalt/radar` and `src/cobalt/aset` finds nothing.
  - `radar/notes.py:160,313` reads the job *registry* for the label `com.cobalt.backup`, not `backup.yaml`.
  - `smoke/checks.py` and `dayopen/checks.py` do not call `backup_freshness`, `take_beat` or `run_beat`.
- **Readers: 2 jobs**, both one-shots (`com.cobalt.backup`, `com.cobalt.heartbeat`), plus two operator commands.
- **Correction:** the builder's ESCALATE 1 (`ops-2026-09-21.md:178`) says "only the one-shot `com.cobalt.backup` reads it". The round-1 check carried that claim unchallenged, but the heartbeat reads the file too. Both readers are one-shots, so the derived restart is the same (none).

## Why the rule is a registry row (drafter's finding)
- The `no_resident_reads:` table already exists for this purpose:
  - Location: `jobs.yaml:292-316`, ruled 2026-09-15.
  - Read at: `restarts.py:205-208`, which gives the rule `no resident reads (one-shot: …)` with no restart and no escalation.
  - Schema: `jobs/config.py:358-409` refuses a resident as a reader and refuses a path that any resident lists in `reads:`, so a wrong declaration fails loudly.
  - Today's rows: `notify.yaml` and `rules.yaml`. The DevDoc documents it at `restarts.md:7`.
- A hard-coded `if` in `restarts.py` would be worse in three ways:
  - **It adds a second path for the same job (L3).**
  - **`cobalt jobs readers` would not see it.** It would still answer `UNKNOWN PATH` with exit 1 (`jobs/cli.py:98-114`).
  - **It would derive a radar restart by itself.** It is a `src/` change, and radar reaches `restarts.py` by static import: `jobs.yaml:170` `imports: [cobalt.cli]` → `cli.py:69` → `jobs/cli.py:29` `from . import restarts`. That restart is bound to the pause window (L43), which contradicts the order's "name the one-shot only".
- A `jobs.yaml` edit derives nothing itself: `restarts.py:217-218` classifies it `registry; register, no restart`.
- Expected at 77's CLOSE: `jobs restarts main..HEAD` exits 0 with `RESTARTS: none`. This is expected, not proven; the builder runs it. At drafting, main has no runtime-path commits since the branch point: `git -C /Users/cobalt/cobalt log --oneline ops/2026-09-21..main -- src configs ops tests .gitignore` returned nothing.

## RULE PROOF (`grep -c -F -e "<rule>" <new> <original>`, one call per string)
| string | `77` | `02` | | string | `78` | `69` |
|---|---|---|---|---|---|---|
| `"Bash(uv run pytest *)"` | 1 | 1 | | `"Bash(grok *)"` | 1 | 1 |
| `"Bash(uv run cobalt jobs restarts *)"` | 1 | 1 | | `"Bash(agy *)"` | 1 | 1 |
| `"Bash(git add *)"` | 1 | 1 | | `"Bash(mkdir -p scratch/tribunal-bars-0920)"` | 1 | 1 |
| `"Bash(git commit *)"` | 1 | 1 | | `"Bash(git -C /Users/cobalt/cobalt show*)"` | 1 | 1 |
| `"Bash(git diff *)"` | 1 | 1 | | `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 | 1 |
| `"Bash(git status*)"` | 1 | 1 | | `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards show*)"` | 1 | 1 |
| `"Bash(git log*)"` | 1 | 1 | | `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards log*)"` | 1 | 1 |
| `"Bash(git show*)"` | 1 | 1 | | `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards diff*)"` | 1 | 1 |
| `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 | 1 | | `"Bash(ls *)"` | 1 | 1 |
| `"Bash(cd *)"` | 1 | 1 | | `"Bash(grep *)"` | 1 | 1 |
| `"Bash(mkdir -p *)"` | 1 | 1 | | `"Bash(tail *)"` | 1 | 1 |
| `"Bash(ls *)"` | 1 | 1 | | `"Bash(wc *)"` | 1 | 1 |
| `"Bash(grep *)"` | 1 | 1 | | `"Bash(date*)"` | 1 | 1 |
| `"Bash(tail *)"` | 1 | 1 | | `"Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)"` | **2** | **2** |
| `"Bash(wc *)"` | 1 | 1 | | `"Bash(claude -p --model claude-opus-5 *)"` | **2** | **2** |
| `"Bash(date*)"` | 1 | 1 | | deny `"AskUserQuestion"` | **2** | **2** |
| deny `"AskUserQuestion"` | 1 | 1 | | deny `"EnterWorktree"` | **2** | **2** |
| deny `"EnterWorktree"` | 1 | 1 | | deny `"Bash(git push*)"` | 1 | 1 |
| deny `"Bash(git push*)"` | 1 | 1 | | `--add-dir` triplet | 1 | 1 |
| `--add-dir` triplet | 1 | 1 | | | | |

- The four **2**s count in `78` exactly as they do in `69`.
  - The second line for the Sol and Opus strings is the AUTHORIZATION paragraph, which quotes R49's strings for the grep gate.
  - The second line for `AskUserQuestion` and `EnterWorktree` is the Opus-checker launch spelling in §2 (its own `--disallowedTools`).
  - Each string appears once in the hub's launch line in both files. The "each 1" target holds for the launch line, not for the file-level line count; this is recorded, not smoothed.
- `gpt-6-astra`: `77` = 0. `78` = 1, which is the AUTHORIZATION refusal sentence copied from `69`, not the launch line.
- `77`'s launch line differs from `02`'s only in the prompt path, the remote-control name and `--model claude-sonnet-5`. `78`'s differs from `69`'s only in the prompt path and the remote-control name.

**NEW approvals:** none. Both prompts reuse approved lines: 09-20 R25 for `77`; 09-20 R13 + 09-21 R49 for `78`, with `grok`/`agy` under 09-21 R39 through 2026-09-22. The desk still fills in each prompt's launch row `R__`.

READING: `LAWS.md` in full · `reports/ops-6a-check-2026-09-22.md` whole · branch report `ops-2026-09-21.md` (ESCALATE 1, §6) · `restarts.py` whole · `jobs/config.py:265-455` · `configs/cobalt/jobs.yaml` whole · `tests/cobalt/test_jobs_restarts.py` whole · `test_jobs_reads.py:1-190` · `jobs/cli.py` (greps) · reader greps over `src/`, `ops/` · `restarts.md` (grep) · prompts `02`, `69` whole · `06`, `73` (greps) · `cto-2026-09-21.md` rows R43, R53.

## ESCALATE
1. **The rule's file departs from the order.** The order says the rule goes in `restarts.py` and the diff-stat is `restarts.py` + test + DevDoc + report. `77` puts the rule in `configs/cobalt/jobs.yaml` `no_resident_reads:` instead, leaves `restarts.py` untouched, and keeps the same count of files. Reasons: L3, L10, the ruled 2026-09-15 mechanism, and the radar restart described above.
   `ASK DESK: carry 77 as drafted (registry row, restarts.py untouched), or re-issue with a restarts.py rule, accepting a derived com.cobalt.radar restart for the fix itself and a cobalt jobs readers that still says UNKNOWN for backup.yaml? [2026-09-21 19:26 ET]`
   Safe default taken: the registry row. It has no `src/` change, derives no restart and follows the existing mechanism. The desk may re-issue.
2. **The builder's reader claim was wrong, and round 1 did not catch it.** The heartbeat also reads `backup.yaml` (`heartbeat/probes.py:431`). `77` names both readers and requires a code-derived test. `78` asks the checkers for any other reader.
3. **Other classifier gaps I saw, listed only (not fixed, not in `77`'s scope):**
   - `configs/cobalt/watchlists.yaml` is a hard-coded `if` (`restarts.py:243-244`) that predates the `no_resident_reads` table. Moving it to the table would be a separate L3 cleanup.
   - `ops/start_aset.sh` escalates `UNCLASSIFIED` by design (`test_jobs_restarts.py:105-113`).
- Also: `77`'s report is a **new file**, `ops-classifier-fix-2026-09-22.md`, not an append. `06-ops-0921.md` LAUNCH 2 relies on the last line of `ops-2026-09-21.md` being `OPS 0921 DONE` (`grep -c` = 2 in `06`).
- Not mine, carried by id: round-1 ESCALATE 2 (the `cli.md` seam), 3 (the circular restore → 6b), 4 (restic `forget` grouping).

## CONTINUE
step: closed. `77` and `78` are written; rule proof done. The desk's next steps: read both prompts, rule on ASK DESK (ESCALATE 1), fill in the `R__` rows, commit, launch `77`. `78` follows `77`'s `OPS CLASSIFIER FIX BUILT` line and must run by 2026-09-22 23:59 ET (the R39 limit).

## DIGEST FOR THE DESK
- `77`: Sonnet 5 (L29 finding: read-only classifier; the row is read only by the classifier and the readers print). Offline, in `ops-0921` on branch `ops/2026-09-21`, starting from `f6aa4d0`. Z1 is the test first, then the `jobs.yaml` row. Z2 is the DevDoc `restarts.md:7`.
- **Deviation (ASK DESK):** the rule goes in `jobs.yaml` `no_resident_reads`, not in `restarts.py`. `restarts.py` stays untouched, and CLOSE requires `git diff f6aa4d0 -- src` to be empty.
- Why: a `restarts.py` rule is a second path (L3), `jobs readers` would still say UNKNOWN, and as a `src/` change it would itself derive `com.cobalt.radar` (radar imports `cobalt.cli` → `jobs.cli` → `restarts`).
- **Readers: 2 one-shots.** `com.cobalt.backup` (`restic.py:164` via `run_backup.sh:39`) and `com.cobalt.heartbeat` (`probes.py:431` via `runner.py:144`). No resident. The builder named only backup.
- Expected at 77's CLOSE: `jobs restarts main..HEAD` exits 0, backup.yaml row = `no resident reads (one-shot: com.cobalt.backup,com.cobalt.heartbeat)`, `RESTARTS: none`. Suite 2209 → 2210.
- The Z1 test has two halves. One runs the real `classify` on `Change("configs/cobalt/backup.yaml","M")` against the real registry. The other checks the real `src/` tree for callers of the loader and the one path literal, so a new reader turns the test red.
- `78`: four checkers (Grok · Gemini · Sol · Opus 5), five questions. `ready` = yes only if ≥3 houses checked, 0 defects hold, no FIX AGAIN, and both round-1 NO lines are closed in their own authors' words. The staggers cover `68`, `61` and `73`. The date gate ends 2026-09-22 (R39).
- Rule strings: none new. `77` and `02` match 1/1 on all strings; `78` and `69` match string for string (4 strings count 2 in both, from prose).
- The desk fills the `R__` rows in both prompts before launch.

OPS CLASSIFIER FIX PROMPTS DRAFTED · prompts: 2 · builder seat: Sonnet 5 · readers of backup.yaml: 2 · new rule strings: 0 · ESCALATE: 3
