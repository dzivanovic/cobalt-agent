# BRAIN — direction for the desk: the script program, 2026-10-02 (seat `brain` `776c834d`, written 07:45 ET)

Source: `brain-unattended-2026-10-02.md` (`E 7` = a row of its E table; `FOR DEJAN 3` = an item of its last list). His rulings below were given in the brain session, 07:20–07:45 ET; his words are under `## HIS WORDS`. He allowed the brain more than one file.

## §0 Headline
1. He ruled A on FOR DEJAN 2–10. Item 1 is closed: he fixed the daily stops himself. Items 11 and 13 are pending and block nothing here; item 12 is answered by his order below.
2. His order: the script program is built by Anthropic seats only, with no outside house and no wait on a meter; built and deployed within one day, and what misses today lands tomorrow; no ruling per step. One exception, his: the script that touches production gets a Grok check.
3. Today: six builds, six Opus-only checks, ONE stacked deploy in tonight's window. Tomorrow, Saturday 10-03, any hour is lawful (`DEPLOY-HUB.md` P1 (iii)): the hub files adopt the scripts, the deploy scripts, the runner, the close timer.
4. No new card edits `BUILD-HUB.md`, `CHECK-HUB.md` or `DEPLOY-HUB.md` today. The one hub edit of today is the clause in `## DO NOW` 2, made by the desk on his order.
5. This file is the one list (L78). On this program the desk asks him nothing until DONE, except a step that failed twice by approved commands.

## ROWS FOR THE DESK TO RECORD
One `HIS RULING · APPROVED` row each, words to the words file from `## HIS WORDS`.

| # | ruling | takes effect |
|---|---|---|
| 1 | The bare-command fix, all three parts (10-01 R45): the hook, the system-prompt flag on the desk line and the fixed files' lines, the resend line in L78 | hook script: card `17`; his settings edit after tonight's deploy; the lines: tomorrow's adoption card; the law line: tonight's close |
| 2 | Permission by class, once: (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` in his settings and on every line; (b) `Bash(COBALT_ENV=dev uv run cobalt db *)` on the build, check, devfix and deploy lines, `Bash(COBALT_ENV=production*)` denied on the first three; (c) each kind's own report glob | now, as approval; `STANDING-LIST.md` gains a CLASSES section in card `16`; the lines change in tomorrow's adoption card |
| 3 | Desk deny strings: `Edit(//Users/cobalt/cobalt/ops/**)` and the fixed files | tomorrow, once `install-fixed.sh` is on `main` |
| 4 | Under an order the judge seat answers a held finding or a fence question that stays inside the ordered feature; work goes on; he reads the list at DONE and may veto; notes, money, sizing and growth beyond the feature wait for him | now. For this program the judge seat is the brain while he keeps it open |
| 5 | The STRIKE OR MERGE table (26 rows), one yes for the set | tonight's close |
| 6 | Folds at the nightly close only; a row binds from the moment it is written; the day's standing rulings sit in §5, one line each | now: no LAWS, contract, checklist or NOW edit before tonight's close |
| 7 | The close is started by a timer | card tomorrow; tonight the desk launches `desk-launch.sh close 2026-10-02` after the deploy's stop line |
| 8 | A single-branch deploy whose code equals its checked tip takes the check's suite lines (L68) | `DEPLOY-HUB.md` text, tomorrow's adoption card |
| 9 | A set with an empty restart set and no migration deploys at any hour (L43, L66) | `DEPLOY-HUB.md` P1 text, tomorrow's adoption card |
| 10 | The script program: Anthropic seats only, no outside house, no meter wait; built and deployed within one day, the rest tomorrow; no ruling per step. The script that touches production (`deploy-outage.sh`, tomorrow's card `20`) gets a Grok check | now |
| 11 | The brain may write more than one file | now |

## WHAT HIS ORDER SETS ASIDE (L73)
- L67's house A, for the cards this file names and no other. The fresh Opus check stays. Card `20` keeps house A = Grok.
- Nothing else. The three suites stay (L68). Tonight's set restarts the radar (`restarts.py` changes), so the window binds (L43, L66).

## DO NOW — the desk, in order, after `04` reads DEPLOYED
1. Record the rows above. Put the day's standing rulings in §5, one line each. Edit no law file (row 6).
2. `CHECK-HUB.md`: ONE Edit, a new line after the line that begins `- Gemini never sits ahead of a house that is up.`; commit it. His order is the approval (row 10; the precedent is 10-01 R39). The line, byte for byte:
   `- NO OUTSIDE HOUSE, HIS PER-CASE OVERRULE: a card whose header carries the line "HOUSE A: none — overruled <date> R<n>" (proved like a row of RULINGS) is checked by you alone. PREFLIGHT runs no house gate and no probe and records "house A: none (overruled <date> R<n>)". "## 1" and "## 3" are not run; "## 2" is your read; "## 4" to "## 8" bind as written. When "open" is above 0, "house B:" reads "none available" and the open items go under "## DECISIONS". The stop line reads "house A: none (overruled <date> R<n>)".`
3. Launch the build of card `11` now (it stands on `6ae3f133` and shares no file with the rest). Add row 10's number to its `RULINGS`.
4. Launch the cards below as the brain delivers them: `15` first; `16`, `17`, `18` on `15`'s checked tip; `13` on `11`'s checked tip.
5. Every check card of this file carries `HOUSE A: none — overruled 2026-10-02 R<row 10>` and `HOUSE B: as needed`. `desk-launch.sh check` reads neither change: it accepts `as needed` and ignores the new key.
6. A `decisions: ≥1` stop line of this program → MESSAGE the brain the report path; it answers each item (row 4).
7. Tonight: ONE deploy card for every READY branch, in the window. After its stop line: the close.
8. A classifier refusal of step 2 → one bare retry; a second refusal → he says one line in the desk chat.

## THE BUILD LIST — today
Cards `15`–`18` are written by the brain into `prompts/2026-10-02/` next; the desk commits them. Card `12` is taken into `16`. Card `13` is cut to its rows S0–S2 by the brain; its hub-text row moves to tomorrow. The `files` of `16`, `17`, `18` are disjoint by construction, so the stacked gate merges clean.

| card | job | base | builds | touches | check |
|---|---|---|---|---|---|
| `11` (drafted) | dev-rebuild | `6ae3f133` | E 4: `cobalt db dev-rebuild` | `src/cobalt/db_migrations/`, tests, docs | Opus only |
| `13` (rows S0–S2) | slot-guard | `11`'s checked tip | E 6 without hub text: the SLOTS line and the suite's early exit | the same module, `tests/cobalt/conftest.py` | Opus only |
| `15` | ops-seam | `main`; merges `02` `ee667f3c` and `07` `aeefb6df` | E 2, E 3; ONE glob rule classifies `ops/desk/**` as operator scripts and replaces both `OPS_TOOLS` lifts; `CHECK-HUB.md` line 10 keeps every string of both sides (10-01 R57) | `ops/desk/`, `src/cobalt/jobs/restarts.py`, the lock text of the hubs as `07` built it | Opus only; both parents are checked |
| `16` | launcher | `15`'s checked tip | E 5: the `devfix` kind, `DEVFIX-HUB.md`, verbs `dev-rebuild`, `dev-clean`, `dev-level`; E 7: pre-checks, `RECUT`, the watch line printed, the header fixed; the CLASSES section of the standing list | `ops/desk/desk-launch.sh`, `prompts/DEVFIX-HUB.md`, `prompts/CARD.md`, `prompts/STANDING-LIST.md` | Opus only |
| `17` | desk-tools | `15`'s checked tip | E 1 guard script, E 8 watch, E 15 card-fill, E 16 deploy-card, E 17 row and commit, E 18 done, E 19 gate-clean and job-clean, E 20 install-fixed, E 23 order-open, desk-wake, desk-handover | new files under `ops/desk/`, `tests/ops/`, docs | Opus only |
| `18` | worker-steps | `15`'s checked tip | E 9 stage-set, E 11 gate, E 12 authorize, E 13 preflight, E 14 house-probe; no hub file calls them yet | new files under `ops/desk/`, `tests/ops/`, docs | Opus only |

Order and clock: `11` and `15` build first, side by side. `16`, `17`, `18` build side by side on `15`'s tip; `13` on `11`'s. Until `07` is on `main` the launcher refuses a launch while a lock is held, so the desk launches when `ls /Users/cobalt/cobalt-wt/*/.env` is empty; a `FAILED: W` on a held lock is a `CONTINUE: W` when it frees.

## TONIGHT'S DEPLOY
- ONE set (L43): `05` voice-peers `76f7f7d5`, `15` (it carries `02` and `07`), `16`, `17`, `18`, the `13` head (it carries `11`), and `06` if its check is done.
- Window: the 20:00–21:00 pause, or after 21:00 with the outage begun before 04:00.
- A card not READY by 01:00 is dropped from the set, named, and ships tomorrow.
- After DEPLOYED his one install unlocks the desk tools: in `.claude/settings.json`, the allow `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` and the hook entry for the guard. The brain hands him the exact text when `17` is checked.

## TOMORROW — Saturday 10-03, any hour
| card | builds | check |
|---|---|---|
| `19` adoption | the hub files call the step scripts; the SLOTS lines and the self-heal; TREE STATE leaves; the class strings and the system-prompt flag on the four lines; P1 any-hour clause (row 9); the equal-tree clause (row 8) | Opus only; the `DEPLOY-HUB.md` part is read by one other house (L67) |
| `20` deploy steps | E 22: `deploy-step0.sh`, `deploy-outage.sh`, `deploy-smoke.sh` | house A = Grok (his word), plus a dry run before its first real use |
| `21` runner | E 21: `job-run.sh`, tried on one real card | Opus only |
| `22` close timer | E 10: the plist and its jobs registry entry | Opus only |
| his installs | the timer loaded; the desk deny strings (row 3) | — |
| the desk | applies the STRIKE OR MERGE table from tonight's close list | — |

## PENDING HIS WORD — nothing here waits for them
- FOR DEJAN 11: X5 (a tap overwritten by a waiting refresh, live): a fix card now, or backlog.
- FOR DEJAN 13: a standing `BRAIN-HUB.md`.

## HIS WORDS — for `cto-2026-10-02-words.md`, verbatim, brain session 2026-10-02
Answering the brain's "do it here or with the desk, and can it be done today":
"First, you, you may run a separate file for the direction. I allow you more than one file. Second, for the build, of the scripts these are internal scripts that we're working through in Anthropic specific issue where the harness from Anthropic is stopping Anthropic from working so no we don't need another houses to check I want this build as soon as possible and I want them built only by Anthropic seat and we don't need to wait for any checks and houses to be uh, invoked I don't want to four day build this 24 scripts need to be built within one day and deployed within one day if they can't be done today they need to be done tomorrow And they don't need to wait for me to rule on every single step of the process. We create a list now we build the list we check the list and that's it."
Answering the brain's ten items (FOR DEJAN 1–10 of `brain-unattended-2026-10-02.md`, each recommended A; item 1 closed by his own fix):
"1) a 2) a 3) a 4) a 5) a 6) a 7) a 8) a 9) a 10) a"
"We should run an outside Grok check for only one that touches production as well"

DIRECTION WRITTEN — cards `15`–`18` and the cut `13` follow from the brain
