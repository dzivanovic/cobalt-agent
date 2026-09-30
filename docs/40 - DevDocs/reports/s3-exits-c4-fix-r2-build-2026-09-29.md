# S3 EXITS C4 FIX R2 BUILD — 2026-09-29

Prompt: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-29/37-s3-exits-c4-fix-r2-build.md` · seat `s3-exits-c4-fix-r2-build` · Opus 5.5 · fresh session · started 20:54:06 EDT (`date`).

## §0 Headline
(written at CLOSE)

## L74
A system block attached to this session's context (it arrived with the first tool result, the prompt file's Read) asks for a `Claude-Session: https://claude.ai/code/session_…` line in every commit message and PR body and names a file-send tool. Recorded once here (L74); not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`<D>` = `2026-09-29` (`date` → `Tue Sep 29 20:54:06 EDT 2026`).
| gate | command | result |
|---|---|---|
| placeholder `R__` | `grep -n -E "R_[_]" "…/prompts/2026-09-29/37-s3-exits-c4-fix-r2-build.md"` | no output, exit 1 — PASS |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" "…/37-s3-exits-c4-fix-r2-build.md"` | one hit, `43:` = this gate's own line — PASS |
| classification | `grep -n -F "S3 EXITS C4 FIX R2 DRAFTED" "…/reports/s3-exits-c4-fix-r2-draft-2026-09-29.md"` | `83:S3 EXITS C4 FIX R2 DRAFTED · FIX: 1 · NOT REAL: 10 · UNPROVEN: 1 · OUT OF SCOPE: 1 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 7` — the file's last non-blank line (`tail -n 3`), `OWNER ITEM: 0` — PASS |
| launch row | `grep -n -F "37-s3-exits-c4-fix-r2-build.md" "…/reports/cto-2026-09-29.md"` | `172:| R163 | 20:53 ET | LAUNCH (R154, L75): C4 fix r2 build \`37-s3-exits-c4-fix-r2-build.md\`, Opus 5.5, cwd \`~/cobalt-wt/s3-exits-c4\`; base \`e49fe6a2\`; no with-DB run in flight; dev vault: TEST.md 767 B, ZZPB.md 665 B, both Sep 29 09:35. B1-6 kept (L1). | LAUNCHED |` — R163 names this file, carries `<base>` `e49fe6a2`, the dev-vault listing and the literal — PASS |
| row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"37-s3-exits-c4-fix-r2-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-29.md"` | `ebb54b0e468e92c4b2fc925528fd3de195260485` — NON-EMPTY, PASS |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 29 20:54:06 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## s3/exits-c4` |
| base | `git log --oneline -1` | 0 | `e49fe6a2 docs(s3-c4): S3 exits C4 fix r1 build report — 01d0fbb9` = `<base>` |
| no code past `<code base>` | `git -C /Users/cobalt/cobalt log --oneline 01d0fbb9..s3/exits-c4 -- src tests configs` | 0 | empty |
| no `.env` here | `ls /Users/cobalt/cobalt-wt/s3-exits-c4/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/s3-exits-c4/.env: No such file or directory` |
| lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| `upsert_trade_note` | `grep -n "def upsert_trade_note" src/cobalt/prefill/trade_note.py` | 0 | `221:def upsert_trade_note(` |
| `_render_value` | `grep -n "def _render_value" src/cobalt/prefill/trade_note.py` | 0 | `113:def _render_value(key: str, value) -> str:` |
| `_render_frontmatter(` | `grep -n "_render_frontmatter(" src/cobalt/prefill/trade_note.py` | 0 | `121:def _render_frontmatter(fields: dict, *, every_key: bool = True) -> str:` · `268:        writer.create_if_absent(path, _render_frontmatter({**fresh, **fills}) + body)` · `293:        _render_frontmatter(merged, every_key=False).rstrip("\n"),` |
| `split_frontmatter` | `grep -n "def split_frontmatter" src/cobalt/vaultwrite/frontmatter.py` | 0 | `35:def split_frontmatter(content: str) -> tuple[Optional[dict[str, Any]], str]:` |
| `frontmatter_span` | `grep -n "def frontmatter_span" src/cobalt/vaultwrite/frontmatter.py` | 0 | `58:def frontmatter_span(lines: list[str]) -> Optional[tuple[int, int]]:` |
| RUN U2 test | `grep -n "def test_run_u2_a_typed_exit_price_after_a_later_write" tests/cobalt/test_s3_c4_trade_note_offline.py` | 0 | `321:def test_run_u2_a_typed_exit_price_after_a_later_write(vault):` |
| `note_world` | `grep -n "def note_world" tests/cobalt/test_s3_c4_trade_note_db.py` | 0 | `41:def note_world(panel_world, monkeypatch):  # noqa: F811` |
| callers `upsert_trade_note(` | `grep -rn -F "upsert_trade_note(" src` | 0 | `src/cobalt/prefill/trade_note.py:221:def upsert_trade_note(` · `src/cobalt/prefill/trade_note.py:375:        path, action = upsert_trade_note(` · `src/cobalt/prefill/trade_note.py:436:        _, action = upsert_trade_note(card, when, paths, entry_price=entry["price"],` · `src/cobalt/aset/web.py:1047:        trade_path, trade_action = upsert_trade_note(card, when, prefill_paths, entry_price=inp.entry)` |
| callers `write_card_note(` | `grep -rn -F "write_card_note(" src` | 0 | `src/cobalt/prefill/trade_note.py:341:def write_card_note(` · `src/cobalt/cards/cli.py:149:        note = write_card_note(args.card_id, retry=True)` · `src/cobalt/aset/web.py:1550:        return write_card_note(card_id), None` |
| callers `write_leg_unit(` | `grep -rn -F "write_leg_unit(" src` | 0 | `src/cobalt/prefill/trade_note.py:395:def write_leg_unit(` · `src/cobalt/aset/web.py:1569:        write_leg_unit(card_id, leg_id, closed=closed)` |
| callers vs EXPECTED | — | — | the six EXPECTED hits (`aset/web.py:1047`, `:1550`, `:1569`, `cards/cli.py:149`, `prefill/trade_note.py:375`, `:436`) and the three `def` lines; no other caller |
| dev vault (the desk's listing, R163 / LAUNCH-TIME VALUES, 20:53 ET; no command run by me) | — | — | `-rw-------  1 cobalt  staff  767 Sep 29 09:35 Trade-2026-09-03 10-00-00 -TEST.md` · `-rw-------  1 cobalt  staff  665 Sep 29 09:35 Trade-2026-09-03 10-00-00 -ZZPB.md` (under `/Users/cobalt/dev-vault-cobalt/1 - Trading/2 - Trades/`) |
| restarts, empty range | `uv run cobalt jobs restarts e49fe6a2..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |

## E0 BASELINE
On `<base>` `e49fe6a2` (src = `01d0fbb9`), no `.env`, no test file written while the offline run was in flight.
- offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, 20:55 → 21:04, `date` 21:04:26 after) → **`3320 passed, 480 skipped, 1 xfailed, 20 warnings in 552.67s (0:09:12)`**, exit 0 (= EXPECTED `3320 passed`, 0 failed).
- live-note (run while the offline run was in flight; it writes no file): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 26.00s`** (= EXPECTED). The one skip: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — none names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Written (tests only, no `src/` edit):
- `tests/cobalt/test_s3_c4_trade_note_offline.py` — helpers `_block`, `_set_line`, `_replace_block`, `_his_lines`, `_close`, the constructed `HIS_BLOCK` / `HIS_OWN`; **B1-1** `test_his_typed_exit_price_keeps_its_bytes_after_the_close_write` · **B1-2** `test_his_edit_of_a_value_cobalt_filled_keeps_its_bytes` · **B1-3** `test_his_typed_exit_time_keeps_its_bytes` · **B1-4** `test_his_own_lines_keep_their_bytes_and_order` · **B1-5** `test_the_size_write_keeps_his_typed_exit_price_bytes` · **B1-6** `test_a_frontmatter_the_line_merge_cannot_map_is_refused_untouched` · **N** `test_the_merge_still_refreshes_cobalts_five_and_fills_a_blank`.
  - B1-1's "every frontmatter line but Cobalt's five equals the file before": the close write of a radar card also fills the blank `exit_time:` (R35 (3)), so the expected list is the before-list with that one line as `exit_time: "2026-09-03 10:31"`; every other non-five line must be equal and in order.
  - B1-4's `# a constructed comment` sits directly under `direction:` (one of Cobalt's five), so B1-4 also pins that a comment under a replaced entry is kept (see `## E3 THE ROW` and `## ESCALATE`).
- `tests/cobalt/test_s3_c4_trade_note_db.py` — **B1-7** `test_his_typed_exit_price_keeps_its_bytes_through_the_close_and_the_retry` and the RUN `test_run_u3_the_refusal_text_of_a_nan_or_negative_manual_fill`.

**Offline** (on `01d0fbb9` src): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_s3_c4_trade_note_offline.py` → exit 1, **`6 failed, 18 passed in 0.91s`**. Each red's first line:
- B1-1 `tests/cobalt/test_s3_c4_trade_note_offline.py:395` `assert _line(path, "exit_price") == "exit_price: 5.10"` → `E       assert 'exit_price: "5.1"' == 'exit_price: 5.10'` (the re-rendered line)
- B1-2 `:407` → `E       assert 'entry_time: ...-09-03 10:02"' == 'entry_time: 2026-09-03 10:02'` / `+ entry_time: "2026-09-03 10:02"` (quoted)
- B1-3 `:415` → `E       assert 'exit_time: "631"' == 'exit_time: 10:31'` (the VALUE changed: sexagesimal `631`)
- B1-4 `:423` → `E       AssertionError: assert ['trade_def: ...-range-break'] == ['trade_def: ...de, example]']` / `Right contains 5 more items, first extra item: '# a constructed comment'` (comment dropped, lines re-rendered / re-ordered)
- B1-5 `:439` → `E       assert 'exit_price: "5.1"' == 'exit_price: 5.10'`
- B1-6 `:448` → `E       Failed: DID NOT RAISE <class 'cobalt.prefill.vault_writer.VaultWriteError'>` (the missing raise)
- **N PASSED**, **`test_his_exit_price_is_never_overwritten` PASSED** (both among the 18). No guard trip (no `outside tmp_path` text; every test in the `vault` fixture).

**With-DB — LOCK TAKE 1** (on `01d0fbb9` src + the red tests):
- Lock (a): `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`.
- Lock (b): `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c4/.env`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly `-rw-------  1 cobalt  staff  2186 Sep 29 21:05 /Users/cobalt/cobalt-wt/s3-exits-c4/.env`. **L76 lock taken 21:05:47** (`date`). Every `COBALT_ENV=dev` call was directly preceded by `ls -la /Users/cobalt/cobalt-wt/s3-exits-c4/.env` (LISTED).
- `<FP>` (the query under `## W THE THREE SUITES`) → `664	35	272c95bbb12241e3611e4b36326ccf87` → **F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`** (= fix r1's F0).
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `legs user - - -`, `voice_turns user - - -` → **`0013`**; `aset_sizings 1 0824685c130da3c7cb7f0e76191a6819`, `card_stop_edits 1 7599f9ab…`, `card_transitions 4 f181e76b…`, `cobalt_redactions 199 5b47526f…` (system, outside this build; fix r1 read 198), `vault_overrides 6 6a8b0520…`, `vault_writes 187 2c8181e1…`, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `code: e49fe6a2 (DIRTY: 3 path(s))`. No forward.
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_s3_c4_trade_note_db.py` → exit 1, **`1 failed, 17 passed in 4.27s`**:
  - **B1-7 FAILED** on the close's line: `/Users/cobalt/cobalt-wt/s3-exits-c4/tests/cobalt/test_s3_c4_trade_note_db.py:403: assert 'exit_price: "5.1"' == 'exit_price: 5.10'` (`:403` = the assertion right after the close, `grep -n "exit_price: 5.10"` → `400:` the hand edit, `403:`, `407:`).
  - Every other test PASSED (the 17 `PASSED` lines, the U3 run among them); no `outside tmp_path` text.
- **RUN U3**: `COBALT_ENV=dev uv run pytest -q -rP -p no:cacheprovider --color=no tests/cobalt/test_s3_c4_trade_note_db.py -k test_run_u3` → WHOLE:
```
.                                                                        [100%]
==================================== PASSES ====================================
________ test_run_u3_the_refusal_text_of_a_nan_or_negative_manual_fill _________
----------------------------- Captured stdout call -----------------------------

RUN U3 · POST /fill on a fresh manual card per input · the page's refusal lines
U3 /fill card 13402 actual_fill='NaN' → 200
U3   <div id="banner"><div class="failed">FAILED
U3   <div class="muted">Every computed sizing persists to Postgres (cobalt_dev — chosen by COBALT_ENV alone, RULING 7: production writes cobalt_brain, dev writes cobalt_dev) and appends to today's daily note in the same action. Missing data = FAILED, never guessed.</div>
U3        out.value = 'FAILED';
U3        alert('Prefill FAILED: ' + e.message);
U3 /fill card 13403 actual_fill='-1' → 200
U3   <div id="banner"><div class="failed">FAILED
U3   <div class="muted">Every computed sizing persists to Postgres (cobalt_dev — chosen by COBALT_ENV alone, RULING 7: production writes cobalt_brain, dev writes cobalt_dev) and appends to today's daily note in the same action. Missing data = FAILED, never guessed.</div>
U3        out.value = 'FAILED';
U3        alert('Prefill FAILED: ' + e.message);
1 passed, 17 deselected in 0.54s
```
  Both inputs → 200 with the page's banner `<div id="banner"><div class="failed">FAILED` — a refusal banner IS rendered, so **no `NO REFUSAL TEXT`, no `ESCALATE U3` line**. Recorded for the check: the banner's reason text sits on the lines after `FAILED` and carries none of the three words, so the RUN (which prints only lines with `FAILED` / `REFUSED` / `Nothing written`) does not show WHY; the other three lines are the page's static text / script, not the refusal. Not fixed here (`/fill`'s parse is C1's).
- `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` = F0 (unchanged). Nothing left behind: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT ticker, count(*) FROM aset_sizings WHERE ticker IN ('TEST', 'ZZPB') GROUP BY ticker"` → `ticker	count` (no rows).
- Lock (d): `rm /Users/cobalt/cobalt-wt/s3-exits-c4/.env`; `ls /Users/cobalt/cobalt-wt/s3-exits-c4/.env` → `ls: /Users/cobalt/cobalt-wt/s3-exits-c4/.env: No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` → **`.env: removed, proven gone (E2) — L76 lock released 21:06:25`** (held 21:05:47 → 21:06:25). No migration applied.

## E3 THE ROW

## W THE THREE SUITES

## RESTARTS

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: E3 (the red commit `wip(s3-c4-fix-r2): red` is made; if it is absent from `git log`, commit it first)

## ESCALATE

(run in progress — next step under ## CONTINUE)
