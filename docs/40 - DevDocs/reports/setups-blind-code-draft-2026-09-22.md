# SETUPS BLIND CODE SEAT — DRAFT REPORT — 2026-09-22

Drafter `setups-blind-code-draft-0922` (Opus 5), 11:22–11:29 ET (`date`). Wrote `prompts/2026-09-22/23-setups-blind-code-seat.md`. Launched nothing.

## GROK CAN RUN CODE?
**YES, proven 09-16. But NOT under today's approved spelling.** It needs one new rule string.
- 09-16 spelling (`reports/audit-house-2026-09-16.md:235-239`): `cd /Users/cobalt/cobalt-wt/agy-trial && grok --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/toy-check-grok/**)" --allow "Edit(/Users/cobalt/cobalt-wt/agy-trial/scratch/toy-check-grok/**)" --allow "Bash(python3 /Users/cobalt/cobalt-wt/agy-trial/scratch/toy-check-grok/*)" -p "<step-3 prompt, verbatim>"`
- What it did (`:241-247`, `:266-268`): "Exit 0. `scratch/grok-toy-err.log`: empty (0 bytes) — no denials." Grok wrote `check.py`, ran it with `python3`, fixed its own clamp formatting and ran it again. It found the one planted defect. The verdict: "**grok verdict: CAPABLE.** … no denials, sandbox held." The same three rule shapes ran again on the real P2 bundle (`:331-337`) with "Exit 0, `scratch/p2-grok-err.log` empty (no denials)".
- What the sandbox denied: nothing. The `cobalt-job` profile denies only credential directories (`:193-211`).
- Today's approved spelling (`prompts/2026-09-21/66-setups-one-check.md` §2 "GROK", and `38` §2): `--sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)"` only. It has **no `Bash(…)` run rule**. His R39 (`cto-2026-09-21.md:50`) approves `Bash(grok *)` for "the same sandboxed headless read-only use, nothing wider". So running a program needs his word on a new string.
- Side note: LAWS L33 (clarified 09-09) still says "Headless Grok and agy auto-deny shell commands". That sentence predates 09-16's CAPABLE result, which was proven with an explicit `--allow "Bash(python3 …)"`. The two do not conflict, but L33 reads as if the capability does not exist.

## NEW STRINGS
1. **Grok (house PRIMARY, today only, under R39):** inside the house call: `--allow "Bash(python3 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/setups-blind-code/*)"`. It narrows the 09-16 precedent `Bash(python3 /Users/cobalt/cobalt-wt/agy-trial/scratch/toy-check-grok/*)` (`audit-house-2026-09-16.md:238`). It is the same shape and the same interpreter, re-pointed to one packet folder. The 09-16 `Edit(…)` rule is left out on purpose: Grok rewrites its program through the already-approved `Write(…/tribunal-bars-0920/**)`.
2. **Sol (FALLBACK window, Sat 2026-09-26 06:47 ET or later):** the hub's allow string `Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s workspace-write *)`. It is his R49 Sol string (`cto-2026-09-21.md:60`, `-s read-only`) with the sandbox changed to `-s workspace-write`, per LAWS L33 "a Codex run that must write a report or plan launches `-s workspace-write`". The desk's spec named `--cd <the packet folder>`. That flag appears in no approved prompt: `-C ~/tmp/codex-preflight` shows up only in `reports/day-open-2026-09-10.md`. So I left it out, following "never invent a flag". Sol runs from the hub's cwd `~/cobalt-wt/agy-trial`, so its writable root is the whole agy-trial worktree, not just the packet folder (see ESCALATE 5).
- Total new: **2** (1 Grok, 1 Sol). The desk expected 0 for Grok. The run form is proven but not approved today, so it becomes 1.

## DIGEST
- `23` is a Sonnet 5 hub built on `17`'s shape. It stages `17`'s packet plus the detector SOURCE whole: anatomy ×17, formation ×5, `evaluate.py` in 3 parts, `predicate.py`, `loader.py`, `trade_def.py`, `aggregate.py`, an `evaluate_cli.py` excerpt (`_aware` / `admitted_at` / `scan_instants`) and `tunables.yaml` whole.
- Source files are staged as flat `SRC__….txt` names so the house cannot import them. The house must write its own stdlib program. A `## Program` grep marks `RAN STAGED SOURCE` or `OPENED KEEP-OUT`.
- Forbidden-string `grep -c` = 0 on every staged source file at `60ddac4`, except `evaluate_cli.py`: its line 218 holds a `FORMED ` print string, so it is excerpted. Trailing-whitespace count = 0 on every source file.
- Two launch lines by date: LINE-G is Grok today until 23:59 ET; LINE-S is Sol from Sat 06:47. There is no Opus or Fable fallback (L67).
- Gates: the STAGGER on `19` as specified, and a new gate that `15` is not mid-edit in `setups-c1`. The pins are proven unchanged since `60ddac4`. Source moved by `15` is staged at the tip and disclosed.
- Additions to KEEP-OUT: `17`'s report WHOLE (its `## Comparison` carries the pinned values), `16`'s report, the `setups-blind-committed/` and `setups-check-r2/` folders, and `evaluate_cli.py:218`.
- Clock: 60 min, then TaskStop and `TIMEOUT`. The ORDER proof and the 17-row comparison are `17`'s, unchanged. The stop line is as specified.

## ESCALATE
1. **The daily/intraday contradiction is caused by the cutter's construction, and `daily.py` keeps it away from the engine's HTF references. Whether the prior-session row is the right one is UNPROVEN.**
   - Cutter (`tests/fixtures/radar/_cut_p2_fixtures.py:79-107`, `cut_daily`): the intraday bars are shifted by a fixed `DELTA_DAYS` from `REAL_ANCHOR_DATE = 2026-09-14` (`:35-37`, `:46-52`). The daily window is re-dated so that its LAST exported row lands on `2026-01-06` (`:92-99`, "Re-date the trimmed window so its last row lands on the synthetic anchor day"), whatever that row's real date was.
   - So the `2026-01-06` daily row is the export's last real session, which is not necessarily 2026-09-14. It may also be a partial mid-session row. The house's reading, that intraday trades below that row's low, fits this.
   - `daily.py:61-62` (`before`: `session_date < trade_date`) and the module docstring ("reads only sessions STRICTLY BEFORE the trade date") mean `prior_session`, `daily_atr` and `htf_range_break` never read the `2026-01-06` row.
   - What reads do not settle: whether the `2026-01-05` row is the true prior session of the intraday day. The export's real last date is not in the repo; it came from raw prod reads under env paths. If the export ran after 09-14, every daily row is off by the gap, and the HTF references (prior H/L, daily ATR, day_count) come from the wrong sessions. Owner: the fixture's author or the desk. It is not a code fix. The code seat will reproduce whatever the fixture implies, so a MATCH does not clear this item.
2. **`stop.buffer` unit — the source settles the arithmetic and the label is wrong.**
   - `tunables.yaml:32-39` says `value: 0.02, unit: cents`.
   - `formation/stops.py:128` passes that value straight to `structure.structural_stop` as a price delta, and `structure.py:104` computes `raw = extreme + away * buffer`. So the engine applies $0.02 (two cents), and the `cents` label reads as 0.02¢.
   - `23` tells the house "the source is the rule". Owner: a label ruling (`cents` → dollars, or value 2 with unit cents). This is not a pin question.
3. **Drafter disclosure:** I read `reports/setups-blind-committed-day-2026-09-22.md` whole with one `cat` instead of only `## Packet` / `## House` / `## ESCALATE`. Its `## Comparison` carries the pinned values, so the drafter has seen them. None of them appears in `23` or in this report. I am not a checker seat and I put nothing into the packet. `23` now puts that report on the hub's KEEP-OUT list so the hub cannot repeat this.
4. **What the seat cannot get from the packet:**
   - the rest of `evaluate.py`'s imports (`cobalt.cards.*`, `cobalt.settings.card`, `radar/seam.py`, `cobalt.session`, `cobalt.taxonomy.defaults`), which are not staged; if the house finds a formation rule that rests on one of them, it will write UNDERIVABLE;
   - the session clock that sits behind `scan_instants` (TASK.md gives the grid explicitly);
   - `FORMED_AT` (`radar_p2_support.py:38`), which stays excluded.
5. **Sol's writable root is wider than the packet.** Without `--cd`/`-C`, which is unproven in approved prompts, `-s workspace-write` from `~/cobalt-wt/agy-trial` can write anywhere in that reports-only worktree. `ASK DESK: approve `-C /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/setups-blind-code` as part of Sol's string (it narrows the root; the flag is only attested in `reports/day-open-2026-09-10.md`)? [11:29 ET]` Safe default in `23`: no flag, plus the before/after `ls -la` check.
6. **The hub does not re-run the house's program (L35).** That would need a hub `Bash(python3 …)` string, which is not requested here. The comparison is string equality on the house's file, and `## Program` greps enforce independence. If the desk wants a hub reproduction like 09-16's, that is one more string.
7. **The STAGGER gate as specified fails right now.** `19-handicap-tribunal-r2.md` exists but has no report yet. So `23` cannot launch until `19` stops. This is intended; it is noted so the desk sequences `19` first.

SETUPS BLIND CODE PROMPT DRAFTED · house: grok · grok runs code: yes · new rule strings: 2 · ESCALATE: 7
