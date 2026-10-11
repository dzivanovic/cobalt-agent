## §0 Headline
- Card 382 written: one docs-only row T1 in `SHADOW-HUB.md` (`:29` the Terra `Run` sentence, `:26` the note); `bare-guard.py` G7 needs no row.
- G7 tests only the typed prompt's characters (`PLAIN_PROMPT`, `bare-guard.py:108`); it never reads the hub's template text.
- `BASE` and `TIP` are `«FILL` (the desk's); no other `«FILL`.
- Not run: any Python or `uv` (not on the allow list); X5 (`;` inside the quoted prompt) is UNPROVEN and goes to the check.

## DECISIONS
- ASK DESK: the Terra sentence sits in place of `Run no command.`, before `Reply with the list of files you wrote.`; the prompt text said "ends", the same line said "in place of", and the card follows "in place of". Default: in place, the Reply sentence stays last. [any time before launch]
- ASK DESK: line 29 is one template with a `|` alternation, so the card writes the variant split as `Run <no command (GROK, SONNET) or only commands … (TERRA)>.` (`or` because a `|` splits a card table cell). Default: `or`. [any time before launch]

## RECORDS
- Card: `prompts/2026-10-11/382-install-terra-pass-prompt-card.md`; precedent `355-install-shadow-hub-card.md` (header and row shape), `CARD.md` read whole.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `ffb0e99c`; `git status --short` over `SHADOW-HUB.md` and `ops/desk/bare-guard.py` → empty; `git log -1 --format=%h -- SHADOW-HUB.md` → `d4ec4fe3`.
- `SHADOW-HUB.md` read whole (103 lines, `grep -c ""` 103); `grep -n -F "Run no command."` → `29:` only. `:26` Terra note, `:28-29` prompt sentence and template.
- `bare-guard.py` G7: `PASS_PROMPT` `:106`, `PLAIN_PROMPT = r'"[^"\\$`]*"'` `:108`, `builder_command` `:1106-1122`, `builder_call` `:1148-1179`, route `:1081-1093`. The new Terra sentence holds no `"`, `\`, `$` or backtick, so it passes.
- No test reads the prompt text: `tests/ops/test_bare_guard.py:2116` and `test_shadow_hub_file.py:255` use their own prompt words.
- `reports/cto-2026-10-11.md`: R1107 `:9` (HIS RULING · APPROVED), R1109 `:7`.
- Not read: `scan()` (`bare-guard.py:1061`) for `;` inside double quotes; recorded as card CHECK ASK X5.

DRAFTED · decisions: 2
