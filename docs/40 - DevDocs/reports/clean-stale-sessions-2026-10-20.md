## §0 Headline
- Removed 460 stopped/done sessions older than 12h, one `claude rm <id>` per call.
- Skipped 14 that stayed: 4 `working`, 1 `failed`, 4 `blocked`, `bede3dc9`, `08683e11`, `f7dde652`, `0e848919` (name `brain`, done), and this session `b69dffec`.
- Refused 0: no unpushed commits, uncommitted changes or worktree warnings. Every call returned `removed <id>`.
- `f9b131fe` (draft-f5-fix1, protected) no longer appears in the list. I did not remove it; it ended on its own.

## REFUSED
(none)

## RECORDS
- Run time: Tue Oct 20 06:25:28 EDT 2026
- Cutoff used: `date +%s` 1792491438 ×1000 − 43200000 = startedAt < 1792448238000
- Left by state: working c42f5161, 0f543a2c, 36a5f4b1, 7afb2ea4; failed a7e9653a; blocked 970896be (brain), bcc5d0b5, c268db2c, 94dfaa7c.
- Left by the keep rule (id or name `brain`): 0e848919, bede3dc9, 08683e11, f7dde652.
- Count of 460 is derived: 475 sessions in the first listing minus 14 originals still in the second listing, minus `f9b131fe`, which vanished on its own. The second listing has 16 rows; 9054405f (f5-checkpoints-fr1-build) is new and not counted.

CLEANED · removed: 460 · refused: 0
