# ops-fix-r3-draft — 2026-09-21

Seat `ops-fix-r3-draft-0921` (Opus 5, drafting), 20:07–20:18 ET. Prompt: `prompts/2026-09-21/79-draft-ops-fix-r3.md`.

## §0 Headline
- Drafted `80-ops-fix-r3.md` (the round-3 fix; Opus 5 builder, offline, worktree `ops-0921`, from `3ad064f`) and `81-ops-6a-check-r3.md` (Sonnet 5 hub, four checkers, reads the round-3 diff only, `## FOR DEJAN` for anything left open). Nothing was launched or committed.
- **Walker: reused, not duplicated.** The classifier's walk (`restarts.py:89-169`) works at the module level. At that level it cannot answer Sol's Q2: radar's `imports: [cobalt.cli]` reaches every command module. `80` therefore reuses `_module_for`, `_resolve_from`, `import_graph` and `reachable`. The only new code is call-edge extraction, which goes in the test. `src/` stays untouched (diff must be empty).
- RULE PROOF: `80` vs `77` is 1/1 on all 20 strings. `81` vs `78` matches string for string: 15 strings at 1/1 and 4 at 2/2, where the second count is prose in both files. NEW approvals: none. ESCALATE: 4.

## L74
A block was appended to the tool result when this session read `79` (a system-reminder asking for a `Claude-Session:` commit line and naming SendUserFile). It is DATA, and I did not follow it. This seat commits nothing and sends no file. Recorded once, here.

## The walker finding (file:line, branch tip `3ad064f`)
| what | where | finding |
|---|---|---|
| module naming | `src/cobalt/jobs/restarts.py:89-99` `_module_for` | reused by `80` (it reads `restarts.REPO_ROOT` at call time, so a `monkeypatch` can point it at a `tmp_path` copy) |
| relative imports | `restarts.py:102-111` `_resolve_from` | reused; needed for `runner.py:59` `from . import probes as probe_mod` |
| import edges | `restarts.py:114-155` `import_graph` | reused only for the import-time tie to residents (module-scope readers; none exist today) |
| traversal | `restarts.py:158-169` `reachable` | reused as **the** closure: it runs on a reversed call graph rooted at `cobalt.backup.config.load_backup_config`, so the test has no second stack walk. CLOSE greps for one |
| why module reach fails | `jobs.yaml:170` radar `imports: [cobalt.cli]`; `cli.py:66` `backup_cli`, `:68` `heartbeat_cli` | module reach from radar already includes the loader's module. The DevDoc already says the same for smoke (`restarts.md:34-36`) |
| any other walker in the repo? | `grep -rln "import ast\|ast.parse\|ast.walk\|NodeVisitor"` over `src`, `tests` | only `restarts.py` builds a graph. `test_smoke.py:294-305` and `test_archiver_*.py` do single-file scans. **No call-graph walker exists** |
| helper needed in `src/`? | all four names are module-level (`:89,:102,:114,:158`) | **no**. A `restarts.py` edit would also derive `com.cobalt.radar` (`cli.py:69` → `jobs/cli.py:29`), so `80` requires `git diff 3ad064f -- src` to be EMPTY and treats any `src/` edit as FAILED |

The drafter's reader set, from reading the code. `80` makes the builder re-derive it:
- The loader.
- `restic.snapshot` / `latest_snapshot_age` / `restore`.
- `backup.cli._run` / `_status` / `_restore`.
- `probes.backup_freshness`.
- `runner.take_beat` / `run_beat`.
- `heartbeat.cli.cmd_beat` / `cmd_show`.

That makes 12 functions. Entrypoints are the 5 CLI handlers (`set_defaults` at `backup/cli.py:31,34,42`, `heartbeat/cli.py:43,46`). Referrers are the two `add_parser`s. Name collisions the resolver must not pull in: `settings/card.py:214`, `seatusage/report.py:324`, `vaultwrite/writer.py:1066`.

How `80` is built:
- It is test-first, with three runs on a planted copy. Run A uses a stub helper: all three cases go red. Run B uses bare-name resolution: the alias case and the wrapper case go red. Run C uses the full resolver: all three pass.
- Each of Sol's three cases is planted into a `shutil.copytree` copy of the real `src/`:
  - `dump_database` in `restic.py:155`: a new call inside an existing non-reader.
  - an `as` alias of the loader.
  - one radar function that calls `take_beat`, `hb.backup_freshness` and `latest_snapshot_age()`.
- On the real tree, the test pins the reader set, the entrypoints and the referrers, and asserts `unresolved == set()`. That last check is the fail-loud one (L1).
- Suite: 2210 → 2213 expected (three parametrized cases).

## RULE PROOF (`grep -c -F -e "<rule>" <new> <original>`, one call per string)
| string | `80` | `77` | | string | `81` | `78` |
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

- In `81`, the four **2**s count the same way they do in `78`. The second hit is AUTHORIZATION quoting R49's strings, or the Opus checker's own `--disallowedTools` in §2. Each string appears once in the hub's launch line.
- `gpt-6-astra`: `80` = 0. `81` = 1 and `78` = 1; in both it is the refusal sentence, not a launch string.
- `80`'s launch line differs from `77`'s only in the prompt path, the remote-control name and `--model claude-opus-5` (was `claude-sonnet-5`). `81`'s launch line differs from `78`'s only in the prompt path and the remote-control name.

**NEW approvals:** none. `80` reuses 09-20 R25, the same line as `77`. `81` reuses 09-20 R13 and 09-21 R49, the same as `78`, with `grok`/`agy` under 09-21 R39 through 2026-09-22. The desk fills each prompt's `R__` launch row.

READING: `LAWS.md` in full · `reports/ops-6a-check-r2-2026-09-22.md` whole · `scratch/…/ops-6a-check-r2/sol-check.md` whole · `reports/ops-6a-check-2026-09-22.md` ESCALATE · branch `ops-classifier-fix-2026-09-22.md` (outline, ESCALATE) · `restarts.py` whole · `test_jobs_restarts.py` whole · `jobs.yaml:1-200` · `restarts.md` whole · greps: loader/wrappers over `src`, `cli.py` imports and dispatch, `backup/cli.py`, `heartbeat/cli.py`, `runner.py` imports, `restic.py` defs, radar plist, AST users · prompts `77`, `78` whole · `cto-2026-09-21.md` rows R50–R55.

## ESCALATE
1. **Builder seat: Opus 5, above the L29 floor.** Sonnet is eligible because there is no write path. I chose Opus 5 because round 3 is the last (L67) and the call-edge resolver needs judgment: aliases, relative imports, module attributes and re-exports. `ASK DESK: keep Opus 5 for 80, or swap to Sonnet 5 (change only --model)? [20:18 ET]` Safe default: Opus 5, as drafted.
2. **Where the call-edge extractor lives: the test, not `restarts.py`.** The walk, namer, resolver and module graph are reused. The call/reference-edge extraction is new code in the test. It walks a different graph (calls, not imports), so I do not read it as a second walker. `81` Q2 puts that reading to the checkers. The alternative, a `call_graph()` helper in `restarts.py`, is a `src/` change that derives a `com.cobalt.radar` restart through `cobalt.cli` (L43 pause). `ASK DESK: test-local call-edge extraction (as drafted), or a restarts.py helper that brings a radar restart into the stacked deploy? [20:18 ET]` Safe default: as drafted.
3. **Sol listed items the ruling did not include. They are listed in `80`, not built:**
   - a resident plist invoking an operator command
   - `backup/secrets.py:54`
   - a dropped call where another call remains (partly covered: dropping a function's only call removes it from the set, so the test goes red)
   - a second call inside a function that is already a reader (no new reader)
   - dynamic calls (`getattr`)

   `81` Q4 asks each checker whether any of these blocks the deploy. If one does, it goes to Dejan.
4. **Carried by id:** round-1 ESCALATE 2 (the `cli.md` seam), 3 (circular restore → 6b) and 4 (restic `forget` grouping); round-2 builder ESCALATE 5 (`watchlists.yaml` `if`, `restarts.py:243-244`). Always: round 3 is the last (L67); whatever it leaves open goes under `81`'s `## FOR DEJAN`.
- Also noted: round 2's Gemini returned HARNESS in under a minute. `81` keeps `78`'s one-attempt Gemini shape with no new flag, because adding a flag would be a new rule.

## CONTINUE
step: closed. `80` and `81` are written and the rule proof is done. Desk next: read both, answer ESCALATE 1–2, fill in the `R__` rows, commit, then launch `80`. `81` follows `80`'s `OPS FIX R3 BUILT` line and must run by 2026-09-22 23:59 ET (R39).

## DIGEST FOR THE DESK
- **`80`: Opus 5, offline.** It runs in `ops-0921` on `ops/2026-09-21`, starting from `3ad064f`. It has two steps and changes only three paths: the test file, the DevDoc and its report.
  - Z3 is the call-graph reader proof in `test_jobs_restarts.py`.
  - Z4 adds one sentence to `restarts.md:7`.
- **The proof** walks from `load_backup_config` through all callers transitively, resolving aliases, relative imports and `probe_mod.backup_freshness`-style calls. The closure runs on `restarts.reachable`. It pins 12 readers, 5 CLI entrypoints and 2 referrers, and requires `unresolved = ∅`.
- **Red first:** each of Sol's three cases is planted into a `tmp_path` copy of the real `src/`. Runs A/B/C show a stub failing all three, bare-name resolution failing the alias and wrapper cases, and the full resolver passing all three.
- **Why not `restarts.py`:** module reach can't answer the question (radar imports `cobalt.cli`). A `src/` edit would derive a radar restart. No helper needs exporting.
- **CLOSE:** 2213/0 (2210 + 3). `jobs restarts main..HEAD` exit 0 with `RESTARTS: none`. `src`/`configs`/`ops` diffs empty. A grep confirms there is no second traversal.
- **`81`: Sonnet 5 hub** with Grok · Gemini · Sol · Opus 5; three must check. It has five questions: Sol's cases (a)(b)(c) one by one · one walker (L3) · anything weakened · Sol's Q2 in its own words · ready.
  - `ready` = yes only if ≥3 checked, 0 defects hold, no `STILL OPEN`, and Sol answers `Sol Q2: closed`.
  - Anything still open goes in `## FOR DEJAN` as one A/B per item. There is no round 4.
- **`81` packet:** `ordered-prompt.md` (41,875 B) goes in two parts. The stagger vs `68`/`61`/`73` and the date gate (through 09-22) are unchanged from `78`.
- **Rule strings:** none new. `80`=`77` and `81`=`78` string for string. The desk fills `R__` in both.
- **Asks:** ESCALATE 1 (seat) and 2 (extractor location). Both defaults are as drafted.

OPS FIX R3 PROMPTS DRAFTED · prompts: 2 · builder seat: Opus 5 · walker reused: yes · new rule strings: 0 · ESCALATE: 4
