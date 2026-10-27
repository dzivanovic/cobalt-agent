# F4 gate third pass, X15: 2026-10-27

## RESULTS
GATE RESULT: com.cobalt.prefill-refresh · X7 · NOT RUN — [HIS HAND] Obsidian render and re-padding; not in this pass
GATE RESULT: com.cobalt.prefill-refresh · X9 · NOT RUN — [HIS HAND] Sync leg; not in this pass
GATE RESULT: com.cobalt.prefill-refresh · X15 · OK — peak 50/min at 08:43 · per minute 08:40=47, 08:41=47, 08:42=47, 08:43=50, 08:44=47, 08:45=47 · radar 222 · strike 60 · refresh 3 · 429 0 · strike interval 30 s · refresh gate admitted

## FIGURES
```
PROBE X15 OK peak 50/min at 08:43 · per minute 08:40=47, 08:41=47, 08:42=47, 08:43=50, 08:44=47, 08:45=47 · radar 222 · strike 60 · refresh 3 · 429 0 · strike interval 30 s · refresh gate admitted
```
Peak is 50/min, which is within the limit of 50 with no headroom. The 429 count is 0.

## DECISIONS
None. X15 is OK, so nothing needs a ruling. The plist stays unloaded. Loading it is a separate card.

## RECORDS
F4 gate third 1078 — X15 on the deployed 1049-C (0ea89b17, deploy-2026-10-26-f4-strike-reserve); X15 is the plist's load gate (brain R2535, L79); X7 render, X9 Sync and X9 firings his or post-load; X8 post-load watch; X10 OK from the attempt2 deploy gate (reports/f4-gate-run-2026-10-26.md)

- Start `date`: Tue Oct 27 00:37:23 EDT 2026.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main`: `fefb8cc8`. From this launch line I cannot prove that `0ea89b17` is an ancestor of main, because `ls` and `rev-parse` cannot show it. The deploy report holds it.
- `ls -d /Users/cobalt/cobalt-wt/.cobalt_dev.lock`: exit 1, `No such file or directory`. No build holds `cobalt_dev`, so X15 ran.
- `COBALT_ENV=dev uv run prefill probe X15`: ran once, exit 0, with no error.
- Not run: X7 and X9, which are his legs ([HIS HAND]). No `prefill refresh`, no `launchctl`, no database command, no git write and no retry.
- End `date`: Tue Oct 27 00:37:30 EDT 2026.
- `com.cobalt.prefill-refresh` was left unloaded.

GATE THIRD DONE · X15: OK · peak 50/min · 429: 0 · main fefb8cc8
