# Card 933 (cos-tunables) second source-comment amend — preflight r3

Read: card 933 at HEAD `f958ae8d` (last card commit `963a3dfc`); branch `ops/cos-tunables` tip read `af878860`; BASE `e69d5ab8`. Nothing run but reads.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `grep -n -F "DEFAULT"` on the card | 9 hits. `:15`, `:16` header rows: "his word (R2237/R2239); the `value:` line ends `# source: …`, never the DEFAULT comment". `:20` scope prose, `:25` T2 "has a DEFAULT value", `:26` P1 "DEFAULT of ASK DESK 1": other wording. `:24` T1, `:27` FR1, `:46`/`:53` X1/FR-3, `:57`/`:59` markers: each says the string is written nowhere / 0 lines, or names the comment being replaced. None tells the builder to write it. | OK |
| 2 | T1 (`:24`), X1 (`:46`), FR-3 check row (`:53`), FR1 marker sentence (`:27`), DEPLOY PROOF (`:57`, `:59`) | All say 0 lines carrying `DEFAULT (brain; his word may change it)` in `tunables.yaml` after the build. No "2" left. | OK |
| 3 | `git grep -c -F "DEFAULT (brain; his word may change it)" e69d5ab8 -- configs/cobalt/taxonomy/tunables.yaml` / same on `ops/cos-tunables` | BASE: no match (0). Branch tip: `:2` (lines 1009, 1027). Card says `before 0 · after 0`; marker 2 note says exactly 0. Numbering 1, 2 unchanged. | OK |
| 3b | `git grep -c -F "https://cobalt.taild24291.ts.net" e69d5ab8` / `ops/cos-tunables` | both no match (0); card `before 0 · after 1` | OK |
| 4 | `git show ops/cos-tunables:configs/cobalt/taxonomy/tunables.yaml` trailing comments on `value:` lines; card source-comment text | The only trailing comments on `value:` lines are the two DEFAULT ones (`:1009`, `:1027`, form `value: N  # text`, two spaces). The card's `# source: Dejan 2026-10-20 (brain relay)` replaces them in that same place and form. No other row carries a `# source` comment (see NOTE 2). The comment holds no URL; the URL stays in the one `hitl.page_base_url` value line. | OK |
| 5 | Prompt 954 (`:4`) and 955 (`:8`) verbatim lines against card `:75`, `:76`, `:78` | All three match character for character. | OK |
| 6a | `git diff c98c28f5 HEAD -- <card>` | The FR1 row's FR-1 and FR-2 text and its files/proof-column prefix are unchanged context; only the FR-3 text is appended. | OK |
| 6b | `RULINGS:` line `:14` | `2026-10-18 R1863` | OK |
| 6c | `git diff HEAD --stat -- <card>` | empty | OK |
| 7 | step string `FIX ROUND row FR-3` against `desk-launch.sh:698` and `:2632` (`[A-Za-z0-9.\ -]`) | letters, spaces, one hyphen: passes | OK |

## ISSUES
- NOTE 1: card `:20` still says the two values are "the brain's DEFAULTS … written as defaults, not as ruled values, and his word may change them", and T2 `:25` says "`cos.poll_interval_s` has a DEFAULT value". Both are stale next to the FR1 row's "both values are now his". Neither tells the builder to write the DEFAULT string, so nothing blocks the build.
- NOTE 2: no neighbouring row carries a `# source:` comment (`source:` is a YAML field, e.g. `source: ruling`). The form is new but matches the existing trailing-comment position. The FR1 row spells it out, so the builder needs no search.
- NOTE 3: the branch tip is still `af878860` and the FR1 builder is running, so the "before 2" at the tip is expected and goes to 0 only after this fix round.
- Blocks the build: nothing.

PREFLIGHT DONE · card: cos-tunables-fr3 · checks: 10 · fails: 0 · ready: YES
