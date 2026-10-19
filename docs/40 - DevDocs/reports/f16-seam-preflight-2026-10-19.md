# f16-seam preflight — card 790 row SEAM (2026-10-19, read-only)

## CHECKS
| # | command | output | OK/FAIL |
|---|---------|--------|---------|
| 1 | `grep -n SEAM` on card 790 | row at line 23 names only `docs/40 - DevDocs/cobalt/cli.md` and the form `SEAM: … = main's current file with F16's section moved onto it by Edit`; `git show` only, no `git merge`, no rebase; RED is `git diff main -- <file>`; files column lists that one file | OK |
| 2 | `git diff 40e646ed be6fa7b7 -- cli.md` | hunk `@@ -134,3 +134,6 @@`: exactly +3 lines (blank, `## 2026-10-19 — f16-close-1018`, the `cobalt validate` line); matches the row's wording | OK |
| 3 | `git diff 40e646ed main -- cli.md` | hunk `@@ -134,3 +134,6 @@`: +3 lines, `## 2026-10-18 — f20-cos-1018` section (blank, heading, one line); kept by the row | OK |
| 4 | `file:line` proof against main (`cli.md` working tree = main, `git diff HEAD --stat` empty) | main `cli.md:135` `## 2026-10-18 — f23-playbook-1013`, `:136` its line, `:138` `## 2026-10-18 — f20-cos-1018`, `:139` its line (last line); row's "ends with f20 after f23" holds | OK |
| 5 | overlap: main +3 and F16 +3 | both hunks insert after the same anchor `cli.md:136`, the file tail; the diff of F16 has no trailing context, so a patch/merge conflicts (this is the exit 3) | NOTE (not a fail) |
| 6 | apply F16 +3 by Edit after main's `cli.md:139` | F16's lines touch no main line; appending after `:139` gives main + F16, `git diff main` then shows only F16's section as additions; clean | OK |
| 7 | other files | row's file column and RECORDS line (card:67) name only `cli.md`; no other file | OK |
| 8 | BASE / TIP / CHECK REPORT / HOUSE B (card:5, 6, 8, 9) | `40e646ed`, `be6fa7b7`, check report path, `HOUSE B:` empty; untouched by the SEAM commit | OK |
| 9 | `grep -c "«FILL"` on card | 0 | OK |
| 10 | `git diff HEAD -- card 790` | empty; card committed (`8cd64dc8`) | OK |
| 11 | continue step | row ends: `FIX ROUND row SEAM`, then the deploy card; stop line `BUILT` | OK |
| 12 | drafter report / RECORDS line (card:67) | SEAM drafter 844, 0 decisions, cites main `286eac9c`; main is now `8cd64dc8`, `cli.md` unchanged by the two desk commits (diff vs `40e646ed` is still only the f20 +3) | OK |

## ISSUES
- NOTE: check 5 — same-anchor tail insertion; that is why `git merge` fails and the Edit seam is right. Order is f20 then F16 (F16 after `cli.md:139`).
- NOTE: card:67 says main = `286eac9c`; main is `8cd64dc8` now. No effect on `cli.md`.
- Nothing blocks the CONTINUE.

PREFLIGHT DONE · card: f16-close-1018 · checks: 12 · fails: 0 · ready: YES
