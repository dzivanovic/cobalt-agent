## §0 Headline
Card 958 now carries option C (R2251): `timeout_s: 25` from the cold proxy, `max_output_tokens: 256`, BAND LOW, no unload, no live call.
Proxy: `mainframe.log:12` load 8.67 s + warm max 4.97 s = 13.64 s; × 1.5 = 20.46; up to a multiple of 5 s = 25.
Changed on the card: header GATE line, WHY, T1, test line, COLD, X3, DEPLOY PROOF, DECISIONS 1, DECISIONS 3, RECORDS.
Nothing was run and nothing was committed.

## DECISIONS
1. None open. DECISIONS 1 on the card now reads `answered: option C, brain 2026-10-20 (R2251)`.
2. T1's ruled comment has no `Never the voice route's 15 s.` wording, because the comment is exact. The wording stays in the card's WHY (FINAL `:88`) and in the new test, which asserts `timeout_s` is not `local.plan`'s. This is a note, not a question.

## RECORDS
- 2026-10-20 21:16 EDT (`date`). Reads only; nothing run, no model call, no git write.
- Reads: prompt 959; card 958 whole and its greps for `timeout_s: 10`, `(warm model)`, `unapplied` and `ASK DESK`; `ops/logs/mainframe.log` via `grep -n -F "Model loaded successfully"` (`:12` 8.67 s, `:31` 5.47 s); `git show main:configs/cobalt/modelaccess.yaml` (`timeout_s: 60`, `max_output_tokens: 512`, both comments `UNMEASURED`); `reports/cto-2026-10-20.md` R2251 (`:21`).
- Marker counts now on the card's DEPLOY PROOF: `# source: X3 reports/f5-x3-measure-2026-10-20.md` 0→2; `(warm model)` 0→1 (T2 only); `cold load 8.67 s from the mainframe log (proxy, not a live cold call)` 0→1; `source: UNMEASURED` 2→0. The before values come from `main`; the after values are unproven until the build.
- Card greps after the edit: `timeout_s: 10`, `unapplied` and `ASK DESK` match only the amend record in RECORDS. `(warm model)` matches T2 (`:28`) and its proof line (`:62`).

DRAFTED · decisions: 0
