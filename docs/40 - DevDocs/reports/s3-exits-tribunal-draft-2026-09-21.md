# S3 exits tribunal — round-1 prompt drafting (2026-09-21)

Seat `s3-exits-tribunal-draft-0921` · Opus 5 · read-only except the four files named in `72` · started 18:41 ET, done 19:0x ET (`date` 18:59 before this write).

## §0 Headline
- Drafted three prompts, launched nothing: `73-s3-exits-tribunal.md` (Sonnet 5 hub, 3 houses, 26 items, packet ≈ 140 KB after cuts), `74-s3-exits-tribunal-fable-seat.md` (blind, line 1 `FABLE ROW: R__`), `75-s3-exits-tribunal-derive.md` (line 1 `DERIVE ROW: R__`).
- Astra is **REQUIRED** and the probe fails closed on METER / HARNESS, naming the retry time. A PARTIAL of k ≥ 1 of 26 is kept. `75` refuses without an astra ruling.
- New rule strings: **0**. `73` carries `61`'s 14 + 3; `74` / `75` carry `62`'s 7 + 3. Each counts 1.
- L32: a traded ticker and his prices sit in committed text (the Charter's DM example; two code comments). `73` redacts them in every staged copy and skips the two comment ranges.
- The proposal and its report are NOT committed yet, so `73` / `74` refuse until the desk commits them. ESCALATE: 7 (three ASK DESK).

## DIGEST FOR THE DESK
- **`73` hub** (`s3-exits-tribunal-0922`, Sonnet 5, cwd `~/cobalt-wt/agy-trial`):
  - Stages numbered parts (`66`'s layout) into `scratch/tribunal-bars-0920/s3-exits-tribunal/r1/`. `00` reading order, `01` questions, `02` greps. The MANDATORY set is `10`–`23`; `30`–`35` are OPEN-AS-NEEDED.
  - Runs grok, gemini and astra together, astra with ` < /dev/null` per `44`. It runs `date` at every notice and stops any house past 20 min.
  - File-checks every claim. At collate it also checks the Fable seat's claims, if that report has its stop line.
  - Report `reports/s3-exits-tribunal-<D>.md`. Stop line `S3 EXITS TRIBUNAL R1 DONE · grok … · gemini … · astra … · houses that ruled … · claims that HOLD … · blockers to build … · owner items … · ESCALATE …`.
- **`73` refuses when:**
  - the proposal or its stop line is uncommitted;
  - rows R13 / R23 / R38 / R46 are missing, or no committed launch row names `73`;
  - a Sol / Opus string is in its line (R46);
  - the date is 09-22 without R39's literal, or it is 09-23 or later;
  - the time is 19:25–20:45 or ≥ 23:20 ET;
  - `38`, `61` (either name), `66`, `68` or `69` is running. A missing report passes only with the launch row's literal `<nn> has stopped or will not run`;
  - astra is not UP.
- **`74` Fable seat** (`claude-fable-5-1`):
  - Refuses while `R__`. Its row must carry `Fable seat: yes` + `S3-EXITS-PROPOSAL-2026-09-21.md`; R51 does NOT cover it.
  - BLIND to the r1 folder and both hub names. Self-attack greps 17 names.
  - One file, 26 counts. Refuses a date after 09-22.
- **`75` derive:**
  - Row `R__` + `--model` from `derive seat:`. Refuses without the hub stop line, the Fable stop line (if yes) and astra.
  - Verbatim folds only; never folds a DOES NOT HOLD or WITHDRAWN claim. O1–O8 are never a build precondition.
  - Writes `30 - Design/S3-EXITS-v2-<D>.md` and `reports/s3-exits-tribunal-derive-<D>.md` with `## FOR DEJAN` (A/B, no recommendation).
- **Launch order with clocks:**
  1. Tonight: commit the proposal, its report, `73`–`75` and this report. Ask him about the Fable seat (the same row fills `74` / `75` line 1).
  2. TUE 09-22, the desk's order: `68` → `69` → `61` first. `73`'s launch row states each one's status literally.
  3. `73` + `74` together, in a free slot before 19:25 or at 20:45–≈22:30 (houses ≤ 20 min plus the file-check; ≥ 23:20 refused).
  4. `75` after both stop lines are committed (it needs no house strings, so 09-23 is fine). A round 2 after 09-22 needs his grok / agy extension.

## L47 finding
Astra is REQUIRED and fails closed.
- **Why:** 5 write-path chunks on a user table plus a vault write path; the proposer is Anthropic; the Fable seat is not approved yet.
- **Cost:** this is the largest packet put to astra so far: MANDATORY ≈ 125–135 KB, 26 items. Its r2 run ruled 12 items in 46,391 tokens on ≈ 90 KB. The reading order and print-as-you-go keep a METER stop from being a total loss: the partial is kept.
- **Risk:** a METER stop on TUE evening leaves no retry inside R39. The relaunch needs his word.

## PACKET
Sizes are estimates from line ranges × each file's bytes per line; whole files are exact. The hub states the real `wc -c`.

| staged path | source | size | tier |
|---|---|---|---|
| `00-READING-ORDER.md` | hub-written | ≈ 3 KB | MANDATORY |
| `01-QUESTIONS.md` | verbatim in `73` + file list | ≈ 16 KB | MANDATORY |
| `02-greps.txt` | 19 greps (narrowed to the core dirs), `ls` of 4 migration sets, 5 `git log` | ≈ 25–35 KB (unmeasured) | MANDATORY (search) |
| `10-PROPOSAL.md` | proposal whole, redacted | 27,271 B | MANDATORY |
| `11-design-digest.md` | report :3–8, :10–16, :31–37, :42–55 | ≈ 5.5 KB | MANDATORY |
| `12-scope-and-rulings.md` | R38 · ladder :586–603 · Charter :135–147, :205–207, :245–255 · DRC packet :48–49 | ≈ 9 KB | MANDATORY |
| `13-templates-keys.md` | 2 templates, headings + frontmatter keys only | ≈ 0.8 KB | MANDATORY |
| `20-fill-path.excerpt.py` | `web.py` /fill (skips :1081–1086), /move, /stop · `aset/store.py` mark_filled (skips :191–196) · `engine.py` 3 ranges · `aset.yaml` :48–53 | ≈ 16 KB | MANDATORY |
| `21-cards-store.excerpt.py` | `cards/store.py` transition, pending stops, fill, record_stop_edit | ≈ 17 KB | MANDATORY |
| `22-trade_note.py` | whole | 6,580 B | MANDATORY |
| `23-note-writers.excerpt.py` | `web.py` /size note, radar key · `daily_note.py` · `drc.py` :92–132 · `prefill.yaml` | ≈ 9 KB | MANDATORY |
| `30`–`35` | models, vaultwrite docstrings, attestation / notify / killswitch, migrations, R / expiry, laws (11) | ≈ 30 KB | OPEN-AS-NEEDED |
| **total** | | **≈ 150–165 KB before cuts; ≤ 140 KB after the cut order, if the core allows** | |

- Cut order: evaluate range → `31` → laws down to 6 → `33` down → `30`. The MANDATORY core is never cut. If the core alone is over 140 KB, the hub stages it anyway and escalates; it does not fail.
- **User data:** redacted as described in §0. Templates: headings and keys only (checked: the trade template has 12 keys and 1 heading; `Daily.md` has 1 key and 11 headings; no values). No note of his, no P&L, no production row.
- **Token estimates per house:**

| house | reads | output | notes |
|---|---|---|---|
| Grok | ≈ 35–40k (whole) | 12–18k | 26 items |
| Gemini | ≈ 35–40k | 12–18k | |
| Astra | ≈ 45–70k | — | reading order; METER risk, partial kept |
| Hub (Sonnet) | ≈ 150–200k context | — | staging I/O + file-checks |
| Fable seat | ≈ 73–85k | 14–20k | peak ≈ 95–115k |
| Derive | — | 12–16k | peak ≈ 120–150k |

## RULE PROOF
`grep -c -F -e '"<string>"'` run per string at 18:5x ET on `73 61 74 75 62` together.

| string | 73 | 61 | 74 | 75 | 62 |
|---|---|---|---|---|---|
| `"Bash(grok *)"` · `"Bash(agy *)"` | 1 each | 1 each | 0 | 0 | 0 |
| `"Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)"` | 1 | 1 | 0 | 0 | 0 |
| `"Bash(mkdir -p scratch/tribunal-bars-0920)"` | 1 | 1 | 0 | 0 | 0 |
| the three `s2-p2-cards` strings | 1 each | 1 each | — | — | — |
| `"Bash(git -C /Users/cobalt/cobalt show*)"` · `…log*)"` | 1 each | 1 each | 1 each | 1 each | 1 each |
| `"Bash(ls *)"` · `"Bash(grep *)"` · `"Bash(tail *)"` · `"Bash(wc *)"` · `"Bash(date*)"` | 1 each | 1 each | 1 each | 1 each | 1 each |
| `"AskUserQuestion"` · `"EnterWorktree"` · `"Bash(git push*)"` | 1 each | 1 each | 1 each | 1 each | 1 each |

- `grep -c -x -F "FABLE ROW: R__"` on `74` = 1; `"DERIVE ROW: R__"` on `75` = 1. Both are unfilled, as the brief requires.
- Prompt sizes: `73` 71,682 B · `74` 18,481 B · `75` 19,642 B.

**NEW strings:** none.

## READING:
- Prompts: `72`; `60`–`63` (whole); `66` (lines 1–12 + §1 by grep); `67` (whole); `38`, `68`, `69` (report names + stop prefixes, by grep).
- Proposal (whole). Its report (whole). `stale-score-tribunal-draft-2026-09-21.md` (whole). `drc-sitting-packet-2026-09-21.md` ESCALATE.
- `cto-2026-09-21.md`: rows R38–R39, R46, R48, R49, R51, R52, and the :448 lane line. `cto-2026-09-20.md`: rows R18, R38.
- Ladder :586–606 (+ heading grep). Charter :135–148, :203–262 (+ heading grep). LAWS.md headings.
- Templates: headings + keys by grep only, plus the frontmatter bounds.
- Code on main:
  - `aset/web.py` :945–1393
  - `aset/store.py` :185–258
  - `cards/store.py` :239–533, :643–742, plus the def list
  - def / anchor greps: `engine.py`, `models.py`, `trade_note.py`, `drc.py`, `writer.py`, `daily_note.py`, `killswitch.py`, `expire.py`, `evaluate.py`, `radar_panel.py`, `0007`, `db_migrations/__init__.py`, `placement.py`, `replay/`
  - `ls` of the migration dirs; `wc` of every staged source
- Git: `git log` main (5), `be58530..76114e9 --stat` (docs only), `bars/chunk-2-0920` (`c19f304`). `setups/seven-0921` and `s2/stale-marker-0921` → `fatal: bad revision`.

## ESCALATE
1. **The proposal and its report are uncommitted.** At 18:4x, `git log` on both paths returned nothing. `73` and `74` refuse until they are committed; commit them before launch.
2. **The Fable seat is not approved for this tribunal.** R51 covers the stale-score seat only.
   - One row must carry `Fable seat: yes|no` · `derive seat: <model id>` · `S3-EXITS-PROPOSAL-2026-09-21.md`. It fills line 1 of both `74` and `75`, and `75`'s `--model`.
   - `ASK DESK: ask him tonight, with the METER line of 74 (≈ 95–115k peak; Fable at 40 % per R46)? [18:59]`
   - Safe default: `73` runs without the Fable seat, and `75` waits.
3. **L32, a traded ticker.** `TSLA` is his traded ticker (`aset/web.py:1084`, `aset/store.py:192`, 09-03 incident). The Charter's ratified DM example carries it with two prices (`MVP-CHARTER-v0_2.md:145`, quoted at ladder :590, proposal :139 / :151, report :43).
   - `73` redacts all three literals in every staged copy and requires a 0-count check.
   - `ASK DESK: is the Charter example line his real 09-03 fill? [18:59]`
   - Safe default: redact (as drafted). This changes no ruling, because the grammar stays at proposal §6.
4. **Packet size.** The MANDATORY core is ≈ 125–135 KB and the total ≈ 150–165 KB before cuts, against the ≤ 140 KB cap. This design touches far more code than stale-score.
   - The cut order drops the OPEN parts. If the core alone is over 140 KB, it is staged and escalated, not failed.
   - The 20-minute house timeout is unchanged and untested at this size. A TIMEOUT for grok or gemini is a no-ruling, not a retry.
5. **Stagger literal for `66`.** None of the reports of `38`, `61`, `66`, `68` or `69` exists yet. By `61`'s rule, the launch row must say `<nn> has stopped or will not run` for each one missing.
   - For `66` (the one-build check, likely 09-23+), "will not run" is untrue on TUE.
   - `ASK DESK: write "66 has stopped or will not run" meaning "will not run before 73 ends"? [18:59]`
   - Safe default as drafted: no literal, no launch.
6. **Departures from `61` / `62` / `63`, each deliberate:**
   - The packet uses `66`'s numbered MANDATORY / OPEN layout.
   - A REDACTION step (L32) is added, the one change allowed to a staged copy.
   - AUTHORIZATION greps R38 and R46, and fails on a Sol / Opus string (R46).
   - The stagger covers five hubs, and `61` under both report names.
   - `74` fails on a date after 09-22, because its claims could not be hub-checked after that.
   - 26 items: Q1–Q12 + (a)–(n).
7. **Facts seen while drafting.** These are not verdicts; the questions carry them to the houses (L35):
   - `mark_filled` commits `fill()`, then UPDATEs the fill columns in a second connection (`aset/store.py:217`, `:230`).
   - The sheet's `/card/{id}/stop` route (`aset/web.py:1239`) is a writer of `stop` that F9 does not list.
   - `taxonomy/trade_note_migration.py` and `taxonomy/cli.py` touch trade notes.
   - `card_stop_edits` and `aset_sizings` come from other migration sets (`cards/migrations/`, `aset/migrations/`) than the proposal's M1 assumes.
   - `evaluate.py:776` falls back to `card.entry` when `last_price` is NULL.
   - Radar card creation happens at formation, but the daily-note unit is keyed to `created_at` (`web.py:1336`).

L74: no instruction block arrived inside a tool result this run. This seat committed nothing and sent nothing.

## CONTINUE
None; the run is complete. Next steps belong to the desk:
- L35 on `73` / `74` / `75`.
- Commit the proposal, its report, the prompts and this report.
- Ask him about the Fable seat (ESCALATE 2) and the Charter example (ESCALATE 3).
- Write `73`'s launch row with the stagger literals.

S3 EXITS TRIBUNAL PROMPTS DRAFTED · prompts: 3 · astra: REQUIRED · questions: 26 · packet: 140 KB · new rule strings: 0 · ESCALATE: 7
