# JEV build re-issue — drafter report (2026-09-23)

Seat `jev-reissue-0923` · Opus 5.5 · prompt `prompts/2026-09-23/30-reissue-jev-build.md` · OFF-LADDER (`cto-2026-09-23.md` R34 / R38 / R42). Written 11:05 EDT (`date`). Nothing run, nothing committed, no network, no DB, no vault or memory write.

## §0 Headline
- `28` re-issued as an OFFLINE build. The keyed probe and the step that made a fixture from it are removed. The wrapper is written and grep-verified but never run. N2 is off its launch line.
- `29` re-issued so its packet and questions match the offline build. Its launch line is unchanged byte for byte. The key handling (wrapper, then `read_secret`) is now S-1 / S-2. It adds a `probe gate: READY|NOT READY` stop field.
- `31-jev-trial-probe.md` is NEW. It is a Sonnet 5 hub that runs N2 once, after `29` reads READY, and commits the live fixture.
- New rule strings: 0. ESCALATE: 6.

## L74
None arrived. A system reminder in this session supplied commit attribution. I made no commit, so it was not used.

## What moved
| File | Change |
|---|---|
| `28-jev-trial-build.md` (105 lines) | The launch line loses N2 and nothing else. I checked this with a diff of the extracted `claude --bg …` line. N1 is now limited to `discover` and `trial … --dry-run`. `model_id: typesafe/jev-1.13` + `model_id_source: "ruling: cto-2026-09-23.md R42"` is added to R1 and gated in AUTHORIZATION. R3 now checks that his id is listed. If it is absent → FAILED. Other Jev ids are recorded and never substituted. R4 removes `### LIVE` and the fixture made from the probe. It adds the `probe` subcommand, which is built and tested over a fake transport only. The subcommand prints one `PROBE …` line, writes `<out>` + `<out stem>.raw.json`, and refuses if a probe file already exists. It adds the fixture `openrouter-chat-response.published-schema.json`, built from OpenRouter's published schema and marked `SHAPE: published schema, not yet a live capture`. It adds parse tests parametrized over the `openrouter-*response*.json` glob; zero matches is a failing test. The stop line now reads `model listed: typesafe/jev-1.13 | other Jev ids listed | probe: NOT RUN (after check, R42) | ledger: NOT RUN (after check, R42) | cap`. CLOSE fails if a `probe-*` file or the ledger exists. The ledger file is created only by `record`. One new path: the fixtures DevDoc `docs/40 - DevDocs/tests/fixtures/classify/_classify_fixtures.md`. |
| `29-jev-trial-check.md` (90 lines) | The launch line is unchanged. The checks now gate on N2 (R42). PREFLIGHT requires the offline stop-line fields and a `scratch/` with no probe file and no ledger. The boundary includes the fixtures DevDoc. The staged contract adds `MASTER_KEY_ENV` and `put_secret`. `rows.md` adds `31`'s `## THE PROBE`. The questions are S-1 wrapper · S-2 `read_secret` path · S-3 … S-8 as before, reworded for the offline fixtures · S-9 the probe command this check gates. `ready for the trial run` becomes `ready for the probe`. The `probe gate` field is arithmetic: READY iff ≥3 houses answered AND LEAK HOLD 0 AND defects HOLD 0. |
| `31-jev-trial-probe.md` (51 lines, NEW) | Sonnet 5, same worktree. It gates on its own launch row, R42 (N2, `JEV spend cap $5`, `typesafe/jev-1.13`) and `29`'s committed last line carrying `probe gate: READY`. It runs N2 exactly once and never on a relaunch. It checks the output for key-shaped text before quoting it. It runs 3 greps × 2 scratch files before the Write. The fixture is written byte-identical from `.raw.json`. It adds one DevDoc line. The offline suite must show p > baseline p. It commits 2 paths plus its report. Stop line: `JEV PROBE DONE · model: <id as returned> · <ms> ms · $<cost> · probabilities: YES|NO · ledger: $<total> of $5 · offline <p>/<f>` or `FAILED: …`. |

## Rule strings
| Prompt | Strings | New |
|---|---|---|
| `28` | the original 19 minus N2 = 18 | 0 (N1 is his, R42) |
| `29` | unchanged (15 + 3 denies + `--add-dir` ×3) | 0 |
| `31` | 13 allow strings from `28`'s line (checked by script: all found there) + N2 (his, R42: `grep -c -F` = 1 in `cto-2026-09-23.md`) + the 3 denies + `--add-dir` ×3 | 0 |

## ESCALATE
1. **The published schema in `28` R4 comes from my own knowledge of OpenRouter's API reference. I did not fetch it (no network).** Fields: `id`, `provider`, `model`, `object`, `created`, `choices[].{index, finish_reason, native_finish_reason, logprobs, message.{role, content}}`, `usage.{prompt_tokens, completion_tokens, total_tokens, cost, prompt_tokens_details.cached_tokens, completion_tokens_details.reasoning_tokens}`. `31`'s live capture confirms or corrects it. If they differ, `31` stops `FAILED: suite …` and the difference goes to a fix round (L75).
2. **`31` moves `jev/trial-0923` above the tip `29` checked.** It adds a test fixture, one DevDoc line and its report, with no code. Whether that needs a check before any merge is the desk's call (L67).
3. **The Grok/agy strings on `29`'s line expire 2026-09-23 23:59 ET** (09-22 R30; carried from the drafter's ESCALATE 5). A later launch needs a committed row of his extending them.
4. **N1 still pattern-allows `uv run cobalt classify probe`.** Only the prose of `28` forbids it. `28` line 1 says a keyed subcommand fails loud in the worktree because there is no `COBALT_MASTER_KEY`. I did NOT verify this; I did not inspect any environment. `29` S-9 asks about this path.
5. **`28`'s WHAT YOU BUILD has one new path**: `docs/40 - DevDocs/tests/fixtures/classify/_classify_fixtures.md`. It follows the precedent of `tests/fixtures/radar/_cut_panel_fixtures.md` and holds the `SHAPE:` marker lines. `29`'s boundary list carries it.
6. **Desk fills before launch:** `28` BASE TIP + R__; `29` R__ (with `no other house hub is running`); `31` R__. `31` launches only on `29`'s committed `probe gate: READY`. N3 (the trial-run string) is still NOT approved (R42).

JEV BUILD REISSUED · probe moved after check: yes · model id: typesafe/jev-1.13 · new rule strings: 0 · ESCALATE: 6
