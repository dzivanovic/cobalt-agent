# Draft — Gemini probe-id card (prompt 668) · 2026-10-17

## §0 Headline
- Card `prompts/2026-10-16/670-gemini-probe-id-card.md` drafted: BUILD, K5, job `gemini-probe-id`, rows P0 (id proof), G1 (id swap + pin), P1 (probe + sweep).
- Two `«FILL»` stand for the desk: `BASE`, and the `agy models` record in `## RECORDS` (the pre-edit list proof; a build line cannot run `agy`).
- The prompt's "583 does not touch CHECK-HUB.md" is wrong: 583 changes lines 64 and 117; this card changes 95 only. Text-disjoint.
- Not committed (no git write on this seat).

## DECISIONS
1. ASK DESK: `agy models` is not on the build line, so the builder cannot list the models. Who runs it? [Sat Oct 17 08:02 EDT] Default taken: the desk runs it before launch and fills the `## RECORDS` slot. The builder quotes it at P0 and stops `FAILED: id not listed` if the id is missing.
2. ASK DESK: the probe after the edit must run the worktree's `house-probe.sh`. The build line's `sh` string covers only the repo path, which still holds the old id until the deploy. [08:02] Default taken: the builder records an ASK DESK at P1. The desk runs `sh /Users/cobalt/cobalt-wt/gemini-probe-id-1017/ops/desk/house-probe.sh gemini` before the check, and the deploy smoke read re-runs it on `main` (`gemini: UP`).
3. ASK DESK: `STANDING-LIST.md:13` records the house spellings his R60 approved, and it is in scope per prompt 668. Edit it or leave it as history? [08:02] Default taken: edit the id token only. The allow string `Bash(agy *)` is unchanged.
4. ASK DESK: what BAND? [08:02] Default taken: `BAND: MID`, as card 641 (K5 ops script) has it.
5. ASK DESK: the existing pin `tests/ops/test_house_probe.py:253` names the old id and goes red on the edit. [08:02] Default taken: change only its id token. This is the one existing test line edited.

## RECORDS
- Read: prompt 668; `prompts/CARD.md`; `prompts/BUILD-HUB.md` lines 3, 12, 14, 76 (the allow line holds no `agy` string; its `sh` string covers only `/Users/cobalt/cobalt/ops/desk/*`); card 641 (the shape); `reports/cto-2026-10-17.md` R1736, R1738, R1742, R1748; `reports/gemini-bakeoff-answer-2026-10-17.md`; `reports/check-scratch-fr-check-2026-10-16.md:75`, `:221`; `reports/agy-trial-2026-09-15.md:20` (`agy models` is the CLI's list verb); `topics/writing-rules.md`.
- Proved on `main` (f2140694 at 08:02 EDT): `git status --short` printed nothing for the files below, so the working tree equals `main` for them. `ops/desk/house-probe.sh:24`, `:104` (old id); `prompts/CHECK-HUB.md:95` (old id, the only `agy --model` line; 127 lines); `prompts/STANDING-LIST.md:13`; `tests/ops/test_house_probe.py:21-22` (PROBE, CHECK_HUB), `:193` (127-line pin), `:253` (old id); `prompts/SHADOW-HUB.md:88` (card 671); `ops/desk/desk-launch.sh:398` and `tests/ops/test_desk_launch_shadow.py:216-217` (card 671); `src/cobalt/jobs/restarts.py:38`, `:225`, `:232`, `:245` (RESTARTS none).
- Owners of `gemini-3.1-pro-high`: card 670 owns `house-probe.sh:24`, `house-probe.sh:104`, `CHECK-HUB.md:95`, `STANDING-LIST.md:13` and `test_house_probe.py:253`. Card 671 owns `SHADOW-HUB.md:88` and `test_desk_launch_shadow.py:216-217`. Dated prompts are history and stay.
- `git -C /Users/cobalt/cobalt diff main...ops/band-routing-1015 --stat` lists `CHECK-HUB.md | 4 +-`. Its hunks replace one line each at `:64` and `:117`.
- R1736 is committed at d01849e7. R1738 and the answer file are committed at b57cbf8e.
- Nothing was run but reads. Every RED in the card is UNPROVEN until the builder quotes it (L70).
DRAFTED · decisions: 5
