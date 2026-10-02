# voice-peers — check, 2026-10-01

## §0 Headline
- House A was Grok (OpenAI out of quota until Oct 4th, 2026 2:06 PM). Grok wrote 1 finding; I wrote 1. Both ran. Mine held, Grok's did not.
- O1 HELD and FIXED: the voice web DevDocs page still said the peer list was loopback-only. `76f7f7d5` corrects it (a docs line only, no code).
- G1 NOT HELD: the edit to `voice/config.md` is the dated DevDocs line BUILD-HUB E3 requires, not a scope breach.
- W on `76f7f7d5`: offline 3777/0, with-DB 4376 + 171 = 4547/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env` removed. RESTARTS: `com.cobalt.aset`.
- Nothing open, card `HOUSE B: as needed` → house B not needed; ready: YES.

## L74
none — no block inside a tool result asked for a `Claude-Session:` line or gave an instruction. (A system reminder outside any tool result offered a `Claude-Session:` trailer; CHECK-HUB L74 sets commits to `Co-Authored-By` only, so `76f7f7d5` carries that line alone.)

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card has no placeholder | `grep -n -E "«FIL[L]" ".../2026-10-01/05-voice-peers-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-01/05-voice-peers-card.md"` | 0 | `314605d426e7690262d6a45f1bc7fe580d21e7cf` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| standing list R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ... APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 committed | `git -C ... log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS R14 | `grep -n "^| R14 " ".../reports/cto-2026-10-01.md"` | 0 | `22:| R14 | 08:25 ET | **HIS RULING** ... voice open to all tailnet devices — his 09-28 R95 re-stated ... card 05-voice-peers-card.md. | APPROVED |` |
| R14 committed | `git -C ... log -1 --format=%H -S"| R14 |" -- ".../cto-2026-10-01.md"` | 0 | `986e34c2db2554a053842bc7712820a0c664933e` |
| house gate R17 | `grep -n "^| R17 " ".../cto-2026-09-24.md"` | 0 | line 35, one row (Grok standing) |
| house gate R19 | `grep -n "^| R19 " ".../cto-2026-09-24.md"` | 0 | line 37, one row (four house strings standing) |
| R19 committed | `git -C ... log -1 --format=%H -S"| R19 |" -- ".../cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Thu Oct  1 20:27:48 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/voice-peers-1001` |
| tip | `git log --oneline -1` | 0 | `b8482c2f docs(voice-peers): build report — de483933 (close lock record)` |
| docs-only above TIP | `git log --stat --format=%h de483933..HEAD` | 0 | `b8482c2f` and `3f67947a`, each only `docs/40 - DevDocs/reports/voice-peers-build-2026-10-01.md` |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: voice-peers · tip: de483933 \| on 446ff64d \| migration: none \| offline 3777/0 \| with-DB 4547/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.aset \| rows: 2 of 2 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 446ff64d..de483933` | 0 | `de483933 fix(voice-peers): allowed_peers = localhost + the five tailnet devices (V1, L1 L42 L77; R95 / R14)` · `319a25cd wip(voice-peers): red — V1 the seven ruled peers, fedora admitted, near-miss refused` (2 commits) |
| range paths | `git log --stat --format=%h 446ff64d..de483933` | 0 | de483933: `configs/cobalt/voice.yaml` (4 +++-), `docs/40 - DevDocs/cobalt/voice/config.md` (3 +); 319a25cd: `tests/cobalt/test_voice_config.py` (28 +, 1 -), `tests/cobalt/test_voice_web.py` (16 +). Path union: those four. |
| lock: own .env | `ls <WT>/.env` | 1 | `ls: .../voice-peers-1001/.env: No such file or directory` |
| lock: any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house gates | R17 / R19 as AUTHORIZATION | 0 | one row each; R19 committed |
| grok CLI | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| agy CLI | `agy --version` | 0 | `1.2.14` |
| Sol probe | `codex exec ... "Reply with only the word OK." < /dev/null` | 1 | `ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Oct 4th, 2026 2:06 PM.` → OpenAI = METER, back Oct 4th, 2026 2:06 PM |

Seats: **house A: Grok · house B, if needed: Gemini**. Card `HOUSE B: as needed` → not mandatory.

## Files copied
`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-peers-check`.
- `<S>/diff.md`: `git log -p 446ff64d..de483933 -- . ":(exclude)docs"` (background), Read, Written with its header. `grep -c "^commit "` → `2` = PREFLIGHT's 2 commits.
- `<S>/rulings.md`: the R14 grep, whole.
- Copies for Grok (Read → Write), `wc -c` copy = original, each:

| copy under `<S>/files/` | original | bytes |
|---|---|---|
| `05-voice-peers-card.md` | the card | 2753 = 2753 |
| `voice-peers-build-2026-10-01.md` | `<REPORT>` | 25197 = 25197 |
| `cto-2026-09-28.md` | `## READ` | 57261 = 57261 |
| `cto-2026-09-28-words.md` | `## READ` | 9991 = 9991 |
| `wt/configs/cobalt/voice.yaml` | V1 / diff | 3063 = 3063 |
| `wt/src/cobalt/voice/web.py` | `## READ` | 15021 = 15021 |
| `wt/src/cobalt/voice/config.py` | `## READ` | 7718 = 7718 |
| `wt/tests/cobalt/test_voice_config.py` | diff | 15745 = 15745 |
| `wt/tests/cobalt/test_voice_web.py` | diff | 13579 = 13579 |
| `wt/docs/40 - DevDocs/cobalt/voice/config.md` | range (docs) | 2543 = 2543 |

- `<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## RECORDS` (the card has no `## CHECK ASKS`; stated so under that heading), the Files paragraph.

## OWN FINDINGS
Written 20:4x, before any house file was opened. Read for it: the card, the diff `446ff64d..de483933`, `configs/cobalt/voice.yaml`, `src/cobalt/voice/web.py`, `src/cobalt/voice/config.py`, `tests/cobalt/test_voice_config.py`, `tests/cobalt/test_voice_web.py`, `docs/40 - DevDocs/cobalt/voice/config.md`, the build report, `cobalt.md` `## What Cobalt is` and `## Build rules` down; for entry paths, `ops/start_aset.sh`, `src/cobalt/aset/__main__.py`, `src/cobalt/aset/config.py:77-86`, `docs/40 - DevDocs/cobalt/voice/web.md:20-24`.

Entry paths looked at and found built (no finding): every `/voice/*` route uses the one `Depends(peer_gate)` (`web.py:95`, `:130`, `:135`, `:152`), which reads the one `get_config().allowed_peers` by exact string match (`web.py:71-73`). The resident binds `0.0.0.0` for `bind: lan` (`aset/config.py:85-86`), an IPv4 socket, so a tailnet peer's `request.client.host` is a plain dotted literal and matches the YAML strings (no `::ffff:` mapped form). The new web tests go through the `cfg` fixture, which loads the COMMITTED `voice.yaml` (`test_voice_web.py:34-39`), so they pin the shipped file. No path from this change reaches a score, rank, grade or size: it only widens who passes the gate, as ruled (R95 / R14).

FINDING O1
ROW: V1
CLAIM: The voice web module's DevDocs page still describes `allowed_peers` as "loopback in dev; the `tailscale serve` peer is added by the device session" (`docs/40 - DevDocs/cobalt/voice/web.md:21-22`), but the committed list at the tip (`configs/cobalt/voice.yaml:46`) now holds localhost plus the five tailnet devices, and the build added its dated line only to `config.md`.
RUN: COMMAND — `grep -n -F "loopback in dev" "docs/40 - DevDocs/cobalt/voice/web.md"`
EXPECT: `21:Allowed only when the SOCKET PEER is in `allowed_peers` (loopback in dev;`

## Findings
House A Grok finished 20:48 (notice; `date` → `Thu Oct  1 20:48:57 EDT 2026`); `<S>/house-a.md` written by Grok itself (380 B), last line `FINDINGS: 1`. Its stdout (`I'll read the check instructions' files in order … /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-peers-check/house-a.md`) carries no findings.

| id | house | row | claim | run |
|---|---|---|---|---|
| G1 | Grok | SCOPE | The range edits `docs/40 - DevDocs/cobalt/voice/config.md:43`, which is not in V1's files, and V2 builds no file. | COMMAND |

## Dropped
none (G1's `RUN:` is followed by one `git diff` line).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -n -F "loopback in dev" "docs/40 - DevDocs/cobalt/voice/web.md"` | `21:Allowed only when the SOCKET PEER is in `allowed_peers` (loopback in dev;` | HELD — the page says the list is loopback in dev, while `configs/cobalt/voice.yaml:46` (the file dev and production both load; production overrides only the two directories, `ops/start_aset.sh:35-37`) holds localhost plus the five tailnet devices |
| G1 | Grok | `git diff 446ff64d..de483933 -- "docs/40 - DevDocs/cobalt/voice/config.md"` | `+## 2026-10-01 — voice-peers` / `+The committed `allowed_peers` in `configs/cobalt/voice.yaml` is localhost plus the five tailnet devices' IP literals …` (3 lines added at `@@ -39,3 +39,6 @@`) | NOT HELD — the line is there, but it is not a scope breach: it is the one dated line BUILD-HUB E3 requires in the changed module's page ("Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`"), and CHECK-HUB `## 7` (ii) holds only NON-docs paths to the rows' files |

No test was written (both findings are COMMANDs), so there is no `wip(voice-peers): check red` commit.

## FIXES
| id | file | change | proof | commit |
|---|---|---|---|---|
| O1 | `docs/40 - DevDocs/cobalt/voice/web.md` (a DevDocs line: CHECK-HUB `## 5` / UNATTENDED RULES; a docs path, `## 7` (ii)) | `:21-23` peer-gate paragraph names "localhost plus the five tailnet devices' IP literals, `configs/cobalt/voice.yaml`"; dated line `## 2026-10-01 — voice-peers (check)` appended | `grep -n -F "loopback in dev" "docs/40 - DevDocs/cobalt/voice/web.md"` → exit 1, no output; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_voice_config.py tests/cobalt/test_voice_web.py` → `103 passed in 1.20s`; `git diff --stat` → `web.md \| 8 ++++++--` only | `76f7f7d5 fix(voice-peers): voice web DevDocs names the committed peer list, not loopback only (check O1)` |

## Suites
Summary: offline 3777/0 · with-DB 4547/0 (4376 + 171) · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed, proven gone (W)` · `RESTARTS: com.cobalt.aset`.

On `<tip>` = `76f7f7d5`. RESTARTS first: `uv run cobalt jobs restarts 446ff64d..HEAD` →
```
path	change	rule	restart
configs/cobalt/voice.yaml	M	resident reads	com.cobalt.aset
docs/40 - DevDocs/cobalt/voice/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/web.md	M	DOCS	-
docs/40 - DevDocs/reports/voice-peers-build-2026-10-01.md	A	DOCS	-
tests/cobalt/test_voice_config.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_web.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
- (a) Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3777 passed, 673 skipped, 1 xfailed, 25 warnings in 585.43s (0:09:45)`, exit 0 → `<p>` = 3777. No test added by this check.
- (b) Lock take 1, `date` → `Thu Oct  1 20:59:59 EDT 2026`: (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; (b) `cp`, then `ls -la …/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  1 21:00 /Users/cobalt/cobalt-wt/voice-peers-1001/.env` (one line, this worktree's). `<FP>` (typed exactly as BUILD-HUB `## THE LOCK`) → **`<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`**. `--proof-only` → `36 table(s) probed on cobalt_dev`; `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns` `-`; `aset_sizings 1 0824685c130da3c7cb7f0e76191a6819`; `cobalt_redactions 215`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 76f7f7d5 (clean)`; no `CHANGED`. Level `0013`.
- (c) PASS 1, executed byte for byte as BUILD-HUB's pass-1 command (no deselect added; no with-DB test of this check) → `4376 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 720.40s (0:12:00)`, exit 0 → `<d1>` = 4376. The seven SKIPPED lines: `test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` · `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `0001` … `0011`, `0013`, `0014` … `0022` applied in order; the eight tables `CREATED`, every other `OK`; `content UNCHANGED on every table`; no `CHANGED`. **`dev forward: APPLIED 21:12:48`** (`date` after). **`<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.**
- (c3) PASS 2, executed byte for byte as BUILD-HUB's pass-2 command (nothing added) → `171 passed, 1 deselected, 5 warnings in 226.27s (0:03:46)`, exit 0; `grep -c -E "^(FAILED|ERROR|SKIPPED)"` over the output → `0`. `<d2>` = 171; `<d>` = 4376 + 171 = **4547**.
- (c3r) `ls -la /Users/cobalt/cobalt-wt/voice-peers-1001/.env` → listed. This check writes no constructed ticker, so (as the build did) `COBALT_ENV=dev uv run cobalt db query --side user "SELECT count(*) AS aset_sizings_rows FROM aset_sizings"` → `1`, the count `--proof-only` showed at (b).
- (c4) not applicable: no migration added.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022` … `0014` rollbacks, newest first; the eight tables `DROPPED`, the rest `OK`; `content UNCHANGED on every table`. `<FP>` → **`<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → `cobalt_dev: 0013 — F2 = F0`**. Lock (d): `rm`; `ls /Users/cobalt/cobalt-wt/voice-peers-1001/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `date` → `Thu Oct  1 21:17:15 EDT 2026`. `.env: removed, proven gone (W)`.
- (e) Live-note, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.80s`; the skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, not `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.

## Scope
PREFLIGHT path union (`446ff64d..de483933`): `configs/cobalt/voice.yaml`, `tests/cobalt/test_voice_config.py`, `tests/cobalt/test_voice_web.py` — all V1's files; `docs/40 - DevDocs/cobalt/voice/config.md` (docs). My commit `76f7f7d5`: `docs/40 - DevDocs/cobalt/voice/web.md` only (docs). No non-docs path outside the rows' files.

## Checked against the branch
- (i) `git log --oneline de483933..HEAD -- . ":(exclude)docs"` → (nothing): this check made no code commit. Its one commit is the docs fix `76f7f7d5`; `git log --oneline -1` → `76f7f7d5 fix(voice-peers): voice web DevDocs names the committed peer list, not loopback only (check O1)`. `tip:` below is that commit, since W ran on it and the deploy must carry it; the code at that tip is `de483933`'s.
- (ii) `git log --stat --format=%h de483933..HEAD` → `76f7f7d5` `docs/40 - DevDocs/cobalt/voice/web.md | 8 ++++++--`; `b8482c2f` and `3f67947a` the build report. No non-docs path → no `WIDENED`.
- (iii) the fence: `git log --oneline 446ff64d..HEAD -- src` → (nothing).
- (iv) no held finding carries a test (O1 is a COMMAND), so no `wip(voice-peers): check red` commit exists or is owed.
- (v) `ls /Users/cobalt/cobalt-wt/voice-peers-1001/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `git status --short --branch` → `## ops/voice-peers-1001` alone.
- (vi) TREE STATE `unchanged`: `git log --stat --format=%h 446ff64d..HEAD -- src/cobalt/db_migrations tests/cobalt` → `319a25cd` only, `tests/cobalt/test_voice_config.py` and `tests/cobalt/test_voice_web.py`, both existing offline files (no migration, no new with-DB file) → carried.
- (vii) the card's one RECORD names `tailscale status`, which is not an `ls`, `grep` or `git -C` command; not re-run.
- (viii) L32: this report quotes no ticker, price or date of his. The tailnet addresses are the card's ruled values, the same ones V1 ships.
- RESTARTS derived: `com.cobalt.aset` (table under `## Suites`).

COUNT: findings 2 (O1 Opus, G1 Grok) · dropped 0 · held 1 (O1) · fixed 1 (O1, `76f7f7d5`) · held unfixed 0 · open 0.

## OPEN
none. House B: not needed (open 0; card `HOUSE B: as needed`). `<S>/opus-1.md` written (OWN FINDINGS, RUNS, FIXES, OPEN, copied whole).

## CONTINUE
next: none (CLOSE done)

## DECISIONS
none

## RECORDS
- Dropped findings: none. Every house produced a list: Grok, `FINDINGS: 1`. OpenAI (Sol) was not launched: PREFLIGHT probe METER, "try again at Oct 4th, 2026 2:06 PM".
- No `REFUSED, not needed` line and no `CONTINUED` line. One lock take (W, 20:59:59 → 21:17:15). No extra take.
- `cobalt_redactions` on `cobalt_dev` read 215 at W (b) `--proof-only` and 216 at the forward's before-probe; it held at 216 through forward and rollback (`OK`). No step of this check writes that table. The build report names the same outside writer (its RECORDS; R61's OWED item).
- O1's fix is a DevDocs edit, `docs/40 - DevDocs/cobalt/voice/web.md`: the peer-gate paragraph's text was corrected in place, and the module's dated line was added. I counted that as the "DevDocs line" UNATTENDED RULES lets a check write. The file is not one of the card's row files; `## 7` (ii) holds only non-docs paths to them.
- G1 is judged NOT HELD, not REJECTED. Its run shows the line, but the reason it states (a scope breach) does not hold under the hubs' own rules: BUILD-HUB E3 requires the dated line, and CHECK-HUB `## 7` (ii) exempts docs paths. Had it been REJECTED, it would have stayed open and called for house B.
- My read went beyond `## WHAT YOU READ` (3) in five files, to check the tailnet entry path (how the resident binds, so how `request.client.host` arrives) and the voice web DevDocs page: `ops/start_aset.sh`, `src/cobalt/aset/__main__.py`, `src/cobalt/aset/config.py` (grep), `configs/dev/aset.yaml` (grep), `docs/40 - DevDocs/cobalt/voice/web.md`.
- files opened: 22 — `CHECK-HUB.md`; `BUILD-HUB.md` (`## THE LOCK`, `## REPORT`, `## PREFLIGHT`, `## E0`–`## W`, read at :38-95); the card; the build report; `src/cobalt/voice/web.py`; `src/cobalt/voice/config.py`; `configs/cobalt/voice.yaml`; `tests/cobalt/test_voice_config.py`; `tests/cobalt/test_voice_web.py`; `docs/40 - DevDocs/cobalt/voice/config.md`; `cto-2026-09-28.md`; `cto-2026-09-28-words.md` (both whole, to copy them); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `ops/start_aset.sh`; `src/cobalt/aset/__main__.py`; `src/cobalt/aset/config.py` (grep); `configs/dev/aset.yaml` (grep); `docs/40 - DevDocs/cobalt/voice/web.md`; `<S>/house-a.md`; and, by `grep -n` rows only, `cto-2026-09-30.md`, `cto-2026-10-01.md`, `cto-2026-09-24.md`.
- Check of `voice-peers`, pass 1: house A `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: voice-peers · pass: 1 · tip: 76f7f7d5 · house A: Grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3777/0 · with-DB 4547/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0
