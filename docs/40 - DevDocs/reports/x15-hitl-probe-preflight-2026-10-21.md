# x15-hitl-probe — card 977 preflight (2026-10-21, read only)

Every row below is a read of the card, of `git show main:<file>`, or of a file on disk. Nothing was run but reads.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read card header `:1-14` | JOB `x15-hitl-probe`, BRANCH `ops/x15-hitl-probe`, WORKTREE `x15-hitl-probe`, BAND HIGH, RULINGS `2026-10-18 R1863`, INSTALL none, HOUSE B `as needed`, CHECK REPORT path as 976 gave it | OK |
| 2 | Read card `:3` against prompt 976 `:6` | `CLASS: K2`. `K4` appears nowhere in the card (976: "CLASS K2 serving K4") | FAIL |
| 3 | Read card `:13` against 976 `:10` | `RESTARTS: com.cobalt.aset com.cobalt.radar`. 976 expected aset. `jobs.yaml:203` `imports: [cobalt.cli]` and `cli.py:88` imports `hitl.cli`, so radar is reached by reading; `com.cobalt.cos` (`:226`, `cobalt.cos.run`) is not | OK (NOTE 1) |
| 4 | `git grep -n -E "migration" ` over the card | no migration row; `NOT IN THIS JOB` bars any migration | OK |
| 5 | `git log --oneline -2 -- <card>` and `git diff HEAD --stat -- <card>` | `1944e605` commits it; the diff is empty | OK |
| 6 | BASE `41804777` | in main's recent log; main is 3 desk commits ahead (`1944e605`), not a fail | OK |
| 7 | `git show main:src/cobalt/aset/web.py` for the card's `:` anchors | `_hitl_store :1395`, `_hitl_page :1401`, `_hitl_key_sha :1412`, `_hitl_refusal :1419`, `hitl_list :1436`, `@app.get("/hitl/{row_id}") :1451`, `hitl_detail :1452-1490`, pending `:1466`, Approve form `:1468-1471`, script `:1476-1479`, `hitl_approve :1493`, `hitl_deny :1524-1544`. Every card anchor matches | OK |
| 8 | `grep -n "location.hash"` over main's `web.py` | one hit, `:1478`. `test_the_key_script_is_one_source` is satisfiable if the new code's comments do not repeat the string | OK |
| 9 | `git show main:src/cobalt/hitl/cli.py` | docstring `:1` `Read only.`; `_list :10`; `add_parser :22-27` | OK |
| 10 | `git show main:src/cobalt/hitl/card.py` | `page_base_url :31` (https only, raises on null); `card_text :46` | OK |
| 11 | `git show main:src/cobalt/notify/mattermost.py`, `grep -n redact` | rule text `:13-17`; `send_dm :130`; `redact(...)` call `:140` | OK |
| 12 | `git show main:src/cobalt/env.py` | `resolve_env :60` returns `dev`/`production` and RAISES `EnvConfigError` when unset (`:60-70`) | OK (NOTE 2) |
| 13 | `grep -n -A2 hitl.page_base_url` over `tunables.yaml` | `:1038` key, `:1039` `https://cobalt.taild24291.ts.net` | OK |
| 14 | `git grep` F20-FINAL | B `:43`, X15 `:81`, X20 `:82` as the card cites | OK |
| 15 | Builder commands against `BUILD-HUB.md:14` and `:16` | card ORDER uses `uv run pytest -q -p no:cacheprovider --color=no …` (`uv run pytest *`), `uv run cobalt jobs restarts <BASE>..HEAD`, `grep -c -F` markers (`grep *`). No network call, no `git mv`, `rm`, `mv`. `node` runs inside pytest, not as a Bash string | OK (NOTE 3) |
| 16 | P1 route and order | literal `GET /hitl/x15-probe` is placed above `hitl_detail` (`:1451`), so `{row_id}: int` cannot shadow it; `test_probe_route_is_not_shadowed` pins the route index. No `_hitl_store()`, no form, no Approve or Deny control, no write, no URL log line | OK |
| 17 | P1 and S1 script rules | one shared `_hitl_key_script()` for both pages; reads `k` as at `:1478`; the key goes only into `.hitl-k` inputs; no `fetch`, `XMLHttpRequest`, `sendBeacon`, `location` write or submit; readout shows only `k: seen` / `k: missing` | OK |
| 18 | P2 | `forms` opens with `_hitl_k_readout()` above Approve (`:1468`) and ends with `_hitl_key_script()`; approve and deny and `_hitl_key_sha`, `_hitl_refusal` unchanged by the row's own diff rule | OK |
| 19 | P2 test `test_real_page_shows_the_readout_above_approve` | asserts `hitl-k-state` appears ONCE on a pending page. S1 makes the script select `.hitl-k-state`, so the string occurs in the `<div class="hitl-k-state">` and again in the script text: count is 2, the assertion cannot pass as written | FAIL |
| 20 | P3 dev-only and send | `_x15_send` refuses unless dev (exit 2, nothing sent); `secrets.token_hex(16)`; `page_base_url()`; ONE `send_dm("X15 test, approves nothing\n<base>/hitl/x15-probe#k=<hex>")`; prints one `X15 SENT/NOT SENT` line; key never printed or stored. Exact hub string given: `"Bash(COBALT_ENV=dev uv run cobalt hitl x15-send)"` (`## GATE`) | OK |
| 21 | Redaction at `mattermost.py:13-17,140` vs `#k=<32 hex>` (F20 X20) | By reading `redact.yaml`: `:131` needs a `?` or `&` before a name in an auth/token/key list (`#k=` has neither, and `k` is not in the list); `:190` needs a name holding PASSWORD/SECRET/TOKEN/API_KEY…; no bare-hex or entropy pattern (`grep` of `redact/` and `redact.yaml`). So the link is not redacted. But NO row of the card runs `redact()` over the real message (the P3 test patches `send_dm`), and the card never names X20 or says how it is checked | FAIL |
| 22 | Tests: probe route touches no store | `test_probe_route_touches_no_store` patches `_hitl_store` and `HitlStore` to raise, asserts 200 and no `<form`/`Approve`/`Deny`/`fetch(`/`XMLHttpRequest`/`sendBeacon`; `test_probe_path_takes_no_post` covers `/approve` and `/deny` | OK |
| 23 | Tests: readout k present, absent, empty | `test_readout_logic_k_present_absent_empty` runs the script under `node` for a 32-hex key, no fragment, `#k=`, `#x=1`; `pytest.fail` (no skip) when `node` is absent | OK (NOTE 3) |
| 24 | Tests: real approve still needs k, RED first | `test_hitl_web.py` whole stays green (`test_no_key_and_wrong_key_are_refused`); every row has a named `RED on BASE` reason (K25); `test_hitl_offline.py` T3 `_VERB :169`, `:180` passes the new names | OK |
| 25 | `## DEPLOY PROOF` smoke read | `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/hitl/x15-probe` and `…/`; both match `DEPLOY-HUB.md` allow `curl … https://cobalt.taild24291.ts.net/*`. No `http://127.0.0.1:5010/`, no `uv run` line | OK |
| 26 | `## DEPLOY PROOF` marker form | three `grep -c -F … · before 0 · after 1` lines; the single-quoted forms have precedent (`877-cos-probe-card.md`, `910-deploy-cos-probe-fr1-card.md`) | OK |
| 27 | `## GATE` | "The deploy runs after 16:00 ET, outside his trading hours." | OK |
| 28 | `## RECORDS` first line against 976 `:12` | `X15 card — /hitl/x15-probe (no DB, shared hash script, k seen/missing readout), the readout also on /hitl/<id>, dev cobalt hitl x15-send DM; BAND HIGH; deploy after 16:00 — brain 9b07db5a 2026-10-21` matches byte for byte | OK |
| 29 | What blocks the card's own build | nothing external: base is on main, the worktree is fresh, the commands are admitted. Rows 2, 19 and 21 are card-text gaps, not blocks | OK |

## ISSUES
- FAIL 2: the header has `CLASS: K2`; 976 asked for `CLASS: K2 serving K4`. Amend the line.
- FAIL 19: `test_real_page_shows_the_readout_above_approve` pins `hitl-k-state` "once", but the shared script also holds that selector, so the count is 2. Pin the element instead (`class="hitl-k-state"` once, its index below `>Approve<`), or have the script use a different selector. A builder would otherwise have to deviate from the card.
- FAIL 21: no row proves the DM text survives `redact()` (F20 X20). Add one offline assertion to P3: `redact()` on the exact `…/hitl/x15-probe#k=<32 hex>` line is clean and returns the text unchanged. Otherwise a redacted link on the phone reads as `k: missing` and would be taken for an X15 failure.
- NOTE 1: RESTARTS adds `com.cobalt.radar` to the brain's `com.cobalt.aset`. By reading it is correct, because `hitl/cli.py` ships through `cobalt.cli`. Row R1's tool output is the record.
- NOTE 2: `resolve_env()` raises on an unset `COBALT_ENV` rather than returning a value, so the P3 "unset → REFUSED, exit 2" case needs the `EnvConfigError` caught in `_x15_send`. The card's wording implies it but does not say so.
- NOTE 3: the node test needs `node` on the builder's PATH. `ls /opt/homebrew/bin/node` listed it (976 records), but PATH under `claude --bg` is not proven. A builder without it reds loud, by design (ASK DESK 2).
- NOTE 4: `configs/cobalt/notify.yaml` names one bot and no dev notify file exists, so `COBALT_ENV=dev … x15-send` DMs through that same bot. Whether it counts as "the dev bot" of X15 is the desk's call.

PREFLIGHT DONE · card: x15-hitl-probe · checks: 29 · fails: 3 · ready: NO
