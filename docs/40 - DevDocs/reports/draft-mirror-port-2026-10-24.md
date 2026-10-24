# draft-mirror-port — card 1032 radar-mirror-scope-port (2026-10-24)

## §0 Headline
- Card at `prompts/2026-10-23/1032-radar-mirror-scope-port-card.md`: job `radar-mirror-scope-port`, BAND HIGH, BASE `148b03ef` (desk resets), spec `git diff 11ed17b8 25994142` over seven files (312+, 16−).
- All nine spec paths are byte-unchanged on main since `11ed17b8` (revert `41bb2402`): a pure re-application; row P0 re-proves it per file, row E1 proves diff equality per file.
- RESTARTS re-derived `com.cobalt.aset com.cobalt.cos com.cobalt.radar`; DEPLOY PROOF copied from 1020 (ls smoke reads, mapped and admitted); `## GATE` puts the deploy after the K3 restore.
- Four ASK DESK items, each with its default taken.

## DECISIONS
1. ASK DESK: card 1020 has no `CLASS` line to copy. Default: the port card carries none. [19:55]
2. ASK DESK: `RESTARTS` set to the check's tool line `com.cobalt.aset com.cobalt.cos com.cobalt.radar`, not 1020's `com.cobalt.radar`. Default: as written; row R1 is the record. [19:55]
3. ASK DESK: marker 2 `before 0` reads `No such file or directory` on main (test file absent). Default: 1020's line kept; deploy 1027 took absent as valid before. [19:55]
4. ASK DESK: card 1020's suite gains `tests/cobalt/test_radar_replay.py` (the check's A1 fix, a spec file). Default: included. [19:55]

## RECORDS
- Start 2026-10-24 19:54 EDT, card written 19:55 EDT (`date`). Reads only; nothing run, nothing committed, no git write.
- Read: the prompt 1031; `prompts/CARD.md`; card 1020 whole; card 994 whole; `reports/radar-mirror-scope-check-2026-10-23.md` (`## DECISIONS` none, `## RECORDS`, stop line); `git show HEAD:"docs/40 - DevDocs/prompts/BUILD-HUB.md"` (`:3`, `:14`, `:16`); `topics/writing-rules.md`.
- Read: `reports/deploy-deploy-radar-mirror-scope.md` (§0, `## RESTARTS`, `## Smoke`, `## DECISIONS`); `git show HEAD:` deploy card 1027; `git show HEAD:ops/desk/deploy-smoke.sh`; `git grep HEAD` of `DEPLOY-HUB.md` (`:11`, `:152`, `:158`).
- git: `rev-parse --short=8 HEAD` → `148b03ef`; `log --oneline -8 main`; `diff --numstat 11ed17b8 25994142`; `log --oneline 11ed17b8..25994142`; `diff --stat 11ed17b8 HEAD --` the nine spec paths → nothing; `diff --stat 11ed17b8 HEAD -- src tests configs ops` → `configs/cobalt/rules.yaml` (`7001737f`); `diff 11ed17b8 25994142` of the seven files.
- Markers: `git grep -c -F "MIRROR_SOURCE_PREFIX = "` HEAD → no match, `25994142` → 1; test marker `25994142` → 1; `ls-tree HEAD` → test file absent.
- Rulings and desk rows: `cto-2026-10-18.md:90` R1863; `cto-2026-10-23.md:30` R2389; `cto-2026-10-24.md:7-9` R2409–R2411.
- `ls /Users/cobalt/cobalt-wt/` → no `radar-mirror-scope-port`.

DRAFTED · decisions: 4
