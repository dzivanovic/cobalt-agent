JOB: terra-pass-prompt-1011
LADDER: OFF-LADDER — reports/cto-2026-10-11.md R1107
BRANCH: ops/terra-pass-prompt-1011
WORKTREE: terra-pass-prompt-1011
BASE: ffc704da
TIP: none
REPORT: /Users/cobalt/cobalt-wt/terra-pass-prompt-1011/docs/40 - DevDocs/reports/terra-pass-prompt-build-2026-10-11.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/terra-pass-prompt-check-2026-10-11.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-11 R1107

## ROWS

WHY: his word "I approve terra read" (row `R1107` of `reports/cto-2026-10-11.md:9`, `HIS RULING · APPROVED`; brain direction R1109, L79) lets the Terra arm run commands that read files. `SHADOW-HUB.md` is a fixed file, so it changes by card row, never in place. No preflight ran (brain direction); a Grok check, as with card 355. No row adds a command class (R411, R412): the Terra builder allow string and command stand as signed.

| row | what | red first | files |
|---|---|---|---|
| T1 | In `SHADOW-HUB.md:29` (the `<pass prompt>` template, one line) the sentence `Run no command.` becomes `Run <no command (GROK, SONNET) or only commands that read files; no command that writes, deletes or uses the network (TERRA)>.` in place (`or` stands where the line's own `|` alternation would be; a pipe inside this table cell would split it); every other character of the line stays, and `Reply with the list of files you wrote.` still follows it. Filled for Terra the sentence reads `Run only commands that read files; no command that writes, deletes or uses the network.`; filled for Grok and Sonnet it reads `Run no command.`. In `:26` (the Terra note) append to the line: ` Reads are not confined by workspace-write; accepted by HIS word 2026-10-11 (R1107).` No other line changes: `grep -c ""` stays 103; `git diff --numstat` on the file against `BASE` is 2/2. `bare-guard.py` is NOT edited: G7 (`builder_call`, `ops/desk/bare-guard.py:1148-1179`) fills the `## BUILDERS` row's command and tests the prompt only with `PLAIN_PROMPT = re.compile(r'"[^"\\$`]*"')` (`:108`), which accepts every character of the new Terra sentence (`;` and `,` included; no `"`, `\`, `$` or backtick); it never reads the template at `SHADOW-HUB.md:29`. Backed by `reports/cto-2026-10-11.md` rows `R1107` (`:9`) and `R1109` (`:7`), `SHADOW-HUB.md:12`, `:26`, `:28-29` | `grep -c -F -e "Run no command." "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` → 1 on `BASE` (`:29`), 0 after. `grep -c -F -e "Run only commands that read files; no command that writes, deletes or uses the network" ` on it → 0 on `BASE`, 1 after. `grep -c -F -e "(GROK, SONNET)" ` on it → 0 on `BASE`, 1 after (the Grok and Sonnet variants keep `no command`). `grep -c -F -e "Reads are not confined by workspace-write; accepted by HIS word 2026-10-11 (R1107)." ` on it → 0 on `BASE`, 1 after. `grep -n -F "Run <no command (GROK, SONNET) or only commands that read files; no command that writes, deletes or uses the network (TERRA)>." ` on it → empty on `BASE`, `29:` after. `grep -c -F -e "«SIGN" -e "«INSTALL"` on it → 0 before and after (no sign mark returns). Every row ends with `uv run pytest -q tests/ops/test_shadow_hub_file.py tests/ops/test_bare_guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_authorize.py` → `0 failed` | `docs/40 - DevDocs/prompts/SHADOW-HUB.md` (`:26` and `:29` only) |

## NOT IN THIS JOB
- `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `ops/desk/authorize.sh`: read only. G7 checks the prompt's characters, not its text (row T1); no guard row.
- Any other line or cell of `SHADOW-HUB.md`: line 1 (the `INSTALL:` title `authorize.sh` reads), the three `## BUILDERS` rows and their sign cells, the launch line, `## RESULTS TABLE`, the `:28` sentence about the prompt's characters.
- `SPIKE-HUB.md`, `STANDING-LIST.md`, LAWS, `.claude/settings.json`, any `settings.local.json`, any test file.
- The Terra arm's launch, X1 and the decoy `.env` row (cards 367 and 381): the desk's; 367 relaunches after this card deploys (R1109).
- A new command of any kind (R411, R412): a row that needs one is not built; the build stops with `decisions: 1`.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md` whole (103 lines), lines 12, 21, 26 and 28-29.
- `ops/desk/bare-guard.py` lines 105-108 (`WT_TOKEN`, `PASS_PROMPT`, `PLAIN_PROMPT`) and 1148-1179 (`builder_call`), 1106-1122 (`builder_command` reads the `builder command` cell only).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md` lines 7 and 9 (R1109, R1107).
- Precedent: `prompts/2026-10-11/355-install-shadow-hub-card.md` (header and row shape).

## CHECK ASKS
- X1 Is the diff of `SHADOW-HUB.md` only `:26` (the appended sentence) and `:29` (the one sentence), `git diff --numstat` 2/2, `grep -c ""` 103 before and after?
- X2 Does `PLAIN_PROMPT` (`bare-guard.py:108`) accept the Terra prompt filled from the new `:29`, and is no `"`, `\`, `$` or backtick in `:29`? Fill the template for each of Grok, Sonnet and Terra and run `grep -c` for those four characters on each.
- X3 Does the Terra sentence read exactly `Run only commands that read files; no command that writes, deletes or uses the network.` once filled, and `Run no command.` for Grok and Sonnet?
- X4 Does any test or script read `SHADOW-HUB.md:26` or `:29` (`grep -rn "Run no command\|SHADOW-HUB" tests ops`)? The drafter's grep found none for the prompt text.
- X5 `;` inside the double-quoted prompt: does `scan()` (`bare-guard.py:1061`) treat it as quoted, so the G1 or G3 rules do not cut the command there? UNPROVEN by the drafter (no Python run on its allow list); name the test or the run.
- X6 R1107 is his and approved: write no finding that rests only on Terra reading files being allowed.

## RECORDS
- Read by the drafter `draft-terra-pass-install`, 2026-10-11, against `HEAD` `ffb0e99c` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`): `git -C /Users/cobalt/cobalt status --short -- "docs/40 - DevDocs/prompts/SHADOW-HUB.md" ops/desk/bare-guard.py` → empty, so both files equal `HEAD`; the hub's last commit is `d4ec4fe3`.
- `grep -n -F "Run no command." SHADOW-HUB.md` → `29:` only (count 1); `grep -c ""` → 103. `:26` is the Terra note under `Notes on the rows`; `:28-29` hold the `<pass prompt>` sentence and template.
- G7 reads (`bare-guard.py`): `builder_command` (`:1106-1122`) takes cell 4 of the model's `## BUILDERS` row; `builder_call` (`:1148-1179`) splits the filled command at `"<pass prompt>"` and tests the typed prompt with `PLAIN_PROMPT` (`:108`) alone. No line of the guard reads the template at `SHADOW-HUB.md:29`.
- Tests: `tests/ops/test_bare_guard.py:2116` builds its own `PASS_PROMPT`; `test_shadow_hub_file.py:255` fills `PROMPTWORD`; no test reads `Run no command` (`grep -rn "Run no command" tests` → empty).
- Rows `R1107` (`:9`, HIS RULING · APPROVED) and `R1109` (`:7`) of `reports/cto-2026-10-11.md` read at `HEAD`.
- No preflight ran: brain direction, L79. A Grok check as with card 355; docs only, `DB: none`, house A is Grok, never OpenAI (R920). RESTARTS: every path is `docs/` (`uv run cobalt jobs restarts <BASE>..HEAD` UNPROVEN at drafting; the build hub runs it).
- `BASE` and `TIP` are the desk's: `BASE` is `main` at the launch; `TIP` starts as BASE and is rewritten after the build, before the check.
