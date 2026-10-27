# His legs — setup state (DAY PLAN goal 5, 2026-10-27)

Rule (R2384): the desk sets up each leg on his "ready". Source of the rows below: brain 9b07db5a, L79, 2026-10-27 (07:05 ET). Each leg: what he does · what he reports · what the desk reads.

Order for one sitting (about 60 min): cos DM → X15 → X12 / F4 X7 look → F23 decks → X7 → X10 + F4 X9 → X5 last (after 16:00).

| Leg | What he does | What he reports | What the desk reads |
|---|---|---|---|
| COS DM | Sends any short DM to the Cobalt bot in Mattermost (the bot of `notify.yaml:13-14`) | Whether a reply came | `logs/cos.log` for that turn `ok` and `CoS turn FAILED` = 0; moves LaunchAgent auth UNPROVEN → PROVEN (929 / cos-bootstrap-2 smoke (s)) |
| X15 (four legs) | The desk runs `cobalt hitl x15-send` (994, deployed); he gets a DM link to `/hitl/x15-probe#k=…` and opens it from (1) laptop Mattermost app, (2) Mattermost in a laptop browser, (3) phone Mattermost app, (4) Mattermost in a phone browser | Per leg: did the page load; does it show "k: seen" or "k: missing" | the page result he reports |
| F5 X12 + F4 X7 render | Opens the dev test note in Obsidian | Any marker text visible? All four checkpoint units shown? His own dash line shown? Is F4's stamp above the table, and do the table cells keep their spacing on open? | his answers |
| F23 E1 / E2 | Opens the two E2 decks (`/Users/cobalt/cobalt-wt/.f23-render/pytest/test_table_rows_newest_first_80/out/opening_drive.pptx`, `.../test_why_is_cut_to_120_plus_el0/out/opening_drive.pptx`) and one E1 deck (`/Users/cobalt/cobalt-wt/.f23-render/data/2026-10-25`) in Keynote and in PowerPoint | Any ticker or `why` text cut off? During one open, did the open deck complain when the desk ran the render swap? | the desk runs the render's swap once during one open (SECOND PASS, f23-gate-run ec994048) |
| F5 X7 | Opens Obsidian on the DEV vault copy (path from 970's report) for 15 min | "done" | the desk fires two test checkpoints into the test note; his bullet byte-identical; no refused write |
| F5 X10 | Turns Obsidian Sync ON for the dev copy; the desk runs one test checkpoint; he turns Sync OFF | "done" | no `sync_revert_of` rows; no conflict file |
| F4 X9 Sync | During X10's Sync-on window, edits the open dev note once | "done" | no revert, no conflict |
| F5 X5 | Uses voice normally if he wishes (last, after 16:00); the desk starts scripted voice calls every 20 s for 10 min | Whether it felt slow | voice timeouts at 15 s; checkpoint latency |
| Check-in timer | Install `com.cobalt.checkin-timer` (R1959) | — | — |

Held, not a leg: F21 production genesis import — no card exists; his scope call, held for the memory discussion (brain 9b07db5a 2026-10-27).

After his legs: F23 pass two, then bootstrap deploy 1051; F4 plist load, then bootstrap deploy 1048.
