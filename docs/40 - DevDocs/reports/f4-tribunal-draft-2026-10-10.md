# F4 tribunal prompts · drafter report · 2026-10-10

## §0 Headline
- Three prompts written: hub `237`, blind Opus seat `238`, derive `239`; 21 questions (the 15 decisions + 6 added).
- Launch strings: 17/17 hub, 10/10 seat, 10/10 derive count 1 in both new file and template; none new.
- Gates: 09-22's dated grok/agy gate expired, replaced by the standing R17/R19 gates (newest hub that ran, `prompts/2026-09-29/12`).
- Floor stricter than L67's text (R860): two outside houses must sit; Astra METER with Gemini not seated stops the hub at preflight.
- Open for the desk: launch-row literals before launch, and L53 on the refresh cadence (D5).

## CHANGES
| File | What |
|---|---|
| `prompts/2026-10-10/237-f4-tribunal.md` | new: hub `f4-tribunal-1010`, Sonnet 5.5; probe first; Astra · Grok · Gemini (optional); floor; packet; 21 items; collate; Opus-seat file-check |
| `prompts/2026-10-10/238-f4-tribunal-opus-seat.md` | new: blind seat `f4-tribunal-opus-1010`, `claude-opus-5-5`, `FABLE ROW: R109`; SELF marks on C12 and (e) |
| `prompts/2026-10-10/239-f4-tribunal-derive.md` | new: derive `f4-tribunal-derive-1010`, `DERIVE ROW: R109`; refuses without both stop lines and `floor: MET`; writes `F4-FINAL-<date>.md` and `reports/f4-tribunal-derive-2026-10-10.md` |
| `reports/f4-tribunal-draft-2026-10-10.md` | this report |

Changed from the 09-22 template: model `claude-sonnet-5-5`; seat = Opus 5.5 (never Fable 5.1); Astra USED after her probe (R13's skip expired); `--name` added; Grok `grok -m grok-4.7`, Gemini `gemini-3.8-flash-high` (his 10-03 R3 / R6, `CHECK-HUB.md:91`); Astra launch with ` < /dev/null` (as the Sol line of `CHECK-HUB.md`); launch row replaces the R109-only gate (row names `237`, three literals, one Gemini literal); STAGGER and probe order from `12`; 23:20 and 19:25 window refusals dropped (they bound the expired grok/agy window; `12` carries none); packet and items re-pointed to F4; round 2 text of `12` §5 not carried (the derive lists `## NEEDS ROUND 2`).

## DECISIONS
| # | Decision (default taken) | Need |
|---|---|---|
| D1 | Model ids in the house spellings: `grok-4.7` and `gemini-3.8-flash-high`. The allow strings `Bash(grok *)` and `Bash(agy *)` stand (L62); `STANDING-LIST.md` and `CHECK-HUB.md:92` still spell Gemini `gemini-3.1-pro-high`. Gemini is optional: a refused id is `HARNESS`, never retried | his word if he wants `gemini-3.1-pro-high` (R411) |
| D2 | The desk writes the launch row BEFORE launch: names `237-f4-tribunal.md`, carries `f4-design-proposal-2026-10-10.md` · `Fable seat: yes` · `derive seat: claude-opus-5-5`, one of `gemini: sits` / `gemini: not seated`, and `no other house hub is running`. Without them `237` / `238` / `239` stop at preflight | desk |
| D3 | Floor per R860 = proposer + two outside houses. Stricter than L67's "never below two houses". Astra METER and `gemini: not seated` → `FAILED PREFLIGHT: floor`, nothing launched | desk (set `gemini: sits` or wait for Astra) |
| D4 | An absent house never holds the FINAL while the floor is met; the derive lists `## ABSENT HOUSES`; the desk may offer the read, never a precondition | brain / him if he wants Astra on every design |
| D5 | The proposal says no owner item. L53 reserves the Finviz request ceiling and the scan cadence to him (`source: ruling`); the proposal commits the refresh cadence as `source: dwv`, `status: proposed` and adds ~3 Finviz requests per run. Asked as C2 and (c); the derive carries it to him only if the hub's file-check of L53 holds | him, if it holds |
| D6 | SELF marks only on C12 and (e) (the build seat); the derive keeps the seat because L29 and L67 name it | none |
| D7 | 21 items = the drafter's 15 decisions + (a) fact base, (b) ownership walk, (c) L52/L8/L1/L53, (d) seam, (e) chunks and seats, (f) RESTARTS | none |
| D8 | Static check only of `desk-launch.sh prompt` rules (one launch line, no `<` `>`, one `cd` span, mode `auto`, `--remote-control` before `--name`, denies, paths under `--add-dir`). The three files are untracked: the desk commits them before launch (`committed` check) | desk |

## RECORDS
| Item | Value |
|---|---|
| Clock | Sat 2026-10-10 08:14:50 EDT |
| RULE PROOF `grep -c -F -e` | `237` vs `63`: 14 allow strings, the deny trio, `--add-dir` trio, `--permission-mode auto` = 17 strings, each 1 in both. `238` vs `64` and `239` vs `65`: 7 allow strings, the deny trio, `--add-dir` trio, `--model claude-opus-5-5 --permission-mode auto` = 10 strings, each 1 in both (a four-file call per string) |
| Launch-line shape | `claude --bg "Read ` occurs once per file (`237` `238` `239`); one backticked `cd /Users/` span per file |
| NEW strings | none |
| Sizes of the new files | `237` 67,322 B · `238` 20,657 B · `239` 25,493 B (`239` after the one edit) |
| Packet, sources at drafting (`wc -c`) | proposal 16,224 · seam 4,503 · drafter report 6,363 · `daily.py` 24,310 · `prefill/config.py` 6,006 · `cli.py` 2,581 · `market.py` 3,490 · `prefill.yaml` 1,001 · `daily.md.j2` 2,423 · `jobs.yaml` 20,349 · `writer.py` 59,388 · `merge.py` 6,745 · `store.py` 10,932 · `jobs/config.py` 20,969 · `radar/notes.py` 30,852 · `test_finviz_consumers.py` 7,830 · `clock.py` 12,394 · `daymode/note.py` 9,770 · Charter 29,164 · ladder 126,331 |
| Packet bound | MANDATORY ≤ ≈150 KB, whole ≤ ≈215 KB: an upper bound (whole files, or 100 B per line of a range), not a measurement; ceiling 200,000 B; the hub measures; cut order in `237` §1 |
| Code base | `d0a5fbb8` = `d0a5fbb8761a7ddf46b22310db4089eec32f8b27`; the staged paths are proven unchanged by `git log` against it |
| Rows read | `cto-2026-10-10.md` R849 :26, R860 :13, R866 :7; R109 `cto-2026-09-22.md` :56; R17 / R19 `cto-2026-09-24.md` :35 / :37; R95 / R97 `cto-2026-09-23.md` (literals counted 1) |
| Astra slug | `gpt-6-astra` in `~/.codex/models_cache.json` (count 1) |
| Anchors checked | `daily.py` :412 `slot_state`, :463 `SLOT_SPECS`, :482 `regenerate_rules_config`; `writer.py` :559, :673, :846; `store.py` :91, :111, :232, :247; `merge.py` :100; `jobs.yaml` :207, :284, :330; Charter :82-93; ladder :923, :932, :939 |
| Not done | no staging, no launch, no commit, no `desk-launch.sh` run |

F4 TRIBUNAL PROMPTS DRAFTED · prompts: 3 · new rule strings: 0 · decisions: 8
