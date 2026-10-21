# draft-cos-tunables-fr1 — 2026-10-20

## §0 Headline
Card 933 now has fix-round row FR1 (FR-1 admit the sheet-daymode test stub; FR-2 an unreadable owed file makes `cos`/`hitl` red with the error, never a raise in `take_beat`).
`BAND:` set to `HIGH`; one `## CHECK ASKS` line added (job `cos-tunables-fr1`, scoped to FR1); the verbatim RECORDS line added.
Card edited in place, nothing committed, nothing run.

## DECISIONS
1. ASK DESK: the card's `## ROWS` intro and P1 text still say "raises"; FR1 says it supersedes them but I did not rewrite P1. Default: leave as context. [20:20]
2. ASK DESK: the old `probes.md` line "`BootstrapOwedError` is not caught" (`:149`) is left; the builder's dated FR1 line supersedes it. Default: as written. [20:20]

## RECORDS
- 2026-10-20 20:18 EDT (`date`). `ops/cos-tunables` = `ace7a92a`, the checked tip, so FR-1's byte-equality proof is trivially true at the tip; the builder re-runs it on its own tip.
- Read: prompt 949; card 933 whole; check report whole; `git show ops/cos-tunables:` `probes.py`, `test_cos_probes.py`, `probes.md`; `git grep` on `runner.py:127,150-151` and `watchdog.py:59-82`.
- Edited only the card (BAND, row FR1, CHECK ASKS line, two RECORDS lines). One Bash call with a redirect was refused by the bare-guard hook and redone with Edit.

DRAFTED · decisions: 2
