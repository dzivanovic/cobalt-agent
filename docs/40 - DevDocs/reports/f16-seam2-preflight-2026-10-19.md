## CHECKS
Path abbreviations: `CLI` = `docs/40 - DevDocs/cobalt/cli.md`; `CARD` = `docs/40 - DevDocs/prompts/2026-10-18/790-f16-close-card.md`. main = `ef60f42f` (`git rev-parse --short=8 main`); `git diff main --stat -- CLI` empty, so the working file equals main's.

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read CARD, row `SEAM` (second, the last row, after `PORT`) | names exactly one file, `CLI`; form `SEAM: CLI = main's current file with F16's section added after main's last section by Edit` | OK |
| 2 | same row, method | reads main's file by `git show main:"CLI"`; Edit on its own copy; `git diff main -- CLI` shows only F16's section as added lines, no main line removed; "No `git merge`, no rebase, no other file touched" | OK |
| 3 | `git diff main c5eafaf1 -- "CLI"` | one hunk `@@ -138,5 +138,5 @@`: removes the f21-genesis-1013 heading and text, adds `## 2026-10-19 — f16-close-1018` and the one sentence `` `cobalt validate` builds the F23 playbook config and the F4 daily-refresh config and prints one line for each; a bad file fails loud.`` | OK |
| 4 | `git diff 6452f70e c5eafaf1 -- "CLI"` (BASE to TIP) | `@@ -137,3 +137,6 @@`: F16's own change is exactly 3 added lines: a blank line, the heading, the one sentence; row says "the two lines starting `## 2026-10-19 — f16-close-1018`" (heading and sentence), blank line between: matches | OK |
| 5 | `git diff 6452f70e main -- "CLI"` | `@@ -137,3 +137,6 @@`: main adds a blank line, `## 2026-10-19 — f21-genesis-1013` and its text after f20-cos-1018; this section is kept by the row (it stays, F16 goes after it) | OK |
| 6 | `grep -n "^## " CLI` (equals main) | `:135` f23-playbook-1013, `:138` f20-cos-1018, `:141` f21-genesis-1013 (the last heading); the card's cites (`:135`, `:138`, `:141`, text `:142`) match; the diff in #5 shows the text on the line after the heading | OK |
| 7 | other files named in the row | the `files` cell is `CLI` only; row text says "no other file is touched" twice | OK |
| 8 | continue step | row ends: "After the row the continue step is `FIX ROUND row SEAM`, then the deploy card" | OK |
| 9 | `grep -n "^BAND" CARD` header | `BAND: HIGH` (line 10); drafter report: "header already HIGH, not edited" | OK |
| 10 | `git diff 7c721da7 ef60f42f -U0 -- CARD` (the drafter's commit) | only two added lines: row `SEAM` (line 27) and one `## RECORDS` line (line 80); BASE `6452f70e`, TIP `c5eafaf1`, CHECK REPORT `…f16-close-fr1-check-2026-10-19.md`, HOUSE B `as needed` not in the diff | OK |
| 11 | `grep -c "«FILL" CARD` | `0` | OK |
| 12 | `git diff HEAD --stat -- CARD`; `git log --oneline -3 -- CARD` | empty; last commit `ef60f42f` (card committed, working copy equals HEAD) | OK |
| 13 | brain direction: `grep -n "R2028" reports/cto-2026-10-19.md` | `R2028` (09:58 ET, brain, L79): "row SEAM (main's file plus F16's section by Edit, no git merge) … a second conflict goes to port". The row cites it as the 10-09 seam rule; `R2031` records the first SEAM's trial merge still conflicting. No R-line yet for this second seam on the port job (see ISSUES) | OK |
| 14 | main's current `CLI` plus F16's lines, overlapping hunk? Base-to-F16 hunk (#4) and base-to-main hunk (#5) are both `@@ -137,3 +137,6 @@` at the same anchor, so a 3-way merge overlaps (that is the exit 3). By Edit: F16's blank line, heading and sentence appended after main's last line `:142` touch no main line; `git diff main c5eafaf1` (#3) shows the only difference between the two files is the f21 section vs F16's section, so after the append `git diff main` is 3 added lines (blank, heading, sentence), 0 removed | no overlapping hunk for the Edit form; overlap exists only for the merge form, which the row forbids | OK |

## ISSUES
- NOTE 1: the row's RECORDS line gives main `7e75d336`; main is now `ef60f42f`. `CLI` is unchanged between them (`git diff main --stat` empty, #6), so the row stands; the builder reads `git show main:` at its own launch.
- NOTE 2: `cto-2026-10-19.md` holds no R-line yet for this second seam (latest `R2041`); the direction rests on `R2028` ("a second conflict goes to port") and the 10-09 seam rule. The desk may add the R-line before the launch.
- NOTE 3: F16's section is three added lines in the diff (a blank line, heading, sentence), the row calls it "the two lines" with "a blank line between": consistent, no fix.
- NOTE 4: main moves again (F21 469, F5 also touch `cli.md`); if main changes `CLI` before the build, the builder re-reads by content (the row says `git show main:`).
- Blocks the launch: nothing. Note: no check ran code or a merge (read-only; one earlier `git rev-parse` call failed on a multi-revision argument and was re-run separately).

PREFLIGHT DONE · card: f16-close-fr1 · checks: 14 · fails: 0 · ready: YES
