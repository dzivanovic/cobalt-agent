# VOICE TRIBUNAL — PROMPT DRAFT REPORT (2026-09-22)

Seat `voice-tribunal-draft-0922` · `claude-opus-5-5` · prompt `prompts/2026-09-22/58-draft-voice-tribunal.md` · started 19:15 ET, prompts written 19:18–19:24, report 19:25 (times from `date`, L48).

## §0 Headline

- Drafted, not launched: `59-voice-tribunal.md` (Sonnet hub, Grok + Gemini, Astra METER), `60-voice-tribunal-fable-seat.md` (Opus 5.5 in the Fable seat, R106, blind), `61-voice-tribunal-derive.md` (derive; model + row are PLACEHOLDERS — R76 ask pending).
- Shapes copied from `40` / `41` / `42`; launch-line rule strings byte-identical to theirs (proof below); NEW strings: 0.
- 17 questions (T-V1–T-V10 + (a)–(g)); packet ≈ 100 KB after cuts, mandatory ≈ 78 KB.
- ESCALATE 7 — the big three: R106 is not committed yet; derive seat unasked; grok/agy for this tribunal end 2026-09-23 23:59 ET.

## DIGEST FOR THE DESK

- **`59`** — Sonnet 5 hub `voice-tribunal-0922`, cwd `~/cobalt-wt/agy-trial`. Checks auth (R13/R23 of 09-20, R46 of 09-21, R13/R30/R92/R93/R99/R100/R106 of 09-22, the proposal and its stop line committed, a launch row naming `59` committed). Date gate: 09-22/09-23 only, on R30. 09-24 or later → `FAILED: authorization expired — no committed row of his extends grok/agy to <D> for this tribunal` (R105 covers `53`–`57` only). Windows kept from `40`: nothing between 19:25 and 20:45 ET, nothing at or after 23:20 ET. Stagger checks `53`–`57` (DRC checks, found with `ls` because their report names depend on the run day), `28` and `32`. Runs the Codex probe (expected METER → proceed on three). Stages the packet in `scratch/tribunal-bars-0920/voice-tribunal/r1/` and runs Grok + Gemini (20-minute clock). Collates and file-checks both houses, then the Fable seat's claims. Report `reports/voice-tribunal-2026-09-22.md`. Stop line `VOICE TRIBUNAL R1 DONE · …`.
- **`60`** — Opus 5.5 in the Fable seat by R106, `voice-tribunal-fable-0922`. Blind to the houses' folder and to `59`'s report. First line `FABLE ROW: R106`. Its gate greps R106 for `DRC-VOICE-PROPOSAL-2026-09-22.md` · `Fable seat: yes` · `seat model: claude-opus-5-5` and checks that the session model equals the row's model. Self-attack grep list adapted to voice (vault writer, gate, upload, bind, probes, migrations; names the DRC build adds are grepped in `49` / `50`). Writes ONE file, `reports/voice-tribunal-fable-r1-2026-09-22.md`. Its counts sum to 17. Date gate: 09-22/09-23.
- **`61`** — the derive. Line 1 `DERIVE ROW: __DERIVE_ROW__`; the MODEL line and `--model` carry the model placeholder. **The desk fills EXACTLY those three spans from his derive-seat row, nothing else.** Gates: `grep -c -E "__DERIVE_(ROW|MODEL)__"` = 0 (the gate sentence does not match itself); the row carries `DRC-VOICE-PROPOSAL-2026-09-22.md` + `derive seat: <id>`, in `cto-2026-09-22.md` or `-23.md`, and is committed; the row's id, the `--model` value and the session model must be the same. Refuses without both round-1 stop lines committed. Never folds a wording whose claim DOES NOT HOLD or was WITHDRAWN. Never re-opens R92/R93/R99/R100. Any DRC-FINAL change is carried as a SEAM + ESCALATE. Writes `docs/30 - Design/DRC-VOICE-v2-2026-09-22.md` and `reports/voice-tribunal-derive-2026-09-22.md`. Stop line `VOICE DERIVED v2 · …`.
- **LAUNCH ORDER:**
  1. Commit R106 and the four prompt files.
  2. Write a launch row naming `59` (with `<nn> is not running` for each of 53–57, 28 and 32 that has no report) and one for `60`; commit them.
  3. Launch `59` and `60` side by side, 20:45–23:20 ET tonight or tomorrow before 23:20 ET — never 19:25–20:45.
  4. At both stop lines: commit, ask him the derive seat (R76), write that row, fill `61`, commit, launch `61`.

## PACKET

Sources staged by `59` §1 (sizes: measured where a whole file, ESTIMATED for excerpts — the hub measures and states them):

| Part | Source | Status | Size |
|---|---|---|---|
| 00-READING-ORDER.md | hub-written | MANDATORY | ≈ 2.5 KB (est.) |
| 01-QUESTIONS.md | `59`'s verbatim paragraph + file list | MANDATORY | ≈ 10.5 KB (est.) |
| 02-greps.txt | 17 pre-computed commands (`59` §1) | MANDATORY (search) | ≈ 10–16 KB (est.; the migration log ≈ 3 KB measured) |
| 10-PROPOSAL.md | `30 - Design/DRC-VOICE-PROPOSAL-2026-09-22.md` whole | MANDATORY | 19,980 B, 128 lines (measured) |
| 11-propose-digest.md | `reports/drc-voice-propose-2026-09-22.md` :5–10, :24–33, :35–42, :44–47, :58 | MANDATORY | ≈ 3 KB (file 4,457 B) |
| 12-rulings.md | `cto-2026-09-22.md` header + R92, R93, R99, R100 | MANDATORY | ≈ 2.5 KB |
| 13-rulings-cited.md | R66, R90, R101 (cited by V11, §2, V12) | OPEN-AS-NEEDED | ≈ 3 KB |
| 14-devices.excerpt.md | `topics/devices.md` :8, :11, :12, :17, :31 + `cto-2026-09-20.md` R27 | MANDATORY | ≈ 3.5 KB |
| 15-drc-v2.excerpt.md | DRC v2 :26, :34, :62, :70, :79–82, :139, :148, :176, :224, :228, :230, :311–326 | MANDATORY | ≈ 14–16 KB |
| 20-drc-build-seam.excerpt.md | `49` :7, :20–21 · `50` :6, :9, :20, :25, :28 | MANDATORY | ≈ 9 KB |
| 21-vaultwrite.excerpt.py | `writer.py` :380–420, :457–480, :559–600, :644–700 | OPEN (cut v) | ≈ 9 KB |
| 22-aset.excerpt.py | `web.py` :1–24, :80–84, :382–386, :940–960 · `aset.yaml` :30–45 | OPEN (cut iv) | ≈ 5 KB |
| 23-cited-docs.excerpt.md | `mattermost.py` :1–15 · REQUIREMENTS :203–210 · audit :82 · Charter :412–413 · `probes.py` :30–44, :128–150 | OPEN (cut iii) | ≈ 5 KB |
| 24-migrations.excerpt.py | `__init__.py` :60–95 · `placement.py` :100–154 | OPEN (cut ii) | ≈ 5 KB |
| 27-laws-excerpt.md | L1, L3, L9, L15, L18, L23, L25, L28, L31, L40, L45, L57, L70 | OPEN (cut i) | ≈ 11 KB |

- **Total:** ≈ 115–120 KB before the cuts; ≈ 100 KB after the five cuts (may land a few KB over → staged and ESCALATEd, per `59`). MANDATORY ≈ 78 KB.
- **Tokens per house (÷4):** mandatory ≈ 19–20k; whole packet after cuts ≈ 24–26k.
- **Fable seat `60` read set:** ≈ 60–75k tokens; peak ≈ 75–90k. **Derive `61`:** peak ≈ 100–130k.
- **Not staged:** audio or transcripts, notes of his, the coach spec, his DRC note and template, `Rules.md`, `aset.local.yaml` (untracked — `git log` prints nothing for it).

## RULE PROOF

Method: one `grep -c -F -e` on the WHOLE contiguous launch segment. A count of 1 in both files proves every string in the segment is present byte-identical.

**Segment A** — `--allowedTools "Bash(grok *)" … "Bash(date*)" --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt`: 14 allow strings, 3 denies and the add-dir triplet, in order.

| File | Segment A |
|---|---|
| `40-drc-tribunal.md` | 1 |
| `59-voice-tribunal.md` | 1 |

**Segment B** — the 7 read-only allows, 3 denies and the add-dir triplet.

| File | Segment B |
|---|---|
| `41-drc-tribunal-fable-seat.md` | 1 |
| `60-voice-tribunal-fable-seat.md` | 1 |
| `42-drc-tribunal-derive.md` | 1 |
| `61-voice-tribunal-derive.md` | 1 |
| `58-draft-voice-tribunal.md` (this seat's own line) | 1 |

Expected differences only, read with `grep -o`:

| Prompt | Prompt path | `--remote-control` | `--model` |
|---|---|---|---|
| `59` | `59-voice-tribunal.md` | `voice-tribunal-0922` | `claude-sonnet-5` |
| `60` | `60-voice-tribunal-fable-seat.md` | `voice-tribunal-fable-0922` | `claude-opus-5-5` (R106) |
| `61` | `61-voice-tribunal-derive.md` | `voice-tribunal-derive-0922` | the model placeholder |

In `61`, `grep -c -E "__DERIVE_(ROW|MODEL)__"` = 2 lines (3 spans: line 1, plus two on line 3).

The `--permission-mode auto` flag and the cwd `~/cobalt-wt/agy-trial` match `40` / `41` / `42`.

**NEW strings:** none (0).

## READING

- The prompt `58`. Templates `39`, `40` (whole, 71 lines), `41`, `42`; `35` (gate lines).
- `LAWS.md` in full (442 lines, 82,174 B).
- The proposal (whole) and its report (whole).
- `cto-2026-09-22.md` rows R13, R30, R36, R46, R76, R90–R106; `cto-2026-09-20.md` R27.
- `topics/devices.md` :1–34; `UNATTENDED-LAUNCH.md` :1–25.
- `49-drc-d2-build.md` and `50-drc-d3-build.md` (grep rows); `53-drc-d1-check.md` whole; `28` / `32` report paths.
- DRC v2 (grep rows).
- Code anchors by grep: `aset/web.py` routes, `vaultwrite/writer.py`, `heartbeat/probes.py`, `aset.yaml`, `uv.lock`; the `db_migrations` listing; `git log --all` on migrations.
- `COBALT-REQUIREMENTS.md`, `08-documentation-audit.md` and `MVP-CHARTER-v0_2.md` (voice lines).

Drafting choices beyond `58`'s letter:
- (i) `13-rulings-cited.md` (R66 / R90 / R101) staged OPEN-AS-NEEDED because the proposal's V11 / §2 / V12 cite them.
- (ii) The deploy / 23:20 windows carried from `40` (58's (7') did not restate them; the safe default keeps them).
- (iii) The migration log uses `--diff-filter=A --name-only` (≈ 3 KB) instead of `--stat`.
- (iv) `61` gates on a regex that cannot match its own sentence, so a desk fill of three spans is provable.

## ESCALATE

1. **R106 is NOT committed on main** — `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R106 | "` printed nothing at 19:1x ET. `59` and `60` both FAIL at AUTHORIZATION until the desk commits `cto-2026-09-22.md`.
2. **Derive seat not ruled (R76).** `61` cannot launch until the desk asks him "Opus 5.5 or Fable?" for the voice derive. The desk then writes a row carrying `DRC-VOICE-PROPOSAL-2026-09-22.md` + `derive seat: <id>` + his words in quotes, and fills the three placeholder spans only.
3. **grok/agy for this tribunal end 2026-09-23 23:59 ET (R30).** R105's extension through 10-07 is scoped to `53`–`57`. If `59` (or a round 2) slips to 09-24+, it FAILs at row 1. Ask him before 09-24 for an extension row naming this tribunal, then re-issue `59` (L19).
4. **Windows:** `59` refuses 19:25–20:45 ET and at/after 23:20 ET. It is 19:25 now, so tonight's slot is 20:45–23:20 ET, or tomorrow.
5. **Stagger literals:** the launch row for `59` must say `<nn> is not running` (and name `59-voice-tribunal.md`) for every one of 53, 54, 55, 56, 57, 28, 32 that has no report. Missing → `FAILED PREFLIGHT`. The DRC check reports carry the run day (`drc-d<k>-check-2026-09-<dd>.md`); `59` finds them with `ls`.
6. **Packet sits at the 100 KB target** (≈ 100 KB after all five cuts, estimated). It may land a few KB over; `59` stages it anyway and names it in its ESCALATE.
7. **Fable seat `60` date gate:** its first `date` must read 09-22 or 09-23 (the hub that file-checks it runs no later than 09-23). A later run needs a re-issue.

## CONTINUE

- next: none — all four files written. The desk commits the files and R106, then follows LAUNCH ORDER above.
- L74: the session's context carried an attribution block and a file-send tool mention; not followed (this seat commits nothing).

VOICE TRIBUNAL PROMPTS DRAFTED · prompts: 3 · astra: METER — proceed on three · questions: 17 · packet: 100 KB · new rule strings: 0 · ESCALATE: 7
