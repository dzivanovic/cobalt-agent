# Preflight — card 877 `cos-probe-1019` (read-only) · 2026-10-19

Card: `prompts/2026-10-19/877-cos-probe-card.md`. Every `main` read below is `git show main:` or a read of the on-disk file; `git diff HEAD --stat -- src tests configs/cobalt/redact.yaml configs/cobalt/agents "docs/30 - Design/F20-FINAL-2026-10-11.md"` is empty, so disk equals main.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git merge-base --is-ancestor 07eb89a3 main` | exit 0 | OK |
| 1b | `git log --oneline 07eb89a3..main` | `b6a13695`, `fad644f5`: 2 commits, both `docs(desk)` | OK |
| 1c | `git log --oneline 07eb89a3..main -- src/cobalt/cos tests/cobalt src/cobalt/cli.py` | empty | OK |
| 2a | grep `«FILL` in the card | none | OK |
| 2b | JOB / BRANCH / WORKTREE / REPORT | `cos-probe-1019` / `ops/cos-probe-1019` / `cos-probe-1019` / `…/cos-probe-1019/docs/…/cos-probe-1019-build-2026-10-19.md` | OK |
| 2c | BAND · RULINGS | `HIGH` · `2026-10-18 R1863` | OK |
| 2d | header keys vs `CARD.md` build column; `desk-launch.sh:1312` `need JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS` | all present; TIP, CHECK REPORT empty; BASE 8 hex; BAND present (card dated 10-19, `BAND_FROM=20261016`) | OK |
| 2e | `## DEPLOY PROOF` marker lines (`· before` / `· after`) and smoke reads | 2 marker lines and 2 smoke lines | OK |
| 3 | FINAL lines `:82, :84, :85, :86, :87, :91`: `git show main:"docs/30 - Design/F20-FINAL-2026-10-11.md"` | each quote in the card matches the table row verbatim (X20 / X11 / X12 / X3+X14 / X17 / X2+X10) | OK |
| 3b | rows for X2, X10, X11, X12, X3, X14, X17 | all seven in P1 (choices list) with a pass rule; RED-first is the `--help` test and P2's `invalid choice: 'probe'`; X2/X10 split, X3 killed-child rule, X14 and X17 marked ASK DESK with a default | OK |
| 3c | `ALLOWED_ENV` (`session.py:54`) · `TOOLS` count · `cos.yaml` | `("PATH","HOME","USER","LANG","COBALT_ENV")` · `test_cos_offline.py:50` asserts the set equals `SEVEN` · `model: claude-sonnet-5-5` | OK |
| 4a | `redact` definition | `src/cobalt/redact/guard.py:80`, `def redact(text, *, channel, cfg, record)` | OK |
| 4b | `card_text` | `hitl/card.py:46`; the `#k=` line is `:50`: `…{base_url}/hitl/{row_id}#k={key}` | OK |
| 4c | every `redact.yaml` pattern vs `…/hitl/7#k=<32 hex>` | `url_query_secret` (`:125`, regex `:131`) needs `[?&]` before the key name: `#k=` has neither. `env_assignment_secret` (`:176`, regex `:190`) needs PASSWORD/SECRET/TOKEN/API_KEY/MASTER_KEY/… in the name: `k` is not one. `fernet_key`, `mattermost_token`, `finviz_token_named` need a named prefix; `sk-`, jwt, AWS, Google shapes do not occur in a 32-hex string. Literal half: `load_literals` reads `COBALT_MASTER_KEY` (`secrets.py:129`); deleting it makes the half inactive. The fragment survives, so the test is GREEN on BASE and is the control | OK |
| 4d | `RedactResult.text` / `.clean` | `guard.py:59`, `:63` (`clean = not hits`) | OK |
| 4e | mutation | `[?&]` → `[?&#]` and `key` → `k\|key` (`\|` is the table escape; the builder writes `k|key`): `#k=` then matches and the `secret` group is replaced, so the test goes red on the missing key | OK |
| 4f | card vs FINAL `:82` | FINAL's pass = the key survives (a redacted key breaks the link); the card follows the FINAL and says the drafting prompt's "removes the hex" is the ASK DESK item. Card: control, green today | OK |
| 5 | grep `launchctl\|keychain\|\.claude\.json\|send` in the card | `launchctl`: NOT IN THIS JOB, the P2 recorder, the boundary (e). `keychain`: `:36` prohibition. `.claude.json`: `~/.claude.json` only in prohibitions (`:22`, `:36`, `:47`); `home/.claude.json` is the planted file inside the scratch HOME. `send`: `send_dm` patched to raise, `:23`. No launchd label, no resident, no credential, no DM | OK |
| 6 | the auth route: card A1 + `draft-cos-probe-2026-10-19.md:5, :15` | A1 names `claude auth status`, sourced to `claude auth --help` run 16:11 (quoted in `## RECORDS`; not in repo code). Card states non-zero exit gives `PROBE <item> FAIL auth: …`, nothing spawned, output not kept; no credential copying (`NOT IN THIS JOB` last-but-one line). Drafter decision 6 says it is not proven the CLI sees the login from a scratch HOME | OK (see NOTE 1) |
| 7a | `cos/cli.py` `_run` `:11-14`, `add_parser` `:17`, `run` parser `:20-23` | match the `show main:` text | OK |
| 7b | `session.py:54` `ALLOWED_ENV` · `:67` `PERMISSION_MODE` · `:93` `child_env` · `:98` `build_options` · `:118` `_scrubbed_environ` · `:130` `_kill_tree` · `:206` `sdk_client_factory` · `:255` `class CosSession` · `:361` `_dm` | all found at those lines | OK |
| 7c | `session.py:201` `_transport._process` (X12's pid) | present in `_SdkClient.kill` | OK |
| 7d | `src/cobalt/cli.py:87` `from cobalt.cos import cli as cos_cli`; `:554` `cos_cli.add_parser(sub)` | both match | OK |
| 7e | `hitl/card.py:46`, `:50`; `guard.py:80`; `redact.yaml:125`, `:176` | match | OK |
| 7f | `test_hitl_offline.py:141` | `assert "https://sheet.example.invalid/hitl/7#k=" + key in seen[0]`: the pre-redaction text, as the card says; `:34` is the `_record` stub precedent | OK |
| 7g | `test_cos_offline.py:139, :160, :180, :350, :412, :458, :515` | `test_options_allowlist…`, `test_spawn_env_is_the_allowlist`, `test_hang_max_turns…`, `…o6_a_hung_connect…`, `test_max_turns_leaves_no_descendant…`, `test_cos_run_without_the_flag…`, `test_max_turns_leaves_no_orphaned…` | OK |
| 7h | `808-deploy-f20-cos-card.md:21` | the `## LAUNCHD` line; the gate list matches the card's RECORDS; the seven probe items plus X20 are in it | OK |
| 7i | `jobs.yaml:203` `imports: [cobalt.cli]` (radar); `:226` `imports: [cobalt.cos.run]` (cos) | match | OK |
| 8 | `restarts.py` `classify` `:178-264` and `import_graph` `:120-161` | read by content. The graph walks every `ast.Import`/`ImportFrom` in the tree, lazy ones too. `src/` file: restarts = residents whose reach holds the module. `cobalt.cos.cli` is imported by `cobalt/cli.py:87`, which radar reaches. `cos/run.py` imports `.session`, `.listener`, `.store` and never `cos.cli` or `probe`; `cos/__init__.py` imports nothing. `tests/` → "test/documentation; no resident". `docs/` → `DOCS`, empty. Header `RESTARTS: com.cobalt.radar` equals this reading. R1 (the tool run) is still the record | OK |
| 9a | `git log -1 --format=%h%n%s -- <card>` | `b6a13695` · `docs(desk): cos probe card 877 drafted, preflight 878 R2084` | OK |
| 9b | `git diff HEAD --stat -- <card>` | empty: committed and unchanged | OK |

## ISSUES
- NOTE 1: `claude auth status` is proven only by the drafter's 16:11 `--help` runs, quoted in the card's `## RECORDS`, not by repo code or docs; the card names it and does not say `unproven`. Whether it exits 0 under a scratch HOME is unproven: every item may print `FAIL auth`. The card routes that to the desk (drafter decision 6), so it is a run-time outcome, not a build blocker.
- NOTE 2: the header carries `CLASS: K2` and `INSTALL: none`, which `CARD.md` does not list for a build, and `HOUSE B: as needed` where `CARD.md` says build leaves it empty. `desk-launch.sh:1312` requires neither; line `:2086` accepts `as needed`. No launch refusal found.
- NOTE 3: my prompt gave the FINAL at `reports/F20-FINAL-2026-10-11.md`. The file is `docs/30 - Design/F20-FINAL-2026-10-11.md`, which is the card's path.
- NOTE 4: the mutation text in row X20 uses `k\|key`; read it as the table escape and write `k|key` in the regex.
- NOTE 5: R1 (`uv run cobalt jobs restarts`) was not run here (no `uv run`); the reading above is by content only. X14 and X17 are the card's ASK DESK defaults.

Blocks the launch: nothing.

PREFLIGHT DONE · card: cos-probe-1019 · checks: 30 · fails: 0 · ready: YES
