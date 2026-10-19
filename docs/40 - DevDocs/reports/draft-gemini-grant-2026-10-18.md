# Draft — card gemini-grant-1018 (prompt 799)

## §0 Headline
- Card: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/800-gemini-grant-card.md`, BASE `55d8b50e`, BAND HIGH, uncommitted.
- Rows: P0 (run), G1 add + EXIT trap, G2 serial refusal + orphan sweep + new kind `grant-sweep`, G3 byte-for-byte test, H1 hub `:28` and `:12`, P1 (run).
- The launcher exits at `claude --bg` (`desk-launch.sh:269-285`, `:2443`), so its trap covers only a failed launch; BUILT, FAILED and killed seats are swept by `grant-sweep` or by the next Gemini launch.
- RULINGS carries one `«FILL»`: the desk's HIS RULING row for "A" is not in `cto-2026-10-18.md` yet (decision 1).

## DECISIONS
- ASK DESK: 1 RULINGS row. `grep -n "gemini-grant"` finds only R1943 (LAUNCHED), not a HIS RULING · APPROVED row. Default: the card holds `«FILL: …»`; the desk commits its row and fills it before the preflight (the launcher refuses until then). [20:48]
- ASK DESK: 2 Removal after a launched seat. Default: new kind `desk-launch.sh grant-sweep`, run by the desk once it has closed the seat with `desk-done.sh`, plus the same sweep at every Gemini launch; a killed seat → sweep / next launch, no trap. Alternative: `desk-done.sh` calls the sweep (a second file; left out). [20:52]
- ASK DESK: 3 Live or orphan. Default: a rule `write_file(<WT>/<n>/)` is live when `claude agents --json` holds a row with a pid named `<n>-gate`. This needs JOB = WORKTREE on a Gemini card, so the card adds that refusal (cards 717/718/719 comply). [20:52]
- ASK DESK: 4 An idle gate seat that still has a pid counts as live: the next Gemini launch is refused until the desk closes it (W8 first). Default: yes. [20:52]
- ASK DESK: 5 The file edit is a text edit of one line by inline `python3` (the form of `:2408`), checked with `json.loads` (equal but for the one element), written atomically with the mode kept. An inline allow list, invalid JSON, or an orphan whose removal would change a comma are refused, nothing written. Default: as pinned. [20:52]
- ASK DESK: 6 Where an orphan's removal is recorded. Default: the launcher's stderr `ORPHAN: removed …` line, copied into the desk's §4 row; no log file. [20:52]

## RECORDS
- 20:48 `date`; 20:48 `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `55d8b50e`.
- 20:48 read `git show main:` of `prompts/CARD.md`, `prompts/2026-10-18/787-hub-deferred-card.md` (precedent), `prompts/SHADOW-HUB.md` (GRANT on `:12`, `:28`), `prompts/2026-10-18/759-agy-read-card.md`; `writing-rules.md` (Vault).
- 20:48 `grep -n "gemini-grant" reports/cto-2026-10-18.md` → `:16` R1943 LAUNCHED, `:134` OWED; there is no HIS RULING row.
- 20:49 `git diff main` on SHADOW-HUB.md, desk-launch.sh, cto-2026-10-18.md: only the cto report differs (§5 lines).
- 20:50 `git show main:ops/desk/desk-launch.sh` (whole, saved to the tool-results file): `:222-225` refuse, `:269-285` run_launch, `:358` usage, `:1061-1064` worktree pattern, `:1697-1789` build|shadow arm, `:2322-2443` line and launch; there is no `trap`.
- 20:50 `tests/ops/test_desk_launch_shadow.py` `:95-185`, `:352-471` (grep); `tests/ops/test_shadow_hub_file.py` `:370-410`.
- 20:51 card headers 717/718/719: JOB = WORKTREE in each.
- 20:51 Grep of the repo, excluding reports and dated prompts, for `antigravity-cli/settings.json`: no fixed file names it outside SHADOW-HUB.md (only the launcher and the tests).
- 20:51 settings file, structure only: `grep -n -F '"allow"'` → `5:    "allow": [` (`:4` `"permissions": {`); 20:52 `grep -c` of the 717 grant → `0`.
- 20:52 card written; 20:53 report written. Nothing committed.

DRAFTED · decisions: 6
