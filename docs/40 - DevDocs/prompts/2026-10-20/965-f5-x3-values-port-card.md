JOB: f5-x3-values-port
LADDER: OFF-LADDER — reports/cto-2026-10-20.md R2217
CLASS: K2
INSTALL: none
BRANCH: ops/f5-x3-values-port
WORKTREE: f5-x3-values-port
BASE: bac9b683
TIP:
REPORT: /Users/cobalt/cobalt-wt/f5-x3-values-port/docs/40 - DevDocs/reports/f5-x3-values-port-build-2026-10-21.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x3-values-port-check-2026-10-21.md
HOUSE B: as needed
BAND: LOW
RESTARTS: com.cobalt.aset
RULINGS: 2026-10-18 R1863

## ROWS

WHY: card 958 (job `f5-x3-values`, check `reports/f5-x3-values-check-2026-10-20.md` ready YES, code tip `e9245a8e`, head `3680824c`, BASE `20dd871d`) deployed and was rolled back at smoke (s): the card's read `curl … http://127.0.0.1:5010/` is not admitted by the deploy launch line (`DEPLOY-HUB.md:11` admits only `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/*`) and was refused (`reports/deploy-f5-x3-values.md` `## DECISIONS` D-2). The code and every other read were green. Main holds the merge `d71bcb4a` and its revert `7e4f946d`, so `e9245a8e` is an ancestor of main and `deploy-card.sh:553` refuses it. THE FIX (brain, L79, precedent card 923): a fresh port from current main re-applies the same diff; never a revert-of-revert, never `recut`. THE SPEC is `git diff 20dd871d e9245a8e` (three files, 43+, 4−), nothing else; the values are card 958's and are not re-opened. HOW: Edit / Write ONLY (`BUILD-HUB.md:14` admits `git show*` and `git diff *`, no `git apply`, `cherry-pick` or `git mv`; `:16` never types `rm`). For each file: `git show e9245a8e:<path>` read whole, then the worktree file is brought to those bytes (Edit hunk by hunk, quoting the spec's lines). No line is improved, reflowed or renamed. Every spec file is unchanged on main since `20dd871d` (`## RECORDS`), so each port is a pure re-application. No `src/` change, no plist, no migration, no database, no model call.

| row | what | red first | files |
|---|---|---|---|
| P1 | THE TEST. `tests/cobalt/test_checkpoints_offline.py` becomes byte-equal to `git show e9245a8e:tests/cobalt/test_checkpoints_offline.py` (spec: 36+; card 958 T1/T2's NEW test `test_route_budgets_are_measured`, after `test_route_is_loaded_and_local` at `:553`). Ported FIRST, before P2 | RUN on BASE's `modelaccess.yaml` with P1's test: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_checkpoints_offline.py`, quoted whole. RED, by name: `test_route_budgets_are_measured`, on `assert "UNMEASURED" not in "\n".join(block_lines)` (the block holds the two UNMEASURED comments, `modelaccess.yaml:77`, `:79`); quote the assertion it fails on | `tests/cobalt/test_checkpoints_offline.py` |
| P2 | THE CONFIG. `configs/cobalt/modelaccess.yaml` becomes byte-equal to `git show e9245a8e:configs/cobalt/modelaccess.yaml` (spec: 4+, 4−; route `checkpoint.narrative` at `:70`, the four lines `:77-80`: two `# source: X3 reports/f5-x3-measure-2026-10-20.md …` comments, `timeout_s: 25`, `max_output_tokens: 256`) | P1's red turns GREEN; the same command, quoted whole, `0 failed` | `configs/cobalt/modelaccess.yaml` |
| D0 | THE MODULE DOC. `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` becomes byte-equal to `git show e9245a8e:"docs/40 - DevDocs/cobalt/prefill/checkpoints.md"` (spec: 3+, the section `## 2026-10-20 — f5-x3-values`, kept as it is). No section of this job's own is added (the port is the record) | the symbol-check gate, if it asks | `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` |
| D1 | THE CITED SOURCE (ASK DESK 1 of the drafter; default: ported). `docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md` is written byte-equal to `git show 20dd871d:"docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md"` (182 lines). It is the report both P2 comments cite; it reached main only through the reverted merge and is off main's tree now. Its `.result` is not ported | — (docs only) | `docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md` |
| E1 | RUN — asserts nothing. THE EQUALITY PROOF, on the committed port tip `<tip>`, each output quoted whole: (a) `git diff --stat <BASE> <tip> -- configs/cobalt/modelaccess.yaml "docs/40 - DevDocs/cobalt/prefill/checkpoints.md" tests/cobalt/test_checkpoints_offline.py` and `git diff --stat 20dd871d e9245a8e --` the same three paths: the two tables are equal line for line (`modelaccess.yaml` `8`, `checkpoints.md` `3`, `test_checkpoints_offline.py` `36`; 43 insertions, 4 deletions); (b) `git diff e9245a8e <tip> --` the same three paths prints NOTHING; (c) `git diff --stat <BASE> <tip> -- src tests configs ops` names only `configs/cobalt/modelaccess.yaml` and `tests/cobalt/test_checkpoints_offline.py`; (d) with D1: `git diff 20dd871d <tip> -- "docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md"` prints NOTHING. Any line of (b) or (d) is a FAIL of this row, fixed by re-quoting from the spec commit, never by a `## DECISIONS` waiver | — (tool output quoted in the report) | none |
| R1 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`, the table WHOLE; the header's `RESTARTS` is the drafter's reading (`## RECORDS`), the tool's last line is the record | — (tool output quoted in the report) | none |

THE DOCS OUTSIDE THE SPEC (excluded from E1 (a)-(c), listed): the old job's build report `reports/f5-x3-values-build-2026-10-20.md` and its `.result` (on head `3680824c`, off main since the revert) are NOT ported; this job writes its own `REPORT` and `.result` instead. D1's X3 report is proved by E1 (d) alone.

ORDER: P1 (then its RED run), P2 (then GREEN), D0, D1, card 958's suite `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_checkpoints_offline.py tests/cobalt/test_modelaccess_config.py tests/cobalt/test_checkpoints_registry.py` (whole, quoted, `0 failed`), the commit, E1, R1, the `## DEPLOY PROOF` marker reads on the tree, the three suites (BUILD-HUB `## W`), the stop line. No live run, no model call in this job.

## NOT IN THIS JOB
- Any change to the spec's content: a line of the three spec files that differs from `e9245a8e` (or of D1's file from `20dd871d`) is a defect of this port. A flaw found in the spec is a `## DECISIONS` item, UNPROVEN (L70), never fixed here (card 958, the X3 report and its check stand).
- Re-deciding the values or their rule (R2217, R2248, R2251): `timeout_s: 25` and `max_output_tokens: 256` are card 958's.
- Any file outside the three spec files and D1's report, but this job's own build report and `.result`.
- `git apply`, `git cherry-pick`, `git merge`, `git revert`, `git checkout <ref> -- <path>`, `git mv`, `rm`, `mv` (`BUILD-HUB.md:14`, `:16`); the re-land string `git revert --no-edit 7e4f946d` (the desk's, not taken: brain L79); `desk-launch.sh recut`.
- Loading any plist: `com.cobalt.checkpoint-0715/-0745/-0815/-0845` stay unloaded; `configs/cobalt/jobs.yaml` (their `timeout_s: 300`) is read, never edited.
- `local.plan`, `local.embed`, any other `modelaccess.yaml` key; `src/`; `ops/`; any migration; any database; any production command; any `lms`, `launchctl` or `curl`.

## READ
- `prompts/2026-10-20/958-f5-x3-values-card.md` whole (the spec's rows T1, T2, COLD; its `## CHECK ASKS` X1–X4).
- `git diff 20dd871d e9245a8e` (the spec); `git show e9245a8e:<path>` for each of the three files and `git show 20dd871d:"docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md"` (the bytes to write).
- `reports/f5-x3-values-check-2026-10-20.md` (its stop line: `ready: YES`, `held unfixed: 0`, `RESTARTS: com.cobalt.aset`).
- `reports/deploy-f5-x3-values.md` `## Smoke` (s) and `## DECISIONS` D-2 (why this port exists).

## CHECK ASKS
- X1 THE DIFF EQUALITY: re-run row E1 on the check's own read of the tip: is `git diff e9245a8e <tip> --` the three spec paths empty, and is `git diff --stat <BASE> <tip>` over them equal, file for file, to `git diff --stat 20dd871d e9245a8e` over them? Does `git diff --stat <BASE> <tip> -- src tests configs ops` name only `modelaccess.yaml` and `test_checkpoints_offline.py`?
- X2 THE CONTENT: for each of the three files, does `git show <tip>:<path>` equal `git show e9245a8e:<path>` byte for byte (and D1's report equal `20dd871d`'s)? Did the port touch any file but those, the build report and its `.result`?
- X3 RESTARTS re-derived: `com.cobalt.aset` only (`jobs.yaml:86`: aset reads `modelaccess.yaml`; the test and the docs restart nothing)?
- X4 THE SMOKE READ: is the `## DEPLOY PROOF` smoke line's command exactly the admitted form of `DEPLOY-HUB.md:11` (`curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/…`), with no `http://127.0.0.1:5010/` read and no `uv run pytest` line in the section?
- X5 SCOPE: the check is diff equality plus card 958's offline suite and the three suites. The values, the X3 report and card 958's check stand: write no finding that rests on re-deciding them.

## DEPLOY PROOF
- `grep -c -F "source: UNMEASURED" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `2` · after `0`
- `grep -c -F "# source: X3 reports/f5-x3-measure-2026-10-20.md" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `2`
- `grep -c -F "(warm model)" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `1`
- `grep -c -F "cold load 8.67 s from the mainframe log (proxy, not a live cold call)" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `1`
- the sheet answers after the aset restart · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/` · exit 0, `200`
- checkpoint plists stay on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` · exit 0, listed

## DECISIONS
1. ASK DESK (drafter, D1): the X3 report the two `# source:` comments cite is off main's tree since the revert; default taken: ported as docs-only row D1, byte-equal to `20dd871d`. Strike D1 and E1 (d) to keep the port to the three spec files.
2. The smoke read is the admitted https form (`DEPLOY-HUB.md:11`). `ops/desk/deploy-smoke.sh` does NOT map it (its curl shape reads `http://127.0.0.1:5010/` only: "curl reads http://127.0.0.1:5010/ only"); no hub step calls `deploy-smoke.sh` (`git grep` on HEAD: only `deploy-step0.sh:47`, a comment). The hub runs it at (s) (`DEPLOY-HUB.md:157`) against the launch line's own `curl` entry; the same URL is already one of (c)'s three reads (`DEPLOY-HUB.md:152`).
3. BAND LOW, CLASS K2, RESTARTS `com.cobalt.aset`: copied from card 958 (two config values, one test, one DevDocs line; the port adds one docs file). The builder's `cobalt jobs restarts` line (R1) overrides the header if it differs.
4. BASE `bac9b683` = main's HEAD at the drafter's read; the desk resets it at launch.

## RECORDS
- 958 rolled back on a card-fault smoke string (http curl not admitted); re-ships as fresh port f5-x3-values-port with PROOF = diff equality to e9245a8e, smoke read via https://cobalt.taild24291.ts.net/ — brain 9b07db5a 2026-10-21
- Drafter `draft-f5-x3-values-port` (prompt 964), 2026-10-21 01:11–01:16 EDT (`date`). Reads only; nothing run, no git write, nothing committed. `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `bac9b683` (`bac9b683 docs(desk): R2267 958 re-ships as port f5-x3-values-port, drafter prompt 964`). `ls /Users/cobalt/cobalt-wt/` → no `f5-x3-values-port` (fresh).
- THE SPEC: `git diff --stat 20dd871d e9245a8e` → `configs/cobalt/modelaccess.yaml | 8` · `docs/40 - DevDocs/cobalt/prefill/checkpoints.md | 3` · `tests/cobalt/test_checkpoints_offline.py | 36` (3 files, 43+, 4−).
- PURE RE-APPLICATION: `git diff --stat 20dd871d main -- configs/cobalt/modelaccess.yaml "docs/40 - DevDocs/cobalt/prefill/checkpoints.md" tests/cobalt/test_checkpoints_offline.py` → nothing. Main's code moved elsewhere since BASE: `git diff --stat 20dd871d main -- src configs tests ops` → `configs/cobalt/rules.yaml`, `ops/desk/deploy-outage.sh`, `deploy-step0.sh`, `desk-launch.sh`, four `tests/ops/` files (none a spec path).
- `git merge-base --is-ancestor e9245a8e main` → exit 0 (why `deploy-card.sh:553` refuses the old tip).
- D1: `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x3-measure-2026-10-20.md"` → No such file; `git diff --stat main 20dd871d -- "docs/40 - DevDocs/reports/"` → `f5-x3-measure-2026-10-20.md | 182 +++`.
- MARKERS on HEAD (01:12): `git grep -c -F "source: UNMEASURED" HEAD -- configs/cobalt/modelaccess.yaml` → `2` (`:77`, `:79`); the other three strings → `0` (no match). On `e9245a8e`: `source: UNMEASURED` + `# source: X3 …` → `2` together, the spec removing both UNMEASURED lines; `(warm model)` and the cold-load string each on one added line (the spec diff). Each `after` read green at the failed deploy's smoke (d) on the same code (`deploy-f5-x3-values.md:189`).
- Anchors on HEAD: `modelaccess.yaml:70` `checkpoint.narrative:`, `:77-80` (the two UNMEASURED comments, `timeout_s: 60`, `max_output_tokens: 512`); `test_checkpoints_offline.py:553` `test_route_is_loaded_and_local`; `jobs.yaml:86` aset `reads:` `configs/cobalt/modelaccess.yaml`.
- `BUILD-HUB.md:14` (HEAD): `"Edit(//Users/cobalt/cobalt-wt/**)"` (governs Write too, `:16`), `git show*`, `git diff *`; no `git apply`, `cherry-pick`, `git mv`. `:16`: `Never typed: … rm of anything but the …`.
- SMOKE: `DEPLOY-HUB.md:11` admits `"Bash(curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/*)"` only; `:152` (c) reads `https://cobalt.taild24291.ts.net/` already; `:157` (s) runs each `## SMOKE READS` line. `ops/desk/deploy-smoke.sh` (HEAD) curl shape: `http://127.0.0.1:5010/*` only. No `uv run pytest` line in `## DEPLOY PROOF` (unmapped, prompt 964).
- RESTARTS, carried from the failed deploy's run of the tool on the same diff (`deploy-f5-x3-values.md` `## RESTARTS`): `configs/cobalt/modelaccess.yaml M resident reads com.cobalt.aset`, `checkpoints.md` and reports `DOCS`, the test `test/documentation; no resident` → `RESTARTS: com.cobalt.aset`. Row R1 is the record.
- RULINGS: `cto-2026-10-18.md:90` R1863 `HIS RULING · APPROVED` (as card 958). The route: brain 2026-10-21 (L79), a fresh port (prompt 964; desk row R2267).
