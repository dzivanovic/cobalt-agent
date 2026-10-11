## §0 Headline
Card 355 drafted: `prompts/2026-10-11/355-install-shadow-hub-card.md`, one row S1, `DB: none`, no `«FILL` but BASE and TIP (the desk's).
S1 signs the 3 `SHADOW-HUB.md` cells (`:19-21`) and line 1, and `SPIKE-HUB.md` (1 `«SIGN` at `:24`, token at `:1`), on R1069.
The build does line 1 by hand; `install-fixed.sh` would write text about `STANDING-LIST.md`.
The row also edits two tests that pin the unsigned real files, so it is not docs-only.

## DECISIONS
1. ASK DESK: the row's files include `tests/ops/test_spike_hub_file.py:92` and `tests/ops/test_desk_launch_shadow.py:291` (both go red once the marks leave; `tests/ops/` keeps `DB: none`). Your brief said docs-only. [before the build launches] Default: keep them in S1.
2. ASK DESK: R1069 names SHADOW-HUB only; SPIKE-HUB's mark is its own new command class (R411). Card signs both on your instruction. [before the build launches] Default: sign both; delete the SPIKE-HUB half of S1 if R1069 does not reach it.
3. ASK DESK: line 1 is written by the build as `HIS RULING · APPROVED 2026-10-11 R1069` (precedent 306 I1), not by `install-fixed.sh`. [before the build launches] Default: by hand.

## RECORDS
- `git rev-parse --short=8 HEAD` → `2322ed1e`; `git status --short` over both hubs, `desk-launch.sh`, `install-fixed.sh` → empty (2026-10-11).
- `grep -n -o "«SIGN"` `SHADOW-HUB.md` → `:19`, `:20`, `:21`; `«INSTALL` → `:1`. `SPIKE-HUB.md`: `«INSTALL` `:1`, `«SIGN` `:24` (count 1, so included). `wc -l`: 103 and 26.
- Launcher checks: `desk-launch.sh:892-893` (token), `:1341-1342` (shadow sign), `:390-395` (spike, both). Tests that exist: `test_desk_launch_shadow.py:208`, `:233`; `test_desk_launch_spike.py:148`.
- `install-fixed.sh:1-14, 35-65` read: replaces only the `«INSTALL … »` span of line 1 with `INSTALL: <date> R<n> of his approval of STANDING-LIST.md`.
- `cto-2026-10-11.md:8` row R1069 holds `HIS RULING` and `APPROVED`; last commit `2322ed1e`. No preflight (his override, L79).
- Read whole: CARD.md, `306-ops-hand-install-card.md`, both hubs, `writing-rules.md`. BASE and TIP left as `«FILL` for the desk, in the shape of the precedent's fields.
- Not run: `pytest`, `uv` (not on the allow list); the card's red-first counts are read from the files, not executed.

DRAFTED · decisions: 3
