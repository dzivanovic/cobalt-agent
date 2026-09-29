# F15 tribunal drafter — report (seat `f15-tribunal-draft-0929`, 2026-09-29)

## 0. Headline
- Wrote three prompts in `prompts/2026-09-29/`: `12-f15-tribunal.md` (round-1 hub), `13-f15-tribunal-anthropic-seat.md` (blind Opus 5.5 seat), `14-f15-derive.md` (derive).
- Shapes copy `2026-09-25/16`, `17`, `18`. Launch-line rule strings byte-identical to their precedents: 0 new.
- Delta from `16`: Astra sits in round 1 behind a fail-closed probe (METER → the round runs without her, the derive names a DRAFT FINAL, `12` §5 seats her in round 2); 20 items (S1–S8, O1–O6, L52 A–D, E1–E2); packet ceiling 200,000 B derived.
- Desk fills: `R__` in all three (launch row), the stagger sentence `no other house hub is running` in the launch row for `12`. Nothing committed, launched or run.

## L74
- No block arrived inside a tool result. The commit-attribution reminder (a `Claude-Session` line) arrived in a system-reminder turn, not a tool result; recorded once here as data, not followed; no commit made.

## AUTHORIZATION
- `grep -n -F "11-draft-f15-tribunal.md" cto-2026-09-29.md` printed R60 (11:48 ET, LAUNCHED; writes `12`, `13`, `14` and this report; strings = `07`'s seven) and the row-76 seat line. Authorization holds.
- Also read: R57 (his word), R58, R59 (the desk's readings of the proposal's ESCALATE 1–2), rows R17 / R19 of `cto-2026-09-24.md` (house strings standing).

## PACKET
`wc -c` of the ranges at drafting (main; `s3/exits-c4` for S3). The ceiling is the sum plus range headers plus drift, not a guess.

| Part | Content | Bytes | Class |
|---|---|---|---|
| 10 | proposal, whole | 30,357 | MANDATORY |
| 11 | proposer report, whole | 4,967 | MANDATORY |
| 12 | R57–R60, R109, R95–R97 rows + words `## R57` | ≈ 7,000 (estimate; the hub measures) | MANDATORY |
| 20 | `scoring.py` 17,040 + `models.py` :110-135 1,254 + `radar.py` :170-190 1,010 + `store.py` :1030-1060 / :1076-1140 / :1191-1250 (1,906 + 3,450 + 3,495) | 28,155 | MANDATORY |
| 21 | `evaluate.py` :160-204 / :615-630 / :1416-1506 / :1597-1662 / :1800-2064 (1,778 + 741 + 4,580 + 3,956 + 16,244) + `audit_export.py` :206-271 / :290-300 (3,478 + 593) + `replay/cards.py` :1-57 (3,233) | 34,603 | MANDATORY |
| 22 | 0007 :100-202 (4,501) + 0006 :76-109 (1,597) + 0009 :47-121 (4,063) + `placement.py` :100-115 (649) | 10,810 | MANDATORY |
| 25 | S3-EXITS-v3 :215-235 (5,113) + DRC v2 :30-45 (4,320) + ADR-0008 :125-135 (1,033) + ladder / charter rows (≈ 1.5 KB) | ≈ 12,000 | MANDATORY |
| 01 | question paragraph, measured in `12` | 8,949 (+ file list) ≈ 9,300 | MANDATORY |
| 02 | pre-computed greps | ≈ 12,000 (estimate) | MANDATORY |
| 23 | `cli.py` :190-245 (2,635) + `aset/web.py` :1355-1370 (648) + `evaluate_cli.py` :405-415 (500) + test :97-132 (1,928) | 5,711 | OPEN |
| 24 | `0021_legs.sql` 5,672 + `legs.py` :107-112, :677-705 (≈ 2,100) | ≈ 7,800 | OPEN |
| 27 | LAWS L1 L3 L7 L8 L10 L28 L32 L45 L52 L57 L67 L68 L72 L75 L76 (measured by awk) | 14,649 | OPEN |

- Parts ≈ 177 KB + ≈ 5 KB range headers = **≈ 182 KB** whole; MANDATORY ≈ 154 KB.
- **Ceiling 200,000 B** (≈ 182 KB + ≈ 8 % drift ≈ 196 KB). Cut order in `12` §1: laws → `24` → `23` → `evaluate.py` :1800-2064 down to :1800-1849 and :1926-2017. The core (`00`, `01`, `02`, `10`, `11`, `12`, `20`, `21`, `22`, `25`) is never cut.
- Whole-file sizes for the hub's drift check are in `12` §1. Sizes of files that may move (`store.py`, `evaluate.py`) are re-checked by the hub; a moved file is staged as read, at the anchors' lines.
- `s3/exits-c4` tip: `git rev-parse` failed on my combined call (`Needed a single revision`); `git show s3/exits-c4:…` worked. The hub proves the tip itself and names any drift from the proposal's `d05ae72d`.

## NEW STRINGS
0. Launch lines: `12` = `16`'s 14 allow + 3 deny + `--add-dir` triplet (compared with `grep -o`/`diff`: identical after the prose; only the path, the remote-control name, `--name` and the model `claude-sonnet-5-5` differ). `13` and `14` = `17`'s and `18`'s seven allow + three deny (identical). Astra's slug `gpt-6-astra` and Gemini's `gemini-3.1-pro-high` are unchanged in the newest precedents / `~/.codex/models_cache.json`. Astra's launch spelling is `2026-09-21/38` line 47's; its sentence is that one re-pointed at this folder and these items.

## OWNER ITEMS
The proposal's two, carried to the derive's `## FOR DEJAN` only if the tribunal agrees they pass the test:
1. Cards graded before F15 lands stay partly unreplayable (tap results and settings were never stored). Owner test: his law (L57) and his data; a house can price a backfill but cannot decide to accept the gap. ASSUMED default: accept, no backfill.
2. Corpus retention: every tap record copies his `card.proposed_key` bands and enabled keys into a USER row. Owner test: his data (L32); a house cannot decide his retention. ASSUMED default: keep, USER side only, never pruned or shipped.
- `01-QUESTIONS.md` asks each house to say whether each passes or a house can settle it. No third item identified by the drafter. No chunk's build depends on either.

## CONTINUE
- Done. The desk commits `12`–`14` and this report, fills `R__`, then launches `12` (one Grok hub at a time) and `13` beside it; `14` waits for both stop lines.
- Notes for the desk:
  - `12` §1 has `02-greps.txt` name `git -C /Users/cobalt/cobalt grep …`, which is not in the hub's allow list; the hub is told to record any denial and fall back to `git show`. Drop that one line at launch if you prefer.
  - Prompts follow the 09-25 precedent shape (with WHY, history and reasons) as ordered. `writing-rules.md` says a prompt is tags, launch line, card, steps. Trimming is the desk's call.
  - `12` says "L15" for the stagger, from the desk's own row-76 wording; L15 elsewhere is the dependency law. Check that citation.

## ESCALATE
1. ASK DESK: the packet's S3 excerpts come from `s3/exits-c4` (a branch, not main) and the proposal notes the S3 report `a0ac51c4` reads "FAILED at W: stray cobalt_dev rows". Stage the branch bytes as written, or wait for S3's fix? [09-29] Default taken: stage the branch bytes at the tip the hub sees, name the tip in `## Packet`.
2. ASK DESK: Astra's meter is unknown; with a METER the derive names a DRAFT FINAL and round 2 waits for her return, against the proposal's need of a ruled design by 10-01. Accept the delay risk, or drop the wait for Astra on a design this small (L67 says she sits)? [09-29] Default taken: as L67 and the prompt say — probe, run without her on METER, seat her in round 2.

F15 TRIBUNAL DRAFTED · prompts: 3 · seats: astra grok gemini anthropic · packet: 200000 · new rule strings: 0 · owner items: 2 · ESCALATE: 2
