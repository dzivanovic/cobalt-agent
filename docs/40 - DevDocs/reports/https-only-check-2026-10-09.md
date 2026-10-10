# https-only-1009 — check report (2026-10-09)

## §0 Headline
Check of https-only-1009 at `4dfe6114` → tip now `6e1ccd3d`. House A Sol (4 findings), house B Grok (2), Opus (4): 10 findings, 0 dropped.
3 held and fixed: A2 (the row B pin did not hold the `no microphone` push inside its `else`), A4 (the row D pin read only the first curl arm), B2 (aset DevDocs still described the LAN bind). Each test shown red first (`c11555b5`).
2 open: A3 REJECTED (no host pin on the committed URL; X3 keeps the host out of tests), B1 UNSETTLED (the moved `test_jobs_restarts.py` pin, the builder's DECISION 1).
X1–X4 answered: insecure page → https line only; nothing names `http://127.0.0.1:5010`; host in the five homes only; no committed config binds off loopback.
Gate green: offline 4061/0 · with-DB 4948/0 · live-note 146/0 · `tests/ops` 2702 passed · cobalt_dev 0013 F2 = F0 · `.env` removed.

## L74
The session's attribution reminder asks commits to carry a `Claude-Session:` line. CHECK-HUB L74 says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, so that line is recorded here once and not added.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/156-https-only-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/156-https-only-card.md" · 0 · f693cb651796cc3087acf6c8c0196302e3ec33e9
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/156-https-only-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-09 R718 row · grep -n "^| R718 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 11:| R718 | 07:14 ET | Relayed by brain (L79), then his words 07:20 ET: "yes https only please". Widens R717 to every page: https via `tailscale serve`; http binds 127.0.0.1; probes read https. APPLIED: LAWS L80, NOW at 07:20 ET. | HIS RULING · APPROVED · APPLIED |
RULING 2026-10-09 R718 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R718 |" -- "docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 1458693dbde5371259a29c5d502d74e3878fee3b
RULING 2026-10-09 R718 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35 (one row); `grep -n "^| R19 "` → line 37 (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Fri Oct  9 20:05:06 EDT 2026
status · git status --short --branch · 0 · ## ops/https-only-1009
head · git log --oneline -1; git log --stat --format=%h 4dfe6114..HEAD · 0 · (5 lines)
    94a4161c docs(https-only-1009): build report — 4dfe6114
    94a4161c
    
     .../reports/https-only-build-2026-10-09.md         | 205 +++++++++++++++++++++
     1 file changed, 205 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/https-only-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/s4-p1-1009/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/https-only-1009/docs/40 - DevDocs/reports/https-only-build-2026-10-09.md" · 0 · BUILT · job: https-only-1009 · tip: 4dfe6114 | on e4586978 | migration: none | offline 4059/0 | with-DB 4946/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 239963
range · git log --oneline e4586978..4dfe6114 · 0 · (2 lines)
    4dfe6114 feat(https-only-1009): https-only — https_url home, voice banner on insecure pages, loopback-only bind, probes on https (rows A-D, L80, L1, L3)
    e51eada6 wip(https-only-1009): red — rows A-D tests first (L80, R718)
PREFLIGHT OK
```
The lock is held by `s4-p1-1009` at preflight; this check waits for it at W.

THE RANGE `git log --stat --format=%h e4586978..4dfe6114` → path union:
- 4dfe6114: `configs/cobalt/smoke/s2.yaml`, `configs/cobalt/voice.yaml`, `configs/dev/aset.yaml`, five DevDocs pages (`aset/__main__.md`, `aset/config.md`, `heartbeat/probes.md`, `voice/config.md`, `voice/web.md`), `ops/desk/deploy-smoke.sh`, `src/cobalt/aset/__main__.py`, `src/cobalt/aset/config.py`, `src/cobalt/heartbeat/probes.py`, `src/cobalt/voice/config.py`, `src/cobalt/voice/web.py`, `tests/cobalt/test_jobs_restarts.py` (15 files, +138 −51)
- e51eada6: `tests/cobalt/test_aset_config.py`, `tests/cobalt/test_https_only.py`, `tests/cobalt/test_smoke.py`, `tests/cobalt/test_voice_config.py`, `tests/cobalt/test_voice_web.py`, `tests/ops/test_deploy_smoke.py` (6 files, +187 −23)

`ls <S>` → No such file or directory (fresh).

House probe `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` → exit 0:
```
sol: UP
grok: UP
gemini: UP
```
house A: Sol (OpenAI, `gpt-5.6-sol`) · house B: Grok (`grok-4.7`). HOUSE B: as needed (not mandatory).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → `STAGED 25 files · 393441 bytes · commits 2` (commit count = PREFLIGHT's 2):
```
36090 <S>/diff.md
15318 <S>/files/156-https-only-card.md
31036 <S>/files/https-only-build-2026-10-09.md
27756 <S>/files/wt/configs/cobalt/smoke/s2.yaml
3142 <S>/files/wt/configs/cobalt/voice.yaml
2458 <S>/files/wt/configs/dev/aset.yaml
1903 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/__main__.md
8216 <S>/files/wt/docs/40 - DevDocs/cobalt/aset/config.md
7220 <S>/files/wt/docs/40 - DevDocs/cobalt/heartbeat/probes.md
2850 <S>/files/wt/docs/40 - DevDocs/cobalt/voice/config.md
3385 <S>/files/wt/docs/40 - DevDocs/cobalt/voice/web.md
13154 <S>/files/wt/ops/desk/deploy-smoke.sh
1383 <S>/files/wt/src/cobalt/aset/__main__.py
11755 <S>/files/wt/src/cobalt/aset/config.py
37218 <S>/files/wt/src/cobalt/heartbeat/probes.py
7997 <S>/files/wt/src/cobalt/voice/config.py
15681 <S>/files/wt/src/cobalt/voice/web.py
13005 <S>/files/wt/tests/cobalt/test_aset_config.py
2590 <S>/files/wt/tests/cobalt/test_https_only.py
32407 <S>/files/wt/tests/cobalt/test_jobs_restarts.py
74860 <S>/files/wt/tests/cobalt/test_smoke.py
17003 <S>/files/wt/tests/cobalt/test_voice_config.py
15494 <S>/files/wt/tests/cobalt/test_voice_web.py
11165 <S>/files/wt/tests/ops/test_deploy_smoke.py
355 <S>/rulings.md
```
`stage-copy.sh` (files `## READ` names that the diff does not touch):
- `COPIED 20290 <S>/files/wt/src/cobalt/heartbeat/runner.py`
- `COPIED 65933 <S>/files/wt/tests/cobalt/test_radar_panel_cards.py`

`<S>/HOUSE-INSTRUCTIONS.md` written: the HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS and RECORDS, and the Files paragraph.

## OWN FINDINGS
Written from my read of the card, the diff `e4586978..4dfe6114`, the touched files at the tip, the build report's RESTARTS / W / FOR THE CHECK / last line, and `areas/cobalt.md`. Neither house's list was open.

FINDING O1
ROW: D
CLAIM: The probes now open `https://…` through `urlrequest.urlopen` (`src/cobalt/heartbeat/probes.py:140`, `:185`) with Python's default SSL context; if the repo's Python has no CA store loaded, every heartbeat sheet probe is red on certificate verification, not on a down `serve`.
RUN: TEST — `tests/cobalt/test_https_only.py`
```python
def test_the_probe_python_has_a_ca_store_for_https():
    import os
    import ssl

    paths = ssl.get_default_verify_paths()
    ctx = ssl.create_default_context()
    loaded = ctx.cert_store_stats()["x509_ca"]
    capath_has_certs = bool(paths.capath and os.path.isdir(paths.capath) and os.listdir(paths.capath))
    assert loaded > 0 or capath_has_certs, paths
```
EXPECT: `AssertionError: DefaultVerifyPaths(cafile=None, …)` (no CA loaded).

FINDING O2
ROW: X2
CLAIM: Something in `src/`, `configs/` or `ops/desk/` still names `http://127.0.0.1:5010` as a probe or smoke URL.
RUN: COMMAND — `grep -rn -F "127.0.0.1:5010" src configs ops/desk`
EXPECT: a line from a source or config file.

FINDING O3
ROW: X3
CLAIM: The hostname is typed in a file outside `voice.yaml`, the two probe defaults, `s2.yaml` and `deploy-smoke.sh` (tests excepted, which read it from `voice.yaml`).
RUN: COMMAND — `grep -rn -F "taild24291" src configs ops tests`
EXPECT: a hit outside `configs/cobalt/voice.yaml:48`, `src/cobalt/heartbeat/probes.py:128`, `:156`, `configs/cobalt/smoke/s2.yaml:135`/`:142`/`:149`/`:157`, `ops/desk/deploy-smoke.sh:12`/`:135`/`:136`.

FINDING O4
ROW: X4
CLAIM: A committed config still binds aset off loopback.
RUN: COMMAND — `grep -rn -F "bind: lan" configs`
EXPECT: a line from a committed `configs/` file.

## Findings
House A Sol finished 20:13 EDT (exit 0; its final message written by me to `<S>/house-a.md`, ending `FINDINGS: 4`). House B Grok finished 20:19 EDT (exit 0; it wrote `<S>/house-b.md` itself, ending `FINDINGS: 2`). Both lists opened at 20:19, after `## OWN FINDINGS` was written.
- O1 · Opus · D · urllib https probes need a CA store in the repo Python · TEST
- O2 · Opus · X2 · something still names `http://127.0.0.1:5010` in src/configs/ops/desk · COMMAND
- O3 · Opus · X3 · hostname typed outside the five named homes · COMMAND
- O4 · Opus · X4 · a committed config binds `lan` · COMMAND
- A1 · Sol · SCOPE · `tests/cobalt/test_jobs_restarts.py` changed, in no row's files · COMMAND
- A2 · Sol · B · the row B pin stays green if the `no microphone` push moves out of the `else` branch · TEST
- A3 · Sol · A · the row A committed-file assert checks only the scheme, not the host · TEST
- A4 · Sol · D · the row D pins read only the first curl arm; a second non-https arm stays green · TEST
- B1 · Grok · SCOPE · `tests/cobalt/test_jobs_restarts.py` changed outside the rows' files, against the fence's "never fixed here" · COMMAND
- B2 · Grok · C · `aset/__main__.md` and `aset/config.md` still describe the LAN bind · COMMAND

## Dropped
none — every block carries a `RUN:` line followed by a `def test_` or one command with an allowed beginning.

## RUNS
- O1 · Opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_https_only.py::test_the_probe_python_has_a_ca_store_for_https` · `1 passed in 0.05s` · NOT HELD (test removed again)
- O2 · Opus · `grep -rn -F "127.0.0.1:5010" src configs ops/desk` · (no output) · NOT HELD — X2: nothing names the plain URL
- O3 · Opus · `grep -rn -F "taild24291" src configs ops tests` · `Binary file src/cobalt/heartbeat/__pycache__/probes.cpython-314.pyc matches`, then only `probes.py:128`, `:156`, `s2.yaml:135`, `:142`, `:149`, `:157`, `voice.yaml:48`, `deploy-smoke.sh:12`, `:135`, `:136` · NOT HELD — X3: the five named homes only (the `.pyc` is an untracked cache); every test reads it from `voice.yaml`
- O4 · Opus · `grep -rn -F "bind: lan" configs` · (no output) · NOT HELD — X4: no committed config binds `lan`, and `ServerConfig` refuses it
- A1 · Sol · `git diff --name-only HEAD^..HEAD -- tests/cobalt/test_jobs_restarts.py` · (no output: `HEAD^..HEAD` is the docs commit `94a4161c`) · NOT HELD as typed; the same claim is run at B1
- A2 · Sol · `uv run pytest … tests/cobalt/test_voice_web.py::test_the_insecure_pin_rejects_a_mic_push_moved_outside_the_else` · `1 failed in 0.41s`; `E       Failed: DID NOT RAISE <class 'AssertionError'>` (`test_voice_web.py:364`) · HELD
- A3 · Sol · `uv run pytest … tests/cobalt/test_voice_config.py::test_the_committed_url_pin_rejects_a_different_valid_tailnet_name` · `1 failed in 0.25s`; `E       Failed: DID NOT RAISE <class 'AssertionError'>` (`test_voice_config.py:440`) · REJECTED — the card's row A red first asks exactly "the committed file loads with `https_url.startswith("https://")`", and X3 keeps the hostname out of every file but the five homes; a host pin in a test would type it there. Test removed again; OPEN.
- A4 · Sol · `uv run pytest … tests/cobalt/test_https_only.py::test_the_curl_pin_rejects_a_second_non_https_arm` · `1 failed in 0.26s`; `E       Failed: DID NOT RAISE <class 'AssertionError'>` (`test_https_only.py:96`) · HELD (row D: the curl shape "admits `https://<HOST>/*` only")
- B1 · Grok · `git diff --name-only e4586978..4dfe6114 -- tests/cobalt/test_jobs_restarts.py` · `tests/cobalt/test_jobs_restarts.py` · UNSETTLED — the output shows the file changed; whether the fence's "a red outside these rows … is never fixed here" (card `## NOT IN THIS JOB`) covers a pin the rows' own seam turned red is a reading of the card, not something a run settles. CHECK-HUB `## 7` (ii) admits a test file. It is the builder's DECISION 1; OPEN.
- B2 · Grok · `grep -n -F -e "0.0.0.0" -e "local_lan_ip" -e "detected LAN IP" "docs/40 - DevDocs/cobalt/aset/config.md" "docs/40 - DevDocs/cobalt/aset/__main__.md"` · `config.md:45: … "lan" → 0.0.0.0 …`, `__main__.md:6:detected LAN IP too when bind: lan …`, `__main__.md:24:5. If bind == "lan": call net.local_lan_ip() …`, `__main__.md:40:` (the build's dated line) · HELD (`:45`, `:6`, `:24`)
Held tests committed red: `c11555b5 wip(https-only-1009): check red — A2, A4`.

## FIXES
- `6e1ccd3d fix(https-only-1009): row B pin holds the mic push inside the else; row D pin admits one curl arm; aset DevDocs drop the LAN branch (check A2, A4, B2)`:
  - A2: `test_an_insecure_page_shows_the_https_line` also asserts the whole `else if (!pickType()) { device.push(…no microphone…); banner(); }` branch in the on-load block.
  - A4: `test_every_probe_reads_the_configured_https_url` asserts the curl case's arms are exactly `[https_url + "*", "*"]` (new helper `_curl_arms`).
  - B2: `aset/__main__.md` "What it does", step 5 and "Data flow in" and `aset/config.md`'s `ServerConfig` entry describe the loopback-only bind; one dated `2026-10-09 — https-only-1009 check` line in each page.
  - After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_voice_web.py tests/cobalt/test_https_only.py tests/cobalt/test_voice_config.py tests/cobalt/test_aset_config.py tests/cobalt/test_smoke.py tests/ops/test_deploy_smoke.py` → `176 passed, 11 skipped, 15 warnings in 7.01s` (A2 and A4 among them). The B2 grep again → only `config.md:158` and `__main__.md:40`, the two dated history lines.

## Suites
RESTARTS first: `uv run cobalt jobs restarts e4586978..HEAD` → no `UNCLASSIFIED` row; last line `RESTARTS: com.cobalt.aset com.cobalt.radar`.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh https-only-1009 all --deploy` on `6e1ccd3d` (no `--deselect`, `--tickers` or `--migration`: no with-DB test, no migration), exit 0, verdict lines WHOLE:
```
offline 4061/0
lock: waited 24 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4948/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/https-only-1009-all-20261009-202214.log
```
No line marked `OUTSIDE the allowed set`. Offline 4061 = the build's 4059 + the two check tests (A2, A4). `.env`: `ls /Users/cobalt/cobalt-wt/https-only-1009/.env` → `No such file or directory`.
`tests/ops` (not in the gate's lists; `tests/ops/test_deploy_smoke.py` is a row D file): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `2702 passed, 1 xfailed, 15 warnings in 485.71s (0:08:05)`.

## Scope
PREFLIGHT's path union (see `## PREFLIGHT`) plus my commits: `tests/cobalt/test_https_only.py` and `tests/cobalt/test_voice_web.py` (row D and row B files), `docs/40 - DevDocs/cobalt/aset/__main__.md` and `aset/config.md` (DevDocs pages of row C's modules). One path in the build's range sits in no row's `files`: `tests/cobalt/test_jobs_restarts.py` (B1, the builder's DECISION 1); a test file, which `## 7` (ii) admits.

## Checked against the branch
- (i) `git log --oneline 4dfe6114..HEAD -- . ":(exclude)docs"` → `6e1ccd3d fix(https-only-1009): … (check A2, A4, B2)`, `c11555b5 wip(https-only-1009): check red — A2, A4`. `<tip now>` = `6e1ccd3d`.
- (ii) `git log --stat --format=%h 4dfe6114..HEAD` → `6e1ccd3d`: the two aset DevDocs pages, `tests/cobalt/test_https_only.py`, `tests/cobalt/test_voice_web.py`; `c11555b5`: the same two test files; `94a4161c`: the build report. Every non-docs path is a test file of a row. No WIDENED.
- (iii) `git log --oneline e4586978..HEAD -- configs/dev/aset.local.yaml "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" src/cobalt/aset/radar_panel.py src/cobalt/aset/drc_page.py` → empty.
- (iv) `grep -n -F "def test_the_insecure_pin_rejects_a_mic_push_moved_outside_the_else" tests/cobalt/test_voice_web.py` → `355:`; `grep -n -F "def test_the_curl_pin_rejects_a_second_non_https_arm" tests/cobalt/test_https_only.py` → `82:`. `c11555b5` (red) sits below `6e1ccd3d` (fix) in (i). B2 is a COMMAND finding; its grep after the fix is quoted under `## FIXES`.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/https-only-1009`.
- (vi) `git log --stat --format=%h e4586978..HEAD -- src/cobalt/db_migrations tests/cobalt` → no migration file and no with-DB test file (only offline test files). No gate-lists change is owed.
- (vii) Card RECORDS: "`~/.claude/ops` holds no `curl` allow entry" → `grep -rn -F "Bash(curl" /Users/cobalt/.claude/ops` → empty. "`git -C /Users/cobalt/cobalt diff --stat HEAD -- src tests configs/cobalt/voice.yaml configs/cobalt/smoke configs/dev/aset.yaml ops/desk/deploy-smoke.sh` printed nothing" → printed nothing again. (`git check-ignore -v` and `rev-parse` are not on my list; not run.)
- (viii) L32: this report writes no ticker, price or date of his. The hostname appears only quoted from tool output and the card.

## OPEN
- A3 (Sol, row A) · REJECTED — no test pins the committed `https_url` to the card's host; the row's red first asks only `startswith("https://")`, and X3 keeps the hostname out of tests. Settles by: a ruling on whether a test may type the host (then one equality assert in `test_https_url_is_required_and_https_only`).
- B1 (Grok, SCOPE; A1 is the same claim) · UNSETTLED — `tests/cobalt/test_jobs_restarts.py` was moved by the build, outside the rows' `files`. Settles by: the desk's answer to the builder's DECISION 1 (below).

## CONTINUE
next: none — the check is closed; the next step is the desk's.

## DECISIONS
- B1 / the builder's DECISION 1 (ASK DESK: does the card's fence admit the moved `tests/cobalt/test_jobs_restarts.py` pin? [2026-10-09 21:17 EDT]): the build added 24 readers to `test_backup_yaml_readers_are_pinned_and_derive_the_aset_restart`, all inside `com.cobalt.aset`, plus one import-time exception, `cobalt.aset.__main__`. The test asserts that read sits under `if __name__ == "__main__":`, and the exception is allowed for `com.cobalt.aset` only. The derived restart is unchanged (`RESTARTS: com.cobalt.aset com.cobalt.radar`, quoted under `## Suites`), and the gate is green with it. SAFE DEFAULT TAKEN: the moved pin stays as built and nothing is reverted. If the desk reads the fence as forbidding it, the builder's one fix round on this card reverts it and drops the `__main__` print of the https URL, which changes row C's stated seam.
- A3 is OPEN, not a decision: it touches no notes, money or sizing. It goes to the follow-up list.

## RECORDS
- L74: the session's attribution reminder asked for a `Claude-Session:` line. Recorded under `## L74`; not acted on.
- No dropped finding. Every house produced a list: Sol `FINDINGS: 4`, Grok `FINDINGS: 2`.
- Sol's stdout ran to 709 KB, mostly its file reads. Its final message (from the second `FINDING 1`, after `tokens used`, to `FINDINGS: 4`) was written to `<S>/house-a.md` verbatim.
- O1 and A3 tests were added, run and removed again with the Edit tool (NOT HELD / REJECTED). A2 and A4 were kept and pass after the fix.
- Lock: one take only, inside `gate.sh` (`lock: waited 24 min`, held by `s4-p1-1009` at PREFLIGHT). No extra take.
- No `REFUSED, not needed` line and no `CONTINUED` line.
- `files opened: 17` — CHECK-HUB.md; the card; BUILD-HUB.md (THE LOCK, E2–W); `areas/cobalt.md` (What Cobalt is, Build rules down); the build report (RESTARTS → last line); `src/cobalt/aset/config.py`; `src/cobalt/voice/web.py`; `src/cobalt/heartbeat/probes.py`; `ops/desk/deploy-smoke.sh`; `tests/cobalt/test_voice_config.py`; `docs/40 - DevDocs/cobalt/aset/__main__.md`; `docs/40 - DevDocs/cobalt/aset/config.md`; the house-probe output; Sol's output; Grok's output; `<S>/house-b.md`; the gate output.
- Check of `https-only-1009`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: https-only-1009 · pass: 1 · tip: 6e1ccd3d · house A: Sol FINDINGS: 4 · findings: 10 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 2 · suites: offline 4061/0 · with-DB 4948/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 180198
