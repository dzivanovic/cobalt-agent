# orphan-clean card draft · 2026-10-10

## §0 Headline
- Card `prompts/2026-10-10/229-orphan-clean-card.md` written (10,853 B): 4 rows O1–O4, every row RED on `BASE` with a fake process table and a negative control sparing a healthy resident.
- Script: `ops/desk/orphan-clean.sh <label>` dry run by default; `--kill <label>` signals only a verified ppid-1 `python -m cobalt.aset` that `lsof` proves holds the voice lock or port 5010; TERM, then KILL after 10 s; any unverifiable candidate → exit 1, nothing signalled.
- Widening of CLASS (a) (`2026-10-02 R39`): the first `ops/desk/` script to signal a process it did not start; CLASS (a) would carry it onto every hub line. Owed on his approval: one `STANDING-LIST.md` line naming where `--kill` may run.
- `BASE` left `«FILL»` for the desk; RESTARTS none.

## CHANGES
- NEW `docs/40 - DevDocs/prompts/2026-10-10/229-orphan-clean-card.md`.
- NEW this report.

## DECISIONS
1. Labels: a closed table with `aset` only. Radar (`uv run cobalt radar run`) and agent (`cobalt.sh start` → `uv run src/cobalt_agent/main.py`) do not run as `python -m cobalt.<label>`; a new label is its own card.
2. Proof of holding is `lsof` only (open fd on `/Users/cobalt/.cobalt/voice-scratch/.lock` or LISTEN on `:5010`); the pid inside `.lock` is not proof, since `release` never clears it.
3. The healthy resident is spared two ways: ppid ≠ 1 (today's `uv` child), and pid equal to `launchctl print gui/501/com.cobalt.aset`'s `pid =` (the shape after the orphan-cause card's option (ii)).
4. All or nothing: one unverifiable candidate refuses the whole run.
5. `--kill` escalates TERM → KILL after a 10 s grace, re-reading ppid, start time and command before each signal (R854: 39280 ignored TERM; pid reuse guard).
6. `kill` goes through `${ORPHAN_CLEAN_KILL:-kill}` and the grace through `ORPHAN_CLEAN_GRACE`, both test-only, as `HOUSE_PROBE_LIMIT` is; `ps`, `launchctl`, `lsof` are stubbed on `PATH`.
7. The job does not edit `STANDING-LIST.md`; the widening and the owed line go in the card's `## RECORDS`, default asked: desk settings and the `ops-hand` seat only, never a build, check, devfix or close line.
8. `DB:` omitted per the prompt; the card records that `DB: none` qualifies.

## RECORDS
Every read: `git -C /Users/cobalt/cobalt show d0a5fbb8:<path>` or `git -C /Users/cobalt/cobalt grep -n … d0a5fbb8 -- <path>`, drafter, 07:4x–07:58 EDT 2026-10-10.
- `d0a5fbb8` = Merge branch 'main' into deploy/strike-fallback-env-1010, 2026-10-10 05:13 -0400.
- `ops/desk/` listing: 35 entries; `job-clean.sh` (header, `refuse`, `RUN:` lines), `house-probe.sh` (kills only children it started, lines 92–93), `tests/ops/test_house_probe.py` (PATH stubs, `HOUSE_PROBE_LIMIT`).
- `docs/40 - DevDocs/prompts/STANDING-LIST.md`: line 23 (`launchctl` NEVER on build/check), line 31 (`## CLASSES — approved once, 2026-10-02 R39`), line 36 (CLASS (a) string and "can touch").
- `ops/com.cobalt.aset.plist`: 25 (`start_aset.sh`), 29 (`AbandonProcessGroup`), 42 (`KeepAlive`).
- `ops/start_aset.sh`: 35 (`COBALT_VOICE_SCRATCH_DIR`), 73 (`exec uv run python -m cobalt.aset`).
- `ops/com.cobalt.radar.plist`: 18–22 (`uv run cobalt radar run`). `ops/com.cobalt.agent.plist`: 25 (`cobalt.sh`), 32 (`AbandonProcessGroup`). `cobalt.sh`: 59 (`uv run src/cobalt_agent/main.py`).
- `src/cobalt/voice/scratch.py`: 16 (X-X22), 43 (`LOCK_NAME`), 72 (`ScratchLocked`), 193 (`DirectoryLock`), 212 (`os.pwrite` pid), 225 (`release`). `src/cobalt/voice/web.py`: 161 (lock taken at start).
- `src/cobalt/aset/config.py`: 82 (port 5010); host `127.0.0.1` on loopback.
- `src/cobalt/jobs/restarts.py`: 38, 230–232 (`ops/desk/` → no Cobalt reader) → RESTARTS none.
- `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`: lines 53, 65, 121 spell `launchctl print gui/501/<label>`.
- Working tree (not `d0a5fbb8`): `reports/cto-2026-10-10.md` rows R851, R853, R854, R855, R857; `reports/aset-orphan-answer-2026-10-10.md`; `prompts/CARD.md`; `Memory/topics/writing-rules.md`.
- `wc -c` card: 10,853 B.

ORPHAN CLEAN CARD DRAFTED · decisions: 8
