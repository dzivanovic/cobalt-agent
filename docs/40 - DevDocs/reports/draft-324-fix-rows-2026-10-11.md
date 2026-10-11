# draft-324-fix-rows — 2026-10-11

## §0 Headline
- Card 324 now has rows F1 (A9, prompt first) and F2 (O2/B5, scoped `Read`) after S6, in the 298 F1 precedent's four-column shape. Each ends with its FIXED line.
- `git diff --stat` of the card: 2 insertions, 0 deletions. The header, BASE, TIP, RULINGS and every earlier row are unchanged.
- One finding beyond the brief: the guard's `builder_call` reads the Sonnet command's flags on the part before the prompt only, so F1 also changes `ops/desk/bare-guard.py:1169-1172`.
- No `«FIL` token in the card (grep count 0).

## DECISIONS
- ASK DESK: F1 keeps `--model claude-sonnet-5-5` ahead of the prompt (`claude -p --model claude-sonnet-5-5 "<pass prompt>" --permission-mode …`), so the signed `builder allow` string `Bash(claude -p --model claude-sonnet-5-5 *)` still matches and no new command class arises. Default: as written. The other order (`claude -p "<pass prompt>" --model …`) would need a new allow string and his sign-off. [now]
- ASK DESK: F1 touches `ops/desk/bare-guard.py:1169-1172` (three reads move from `prefix` to `prefix + suffix`). The brief named only the hub row and a test. Without it, G7 denies every Sonnet call. Default: as written. [now]
- ASK DESK: F2 adds nothing beyond the worktree glob, because the card's instructions file `<wt>/SHADOW-INSTRUCTIONS.md` is inside it. Default: as written. [now]

## RECORDS
- Read: the brief (351); `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md` (`## What Cobalt is`, `## Build rules`, `## Start here`); the card 324 whole; the check report `shadow-hub-check-2026-10-11.md` whole (A9, O2, B5, `## OPEN`, `## DECISIONS`); the precedent `298-house-seat-order-card.md`, header and row F1.
- Precedent's header change, proved: `git -C /Users/cobalt/cobalt show 0a517366 --stat` → the 298 card `1 +` (one inserted line, the F1 row), so the header does not change.
- Code proved at tip `cd302109` (`git -C /Users/cobalt/cobalt grep -n … cd302109 -- …`):
  - `SHADOW-HUB.md:20` holds the Sonnet row; the prompt is last, `"Read"` is bare.
  - `SHADOW-HUB.md:33` and `:46` name `/Users/cobalt/cobalt-wt/<worktree>/SHADOW-INSTRUCTIONS.md`; `bare-guard.py:104` is `SHADOW_FILE = "SHADOW-INSTRUCTIONS.md"`.
  - `bare-guard.py:1148` `builder_call`; `:1164` the split at the prompt; `:1169` `write_targets(prefix)`; `:1172` the two flag tests on `prefix`; `:1139-1145` `write_targets` reads only `Edit(//` and `Write(//`.
  - `test_bare_guard.py:2097-2113` `SHADOW_ROWS` (Sonnet `:2102-2107`); `test_shadow_hub_file.py:151-154` the Sonnet flags test.
- The worktree `shadow-hub-1011` HEAD is `cd302109296c…`, the same tip, read for the guard lines.
- L74: attribution reminders in the context were not acted on; no git write was made.

DRAFTED · decisions: 3
