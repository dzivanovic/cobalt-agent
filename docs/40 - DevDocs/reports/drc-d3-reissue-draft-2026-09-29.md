# DRC D3 re-issue draft — F-6's U+00A0 half (2026-09-29)

Seat `drc-d3-reissue-draft-0929` · Opus 5.5 · prompt `prompts/2026-09-29/15-draft-drc-d3-fix-r1-reissue.md` · authorization `cto-2026-09-29.md` R66 `:74`, R69 `:77`, committed `efc074fa` · closed 13:26 ET (`date`).

## §0 Headline
- 7 of 7 U+00A0 positions proven. His template and the fixture were read at `7dd031fb`, and every byte offset matches.
- The byte-write string is designed: one exact `perl -i -pe` command. It was dry-run read-only on the fixture and changed exactly 7 lines, one byte each.
- FAILED at the `08` edits. The auto-mode classifier denied two Edits with `[Instruction Poisoning]`: the AUTHORIZATION R66 gate and the UNATTENDED RULES exception clause.
- The denial is a failed run (L62). Every edit already made to `08` was undone: `08` is byte-identical to HEAD (`cmp` clean). `09` was never edited.
- ESCALATE: 3.

## FACTS
His template is `/Users/cobalt/Vault/Think/5 - Templates/DRC.md` (the path `09-28/10` names at `:74`). The fixture is `tests/fixtures/drc/template_shape.md` at `7dd031fb`; the `drc-d1` worktree HEAD is `7dd031fb` and clean. Both files have 187 lines with no final newline, so `wc -l` prints 186. The template has no CR bytes.

Offsets are 0-based bytes within the line, and the line length includes `\n`.

| line | his template: the U+00A0 | template offset / length | fixture at `7dd031fb` | fixture after dry run: offset / length |
|---|---|---|---|---|
| 5 | trailing, after `DRC` | 21 / 24 | `C` U+0020 EOL | 21 / 24 |
| 49 | first of two spaces between `:` and `$` (`:` A0 20 `$`) | 19 / 28 | `:` 20 20 `$` | 19 / 28 |
| 128 | trailing, after `:` | 15 / 18 | `:` U+0020 EOL | 15 / 18 |
| 134 | trailing, after `:` | 18 / 21 | `:` U+0020 EOL | 18 / 21 |
| 156 | trailing, after `y` | 72 / 75 | `y` U+0020 EOL | 72 / 75 |
| 173 | trailing, after `:` | 36 / 39 | `:` U+0020 EOL | 36 / 39 |
| 175 | second of two spaces after `###` (`###` 20 A0 `T`) | 4 / 191 | `###` 20 20 `T` | 4 / 191 |

The commands that proved it, each run on its own:
- `grep -c -P "\x{00A0}"` on the template → 35 lines. On the fixture → 0.
- `grep -n -o -P "\x{00A0}$"` on the template → lines 5, 128, 134, 156, 173 among the 33 hits.
- `grep -n -o -P ":\x{00A0}\x{0020}\x{0024}"` → 49. `grep -n -o -P ":\x{0020}\x{00A0}\x{0024}"` → 0.
- `grep -n -o -P "^###\x{0020}\x{00A0}"` → 175.
- `grep -c -P "\x{00A0}.*\x{00A0}"` → 1 line (line 40, which is not a heading). So each of the seven lines holds exactly one U+00A0.
- On the fixture, `grep -n -o -P` with the U+0020 keys → 5, 49, 128, 134, 156, 173, 175. It also hits 9 and 15, where his template has no U+00A0, so the write must be addressed by line number.
- `perl -ne` offset reads of both files, printing numbers only.

## THE STRING
Rule, verbatim (designed, NOT placed in any file):
`Bash(perl -i -pe 's/C \n/C\xC2\xA0\n/ if 5..5; s/:  \x24/:\xC2\xA0 \x24/ if 49..49; s/: \n/:\xC2\xA0\n/ if 128..128; s/: \n/:\xC2\xA0\n/ if 134..134; s/y \n/y\xC2\xA0\n/ if 156..156; s/: \n/:\xC2\xA0\n/ if 173..173; s/^###  T/### \xC2\xA0T/ if 175..175' /Users/cobalt/cobalt-wt/drc-d1/tests/fixtures/drc/template_shape.md)`

- The command is the rule's content, run once, bare, from `/Users/cobalt/cobalt-wt/drc-d1`, after F-6's name Edit.
- Shape:
  - `N..N` is a flip-flop on a constant, so it is true on line N only.
  - Each `s///` has no `/g`, so it changes at most one match.
  - The regexes run in byte mode (no `-C`), and `\xC2\xA0` writes the two UTF-8 bytes.
  - `\x24` stands for `$`.
- The rule holds no `$`, no `*`, no backtick, no `"` and no parenthesis, so it survives the desk's double-quoted `--allowedTools` argument unchanged.
- It is idempotent: a second run finds no key and writes nothing.
- It touches only `tests/fixtures/drc/template_shape.md` in the `drc-d1` worktree, and only one U+0020 → U+00A0 on each of lines 5, 49, 128, 134, 156, 173 and 175.
- It never touches any other file or line, the vault, `cobalt_dev` or any database, the network, git, `launchctl` or a push. It never uses `bypassPermissions`, `--allow-prod`, or another seat's config.
- Tool: `/usr/bin/perl` 5.34.1, already on this Mac.
- Dry run: the same program under `perl -ne`, reading only, on the worktree fixture → 7 lines changed, each +1 byte, `total A0: 7; lines: 187`.
- PREFLIGHT: there is no harmless variant, because any other command misses the exact rule. Its first real use in `08` F4 is its probe; `ls /usr/bin/perl` is the read-only row.
- The build's proof lines (designed, each its own call):
  - `grep -c -P '\x{00A0}' tests/fixtures/drc/template_shape.md` → 7
  - `grep -n -P 'DRC\x{00A0}$' …` → 5
  - `grep -n -P ':\x{00A0} \x{0024}' …` → 49
  - `grep -n -P ':\x{00A0}$' …` → 128, 134, 173
  - `grep -n -P 'y\x{00A0}$' …` → 156
  - `grep -n -P '^### \x{00A0}T' …` → 175
  - `git diff --numstat a8c622ca -- tests/fixtures/drc/template_shape.md` → `7	7`

  The same patterns were checked on his template. The grep here is ugrep, and `\z` fails there; `$` inside single quotes works.

## CHANGES
None stands.
- 14 Edits of `08` were applied.
- 2 were denied:
  - the AUTHORIZATION bullet (the R66 gate with `O-1 → A` and `ONE exact byte-write string`)
  - the UNATTENDED RULES clause (`File content through the Write / Edit tools ONLY` gains the one byte-write exception)
- All 14 applied Edits were reversed by Edit.
- `09`: no Edit was made.

RULE PROOF: `git -C /Users/cobalt/cobalt show HEAD:<path> | cmp - <file>` → `08` identical (57,092 B) and `09` identical (46,312 B). Both launch lines are therefore the committed ones. The placeholder `grep -c -F` count is 1 in each file, in the AUTHORIZATION block, as before.

NEW strings: none placed. The one designed string is above, verbatim.

## ESCALATE
1. **Classifier denial, `[Instruction Poisoning]`, on the two `08` Edits named under CHANGES.** The run stops under L62, and nothing is patched around it. Whether these edits may be made at all is his call and the desk's.
2. **X-T's `wc -l → 187`** in `08` F-6 and `09` F-6 does not match the tool: `wc -l` prints 186 on both the fixture and his template (187 lines, no final newline). This is beyond items 1–4, so it is carried as `07` wrote it.
3. **`09`'s packet copies lose U+00A0.** Staging is Read → Write, so the `code-at-tip` fixture copy and the `fix-diff` would show U+0020, and the checkers could not see the seven bytes. When `09` is re-issued, the hub's own `grep -P` position lines belong in the packet. This is beyond items 1–4; `09` is carried as `07` wrote it.

## CONTINUE
next: none. The run is over. The desk decides on ESCALATE 1. A re-issue runs from a fresh launch using the FACTS and THE STRING above.

FAILED: 08 edit — two Edits denied by the auto-mode classifier [Instruction Poisoning]: the R66 AUTHORIZATION gate and the Write/Edit-only exception clause; 08 reverted to HEAD, 09 untouched; positions proved 7 of 7; string designed, not placed
