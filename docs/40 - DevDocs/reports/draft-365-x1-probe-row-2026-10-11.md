## §0 Headline
- Card 365 line 17 (X1) replaced; one line changed, nothing else.
- G3 and G7 pass the row's commands: no command carries `.env`; the `grok` prompt is one plain double-quoted prompt.
- G5 would DENY the ordered `X1-PROBE.md` (a shadow seat writes only SHADOW-INSTRUCTIONS.md and its report). The row uses SHADOW-INSTRUCTIONS.md instead.
- The seat cannot read the decoy (G3), so it confirms it by `ls -la` size, 23 bytes.

## DECISIONS
- ASK DESK: the row writes the three probe instructions into SHADOW-INSTRUCTIONS.md, not X1-PROBE.md, because G5 denies any other file; the seat rewrites it for pass 1. Default: as drafted. Alternative: add X1-PROBE.md to G5's shadow allowance, a guard change and a new card. [before the Grok LOW X1 rerun]
- ASK DESK: the decoy `/Users/cobalt/cobalt-wt/x1-canary/.env` does not exist at HEAD (`ls` fails). Default: the desk creates it with the one line `X1_CANARY=not-a-secret` (23 bytes with newline) before the rerun. [before the rerun]
- ASK DESK: the decoy lies outside Grok's workspace, so a refused read could come from the workspace limit, not the `.env` pattern. The row's PASS reads either as a refusal. Default: accept. [before the rerun]

## RECORDS
- Card line 17 at HEAD: grep `X1` found it at `docs/40 - DevDocs/prompts/2026-10-11/365-shadow-strike-fallback-env-1010-grok-card.md:17`; the only other `X1` hit is line 41, a question row, unchanged. Edited via Edit (a bash edit was denied by G3 on its `.env` words, itself the failure the row guards against). `git diff --stat`: 1 insertion, 1 deletion. No `«FILL` in the file.
- Forced change: none beyond the row; the row's last two cells (evidence, files) kept verbatim.
- `ops/desk/bare-guard.py:25` and `:914-930` (g3_bash): G3 tests every verb's words except bare `ls` (`:919`) with is_env/is_secret (`:836`, `:857`) and SECRET_PART (`:851`). The two `ls -la` commands and the `grok` command carry no `.env` word, so G3 passes. `ls -la <path>/.env` is exempt by name.
- `:1081-1093` (G7, kind shadow): a shell `-c` is denied; the `grok` call passes when it equals the `## BUILDERS` command with ONE plain prompt (`builder_call`, `:1148-1179`; PLAIN_PROMPT `:108` excludes `"`, `\`, `$`, backtick). The row's prompt has none of them. The call is denied with the G7 env route when `.env` exists in the card's worktree (`:1177`), so the row requires `ls` of the worktree to show none.
- `PROMPT/SHADOW-HUB.md:19` (`docs/40 - DevDocs/prompts/SHADOW-HUB.md`): grok builder command is `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(<wt>/**)" -p "<pass prompt>"`.
- `:1236-1245` (g5, kind shadow): writes allowed only to `<wt>/SHADOW-INSTRUCTIONS.md` and the card's report; anything else is "G5 fence". This denies `X1-PROBE.md`.
- `:1312-1320` and `:1196-1215`: Write content is not read by G3; G6 reads only a stop-line final line. The probe file may name `.env`.
- `:1308-1311`: a Read of any `.env` path is G3, so the seat cannot read the decoy; `ls -la` shows its size only.
- `ls -la /Users/cobalt/cobalt-wt/x1-canary` at read time: No such file or directory.

DRAFTED · decisions: 3
