# Stop-guard G7 card: draft · 2026-10-09

## §0 Headline
- Card `prompts/2026-10-09/164-stop-guard-g7-card.md` drafted: JOB `stop-guard-g7-1009`, BASE `1458693d`, rows T0, G7a, G7b, G7c, V.
- Three reds (exit 0 on BASE, exit 2 after) and two negative controls (exit 0 both), the G7 set of `desk-idle-answer-2026-10-09.md` `## CARD ROW`, nothing wider.
- Two existing tests (`test_stop_guard.py:456`, `:564`) gain `(asked R1)`: their `waiting on Dejan` items turn unsettled under G7 (b).
- Builds after `https-only-1009` deploys. Today's report's three QUEUE rows (`cto-2026-10-09.md:35-37`) block the desk once this lands.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/164-stop-guard-g7-card.md` (uncommitted; the desk commits it on `main` before the launch).

## DECISIONS
- ASK DESK: the brief says the drafter writes G7 on card 66; this prompt says a new card 164. Default: new card 164, card 66 unchanged. [11:37]
- ASK DESK: `REPORT` is the main-checkout path the prompt names, not one inside the worktree as `CARD.md` says for a build. Default: the prompt's path. [11:37]
- ASK DESK: G7 lists five tests; two existing tests break under (b). Default: add `(asked R1)` to their items (row T0), assertions unchanged; no other test added. [11:37]
- ASK DESK: the order of the checks. Default: OWED items first (the missing-block message first of all), then QUEUE rows. [11:37]
- ASK DESK: `R<digits>` as a regex. Default: `\bR\d+\b`, so `PR12` or `ARM2` does not settle. [11:37]
- ASK DESK: `contains brain` is case-sensitive. Default: yes, the literal `brain` as G7 writes it. [11:37]
- ASK DESK: a QUEUE row with fewer than three cells. Default: `start it: <the row, stripped>`, no test added. [11:37]
- ASK DESK: the check line goes under `## CHECK ASKS` (CARD.md has no `## CHECK`). Default: `X1` followed by the line verbatim. [11:37]
- ASK DESK: K25 for the reds. Default: each red is its own proof (exit 0 on BASE); each control has one named mutation that turns it red. [11:37]
- ASK DESK: the order. Default: builds after the https-only card deploys. [11:37]

## RECORDS
- `cat "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/163-draft-stop-guard-g7.md"` (11:30 ET) — DOCS.
- `cat "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-idle-answer-2026-10-09.md"`: `## CARD ROW` G7 is the spec — DOCS.
- `git -C /Users/cobalt/cobalt rev-parse main` → `1458693dbde5371259a29c5d502d74e3878fee3b` (11:37 ET).
- `git -C /Users/cobalt/cobalt diff --stat main -- ops/desk/stop-guard.py tests/ops/test_stop_guard.py ops/desk/desk-list.sh` → empty, so the grep line numbers below are main's.
- `git -C /Users/cobalt/cobalt show main:ops/desk/stop-guard.py` — operator script. Its grep: `:20-23` OWED block header, `:89-95` constants, `:198` `owed_block`, `:254-255` `listed` rows, `:269-292` `unsettled` (`:274` WAITING, `:288-289` the cto-desk rule), `:295` `desk`, `:310` missing-block line, `:313-317` caller, `:47` INSTALL Stop entry, `:353` `worker`.
- `git -C /Users/cobalt/cobalt show main:tests/ops/test_stop_guard.py` — test. Its grep: `:267` ROW, `:275` `Desk`, `:306` `owed`, `:315` `lister`, `:332` `missing`, `:407-409` `fold R1`, `:451-456`, `:464`, `:480`, `:562-564`, `:675-678`.
- `git -C /Users/cobalt/cobalt show main:ops/desk/desk-list.sh` — operator script: `:3`, `:16`, row `id · name · cwd · status · state`.
- `grep -n -o -E "\-\-name [a-z-]+" prompts/BRAIN-HUB.md` → `8:--name brain` — DOCS.
- `cat prompts/CARD.md`, `cat prompts/2026-10-08/120-guard-g2-open-reads-card.md` (the precedent card), `cat …/Memory/topics/writing-rules.md` — DOCS.
- `grep -n -E "^(JOB|BRANCH|WORKTREE|BASE):" prompts/2026-10-09/156-https-only-card.md` → `JOB: https-only-1009` — DOCS.
- `grep -n … reports/cto-2026-10-09.md` → `## §5 CURRENT` `:20`, OWED `:21-28`, table `:30-33`, QUEUE `:35-37` — DOCS.
- `grep -n -c -F "ops/desk" configs/cobalt/jobs.yaml` → `0` (11:37 ET) — config.
- K25: `…/Memory/topics/cto-desk-checklist.md:120`; L75: `…/Memory/LAWS.md:374` — DOCS.
- `ls` of the card, both reports, card 66: card 164 and both reports absent before writing, card 66 present.

STOP GUARD G7 CARD DRAFTED · decisions: 10
