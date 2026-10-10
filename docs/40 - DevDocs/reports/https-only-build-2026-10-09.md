# https-only-1009 — build report (2026-10-09)

## §0 Headline
- BUILT, 5 of 5 rows. `https_url` has one config home. On an insecure page the voice banner names the https address. aset binds loopback only (`lan` is refused, naming L80). The probes, the S2 K4 checks and the deploy-smoke curl read `https://<HOST>/`.
- Gate on `4dfe6114`: offline 4059/0 · with-DB 4946/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`.
- RESTARTS: `com.cobalt.aset com.cobalt.radar`. DEPLOY ORDER stands: M5 before the deploy, or aset crash-loops.
- 1 decision: `tests/cobalt/test_jobs_restarts.py` (outside the card's files) moved its backup.yaml reader pin and admits one `__main__`-guarded import-time read.
- Fix round, seam (2026-10-09): `a1b99495` moves this card's hunks off the lines voice fix 193 (main `2041a53f`) changed. Gate on `a1b99495`: offline 4061/0 · with-DB 4948/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`. 1 new decision (DECISION 2).

## L74
- A system reminder arriving mid-session asked commits to end with a `Claude-Session:` line. Recorded once; not acted on (L74). Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/156-https-only-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/156-https-only-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/156-https-only-card.md" · 0 · 84db90abc58e825836eb7a5362844079184432d1
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/156-https-only-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-09 R718 row · grep -n "^| R718 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 11:| R718 | 07:14 ET | Relayed by brain (L79), then his words 07:20 ET: "yes https only please". Widens R717 to every page: https via `tailscale serve`; http binds 127.0.0.1; probes read https. APPLIED: LAWS L80, NOW at 07:20 ET. | HIS RULING · APPROVED · APPLIED |
RULING 2026-10-09 R718 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R718 |" -- "docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 1458693dbde5371259a29c5d502d74e3878fee3b
RULING 2026-10-09 R718 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | quoted below |
| base | `git show --stat e4586978` | 0 | `Merge: 2d580f26 0d187b31` · `Merge branch 'main' into deploy/radar-top50-1009` · `.../reports/deploy-radar-top50-1009.md │ 137 +++` · `1 file changed, 137 insertions(+)` |
| restarts | `uv run cobalt jobs restarts e4586978..HEAD` | 0 | `docs/40 - DevDocs/reports/https-only-build-2026-10-09.md	A	DOCS	-` · `RESTARTS: none` (the untracked report only; no commit in range) |

```
clock · date · 0 · Fri Oct  9 18:52:47 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/https-only-1009
    ?? "docs/40 - DevDocs/reports/https-only-build-2026-10-09.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · e4586978 Merge branch 'main' into deploy/radar-top50-1009
diff · git diff --stat e4586978 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/https-only-1009 · 0 · e4586978 Merge branch 'main' into deploy/radar-top50-1009
env here · ls /Users/cobalt/cobalt-wt/https-only-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

THE CARD'S SYMBOLS (grep / Read, each hit):
- `grep -rn -F "widget_html(" src tests` → `src/cobalt/voice/web.py:306:def widget_html() -> str:` · `src/cobalt/aset/web.py:469:</div>{voice_web.widget_html()}</body></html>"""` · `src/cobalt/aset/web.py:912:    return page.replace("</body>", voice_web.widget_html() + "</body>", 1)` · `tests/cobalt/test_radar_panel_cards.py:705` · `tests/cobalt/test_voice_web.py:232, :240, :256, :270, :288, :297, :303, :308`.
- `grep -rn -F "sheet_http(" src tests` → `src/cobalt/heartbeat/runner.py:133:        probe_mod.sheet_http(),` · `src/cobalt/heartbeat/probes.py:128:def sheet_http(url: str = "http://127.0.0.1:5010/") -> Probe:` · `tests/cobalt/test_sheet_daymode_probe.py:196:        probe = probes.sheet_http(url)`.
- `grep -rn -F "sheet_daymode(" src tests` → `src/cobalt/heartbeat/runner.py:138:        probe_mod.sheet_daymode(),` · `src/cobalt/heartbeat/probes.py:154:def sheet_daymode(url: str = "http://127.0.0.1:5010/api/health") -> Probe:` · `tests/cobalt/test_sheet_daymode_probe.py` :100–:159 (each passes its own URL).
- `grep -rn -F "local_lan_ip" src tests` → `src/cobalt/aset/net.py:12` · `src/cobalt/aset/__main__.py:24` (import), `:33` (call) · `tests/cobalt/test_aset_net.py:5, :24, :28, :31, :35`.
- `grep -rn -F "127.0.0.1:5010" src configs ops/desk tests` → `probes.py:128`, `:154` · `s2.yaml:135`, `:142`, `:149`, `:157` · `deploy-smoke.sh:12`, `:135`, `:136` · `tests/cobalt/test_smoke.py:544`, `:548`, `:1488`, `:1499`, `:1512` · `tests/fixtures/dayopen/heartbeat.log.excerpt:4, :94, :188, :276` · `tests/ops/test_deploy_smoke.py:43`, `:134`.
- `grep -rn -F "bind" src/cobalt/aset tests/cobalt/test_aset_config.py` → `config.py:78`, `:81` `bind: Literal["loopback", "lan"] = "loopback"`, `:86` `return "127.0.0.1" if self.bind == "loopback" else "0.0.0.0"` · `__main__.py:4`, `:6`, `:30`, `:32` `if cfg.server.bind == "lan":`, `:41` · `test_aset_config.py:109`, `:112`, `:117`, `:118`, `:122`, `:124`, `:142`.
- Read: `voice/config.py:41` `class VoiceConfig`, `:42` `extra="forbid"`, `:120` `def load_voice_config`; `voice/web.py:268` `async function start(){`, `:270` `const type = pickType();`, `:271` `if (!type || !navigator.mediaDevices){ … 'no microphone on this device' …`, `:274`, `:300` `if (!pickType()) { device.push(…) …`, `:306`–`:308` `widget_html`; `aset/config.py:74` `class ServerConfig`, `:77`–`:80` comment, `:81`, `:84`–`:86`, `:128` `def load_config`, `:129`; `aset/__main__.py:24`, `:28`, `:32`–`:48`, `:50`; `runner.py:133`, `:138`; `test_voice_web.py:33`–`:39` (`cfg` fixture), `:231`–`:234`, `:262`–`:280`, `:310`; `test_voice_config.py:105` `assert checked == list(GOOD_VOICE["voice"]) and len(checked) == 14`; `test_aset_config.py:108`–`:114`, `:110` comment `(e.g. Dejan may have it set to "lan")`, `:117`–`:119`; `test_smoke.py:1488`, `:1499`; `test_deploy_smoke.py:43`, `:134`; `test_radar_panel_cards.py:703`–`:705`; `deploy-smoke.sh:12`, `:135`–`:136`, `:140`; `configs/dev/aset.yaml:32`–`:41`.
- `wc -l`: voice/config.py 169 · voice/web.py 312 · aset/config.py 269 · aset/__main__.py 50 · heartbeat/probes.py 869 · voice.yaml 46 · s2.yaml 636 · dev/aset.yaml 53 · deploy-smoke.sh 381 · test_voice_web.py 312 · test_voice_config.py 390 · test_aset_config.py 313 · test_smoke.py 1574 · test_deploy_smoke.py 263 · test_radar_panel_cards.py 1270.
- `## READ` names no report; no `tail -n 3` owed.

THE CARD'S RECORDS, copied and re-read:
- L80 read at `LAWS.md:391`–`:393` — re-read (Read): `391 ### L80 HTTPS only` … `393 — 2026-10-09 R718`.
- BIND TODAY — re-read: `grep -n -F "aset.local.yaml" .gitignore` → `50:configs/dev/aset.local.yaml`; `aset/config.py:129` `path = LOCAL_CONFIG_PATH if LOCAL_CONFIG_PATH.exists() else CONFIG_PATH`; `configs/dev/aset.yaml:40` `  bind: loopback`; `__main__.py:50` `uvicorn.run("cobalt.aset.web:app", host=host, port=port)`. The gitignored file itself, the plist and `start_aset.sh` are not re-read (no listed read reaches them without need).
- PROBES TODAY — re-read by the `127.0.0.1:5010` grep above. DEPLOY-HUB lines not re-read (not this job's file).
- PEER GATE BEHIND SERVE — copied; not re-read (uvicorn internals, not a row).
- RESTARTS — copied; derived at RESTARTS.
- DB — copied: every new test is offline.
- BASE at drafting `6f55636b`; the card's BASE is `e4586978` and preflight proves HEAD = BASE.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `4054 passed, 790 skipped, 1 xfailed, 36 warnings in 645.88s (0:10:45)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.56s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
No with-DB red (every new test is offline); no lock taken. Commit `e51eada6` `wip(https-only-1009): red — rows A-D tests first (L80, R718)`.

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_voice_config.py tests/cobalt/test_voice_web.py tests/cobalt/test_aset_config.py tests/cobalt/test_smoke.py tests/ops/test_deploy_smoke.py tests/cobalt/test_https_only.py` → `8 failed, 148 passed, 11 skipped, 15 warnings, 17 errors in 3.23s`. Each red's first line:
- A `test_https_url_is_required_and_https_only`: `cobalt.voice.config.VoiceConfigError: …voice.yaml: invalid voice config: … https_url  Extra inputs are not permitted [type=extra_forbidden, input_value='https://box.example0000.ts.net/', …]` — the row's reason (the key refused as extra).
- A pin `test_every_tunable_names_its_source_in_the_committed_file`: `… 14 == 15)` — the count moves with the new key.
- B `test_an_insecure_page_shows_the_https_line`: `assert 'window.isSecureContext' in "async function start(){\n   if (rec) return;\n   const type = pickType();…"` — the first ordering assert, not `AttributeError`.
- C `test_lan_bind_is_refused`: `test_aset_config.py:120: Failed: DID NOT RAISE <class 'Exception'>` — `bind="lan"` still resolves.
- D `test_every_probe_reads_the_configured_https_url`: `AssertionError: {'K4.1': 'http://127.0.0.1:5010/api/health', 'K4.2': 'http://127.0.0.1:5010/', 'K4.3': 'http://127.0.0.1:5010/radar', 'K4.4': 'http://127.0.0.1:5010/api/radar/pool?since={cutoff}', ...}` — each starts with `http://127.0.0.1:5010/`.
- D (added beside it) `test_the_curl_refusal_names_the_https_url`: `assert 'http://127.0.0.1:5010/' not in '#!/bin/sh\n...'` (rerun alone after reordering its asserts so the plain-URL assert comes first: `2 failed in 0.08s`).
- D moved pins `test_smoke.py` `test_k4_4_asks_the_pool_api_with_the_cutoff_as_since` and `test_render_url_percent_encodes_each_value_and_the_api_parses_it_back`: `AttributeError: 'VoiceConfig' object has no attribute 'https_url'` — they now read the URL from its one home, which BASE lacks.
- D moved pins `tests/ops/test_deploy_smoke.py`, 17 setup errors, each `E   KeyError: 'https_url'`: the `box` fixture writes the curl row from `voice.yaml`'s `https_url`, which BASE lacks. The new refusal case (`curl … http://127.0.0.1:5010/radar` → `not a mapped smoke command`) is masked by that setup error here; its own red is shown by mutation at E3.
- Rewritten once: the first E2 run had `tests/ops/test_deploy_smoke.py` read the URL through `load_voice_config()`, which errored `cobalt.env.EnvConfigError: COBALT_ENV is unset` (tests/ops pins no `COBALT_ENV`); it now reads `voice.yaml` as data.
- The `cfg` fixture added to every widget test that lacked it (`test_voice_web.py`: sheet, radar, endpoints, speech, refused status, device line, no local voice, no form, no card id, hold and tap) — green on BASE.

## E3 THE ROWS
Commit `4dfe6114` `feat(https-only-1009): https-only — https_url home, voice banner on insecure pages, loopback-only bind, probes on https (rows A-D, L80, L1, L3)` — 15 files.

| row | change | greens | mutation → red (first line) |
|---|---|---|---|
| A | `VoiceConfig.https_url: str = Field(pattern=r"^https://[a-z0-9.-]+\.ts\.net/$")` (no default); `voice.yaml` `# source: L80, R718; M3 proof` + `https_url: https://<HOST>/` | `tests/cobalt/test_voice_config.py` → `65 passed in 0.47s` | (1) pattern `^https?://…` → `test_voice_config.py:127: Failed: DID NOT RAISE <class 'cobalt.voice.config.VoiceConfigError'>` (`1 failed, 1 passed, 63 deselected`); (2) `default="https://x.ts.net/"` → `:122: Failed: DID NOT RAISE …` and `test_every_missing_key_crashes[https_url]` `:145: DID NOT RAISE` (`2 failed`); each undone with Edit |
| B | `_WIDGET`: `const HTTPS = __HTTPS__;`; `start()` first test `if (!window.isSecureContext){ banner([{level:'red', text:'voice needs the https address: ' + HTTPS.replace(/\/$/, '') + location.pathname}]); return; }`; on-load `if (!window.isSecureContext) { device.push(<same line>); banner(); }` / `else if (!pickType()) { …'no microphone on this device'… }`; `widget_html()` = `_WIDGET.replace("__HTTPS__", json.dumps(get_config().https_url), 1)` | `test_voice_config.py test_voice_web.py test_radar_panel_cards.py` → `166 passed, 2 skipped in 3.24s` (`test_radar_panel_cards.py` needed no `cfg` fixture: unchanged) | (1) `start()` secure test removed → `test_voice_web.py:335: assert 'window.isSecureContext' in "async function start(){…"`; (2) on-load `else if` → `if` → `:342: assert 'else if (!pickType())' in ' // L80: …'`; each undone |
| C | `ServerConfig.bind: Literal["loopback"]`, a `mode="before"` validator refusing `lan` with `… (L80)`, `host` → `"127.0.0.1"`; `__main__.py` drops the `lan` branch and `local_lan_ip` import, prints `http://127.0.0.1:<port>` and `load_voice_config().https_url`; comment blocks in `config.py` and `configs/dev/aset.yaml` | `test_aset_config.py test_aset_net.py` → `16 passed, 9 skipped in 0.06s` | validator test `v == "lan-mutated"` → `test_aset_config.py:122: assert 'L80' in "1 validation error for ServerConfig\nbind\n  Input should be 'loopback' [type=literal_error, input_value='lan', …]"`; undone |
| D | `sheet_http` default `https://<HOST>/`, `sheet_daymode` `https://<HOST>/api/health`, one docstring line each; `s2.yaml` K4.1–K4.4 `https://<HOST>/…`; `deploy-smoke.sh` header `:12`, case `:135` `https://<HOST>/*) ;;`, refusal `:136` `curl reads https://<HOST>/ only`; `:140` unchanged | `test_https_only.py test_smoke.py test_deploy_smoke.py test_sheet_daymode_probe.py test_aset_config.py test_voice_config.py test_voice_web.py` → `184 passed, 11 skipped, 15 warnings in 11.66s` | (1) case `https://<HOST>/*\|http://127.0.0.1:5010/*` → `test_https_only.py:55` (case ≠ `https+"*"`), `:67` (`'http://127.0.0.1:5010/' not in …`), and the new refusal case `test_a_command_outside_the_mapped_shapes_is_red_and_never_run[curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar]` `test_deploy_smoke.py:228: AssertionError: assert 0 == 1` (`3 failed, 16 passed`); (2) `sheet_daymode` default back to `http://127.0.0.1:5010/api/health` → `test_https_only.py:49: AssertionError: {'sheet_daymode': 'http://127.0.0.1:5010/api/health'}`; each undone |

After the mutations: `git diff --stat` → the 14 row files only (`14 files changed, 72 insertions(+), 48 deletions(-)`), the tree at the fix.

THE FULL SUITE FOR ROWS A AND B: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt tests/ops` → `1 failed, 6478 passed, 788 skipped, 2 xfailed, 36 warnings in 1245.61s (0:20:45)`. The red: `tests/cobalt/test_jobs_restarts.py:469: AssertionError: ['cobalt.aset.__main__.<module>', 'cobalt.aset.web._card_tap', 'cobalt.aset.web._render', …]` — `test_backup_yaml_readers_are_pinned_and_derive_the_aset_restart` pins every function reaching `load_backup_config()`. Rows B and C make `widget_html` → `get_config` → `load_voice_config` → `load_backup_config` reachable from 24 more functions, all in `com.cobalt.aset` (the sheet and `/radar` routes, `__main__`). Moved in that test (see DECISION 1): the readers set (+24), the entrypoints set (+20), the referrers set (+`cobalt.aset.web._result_card`, whose parameter `fill` shares the route's name), and the import-time guard, which now allows exactly `cobalt.aset.__main__` (read under `if __name__ == "__main__":`, asserted from the source) and only for `com.cobalt.aset`. `row.restarts == ("com.cobalt.aset",)` is unchanged. `test_jobs_restarts.py test_jobs_reads.py` → `46 passed in 16.22s`.

`grep -rn -F "127.0.0.1:5010" src configs ops/desk` → only `Binary file src/cobalt/heartbeat/__pycache__/probes.cpython-314.pyc matches` (a stale untracked cache). `grep -rn -F "taild24291" src configs ops tests docs/40\ -\ DevDocs/cobalt` → `probes.py:128`, `:156`; `s2.yaml:135`, `:142`, `:149`, `:157`; `voice.yaml:48`; `deploy-smoke.sh:12`, `:135`, `:136` (plus the same `.pyc`).

DevDocs, one dated line each (`## 2026-10-09 — https-only-1009`): `cobalt/voice/config.md`, `cobalt/voice/web.md`, `cobalt/aset/config.md`, `cobalt/aset/__main__.md`, `cobalt/heartbeat/probes.md`. `ops/desk/deploy-smoke.sh` has no DevDocs page (`grep -rl -F "deploy-smoke.sh" "docs/40 - DevDocs/ops"` → nothing).

## RESTARTS
`uv run cobalt jobs restarts e4586978..HEAD` (row E, RUN):
```
path	change	rule	restart
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
configs/cobalt/voice.yaml	M	resident reads	com.cobalt.aset
configs/dev/aset.yaml	M	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/aset/__main__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/web.md	M	DOCS	-
docs/40 - DevDocs/reports/https-only-build-2026-10-09.md	A	DOCS	-
ops/desk/deploy-smoke.sh	M	operator script; no Cobalt reader	-
src/cobalt/aset/__main__.py	M	static import reach	com.cobalt.aset
src/cobalt/aset/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar
src/cobalt/voice/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_aset_config.py	M	test/documentation; no resident	-
tests/cobalt/test_https_only.py	A	test/documentation; no resident	-
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/cobalt/test_smoke.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_config.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_web.py	M	test/documentation; no resident	-
tests/ops/test_deploy_smoke.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row; nothing classified here. The report row shows because the report is untracked in the tree.

## W THE THREE SUITES
`<tip>` = `4dfe6114`. One call: `sh /Users/cobalt/cobalt/ops/desk/gate.sh https-only-1009 all --deploy` (background, exit 0). No `--deselect` (no with-DB test added), no `--tickers` (no with-DB test writes a ticker), no `--migration`. Verdict lines, WHOLE:
```
offline 4059/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4946/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/https-only-1009-all-20261009-193353.log
```
No line marked `OUTSIDE the allowed set`.
- (a) offline: `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (log :2) → `4059 passed, 790 skipped, 1 xfailed, 36 warnings in 658.28s (0:10:58)` (log :867). E0 had 4054; the +5 are this build's: `test_https_url_is_required_and_https_only`, `test_every_missing_key_crashes[https_url]`, `test_an_insecure_page_shows_the_https_line`, `test_every_probe_reads_the_configured_https_url` and `test_the_curl_refusal_names_the_https_url`. `test_lan_bind_is_refused` replaces `test_server_lan_bind_resolves_to_all_interfaces` (+0).
- (b) lock taken at log :872–:873 (`lock taken: https-only-1009`, `lock: waited 0 min`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :884); `LEVEL 0013`.
- (c) PASS 1 at 0013, the executed command (log :939), WHOLE: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py` → `4751 passed, 7 skipped, 89 deselected, 3 xfailed, 43 warnings in 793.49s (0:13:13)` (log :1093) → `<d1>` 4751.
- (c2) `dev forward: APPLIED 19:58:32` (log :1095); `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (log :1171).
- (c3) PASS 2, the executed command at log :1173 (the gate-lists PASS 2 list; no deselect of this build) → `195 passed, 1 deselected, 5 warnings in 230.15s (0:03:50)` (log :1899) → `<d2>` 195; 4751 + 195 = 4946 = `with-DB 4946/0`. This build adds no with-DB test id.
- (c3r) `stray rows: not read (no --tickers given)`: no with-DB test of this build writes a ticker.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :1965) = F0 → `cobalt_dev: 0013 — F2 = F0`; `lock released` (log :2017–:2018); `.env: removed`; `ls /Users/cobalt/cobalt-wt/https-only-1009/.env` → `No such file or directory`.
- (e) live-note → `146 passed, 1 skipped, 15 warnings in 26.31s` (log :2087); the one skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- `tests/ops` (not in the gate's lists; `test_deploy_smoke.py` is a row file): run in the E3 full run (`tests/cobalt tests/ops` → the only red was the jobs pin, DECISION 1) and alone after row D (`tests/ops/test_deploy_smoke.py` in the `184 passed` run).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason. E2 reds: A `extra_forbidden` on `https_url`; B `'window.isSecureContext' in "async function start(){…`; C `DID NOT RAISE`; D the `http://127.0.0.1:5010/` dict. E3 mutation reds per row are in the E3 table: A ×2, B ×2, C ×1, D ×2. The new deploy-smoke refusal case was masked at E2 by its setup `KeyError`; its own red is shown at E3 mutation (1) of row D: `test_deploy_smoke.py:228: assert 0 == 1`. The moved jobs pin was red at E3 (`test_jobs_restarts.py:469`, then `:508`, then `:546`) before each move. No test stayed green under its mutation.
(2) Every entry path is pinned:
- `widget_html` callers `aset/web.py:469` (the sheet) and `:912` (`/radar`): `test_the_widget_partial_renders_on_the_sheet`, `test_the_widget_partial_renders_on_radar` and `test_radar_panel_cards.py:705`, each rendering with the configured URL. Secure and insecure branches: `test_an_insecure_page_shows_the_https_line` (static, both `start()` and on-load); the secure `no microphone` paths stay pinned by `test_a_device_red_line_survives_every_status_callback` and the hold-and-tap test.
- `sheet_http()` / `sheet_daymode()` bare calls at `runner.py:133`, `:138`: the defaults, pinned by `test_every_probe_reads_the_configured_https_url`. Explicit-URL callers (`test_sheet_daymode_probe.py`) are unchanged.
- `ServerConfig(bind=…)` directly and through `load_config()` (local or committed file): both in `test_lan_bind_is_refused`. Default loopback: `test_server_defaults_to_loopback`, `test_missing_server_section_falls_back_to_loopback_default`.
- `__main__.py`'s start print has no runtime test (a `python -m` script). The jobs pin asserts its `load_voice_config(` read sits under the `__main__` guard.
- The K4 URLs and the curl shape: `test_https_only.py`, `test_smoke.py` K4.4 pins, `test_deploy_smoke.py`.
(3) Every `file:line` was re-read at the tip: `grep -n -F "isSecureContext" src/cobalt/voice/web.py` → `:272`, `:304`; `grep -n -F "https_url" …` → `voice/config.py:67`, `voice.yaml:48`, `voice/web.py:316`, `aset/__main__.py:6`, `:31`; `grep -rn -F "taild24291" …` and `grep -rn -F "127.0.0.1:5010" src configs ops/desk` (E3, after the last edit; the commit changed no content); gate log lines by `grep -n -F` on the log.

## FOR THE CHECK
- `e4586978..4dfe6114`: `e51eada6 wip(https-only-1009): red — rows A-D tests first (L80, R718)` · `4dfe6114 feat(https-only-1009): https-only — https_url home, voice banner on insecure pages, loopback-only bind, probes on https (rows A-D, L80, L1, L3)`.
- Per row reds, mutations and greens: `## E2 RED`, `## E3 THE ROWS`. Caller greps: `## PREFLIGHT`. RUN row E output: `## RESTARTS` (WHOLE).
- Suites: `## W` (executed commands, summaries). F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 `664 35 272c95bbb12241e3611e4b36326ccf87`. Lock taken and released inside the one gate call (log `:872`–`:873`, `:2017`–`:2018`; gate started 19:33:53, forward 19:58:32).
- CHECK ASKS, pointers:
  - X1: `voice/web.py:272` (`start()` returns on an insecure page before `pickType()` / `navigator.mediaDevices`) and `:304`–`:305` (on-load `if` / `else if`). `no microphone on this device` stays at the secure-only branches.
  - X2: `grep -rn -F "127.0.0.1:5010" src configs ops/desk` → only a stale `.pyc`.
  - X3: the hostname grep above lists only `voice.yaml`, the two probe defaults, `s2.yaml` and `deploy-smoke.sh`. Tests read it from `voice.yaml`. The DevDocs line writes `<HOST>`.
  - X4: `ServerConfig.bind` is `Literal["loopback"]` with the `lan` refusal; `configs/dev/aset.yaml:37` is `bind: loopback`. The gitignored `configs/dev/aset.local.yaml` is M5, his.
- `src/cobalt/aset/net.py` (`local_lan_ip`) and `tests/cobalt/test_aset_net.py` are left in place. Row C drops only the import; no caller remains in `src`.
- Records copied at PREFLIGHT: see `## PREFLIGHT`.
- FIX ROUND — SEAM (`CONTINUE: seam`, cto-desk, 2026-10-09; it replaces the withdrawn `CONTINUE: merge`):
  - Main's changes, `git diff e4586978 main`: `voice/web.md` `@@ -52,0` (a section added after the file's last line); `test_voice_web.py` `@@ -250,0` (`test_a_hidden_widget_row_is_not_displayed`, inserted after base `:250`, before the refused-status test's `def`); `src/cobalt/voice/web.py` `@@ -203,0` (`#cv-voice .cv-row[hidden]{display:none}` in `<style>`). Since then main moved only `7fed85ea` (`git diff --stat 2041a53f main` → `202-deploy-s4-p1-card.md`, no shared file).
  - Branch hunks at the tip, `git diff -U0 e4586978 -- <the two files>`: `voice/web.md` `@@ -50,0 +51,3` (this card's section sits above `## 2026-10-01 — voice-peers (check)`, so it is off 193's insertion at `:52`); `test_voice_web.py` `@@ -216`, `-222`, `-231`, `-237`, `-262`, `-283`, `-295`, `-302`, `-307`, `-312,0 +313,56`. No hunk sits at or next to base `:250`/`:251`. Before the round, `-251` (`test_the_widget_reads_a_refused_status_as_red_never_all_clear(cfg)`) touched 193's insertion point; that `def` line is back to main's text (DECISION 2). `src/cobalt/voice/web.py`: this branch's hunks start at `@@ -226` and lie well past 193's `:203`.
  - None of 193's lines is changed by this card.
  - Touched tests at `a1b99495`: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_voice_web.py tests/cobalt/test_https_only.py tests/cobalt/test_voice_config.py` → `109 passed, 1 skipped in 1.40s` (the skip: `test_voice_web.py:163: reaches cobalt_dev (lock-relief G1)`).
  - RESTARTS `e4586978..HEAD` → `RESTARTS: com.cobalt.aset com.cobalt.radar` (unchanged, no UNCLASSIFIED).
  - Deploy gate, `sh /Users/cobalt/cobalt/ops/desk/gate.sh https-only-1009 all --deploy` on `a1b99495`, exit 0. Its output: `offline 4061/0` · `lock: waited 17 min` · `LEVEL 0013` · `pass 1: whole (deploy)` · `stray rows: not read (no --tickers given)` · `cobalt_dev: 0013 — F2 = F0` · `.env: removed` · `with-DB 4948/0` · `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/https-only-1009-all-20261009-225136.log`. Skips, all inside the allowed set (none marked `OUTSIDE`): `test_cards_picks.py:388`, `:401`; `test_radar_evaluate.py:695`; `test_replay_line.py:266`; `test_s3_c4_experiments.py:95`; `test_catalyst.py:365`; `test_predicate.py:262`. Executed commands: log `:2`, `:939` (pass 1), `:1174` (pass 2), `:2034` (live-note). F0 (log `:884`) `664 35 272c95bbb12241e3611e4b36326ccf87` = F2 (log `:1967`).
  - Not run: the merged tree (no `git merge` is typed here). 193's own test, which has no `cfg` fixture, will get its config through `get_config()` from the committed `voice.yaml` after the merge. The refused-status test now runs in exactly that mode and is green above.

## CONTINUE
next: CLOSE (done) — the seam fix round is complete at `a1b99495`. The next step is the desk's: there is no re-check (L75), and the deploy carries 193 and this card together.

## DECISIONS
- DECISION 1 (ASK DESK: a test file outside the card's `files` was moved [2026-10-09 19:33 ET]): `tests/cobalt/test_jobs_restarts.py` `test_backup_yaml_readers_are_pinned_and_derive_the_aset_restart` went red on the rows. It pins every function that reaches `load_backup_config()`, and rows B and C, as the card states them (`widget_html` reads `get_config().https_url`; `__main__` prints `load_voice_config().https_url`), add 24 readers, all inside `com.cobalt.aset`. SAFE DEFAULT TAKEN: the pin was moved to the derived sets, plus one named import-time exception: `cobalt.aset.__main__`, guarded by `if __name__ == "__main__":` (asserted from the source) and allowed for `com.cobalt.aset` only. The derived restart (`com.cobalt.aset`) is unchanged. For the check: does that exception hold, or should `__main__` stop reading voice config, which would change row C's stated seam (L72)?
- DECISION 2 (ASK DESK: one widget test gives up its `cfg` fixture so its hunk stays off 193's lines [2026-10-09 23:36 ET]): voice fix 193 inserts its test right before `def test_the_widget_reads_a_refused_status_as_red_never_all_clear():`. A three-way merge treats an edit to that `def` line as touching 193's insertion, so this branch's `(cfg)` there would conflict. SAFE DEFAULT TAKEN: that one `def` line is back to main's text, and the test reads the committed `voice.yaml` through `get_config()` (green, `109 passed`). Every other widget test keeps `cfg`, as row B states. 193's new test has no `cfg` either and will run the same way after the merge. So no line exists that both cards must change, and 193's lines stay exactly as main has them. For the desk: does that test keep its `cfg`-less signature, or should the deploy's merge resolution add `cfg` to both it and 193's test?

## RECORDS
- One lock take only, inside `gate.sh` at W. No extra take, no `REFUSED, not needed`, no `CONTINUED`.
- L74: a mid-session system reminder asked commits to carry a `Claude-Session:` line. Recorded under `## L74`; not acted on.
- `.env: removed, proven gone (W)`: `ls /Users/cobalt/cobalt-wt/https-only-1009/.env` → `No such file or directory`.
- A stale untracked `src/cobalt/heartbeat/__pycache__/probes.cpython-314.pyc` still matches the old URL by grep. It is a cache file, not committed.
- The card's records, as re-read at PREFLIGHT: L80 `LAWS.md:391`–`:393`; `.gitignore:50`; `aset/config.py:129`; `configs/dev/aset.yaml:40` (now `:37` after the comment change, `grep -n -F "bind: loopback" configs/dev/aset.yaml`).
- 2026-10-09 22:48 EDT (`date`): `CONTINUE: merge` from `cto-desk` — merge `main` (2041a53f, voice fix 193) into `ops/https-only-1009`, resolve `docs/40 - DevDocs/cobalt/voice/web.md` and `tests/cobalt/test_voice_web.py`, rerun the touched tests and the deploy gate, CLOSE with a new tip. NOT FOLLOWED (BUILD-HUB UNATTENDED RULES (b)): `merge` is not a step of BUILD-HUB, and the message adds a command, `git merge`, which BUILD-HUB lists under "Never typed" and which is on no allow string. Nothing was run; the tree is unchanged at `6e1ccd3d`.
- L74: a second system reminder in this session asked commits to carry a `Claude-Session:` line. Already recorded once; not acted on.
- CONTINUED at seam 22:49 EDT: `CONTINUE: seam` from `cto-desk` withdraws `merge`. Its fact was verified: `git -C /Users/cobalt/cobalt log --oneline -6 main` shows `2041a53f`, and `git diff e4586978 main` shows 193's hunks in the two named files (and `src/cobalt/voice/web.py`). It names only listed commands and the Edit tool, and it is the one fix round (L75).
- One more lock take, inside `gate.sh` at the seam round: `lock: waited 17 min`, then released (`.env: removed`; `ls /Users/cobalt/cobalt-wt/https-only-1009/.env` → `No such file or directory`).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

Superseded build line (first build, tip 4dfe6114): job https-only-1009 · on e4586978 · offline 4059/0 · with-DB 4946/0 · live-note 146/0 · RESTARTS: com.cobalt.aset com.cobalt.radar · rows: 5 of 5 · decisions: 1 · tokens: 239963

BUILT · job: https-only-1009 · tip: a1b99495 | on e4586978 | migration: none | offline 4061/0 | with-DB 4948/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 112698
