## §0
- Rows cut: 142 of 182 §4 rows in `reports/cto-2026-09-28.md`; 40 rows at ≤300 stay byte for byte. `git diff --numstat`: 142 lines added, 142 removed, no other line changed.
- Bytes: 109,900 → 57,503. Rows over 300: 0.
- Literals kept: 54 distinct strings; every grep re-run prints its row. Full rows: `reports/_archive/cto-2026-09-28-rows-full.md` (183 lines, each equal to a line of the original).
- Every id, hash, file name, HIS marker and `words ## R<n>` link stays in its row.

## PREFLIGHT
- date: Tue Sep 29 19:34:50 EDT 2026
- ls reports: prints; `cto-2026-09-28.md`, `cto-2026-09-28-words.md` and `_archive` path present
- wc -c TARGET: 109900
- grep -c -F "| R" TARGET: 189
- tail -n 1 TARGET: `HANDOVER: predecessor f030d47a → successor e41f7813 at 22:38 ET`
- git log -1 --oneline: `37612b74 docs(desk): 09-29 R134 desk-rows cleanup prompt 28 + launch row`
- AUTHORIZATION: `grep -n "^| R134 "` on `cto-2026-09-29.md` prints line 142; `git log -1 --format=%H -S"| R134 |"` prints `37612b74f9eff34f63a6f624de87a9a894ab6ead`.

## Literals
Grep of `prompts/2026-09-28/` and `prompts/2026-09-29/` for `cto-2026-09-28.md`; `prompts/2026-09-30/` absent.

| prompt | string | row |
|---|---|---|
| launch-row checks in `2026-09-28/06`–`61` and `2026-09-29/*` | `grep -n -F "| R27 |"`, `"| R28 |"`, `"| R29 |"`, `"| R35 |"`, `"| R108 |"`, `"| R123 |"`, `"| R128 |"`, `"| R167 |"`, `"| R175 |"`, `"| R179 |"` | R27 R28 R29 R35 R108 R123 R128 R167 R175 R179 |
| same | `grep -n "^\| R<n> "` for n = 2 4 26 38 43 61 93 102 124 138 151 159 | same rows |
| `2026-09-28/*`, `2026-09-29/*` | `continue with development process` | R26 |
| `2026-09-28/02` | `change the laws that are stopping this`, `need to have no bloat` (`-S`) | R2, R4 |
| launch prompts with a stagger gate | `no other house hub is running` | R8 R47 R67 R75 R82 R90 R119 R133 R147 R152 R155 R159 R174 R178 |
| each launch prompt | its own file name, for the 28 files: `01-shrink-propose-and-draft` `02-shrink-tribunal` `03-shrink-tribunal-anthropic-seat` `04-shrink-derive` `05-shrink-prechecks` `13-s3-exits-astra-read` `14-draft-drc-merge-main` `15-drc-merge-main-build` `16-draft-drc-merge-fix-r1` `17-drc-merge-fix-r1-build` `28-draft-s3-exits-c1-fix-r1` `31-draft-drc-merge-fix-r2` `32-drc-merge-fix-r2-build` `34-draft-s3-exits-c1-fix-r2` `37-draft-drc-merge-fix-r3` `38-drc-merge-fix-r3-build` `40-radar-no-cards-read` `41-draft-drc-merge-fix-r4` `42-drc-merge-fix-r4-build` `44-radar-no-cards-read-2` `46-radar-stop-record-build` `49-draft-radar-stop-record-fix-r1` `50-radar-stop-record-fix-r1-build` `51-radar-stop-record-fix-r1-check` `52-draft-radar-fix-r1-check-reissue` `53-draft-s3-exits-c2-fix-r1` `56-draft-drc-d2-fix-r2` `60-s2-smoke-look` (`.md`) | its launch row |
| `2026-09-29/*` | R35 gate: row carries `Approved as recomended` and `O5 / O6 = A` | R35 |

## ESCALATE
1. R11 (line 19) carried a stray §5 tail after its status cell (`| OPEN TO HIM | R181 D2 round-3 HOLD 4 … | — | — | — |`). The cut row drops it; it is in the archive. Line 20, the stray `OPEN TO HIM` row, is left unchanged. Desk: remove line 20 or keep it.
2. The R35 row no longer holds C1's two `.env` strings (`Bash(cp … s3-exits-c1/.env)`, `Bash(rm … s3-exits-c1/.env)`). No prompt greps them, but C2–C4 prompts cite "R35 (1)" for the `.env` pair. The archive holds them.

DESK ROWS CLEANUP DONE · rows cut: 142 · over 300 left: 0 · literals kept: 54 · ESCALATE: 2
