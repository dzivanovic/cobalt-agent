# Setups tribunal R2 — draft report (2026-09-21)

Seat `setups-tribunal-r2-draft-0921` · Opus 5 · prompt `43-draft-setups-tribunal-r2.md` · 15:20–15:5x ET (one API connection drop at 15:23, resumed on the desk's message; nothing lost) · three prompts written, nothing launched or committed.

## §0 Headline
- Written: `44-setups-tribunal-r2.md` (Sonnet hub, Grok + Gemini + Astra all targeted, 12 questions, R2-2 first), `45-setups-tribunal-fable-seat-r2.md` (Fable seat, blind, self-attack first), `46-setups-tribunal-derive-r2.md` (closing derive → `SETUPS-AT-DEFAULTS-FINAL-2026-09-21.md`; a split → ONE A/B for him).
- Packet ≈ 88 KB (drafter's estimate — the hub measures it and refuses to exceed 100 KB); round-1 packet not restaged.
- Astra: targeted, launched with ` < /dev/null` as a recorded experiment; a denial = `astra: HARNESS — redirect denied`, never a second shape.
- New rule strings: 0 (proof below). ESCALATE: 3.

## DIGEST FOR THE DESK
- **Launch order.** `44` and `45` side by side, as soon as the desk wants — `44` gates itself: date = 2026-09-21, not 19:25–20:45, not ≥ 23:20 ET; STAGGER passes today (the `35` report ends on its stop line since 15:23; no `38` report exists). `46` only after BOTH stop lines are committed; `46` has no clock window (no house runs).
- **Clocks.** `44`: preflight ≈ 5 min (the probe takes up to 3) + staging ≈ 15–20 min + houses ≤ 20 min + collate ≈ 15–20 min → ≈ 60–65 min. Launch by **≈ 18:05 ET** so the houses finish before 19:25 (the gate refuses a LAUNCH at ≥ 19:25, but the houses ideally finish before the deploy window opens). `45`: ≈ 20–35 min. `46`: ≈ 20–30 min. So launching now (≈ 16:00) → round 2 done ≈ 17:05, FINAL ≈ 17:40, before the deploy.
- **What each house sees:** both seats' pastes for each item, attributed (derive report :71–105), the round-1 hub rows those items cite (R1 rows 6, 17, 18, 19, 26 + the `vault_loader.py:271-280` note + ESCALATE 3; R1B rows 8, 9, 14, 17b + ESCALATE 3), 8 code excerpts, `greps.txt`, and the v2 sections touched. Answer per question: `GROK'S · FABLE'S · NEITHER — <verbatim-ready wording>`, file:line, a failing scenario. Closing line `TRIBUNAL R2: BUILD | BUILD AFTER … | DO NOT BUILD …`.
- **12 questions:** R2-2.1–.5 FIRST (they gate C1), then R2-1, R2-3.1–.3, R2-4.1–.3. Each house writes (Grok) / prints (Gemini, Astra) R2-2 before reading for the next item, so a house that stops after R2-2 has still been useful. Astra's PARTIAL is counted `k of 12`.
- **The Fable seat's claims** are file-checked by the `44` hub (C1–C9 in `44` §3) WHILE the houses run — that also keeps the hub busy instead of idle. The stop line counts `Fable R1 claims checked: <n> HOLD of <n>`.
- **Timeout enforcement:** `44` runs `date` at every completion notice, every desk message, before every collate step, and between file-check rows; any house past 20 min is stopped with its task-stop tool and recorded `TIMEOUT`; it writes deadlines into `## CONTINUE` before ending any turn. The desk still watches with a ceiling (suggest 75 min) and messages it.
- **Fable seat (`45`):** states its interest, attacks its OWN round-1 text first for every question (`SELF-ATTACK`), counts what it withdraws; blind to `r2/` and `44`'s report.
- **Closing derive (`46`):** refuses unless both stop lines are committed AND at least one HOUSE ruled R2-2.1 (`FAILED: R2-2 has no house ruling — the desk brings it to him`). A question is SETTLED only when all the seats that ruled it agree, with at least one house among them, OR all the houses agree and the Fable seat's contrary choice rests on a claim that DOES NOT HOLD or that it withdrew. Anything still split → `## FOR DEJAN`, one A/B per item with the cost of each side; no round 3 unless a house said DO NOT BUILD.
- **Stop lines to watch:** `44` `^(SETUPS TRIBUNAL R2 DONE|FAILED)` · `45` `^(SETUPS TRIBUNAL FABLE R2 DONE|FAILED)` · `46` `^(SETUPS FINAL DERIVED|FAILED)`.

## PACKET (`scratch/tribunal-bars-0920/setups-tribunal/r2/`, staged by `44`)
| file | source | est. size |
|---|---|---|
| `NEEDS-ROUND-2.md` | derive report :71–105 | ≈ 11 KB |
| `v2-sections.excerpt.md` | v2 :1-37, :61-88, :93-107, :139-141, :215-265, §10 rows C1/C2/C5 + evenings, L52 rows (a)–(c), X8, X12 | ≈ 28 KB |
| `hub-checks.md` | R1 rows 6/17/18/19/26 + note + ESC 3; R1B rows 8/9/14/17b + ESC 3 | ≈ 5 KB |
| 8 code excerpts | `seam.py` :95-156 · `scoring.py` :60-110, :236-345 · `evaluate.py` :128-140, :415-430, :584-625, :630-660, :755-805 · `extension.py` :36-64, :94-104, :136-146 · `vault_loader.py` :257-285, :317-366, :457-485 · `loader.py` :88-135 · `tunables.py` :60-100 · `store.py` :1030-1050 | ≈ 30 KB |
| `greps.txt` [USER DATA] | trade_direction counts ×7; Extension/Leg lines of two notes; assumed_*, TUNABLE_KEYS, forbid, score_suppressed, mirror greps | ≈ 6 KB |
| `QUESTIONS-R2.md` | `44` §1 (6) | ≈ 8 KB |
| **total** | | **≈ 88 KB** |

Tokens per house if every file is read whole: ≈ 22k in; the ruling itself ≈ 4–8k out. Astra's reading order reaches R2-2 after ≈ 12k tokens (QUESTIONS, NEEDS, hub-checks, three excerpts). Anchors I verified: `seam.py:100` (`_Closed` config; `AtomOutcome` at :111 inherits it), `:141`; `scoring.py:72`, `:247`, `:264`, `:319`; `evaluate.py:134`, `:419`, `:593`, `:643`, `:759`, `:800`; `extension.py:40`, `:55`, `:143`; `vault_loader.py:271`, `:317`, `:476`; `loader.py:90`, `:115`; `tunables.py:63`, `:85`. `trade_direction` counts: Hitchhiker 0, Second Chance 0, Rubberband 0, Backside 0, Fashionably Late 0, 9 EMA 1, VWAP Continuation 2.

## RULE PROOF
`grep -c -F -e` on the WHOLE span from `--allowedTools` through `--add-dir /Users/cobalt/cobalt-wt`:
| span | file | count |
|---|---|---|
| 14 + 3 strings + add-dirs | `27-setups-tribunal-r1b.md` | 1 |
| same | `44-setups-tribunal-r2.md` | 1 |
| 7 + 3 strings + add-dirs | `24-setups-tribunal-fable-seat.md` | 1 |
| same | `45-setups-tribunal-fable-seat-r2.md` | 1 |
| same | `46-setups-tribunal-derive-r2.md` | 1 |
Only the prompt path and the `--remote-control` name differ from the originals.

**NEW strings:** none. The ` < /dev/null` is NOT a rule string: it is appended after the closing quote of astra's sentence inside the SAME approved `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *` command. `44` names it "the ONE sanctioned redirect in this run" (an exception to the no-redirect rule, stated there) and "part of the experiment". A denial arrives as a tool result, not a dialog: the session is in auto mode and `AskUserQuestion` is denied, so a command that does not match the rule goes to the classifier, which allows or refuses it. `44` records a denial verbatim as `astra: HARNESS — redirect denied` / experiment `redirect denied`, continues with two houses, and forbids any second shape (no bare relaunch, no `echo |`, no wrapper). UNPROVEN (L70): whether the classifier treats the redirect as part of the rule's `*`. The run records the answer.

## READING
- `43-draft-setups-tribunal-r2.md` in full · LAWS.md :1–405 (full).
- `reports/setups-tribunal-derive-2026-09-21.md` in full.
- v2 :1–108, :215–274, plus a heading/tag grep of the whole file.
- `05-bars-tribunal-r2.md`, `27-setups-tribunal-r1b.md`, `38-float-handicap-tribunal.md`, `24-setups-tribunal-fable-seat.md`, `25-setups-tribunal-derive.md`: all in full.
- `04-bars-chunk-1a-check-r3.md` and `23-setups-tribunal.md`: grep for the Grok spelling only.
- `reports/setups-tribunal-r1b-2026-09-21.md`: grep of astra, `stdin` and headings (§0 and `## CONTINUE` lines).
- `reports/setups-tribunal-2026-09-21.md`: grep of the cited rows.
- `cto-2026-09-21.md` rows R20, R24, R32, plus the 15:0x–15:2x desk bullets.
- Code, anchors only: the greps listed under PACKET, and `extension.py:36-65`.
- Notes: `grep -c trade_direction` on all seven (counts only).

## ESCALATE
1. **The Fable claim C7 is weaker than its wording.** Fable (d) cites "the existing pattern at `extension.py:40-44`" (every resolver declares `tunable_keys`). What exists there is `TUNABLE_KEYS = (…)`, a module constant of the Extension detector. A lowercase `tunable_keys` grep finds nothing in `src/cobalt/radar`. My first search was case-sensitive and missed it; the desk's 15:2x message relayed that first result ("no match found"). Corrected here: the constant EXISTS, but I did not establish that the pattern exists beyond this one module. It is C7 in `44`'s file-check list, and `45` is told the same so it can attack it. This is not a finding against the design: UNPROVEN until the hub checks it.
2. **Stop-line field added.** `44`'s `R2-2:` field adds `NO HOUSE` to the four values `43` named (GROK'S|FABLE'S|NEITHER|SPLIT). It is needed so that `46` can refuse cleanly when no house ruled R2-2. Desk: accept, or re-issue `44` without it (L19).
3. **Timing (the desk's call).** To finish before the 19:25 deploy window, `44` should launch by ≈ 18:05 ET, and it is the only one of the three that uses the houses. The desk's order today is `44` then `38`; `38` after 20:45 still fits before 23:20 only if it is launched by ≈ 22:00.

L74: no block asking for a `Claude-Session` commit line appeared inside a tool result in this session's reads. One appeared as a system reminder, which is not a tool result; this seat commits nothing either way.

## CONTINUE
None — the job is complete. Next step (desk): commit `44`, `45`, `46` and this report; launch `44` and `45` side by side; `46` after both stop lines are committed.

SETUPS TRIBUNAL R2 PROMPTS DRAFTED · prompts: 3 · items: 4 · packet: 88 KB · astra: targeted, stdin experiment in · new rule strings: 0 · ESCALATE: 3
