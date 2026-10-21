# draft-f5-gate-run — 2026-10-21

## §0 Headline
- Hub prompt `prompts/2026-10-21/970-f5-gate-run.md` drafted: Opus 5.5, CLASS K2, `RULINGS: 2026-10-18 R1863`, report `reports/f5-gate-run-2026-10-21.md`, 40 `GATE RESULT` lines (10 items × 4 labels).
- X2 = the DEV dry run `COBALT_ENV=dev uv run cobalt checkpoint run --slot 0745 --dry-run`: it fetches the real Groups page (`checkpoints.py:104`, `:224-235`, no env branch). No K5 card and no production string needed. The same run also gives X6 one real-shape prompt through the guard.
- X7 and X13 get offline pytest legs. X4, X5, X10 and X12 have no command on `main`, so they stay `NOT RUN`. X5, X7, X10 and X12 each have a leg that needs his hand.
- Live cost: one gate check, 2 Finviz GETs, 0–1 local `mainframe` call; no `claude` session.

## DECISIONS
1. ASK DESK: the gate file lists `X3` and `values card` for all four labels (`data/deploy/bootstrap-owed.json:5-8`, gitignored, read on disk); prompt 969 leaves them out. [07:29 EDT] Default: the hub writes both as `NOT RUN — not this hub's`, and the desk writes their result from the X3 report and 958 DEPLOYED (R2276).
2. ASK DESK: no command exists on `main` for X4, X5, X7's Obsidian leg, X10 or X13's launchd leg. [07:29 EDT] Default, the cheapest card-based way: one K2 probe build card `f5-probe`, adding `cobalt checkpoint probe X4|X5|X6|X7|X10|X13`. Each probe prints one `PROBE <X> OK|FAIL <clause>` line, runs dev only, and uses temp dirs. The precedent is card `prompts/2026-10-19/877-cos-probe-card.md` and `src/cobalt/cos/probe.py`. X12 stays his eyes. The probe strings then go on a new hub launch line, because the SECOND PASS runs only strings already on 970's line.
3. ASK DESK: X13's offline leg proves the window rule refuses a late fire (`test_checkpoints_offline.py:682`, rule `checkpoints.py:167`, CLI `:820`). It does not prove that launchd fires late. The design's consequence ("a late fire makes the window rule needed and exercised", `F5-FINAL:187`) is already built and tested. [07:29 EDT] Default: the brain may rule X13 met on `OK (offline …)`; until then the line does not count.
4. ASK DESK: X6 on one real-shape prompt (07:45 vs prior close) is one sample, while `F5-FINAL:180` says "prompts". If the dev vault holds no daily note for today, X6 is `NOT RUN` (`checkpoints.py:747-751`). [07:29 EDT] Default: an `OK (one real-shape prompt …)` does not count until the brain rules; the probe card in 2 covers more prompts.
5. ASK DESK: X2 as redefined (R2279) commits no real-shape fixture. The offline tests still parse the synthetic body (`test_checkpoints_offline.py:10-12`: "X2's real capture owed before load"). [07:29 EDT] Default: R2279 stands; the dry run's `OK` is X2.
6. ASK DESK: launcher RULINGS. R2279 is a DESK RECORD, and `desk-launch.sh` refuses `uv run` / `COBALT_ENV=` strings unless they are cited to a HIS RULING · APPROVED row (it refused R1844 the same way, R1869). [07:29 EDT] Default: `RULINGS: 2026-10-18 R1863`, as in 873.
7. ASK DESK (for Dejan): X5 — may a script send a voice planning call every 20 seconds for 10 minutes, before 07:00 or after 16:00 ET on a day you name, so voice may be slow for you in those 10 minutes? [07:29 EDT] Default: X5 stays NOT RUN; nothing else waits on it.
8. ASK DESK (for Dejan): X7 — will you open Obsidian on the dev vault copy (not your real vault) for 15 minutes at a time you name, and leave it open while two test checkpoints write into a test note? [07:29 EDT] Default: X7 stays NOT RUN; nothing else waits on it.
9. ASK DESK (for Dejan): X10 — will you turn Obsidian Sync on for the dev vault copy for one test, and off again after? [07:29 EDT] Default: X10 stays NOT RUN; nothing else waits on it. (Prompt 969 named only X5 and X7 as his; X10 needs his Sync account and X12 needs his eyes.)
10. ASK DESK (for Dejan): X12 — will you open one test note in Obsidian on the dev vault copy and say whether you see any marker text, all four checkpoint units, and your own dash line? [07:29 EDT] Default: X12 stays NOT RUN; nothing else waits on it.
11. ASK DESK: the dry run touches `cobalt_dev`: it reads the stores, and `VaultWriteStore.ensure_schema` re-runs `IF NOT EXISTS` migrations (`checkpoints.py:559-563`). [07:29 EDT] Default: step 0 runs `ls -d /Users/cobalt/cobalt-wt/.cobalt_dev.lock`. If the lock is held, X2 and X6 are `NOT RUN — cobalt_dev lock held`; relaunch when it is free.

## RECORDS
- `date` → 07:23 EDT (start), 07:28 (prompt written), 07:29 EDT (report). Reads only. No network, no database, no production command, no git write, nothing committed, no launch.
- `git -C … rev-parse main` → `6c6e7b80` (after `d678ea0a`). Every `file:line` below was read by `git show main:<path>` or `git grep … main`.
- `data/deploy/bootstrap-owed.json`: not on main (`fatal: … exists on disk, but not in 'main'`; gitignored per `deploy-step-c.sh` header). `grep -n checkpoint` on disk → `:5-8`: four labels, gate `X2, X3, X4, X5, X6, X7, X10, X12, X13, values card`, card 909.
- `docs/30 - Design/F5-FINAL-2026-10-11.md:176-187`: rows X2–X13 read whole. The PASS line is the negation of the "Result that changes the design" column; X2's column is `—`.
- `src/cobalt/prefill/checkpoints.py`: `:20` the dry run ignores the window; `:104` `GROUPS_URL`; `:167` `window_refusal`; `:200-235` parse and fetch Groups; `:238` `fetch_figures`; `:559-563` `default_stores`; `:576` `check_demand`; `:607-610` summary; `:697` gate; `:747-751` note-absent stop; `:779` `narrate`; `:820` CLI refusal; `:824` `as_job(skip=dry_run)`; `:832` report printed; `narrate` `:413-440` (empty delta `:423-425`).
- `src/cobalt/aset/prefill.py:37-42` `resolve_token`: Finviz vault credentials, no env branch. `src/cobalt/env.py`: `COBALT_ENV` must be set; dev → `cobalt_dev` + dev vault. `ops/desk/bare-guard.py:70` G2 route: "a dev read uses COBALT_ENV=dev".
- `src/cobalt/modelaccess/client.py:129-133` guard → `prompt_refused`. `configs/cobalt/modelaccess.yaml:70-74` route `checkpoint.narrative`: local, `mainframe`.
- `src/cobalt/radar/notes.py:664-678` and `strike/measure.py:133-137`: the gate reads the radar notes from the resolved (dev) vault.
- Tests: `test_checkpoints_offline.py` classes `:672` TestOneRun, `:864` TestSeam; tests `:682`, `:689`, `:747`, `:876`, `:912`; `:10-12` synthetic fixture. `test_checkpoints_live.py` read whole: fakes Finviz, so it is no X2. No F5 probe command or X-named test exists (`git grep` over `src/cobalt/prefill`, the checkpoint tests, `ls-tree tests/cobalt`).
- `ops/desk/desk-launch.sh:130-148`, `:785-841`: W6, write strings need RULINGS. `ops/desk/deploy-step-c.sh:185`: one `GATE RESULT: com.cobalt.<label> · <item> · ` line per label.
- Read as well: prompt 969; `prompts/2026-10-19/873-cos-gate-run.md` whole; `prompts/2026-10-20/914-f5-x2-probe.md` whole; `reports/draft-f5-x2-probe-2026-10-20.md` whole (`:11` K5 default, not taken); card 909 whole; `reports/cto-2026-10-21.md` whole (R2276, R2279); `cto-2026-10-18.md:90` R1863 (HIS RULING · APPROVED), `:86` R1869; `topics/writing-rules.md` whole. Not read: 913 (914 and its drafter report carried what this needed).
- `.env` not read; the guard refused a count-only grep, and the hub spells `COBALT_ENV=dev` instead.
- `wc -c` of 970 → 11754 before the per-label edit. It is a new file, so there is no prior size.

DRAFTED · decisions: 11
