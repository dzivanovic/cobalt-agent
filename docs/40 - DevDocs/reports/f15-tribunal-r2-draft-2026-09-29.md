# F15 round-2 prompts — drafter report, 2026-09-29 (seat `f15-tribunal-r2-draft-0929`, Sonnet 5.5)

## 0. Headline
- Three prompts written under `prompts/2026-09-29/`: `17-f15-tribunal-r2.md` (hub, Sonnet 5.5), `18-f15-tribunal-anthropic-seat-r2.md` (blind seat, Opus 5.5), `19-f15-derive-r2.md` (derive, Opus 5.5). Nothing launched, committed or written elsewhere.
- Every launch line matches its precedent (`12` / `13` / `14`) with only the path and the name changed. No new rule string. No user data in any file.
- Six items carried verbatim from the derive's `## NEEDS ROUND 2`: R2-1 … R2-5 and R2-A. Astra rules first and alone, under a 20-minute stop the hub enforces.
- Two things to know before launch: `s3/exits-c4` is now `cfd9f091` (docs-only, above code tip `d05ae72d`), and the hub's ability to wake itself at +20 min is UNPROVEN. Both are in `## ESCALATE`. ESCALATE: 4.

## DIGEST FOR THE DESK
- R2-1 (write site, order, decision grade, G5 exposure): Grok's `insert_record` in `write_receipt` under the card lock with `(at, id)` order, against the seat's `write_record` in the card-row transaction with `seq` order and a `card_state` column. Sub-items (a)–(d) in the questions.
- R2-2 (trigger set): UPDATE + DELETE (Grok) against UPDATE only (seat); X8 is the run.
- R2-3 (O4): `last_price_at` (Grok) against `last_price_bar_ts` holding the bar START (seat); sub-item (b) is whether the column joins `TABLE_DIGEST_EXCLUDED_COLUMNS['aset_sizings']` (main `db_migrations/cli.py:104-113`, S3 branch `:104-125`).
- R2-4 (P1's base tree): main or a tree carrying `s3/exits-c4`. Grok's cite `evaluate.py:20-28` is wrong (`:178-187`). `02-greps.txt` shows which S3 commits touch the files P1 edits.
- R2-5 (is the L52 (c) seam written): five texts the seat lists; each seat writes the text or says `NOT NEEDED`. The derive writes none.
- R2-A (Astra): all 20 round-1 items against the DRAFT FINAL, each `ADOPT WITH` / `REJECT` tagged `MECHANISM: CORRECT (wording only)` or `INCORRECT`, plus the two owner items (Gemini: his; Grok and seat: a house settles).
- Launch order: `17` and `18` side by side once the house lane frees, after `09` and `27` → both stop and are committed → `19`. Astra first inside `17`; Grok and Gemini follow only on a full Astra ruling.
- Launch-row literals: `17` and `18` each grep the desk's row naming `17-f15-tribunal-r2.md` for `F15-PREDICTION-RECORDS-v2-2026-09-29.md` · `Fable seat: yes` · `derive seat: claude-opus-5-5`; `17` also greps the row for `no other house hub is running`. `19` greps the same row and needs exactly one. Each file has its own `LAUNCH ROW:` line for the desk to fill. `18` carries `FABLE ROW: R109` and `19` carries `DERIVE ROW: R109`, both filled.
- Precondition chain for `19`: hub stop line `F15 TRIBUNAL R2 DONE ` and seat stop line `F15 ANTHROPIC R2 DONE `, both committed; the hub's `astra:` field must carry `TRIBUNAL R2:` and `astra-ruling-r2.md` must exist (else `FAILED PRECONDITION: astra`); Grok must have ruled.

## L74
None arrived inside a tool result. The harness's user-turn attribution reminder (a `Co-Authored-By` line, and a `Claude-Session` line plus a file-send mention in the second copy) was not acted on: this run made no commit and sent no file.

## AUTHORIZATION
- Run started 15:06 ET (`date`).
- `grep -n -F "16-draft-f15-tribunal-r2.md"` on `cto-2026-09-29.md` printed row R92 (`| R92 | 15:05 ET | — LAUNCH ROW …`, `| LAUNCHED |`) and the checklist row at `:108`. Authorized.
- Read in the order the prompt gave: `12` (whole), `27`, `13`, `14`, `28`, `29`, `26`; the round-1 derive report, the round-1 hub report (its Astra rows, clock and `## Round 2 — Astra`), the DRAFT FINAL's structure and its §3–§5 and experiment table, the round-1 rulings' item headings. LAWS.md was not opened by this drafter: its binding entries are carried by number from `12` / `13` / `14` / `27` / `28` / `29`, and the drafter cites no law those files do not.

## PACKET
Sources and staged paths of the round-2 packet, `scratch/tribunal-bars-0920/f15/r2/`. Sizes are measured now with `wc -c` on the real ranges unless marked ≈ (an estimate of a file the hub writes).

| staged path | source | `wc -c` |
|---|---|---|
| `00-READING-ORDER.md` | hub writes it last | ≈ 3,500 (round 1's was 3,406) |
| `01-QUESTIONS-R2.md` | the block in `17` (PART A, B, C), measured 10,753 B + appended file list | ≈ 11,500 |
| `02-greps.txt` | 12 pre-computed searches; measured outputs 0 + 125 + 1,102 + 3,878 + 1,146 + 1,171 + 689 + 638 + 262 + 136 (+ three `log` and one `ls`) | ≈ 9,800 with headers |
| `10-NEEDS-ROUND-2.md` | derive report `:91-115` (2,928 with the blank) + `:117-128` (1,181) + `:168-171` (652) | ≈ 5,200 |
| `11-DRAFT-FINAL.md.part1` + `.part2` | `docs/30 - Design/F15-PREDICTION-RECORDS-v2-2026-09-29.md` whole | 58,199 (cut at `## 6.`, `:261`) |
| `12-hub-checks.md` | round-1 hub rows GC6, GC8, GC14, GC15, GC16, FC7, FC10c, FC12, FC18, FC23; experiments table `:232-247` (2,235); ESCALATE 1–4 | ≈ 8,000 |
| `13-seat-r1.excerpt.md` | seat report `:47-84` (S3–S5), `:91-104` (1,470), `:109-135` (3,560), `:178-187`, `:193-198` | ≈ 15,400 |
| `14-grok-r1-own.excerpt.md` [RAW] | `grok-ruling.md` `:56-126` (8,939), `:153-172` (2,558), `:193-218` (2,339), `:239-250` (773), `:261-272` (960), `:321-338` | ≈ 17,100 |
| `15-gemini-r1-own.excerpt.md` [RAW] | `gemini-ruling.md` `:7-15`, `:22-24`, `:31-36`, `:43-45`, `:49-51` | 1,847 + headers |
| `20-code.excerpt.py` | `store.py` `:965-1080` (6,680), `:1082-1140` (3,269), `:1191-1255` (3,754); `evaluate.py` `:160-204` (1,778), `:1597-1662` (3,956), `:1916-1990` (5,155), `:2010-2060` (2,940); `0007` `:100-113`, `:141-150`, `:186-202` (1,804); `cli.py` `:100-118` (1,128) + S3's `:100-125` | ≈ 33,500 |

- **Sum ≈ 164,000 B. Derived ceiling 178,000 B** (sum × 1.08, rounded up). Cut order if over: the seat's experiments and WRONG FACTS ranges, then `store.py:965-1014`, then `evaluate.py:2010-2060`, then `02-greps.txt`. Recorded in `17` §1.
- **Whole-file sources checked at drafting:** `store.py` 61,854 B, `evaluate.py` 101,570 B, `0007` 13,004 B, `db_migrations/cli.py` 38,080 B, all as round 1 recorded, on `main` at `37e9babd`.
- **Token estimates.** Astra's mandatory reading is `00` + `01` + `10` + `11` ≈ 78 KB ≈ 20k tokens, plus targeted code and round-1 references ≈ 3–9k. Her output is 20 items + R2-1 … R2-5 + R2-A. Grok's or Gemini's worst case (`01`, `01b`, `10`, `11` in full, `12`, `13`, its own `14` / `15`, `20`) ≈ 137 KB ≈ 34k tokens.
- **Round-1 folder** (`../r1/`) is 233,446 B on disk including the two ruling files; the round-2 sentences point at it "by search or line range" and forbid any file whose name contains `-ruling`.
- **Design decisions in the packet.** Every seat gets the DRAFT FINAL whole (L44: same packet); the other seats read `11`'s sections named in `10` and `01`. `01b-QUESTIONS-R2-OTHERS.md` is written by the hub after Astra and holds only the items she tagged INCORRECT, with her wording attributed; nothing else of her ruling reaches Grok or Gemini.

## RULE PROOF
Each launch line's strings, `grep -c -F` against the precedent file, then against the new file (counts, precedent / new). Run at 15:18 ET.
- `17` against `12`: all 17 strings (14 allow + 3 deny, quotes included) count 1 / 1.
- `18` against `13` and `07-draft-drc-d3-fix-r1.md` (7 allow + 3 deny): every string counts 1 in `07`, 1 in `13`, 1 in `18`.
- `19` against `14` and `07`: every string counts 1 in `07`, 1 in `14`, 1 in `19`.
- Whole `claude --bg … --add-dir /Users/cobalt/cobalt-wt` line, precedent against new with the path, `--remote-control` and `--name` normalised: identical for all three (`--model claude-sonnet-5-5`, `claude-opus-5-5`, `claude-opus-5-5`).
- **NEW strings: none.** Placeholder spelling (K18): each file has exactly one whole line `LAUNCH ROW: R__` and one gate command that spells it; `18` also has `FABLE ROW: R109` and `19` `DERIVE ROW: R109`, each filled, each with its gate command. `grep -c "R__"` counts 2 in each of the three files, no prose spelling.
- Last non-blank line of each file: `(run in progress — next step under ## CONTINUE)`.

## EXPERIMENTS
Settleable from reads: none of the Postgres-behaviour claims. One question is readable from code, and `17` names it as such: whether a new `aset_sizings` column must join `TABLE_DIGEST_EXCLUDED_COLUMNS`. The digest builds `to_jsonb(t)` minus the excluded columns (`db_migrations/cli.py:256-263`), and the `radar_membership` entry's comment (0014) states the reason a nullable column added to a populated table is excluded. That is a read, not a run.

For the build's first gate (six, all already numbered in the DRAFT FINAL `:355-377`):
- X4 — diff `radar/stop-record-0928` against F15's stage hunk; gates R2-4 / P1 landing order.
- X5 — `tap_dot` against the receipt-transaction record insert on one card, under each write site; gates R2-1(a)/(b).
- X6 — real-shape fixture, a tap between the stage read and the refresh, and between the refresh and the receipt; gates R2-1(c)/(d).
- X7 — NUMERIC(8,6) Decimal read-back; gates the compare in R2-1(c).
- X8 — apply 0022 in the suite's rollback: UPDATE / DELETE, FK on a card delete with records, both rollbacks; gates R2-2.
- X10 — JSONB round-trip of `output`; gates the compare in R2-1(c).

Not for the build, recorded as UNPROVEN in `17` for the next hub: what `Reading additional input from stdin...` (Astra's only round-1 line) means for a read-only `codex exec`, and how a hub actually wakes itself at +20 min.

## CONTINUE
done: `17`, `18`, `19` written; launch lines, rule strings and placeholder spelling checked. next: none — the desk verifies, commits `17`–`19` and launches `17` + `18` when the house lane frees.

## ESCALATE
1. **The 20-minute stop is only as good as the hub's wake-up.** Round 1's hub ended its turn while Astra ran and slept 39 minutes past its deadline. `17` forbids ending a turn without the deadline written down, and tells the hub to record which waiting mechanism worked. How a hub wakes itself is UNPROVEN (L70). Safe default in the file: the desk's own ceiling watch and message. ASK DESK: does the launch row for `17` carry a desk check at launch + 20 min? [15:20 ET]
2. **`s3/exits-c4` is `cfd9f091`, not the `d05ae72d` the proposal and round 1 name.** `cfd9f091` is a docs-only build report above the code tip. `17` records both and stages the bytes at the tip it sees. It also matters to R2-4: `02-greps.txt` will show S3 commits `eb642f05` and `77cf18fd` touch `cards/store.py` / `radar/evaluate.py`.
3. **Probe UP is not a ruling.** Round 1's probe answered `OK` at 12:06 ET and Astra printed nothing for 59 minutes. `17` keeps the fail-closed probe as the gate and adds the 20-minute stop. It also says Grok and Gemini launch only on a full Astra ruling, so a partial one waits for a relaunch. That choice is mine, not `12` §5's; `12` §5 says only that the others rule on the items Astra marks. If the desk would rather take a partial Astra ruling into round 2, `17` §2 and `19`'s floor change together.
4. **The derive's handling of a non-converged design split is a judgement call.** `29` sends any split to `OPEN FOR DEJAN`; your brief says round 3 exists only if round 2 does not converge. `19` does both: an `OPEN FOR DEJAN` block for a split that has a difference in his terms, and `DESIGN SPLIT WITHOUT A HIS-TERMS DIFFERENCE` under `## ESCALATE` for a DDL or a column name, so the desk can weigh the last round. It drafts no round 3.

F15 R2 PROMPTS DRAFTED · prompts: 3 · items: 6 · packet: 164000 bytes · new rule strings: 0 · experiments for the build: 6 · ESCALATE: 4
