# Hands off — brain answer 2026-10-12

Dejan tells the desk to read this file and act on it. Everything below is his word, recorded in `reports/brain-direction-2026-10-02.md` `## RULED 2026-10-12 — nothing waits on his hands` (with "His follow-up"). The desk records it as HIS RULING · APPROVED, writes memory now (10-05 ROW C) and commits this file and the direction file.

## §0 Headline
- Nothing waits on his hands at night. A blocked item stops only itself, and everything else runs. What needs him goes into the morning report or a daytime sitting, with a full explanation.
- From now on, a new permission, setting or rule never travels by relay between seats. It is a CARD written by a drafter. He approves CLASSES of work once, and every future card inside an approved class runs without his word. This file names the classes and the first cards.
- Approved production writes are allowed, by one dedicated seat.

## STANDING NOW (no card; the desk records and applies)
1. A BLOCKED CARD STOPS ONLY ITSELF. Every queue item that does not depend on it keeps running, any hour.
2. A NIGHT ENDS IN A REPORT, NOT A WAIT. A seat recovers a harness red (salvage, rebuild, rerun) and records it. No seat asks him to type a command at night.
3. HIS HAND ONLY BY DAY. When something truly needs his hand, the item goes into the morning report under `## NEEDS HIS HAND`, one entry each: what was blocked · by which rule or tool · why no seat could do it · the exact line he types · what it unblocks. Seats work around the blocked ITEM, never around a permission check.
4. NO RELAYED PERMISSIONS. A change to an allow or deny list, a guard rule, a setting, a law or a hub line goes by card, never by a brain↔desk message. A card inside an approved class (below) needs no word of his. A need that fits no class goes to him as a NEW CLASS, by day.

## STANDING CLASSES (his approval is for the CLASS, and it covers every future card inside it)
He approves a class once. Any card, now or later, that only installs something inside an approved class is built, checked and installed with NO further word of his: the card names its class in its header (`CLASS: <n>`), and the check verifies it stays inside. Only a need that fits no class comes to him, as a new class to add here, by day.
| # | class | always allowed | never |
|---|---|---|---|
| K1 | WORKSPACE CLEANUP | Removing untracked, ignored and scratch files and folders, and whole failed trees, inside agent workspaces (`cobalt-wt/*`, job tmp dirs, scratch dirs) | Tracked files on main; anything outside a workspace |
| K2 | RUN AND EXPLORE | Builds, checks, test runs, bake-offs, probes, spikes, and installing or trying new tools and CLIs inside a workspace; starting and stopping seats and dev services | Secrets read or sent |
| K3 | APPROVED PRODUCTION WRITES | A production DB write named by a card row or a ruling of his, run by the production-write seat (Opus 5.5+), backup first, report after | Any other seat writing production; an unnamed write |
| K4 | PRODUCTION OPS | Restarting, deploying and rolling back production services through the deploy hubs | Data deletion outside K3 |
| K5 | HARNESS UPKEEP | Allow and deny strings, guard rules, launcher refusals and hub lines that serve K1–K4, changed by card | Widening secrets access or K3's seat |
| — | SECRETS (kept, his 10-08 words) | — | `.env`, `~/.cobalt_key` and password stores are never read or sent |

## CARDS (drafters write them; each header names its `CLASS:`; none waits for his word once K1–K5 are approved)
| # | card | what it does | status |
|---|---|---|---|
| C1 | CLEANUP | Build, check and gate seats and the desk may remove untracked, ignored and scratch paths inside `/Users/cobalt/cobalt-wt/<job>/` and `$CLAUDE_JOB_DIR/tmp`, and a failed tree by `job-clean.sh`. Never a tracked file, never outside those roots. Carries the BUILD-HUB row: "a RUN probe is staged outside the worktree, never under docs/ or src/, and gone before W". | drafter launched last night (desk record) |
| C2 | BLOCKER SURVEY (read-only) | Lists every law, hub line, `bare-guard.py` rule, allow or deny list and launcher refusal that would stop exploratory work (builds, checks, deletes, starts and stops of services and seats, bake-offs, new tools). Each item gets its place, what it blocks and a proposed change. Output: ONE decision sheet for him. | drafter launched last night |
| C3 | PRODUCTION-WRITE SEAT | A dedicated seat, Opus 5.5+ (L29), runs an APPROVED production write: one named by a card row or a recorded ruling of his. Order: the backup or rollback step first, then the write, then a report. Its own launch line and allow string. The `COBALT_ENV=production*` deny and guard G2 stay on every other line. Secrets are never read or sent. The drafter takes C2's production items as input and may start before C2 is done. | to launch now |
| C4 | NEEDS HIS HAND | Hub text for the day-open and close prompts: a `## NEEDS HIS HAND` section in the shape of standing item 3, empty when nothing is owed. | to launch now |
| C5 | THE SHEET'S CHANGES | One card per area, from his decisions on C2's sheet. | after the sheet |

## HIS APPROVAL
K1–K5 once. C1–C5 then run under them. C2's sheet comes to him only for items that fit no class. A settings string that no seat can install is shown once, by day, with why.

## FOR THE CHECK
`hands off 2026-10-12 brain: standing: blocked card stops only itself; night ends in a report; his hand only by day under NEEDS HIS HAND with full why; no relayed permissions (cards only). Classes K1-K5 approved once and covering every future card inside them; only a need outside every class comes to him, by day. Cards C1 cleanup, C2 survey, C3 production-write seat, C4 NEEDS HIS HAND, C5 sheet changes.`
