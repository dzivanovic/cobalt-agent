# draft-grok-second-cards · 2026-10-11

## §0 Headline
- LOW: `archiver-429` (card 206), score 1 by card fields (2 by its check's RESTARTS) → card 378 written.
- MID: `worktree-salvage` (card 83), score 4 → card 379 written.
- HIGH: no pick. `ops-hand` (card 231) scores 4 (MID); no checked job without a migration reaches 7 but `s4-p1`. Card 380 not written.
- Candidates `radar-top50` (3, MID, same file as 118) and `ops-hand` (4, MID) fell outside their bands.

## DECISIONS
- ASK DESK: HIGH has no second Grok card. `ops-hand` scores 4 (R4, S0); it is HIGH only if its drafter records X (shared file with an open card) and H (no precedent card): `ops-hand-draft-2026-10-10.md` records neither. Default: n=1 for HIGH, no card 380. [14:56]
- ASK DESK: MID tie at 4 between `worktree-salvage` and `ops-hand` (also `radar-arm-disarm`, `disarm-one-tap`, `voice-clarify-fix`, all RESTARTS aset+radar, file areas not read). Taken: `worktree-salvage`, buildable whole from BASE. `ops-hand` row S (card 231 `:22`) repairs a merge conflict against `ops/hand-1010` tip `6a18ff95` and main's later guard rows; neither exists at BASE `1eb47b59`, so a shadow cannot build it. Default: `worktree-salvage`. [14:56]
- No placeholder token in either card; the header holds no `TIP`, as the launcher's fixture does (`tests/ops/test_desk_launch_shadow.py:127`, empty).

## RECORDS
Read: FINAL `## 1` and `### 2.1` (formula `R + M + S + X + H + $`, LOW 0-2, MID 3-6, HIGH ≥7; F-11 "missing evidence is UNKNOWN, not zero"); r2 proposal; round-1 sample table (`complexity-routing-proposal-2026-10-10.md:27-55`); `364-draft-shadow-cards.md`; `SHADOW-HUB.md` `## BUILDERS` (`grok-4.7`, slug `grok`, `:19`); the cards 154, 206, 231, 83, 215; the check stop lines of the sample's jobs.
Main HEAD at the reads: `bf8430d8`. Cards 154, 206, 231, 83 are unmodified in the working tree (`git status` lists none).

Scores (inputs; `$` = 0 and M = 0 for each, no card names money, sizing or a migration):
- `radar-top50` (card 154): rows A-D = 4 (`154:18-21`) → R1; S2 (`154:37`, check `radar-top50-check-2026-10-09.md:254` RESTARTS aset+radar) → **3, MID**. Outside LOW. Not MID either: its rows edit `radar_panel.py` (`154:18`), card 118's file. Row D (`154:21`) is a fix round against main, not buildable from BASE.
- `archiver-429` (card 206): rows A1, A2, B = 3 (`206:16-18`) → R0; S1 from the card (`206:53`, `com.cobalt.radar` by import; archiver is a one-shot) or S2 from the check (`archiver-429-check-2026-10-10.md:258`) → **1 or 2, LOW**. Highest LOW of the sample: the other LOW jobs score 0-1 (desk-pane-by-id 1, stt-model-fix 1, launcher-next-flow 0, flake-fix-2 0, guard-g2 0, radar-ladder-refresh 2 rows + S2 = 2 but `radar` area). Files `src/cobalt/archiver/*`, differing from 215's `aset/__main__.py`, `aset/strike.py` (`215:16-17`). Not MANDATORY house B (`206:9`).
- `ops-hand` (card 231): rows H1-H6, S = 7 (`231:16-22`) → R4; S0 (`ops-hand-check-2026-10-10.md:234` RESTARTS none); X and H UNKNOWN → **4, MID**. Outside HIGH.
- `worktree-salvage` (card 83): rows W1-W7 = 7 (`83:19-25`) → R4; S0 (`83:29`, check `worktree-salvage-check-2026-10-07.md:171`); `DB: none` (`83:11`) → **4, MID**. Files `ops/desk/job-clean.sh`, `tests/ops/test_gate_clean.py` (`83:32`), differing from 118's. `HOUSE B: as needed` (`83:9`).
- HIGH sweep: of 27 jobs, ≥7 only `s4-p1` (13, the common card), `s4-p2` (migration 0024) and `price-floor` (0023); both excluded.

Check records (each ends `ready: YES`, committed on main):
- `archiver-429`: `archiver-429-check-2026-10-10.md:258`, last commit `2b243142`; CARD COMMITTED `:18` → `93e4c29a`.
- `worktree-salvage`: `worktree-salvage-check-2026-10-07.md:213`, last commit `74b8bbce`; CARD COMMITTED `:16` → `f4edbb9d`.

Cards (two paths):
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/378-shadow-archiver-429-grok-card.md`: from card 206; changed `JOB: archiver-429-grok`, `BRANCH: shadow/archiver-429-grok`, `WORKTREE: archiver-429-grok`, `REPORT`, `CHECK REPORT`, `RULINGS: 2026-10-08 R685, 2026-10-11 R1069`; `TIP` dropped; `SHADOW OF:` added. Body lines 11-55 identical (`grep -v -x -F -f` both ways prints only the header lines; 55 lines each).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/379-shadow-worktree-salvage-grok-card.md`: from card 83; same header changes, `RULINGS: 2026-10-07 R613, 2026-10-11 R1069`; `DB: none` kept. Body lines 11-53 identical, same proof.

Launcher proof (`ops/desk/desk-launch.sh`, HEAD `bf8430d8`):
- `:936` `need JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS`: all present. `:946` JOB `[a-z0-9-]`. `:952-956` RULINGS `<date> R<n>`.
- `:1332` `SHADOW OF:` present. `:1335-1338` BRANCH starts `shadow/`. `:1352-1355` JOB ends `-grok` (slug of `SHADOW-HUB.md:19`). `:1318-1320` REPORT under `$WT/<wt>/docs/40 - DevDocs/reports/`. `:1334` no `ROLE:`. `:1312` no `TAG:`. `:1315-1316` BASE `fa968552`, `c4e52f4e` are commits.
- `:1321-1326`: no worktree or branch of the new names exists (`ls /Users/cobalt/cobalt-wt`).
- Rulings (`:253-279`, one row each, HIS RULING + APPROVED): R685 `cto-2026-10-08.md:38`; R613 `cto-2026-10-07.md:8`; R1069 `cto-2026-10-11.md:33`. `cto-2026-10-08.md` has one unrelated uncommitted line (an OWED row at `:93`), not R685's.
- Not proved: `:974-976` needs the cards committed on main. The desk commits them before the launch.

DRAFTED · decisions: 2
