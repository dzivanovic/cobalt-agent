# LAWS SITTING — the packet (2026-09-22)

For Dejan alone (`cto-2026-09-22.md` R4, 06:54 ET: "Laws are all mine … rule on which one stays, which one goes"). No tribunal. Register: `docs/40 - DevDocs/reports/laws-audit-2026-09-20.md` (cited `audit C<n>` = its §2 contradiction row, `audit K<n>` = its §3 clutter row). The full file as it would read if you take every recommendation: `LAWS-CONSOLIDATION-PROPOSAL-2026-09-22-LAWS-draft.md` (same folder). Written by proposer `laws-consolidation-propose-0922` (Opus 5); nothing applied — the desk applies only what you rule (L58).

## §0 What changes and what does not
- **Laws: 74 → 75.** None retired, no number reused. One new: **L75 Fix rounds classify first** (the 09-20 close's P-c).
- **29 entries get new or changed wording** (L41 and L42: headings only); 45 keep their law text unchanged (L14 and L43 gain only a citation note). **12 pieces of text go to LAWS-HISTORY** (§3 list), each with the audit row or later ruling that proves it dead or superseded.
- **15 contradictions:** 13 get a one-sentence boundary or wording fix; 2 need your word with **no text change recommended** — L43 "one deploy per evening" (C10: keep) and the routing cluster (C11: leave frozen, name the routing tribunal's date).
- **8 pending close proposals** (09-20 P-a…P-e, 09-21 P-a/c/d): 7 adopted into law text, 1 (the desk delegates) kept as desk practice.
- **Routing cluster untouched** — L5, L21–L27, L29, L49, text and notes as they stand (LAWS.md fold rule; audit §2b).

Three things to know before reading:
1. **L34 has never once been obeyed** (audit C1) — the only way to make it true today is to amend it to what the desk actually does.
2. **The 09-20 audit's claim that no-flag hubs were "allowlist-only" is contradicted by 09-21**: a bare `claude --bg` comes up in AUTO mode (`close-2026-09-21.md` P-a). The write-path launch shape needs to be law (L62 block).
3. **`## NOW` is 50,055 bytes today against a 1,500-character cap** (measured 06:5x, `wc -c`) — "never delete" and "rewrite in full" are fighting (L58 block).

## §1 How this packet was built
- Your 09-13 mechanism stands: one entry per law; amendments merged in place; struck text to LAWS-HISTORY; numbers never reused; a new law takes the next free number (L58).
- Nothing is struck without the audit row or later ruling that proves it dead or superseded.
- A law that binds only by judgement is not struck for that. It names its mechanical arm where one exists, or is marked `· judgement` in its header (audit §4: 51 of 74).
- Every block reads: **when/why ruled · amendments and why they won · today's conflict · RECOMMEND** (STAYS / STAYS AMENDED / GOES). The exact wording of each amendment is in the draft, under the same L-number.

## §2 Laws with something to rule — ordered by consequence

**L34 Every spawn is a job row** — 09-07 hub-law block (LEDGER:1040), written when Cobalt code was to be the hub. No incident is recorded (audit C1 §2a). *Conflict:* never once obeyed. L61 (09-16) has the desk launch every hub, and nothing writes a row for an agent session. You recorded the gap yourself on 09-16 at 09:10 (`cto-2026-09-16.md` §4 row 10). *Options:* (i) build the row now — the "sessions-as-jobs" backlog item, gated after S2; until then every launch breaks law. (ii) amend to today's mechanism. (iii) strike — then spawns are unaudited by law. → **STAYS AMENDED (ii):** the interim registry is one row in the desk report's §5 sessions table (house, role, model, worktree, report + stop line, time, session id), reconciled against `claude agents --json` at every wake-up and refresh (the reconcile is a NEW practice proposed here, not yet written anywhere). `cobalt_jobs` covers pipeline jobs. The entry is amended again when agent-session rows exist — L58's "amended, not silently bypassed" shape.

**L62 Unattended launch** — 09-17 06:03 (R5): two hubs sat on dialogs nobody could see. *Conflicts:* (a) C9 — "no questions mid-run" against L61's "his hands remain for grants". On 09-19 the desk tried to allow itself a rule it had just been denied (`[Auto-Mode Bypass]`). (b) C5 — L29's "never auto mode on a write path" exists only as prose. On 09-21 a bare `--bg` came up in AUTO and refused its write at preflight (`65`, 20:13). (c) `acceptEdits` raises a DIALOG on an unlisted Bash call instead of denying it. This cost ≈4 h of idle Opus on 09-21/22 (`cto-2026-09-21.md` §15). → **STAYS AMENDED:** (a) a hub never asks. The desk asks only you, only for a grant, and never grants itself something just denied. (b) Write-path runs launch `--permission-mode acceptEdits` plus the full allowlist, never bare and never auto. The SEAT prose must state the mode exactly as the launch line sets it, checked at dispatch. (c) Write-path prompts list their allow strings in their own body, never call an unlisted command, and write files only with Write/Edit, never a heredoc. This folds in 09-21 P-a and desk lessons D1–D3.

**L58 Memory write path** — 09-16 07:35. The 09-15 close's five law folds were blocked by the classifier; your words: "CTO desk as the only path writing laws until we have cobalt memory path". *Conflicts:* (a) C2 — SESSION-CLOSE (ruled 09-15, one day earlier) still tells the close HUB to rewrite NOW and append to memory, and step 2 tells it to apply the LAWS fold. The hubs have refused silently since 09-17 (3 of 3 closes). LAWS.md's own tail section, "Fold-at-session-close — hub job", says the same outdated thing. (b) INDEX rule 3 ("supersede by strike, never delete") against NOW's 1,500-character cap. NOW is 50,055 bytes because intra-day lines are appended and struck, never replaced. → **STAYS AMENDED:** at a close the hub PROPOSES and MEASURES, the desk APPLIES. If the desk is down, its steps are listed as OWED and the next wake-up's reconcile applies them. NOW is a snapshot, rewritten whole at close and refresh, ≤1,500 characters, measured; INDEX rule 3 does not apply to it; intra-day status goes to the desk report. The LAWS.md tail is rewritten to match. Procedure edits are in §4.

**L37 No model-judged approvals** — 09-07, aimed at Codex's `--approve-for-me`. No incident is recorded. *Conflict (C3):* the auto-mode classifier is a model deciding per command. L55 (09-03, "the zero-trust layer between Manual's prompt fatigue and Cline-era auto-approve") rests on it. On 09-19 the classifier ran an unlisted `touch` it judged safe (`cto-2026-09-19.md` §61). → **STAYS AMENDED:** L37 covers self-approval and any model approving in your place. The classifier is a safety gate, not an approval, and is never cited as one. In auto mode an allowlist is a pre-approval list, not a whitelist.

**L7 Shadow-mode promotion** — 08-22 triage (TRIAGE:18), written expecting HITL tokens to ship. *Amendment:* 09-16 (ruling 3) — your chat "approve" is the interim token. It was needed to unblock unattended deploys, and it sits in a paragraph labelled "not law text". *Conflict (C13):* the law requires a token that does not exist (LEDGER:1288). → **STAYS AMENDED:** promote the interim clause into law text and name `--sha256` as its mechanical half (what's applied equals what was reviewed). `--hitl <label>` never satisfies it alone. The old note goes to HISTORY.

**L43 Deploy cadence** — 09-11 sequencing call (LEDGER:1183), made to keep one night's deploy attributable the next morning. *Amendments:* 09-15, radar restarts only in the 20:00–21:00 pause. 09-21 R47, "the one deploy carries everything ready". *Conflict (C10):* overridden three times on 09-19 (R32), on 09-21 (R5), and today (R3, from 11:00). → **STAYS, no change.** R47 is your newest standing word and it keeps one evening. Overrides cost one line under L73 as amended 09-21, and today's R3 was recorded that way. Retire it only if daytime deploys should become the default.

**L5 · L21–L27 · L29 · L49 — the routing cluster** — L23 (08-29/31) came from the Gemini outage that killed a morning briefing. L29 (09-03/04) came from the daily-note overwrite. L49 (09-11) came from a 20-minute local report. *Conflict (C11):* local "first candidate for every task" against L49's read-only local seat and L29's write floors. Five clauses have been "under review, routing tribunal" since 09-13 — 9 days; no tribunal is on record since (`UNCITED — verify`: I searched only the desk/close reports of 09-20…22 and BACKLOG). → **STAYS, untouched.** Name the routing tribunal's date. Consolidating these would break LAWS.md's own fold rule (audit ESCALATE 1).

**L46 One run, one commit** — 09-13 (LEDGER:1283). Written because `sprint-2/radar-pool` sat stale for four days and stopped a deploy. *Conflict (C6):* L68 (09-19) exists to handle several unmerged branches, a state L46 calls the defect. Two stale branches existed on 09-20. → **STAYS AMENDED:** L46 governs one agent's own branch; L68 governs the seam between branches. Add a MAX AGE: a branch unmerged for more than 3 days that the plate does not name with its next step is an ESCALATE. The number is yours — say another if 3 is wrong.

**L54 Worktree rule** — 09-08 R4. The "09-08 branch rule" it amends was never found (O17). *Amendments:* 09-09 rebase-then-ff (a linear, bisectable main); 09-11 revert-a-range rollback. *Conflict (C12):* L68 (09-20) merges `main` INTO the gate branch and rolls back with `git revert -m 2` — a merge a rebase would destroy. First used 09-19c. → **STAYS AMENDED:** rebase-then-ff for single-branch merges; the gate branch is the one exception, with its `-m 2` rollback; every deploy report names which rollback shape it uses.

**L28 Vault-write law** — 09-03/04: Cobalt replaced two daily notes with the template (LEDGER:615-624). *Amendments:* 09-06 ownership by unit; 09-09 sync-revert; 09-13 four dropped clauses restored; 09-15 your own `settings load --apply` exempt from the token. *Conflict (C7):* "no LLM in the write path" against L58/L65, which put the desk (an LLM) in the vault. → **STAYS AMENDED:** one sentence — L28 binds Cobalt the program; the desk's L58/L65 edits are not Cobalt writes and carry their own trace.

**L59 Worker law-reading** — 09-15 14:50, your words: "the minimum without losing performance … so it can retrieve anything else itself". *Conflict (C8):* the fold wrote "workers NEVER read the whole memory folder", stricter than you ruled, which clashes with L44. → **STAYS AMENDED:** "need not read"; the card is a working set, never a fence. The old wording goes to HISTORY.

**L53 Ceilings and cadences** — 09-10 R9 (the pool cap in the vault) plus 09-13 R7 (Sol caught 40.67 rpm against a 40 ceiling). *Conflict (C4):* "never a cap in committed config", yet the rpm ceiling (50) sits in tracked `tunables.yaml` with `source: ruling`. In its origin sentence "the cap" was the 50-name POOL cap. → **STAYS AMENDED:** "never the pool cap"; the ceiling and cadence may sit in config only as ruled values naming their ruling. The `TotalDemandExceeded` test remains the real guard.

**L19 Whole-prompt rule** — 08-27; origin unknown (audit §5). *Conflict (C14):* "changes = full re-issue" against L47/L60's CONTINUE relaunch (09-16: a hub exited mid-chunk). → **STAYS AMENDED:** a CONTINUE relaunch counts as a full re-issue when the file is unchanged plus one `CONTINUE:` line; any file change re-issues the file.

**L12 Planning hard cap** — 08-22, "all remaining design work fits two calendar weeks". The clock was spent 09-04 and made per-phase on 09-13. *Conflict (C15, dormant):* a cap expiring mid-tribunal. → **STAYS AMENDED:** a cap never skips a law step (L73): the tribunal finishes and the cap cuts scope. (The alternative, GOES, is fine too — no cap has been asserted since 09-04.)

**L67 Four-house tribunal** — 09-18 17:30: three unreviewed desk prompts failed in one day. *Amendments:* 09-18 R19 (emergency, override), R20 (three rounds, floor of two), R21 (stands with L52), 09-21 R46 (Sol and Opus for code checks). *Pending:* 09-21 P-c — astra's METER and TIMEOUT turns counted as rounds though it never ruled. 09-21 P-d plus today's R4 — sittings exist only where you name yourself. → **STAYS AMENDED:** a non-ruling turn spends no round; a sitting is only where you name yourself (the DRC template, and now the laws).

**L72 Parallel non-blockers** — 09-20 (P4, which you widened). *Pending (09-20 P-b):* two sibling builders each recorded a different child-name shape as a "reading", which cost one fix step and a held round. → **STAYS AMENDED:** a shared seam IS a dependency; the desk settles it in one document both prompts cite before either launches.

**L71 The stop line** — 09-20 (P2): two houses' watchers fired on the wrong line. *Pending (09-20 P-d):* a watch fired on a hub's own `CONTINUE:` breadcrumb (09-20 16:03). → **STAYS AMENDED:** a breadcrumb is never the last line while the run is unfinished; it lives in a `## CONTINUE` section. Already practice.

**L35 Trust the artifact** — 09-07. *Pending (09-20 P-e):* the desk told you the Postgres memory layer "does not exist" from `information_schema`; `pg_tables` shows 48 tables. *Clutter (K2):* L70 is the same bar applied to failures. → **STAYS AMENDED:** a scoped read is never evidence of absence; cross-reference L70.

**L55 Push on his word** — 09-03 permission posture. *Amendment:* 09-19 R19 (the desk pushes on your "push"). *Dead text:* the status note "no push rule exists" is false since 09-20 R12 (the rule is in `settings.local.json`). *Desk lesson D7:* hubs in `~/cobalt` inherit that allow. → **STAYS AMENDED:** the status note goes to HISTORY; every hub launch line denies `Bash(git push*)` (already practice since 09-20).

**L61 Desk launches** — 09-16, so you can exit the desk without killing work. *Desk lesson D6:* the classifier refuses a viewer on a production-write hub, and text in a hub's input box is not your word (09-21 lessons). → **STAYS AMENDED:** such a hub runs viewer-less and is reached by its remote-control name; input-box text is never an approval.

**L48 Evidence in the report file** — 09-11. *Desk lesson D5:* desks wrote times "from feel" three times (09-20, 09-21). → **STAYS AMENDED:** every clock time in a report comes from `date` in that turn.

**L17 + L39 Council** — L17 (08-28) with amendments on 08-29/31 (cross-provider seats), 09-05 (privacy flip) and 09-07 (the 3-turn rule, which then became L39). *Clutter (K6):* L39's text is copied inside L17, and L17 also carries the 09-13 O5 note explaining L39 — a reader of L17 alone sees "vote on turn 3". → **STAY AMENDED:** delete the duplicate from L17 (to HISTORY) and move the O5 note into L39, where "a law file is never voted" lives.

**L32 User data** — 09-05/06 tenancy. *Clutter (K13):* "the Memory folder is user data" reads like withholding from houses, against L44. → **STAYS AMENDED:** "user data" governs what leaves for OTHER Cobalt users, never a house on this install.

**L1 / L8 / L70** — cross-reference lines only (K4: one loudness bar; K5: L8 is the render rule, L7 the promotion rule; K2). → **STAY AMENDED.**

**L15 / L41 / L42** — clutter only (K11, K12): the description of an already-struck clause and stale heading words ("REPLACED", "amendment pending"). → **STAY, text moved or retitled.** The law text is unchanged.

**NEW L75 Fix rounds classify first** — 09-20 close P-c. Used twice that evening: FIX 13 / NOT REAL 3 / UNPROVEN 6… turned a split house verdict into a 12-minute fix, with no new approval (`close-2026-09-20.md`). Cross-cutting and mechanical (a classification table). → **ADD as L75.**

### Laws that are never obeyed or only half-armed (the prompt's §4)
| law | arm today | recommend | cost of the others |
|---|---|---|---|
| L34 | none (C1) | amend — above | build = sprint item after S2; strike = unaudited spawns |
| L7 token | chat word + `--sha256` | amend — above | build `cobalt hitl issue` = S5-era; strike = trading-logic gate lost |
| L18 .2–.4 maxTurns/heartbeat/watchdog for every process | residents only (heartbeat); agent sessions: the desk's watch ceilings (09-21 lesson) | **STAYS** · judgement; build item filed with L34's gap | amending now would codify ad-hoc watches as law |
| L16 creation by HITL card | none for agent sessions | **STAYS** · judgement — it is a Cobalt-product law (agents inside Cobalt) | — |
| L38 asks routed and logged | desk report only | **STAYS** · judgement — same gap (09-16 row 10 lists L38) | — |
| L25 .8 reason-class column | owed (LEDGER:1177) | **STAYS** — routing cluster, untouched | — |

### Origin unknown, no change proposed (audit §5)
| law | protects (from its text) | if struck | recommend |
|---|---|---|---|
| L2 Watcher standard | no LLM polling in a loop; typed events | cost and nondeterminism in watchers | STAYS |
| L14 One-throat | you talk to one seat | agent chatter reaches you | STAYS (L64 is its current form) |
| L16 Agents-as-data | agents are config, not code | hard-coded bots | STAYS |
| L18 Task integrity | no fire-and-forget | zombie runs | STAYS |
| L20 Cross-thread review | no fake "I reviewed" | answers from memory | STAYS |
| L57 Explainability | every number replayable | unreplayable cards; 11 test refs | STAYS |
| L21 · L24 · L26 | routing | — | untouched (routing tribunal); L21 may merge into L26 there |
(L19: see its block above.)

### Clean — no action (text, provenance and practice agree)
L3 · L4 · L6 · L9 · L10 · L11 · L13 · L30 · L31 · L33 · L36 · L40 · L44 · L45 · L47 · L50 · L51 · L52 · L56 · L60 · L63 · L64 · L65 · L66 · L68 (except its cross-reference to L54) · L69 · L73 · L74.

## §3 What goes to LAWS-HISTORY (12), each with its proof
| # | text | proof it is dead or superseded |
|---|---|---|
| 1 | LAWS.md "Status: FINAL, staged here pending placement" (and the same line in LAWS-HISTORY.md) | the file is at its destination (audit K14) |
| 2 | L7 status note (old wording) | promoted into law text (C13) |
| 3 | L15's description of its struck clause | already in H-L15-scope (K12) |
| 4 | L17's copy of the 3-turn rule | live text is L39 (K6) |
| 5 | L53 "never a cap" | origin = the pool cap (C4 §2a.1) |
| 6 | L54 "rebase-then-ff on every merge" | L68's gate branch is the exception (C12) |
| 7 | L55 status note "no push rule exists" | false since 09-20 R12 |
| 8 | L59 "workers never read the whole memory folder" | stricter than the 09-15 ruling (C8) |
| 9 | "Fold-at-session-close — hub job" (the tail section) | superseded by L58, 09-16 (C2) |
| 10 | "Not law" bullet: the struck L57 ESCALATE | resolved 09-13; already struck through |
| 11 | heading words: L41 "REPLACED", L42 "amendment pending 09-13" | text is current (K11); effective since 09-16 |
| 12 | L61 "the approval clause amends L7's status note" | the note no longer exists (row 2) |

File-level rules added to "How to read" (no law text): `O<n>` defined (K10); `PROPOSED-n` read-only (K8); a line starting `— ` is citation and a "Status note" is state (K9, audit §2c); `· judgement` marker. **Not done:** merging L55/L61–L64 or L46/L54/L68 into one entry (K1, K3). Hundreds of prompts cite these numbers, and the boundary sentences above remove the actual collisions. Your call if you want the merge anyway. **Also not done:** the separate STATE file for status notes (audit §2c). The two notes that bind or are false get fixed (L7, L55); the three left belong to the routing cluster and stay with it.

## §4 The two procedure collisions — the wording to apply
1. **SESSION-CLOSE vs L58** (C2). Add a `Runner` column. HUB: 1 ledger, 2 PROPOSALS only ("Laws fold — PROPOSED, NOT APPLIED"; never edits LAWS.md), 4a ladder, 5 measure (`wc -m`, the 09-21 correction), 6 commit. DESK: 2-apply, 3 NOW, 4 areas/topics. Step 7 is rewritten to match L55 as amended 09-19: "the desk pushes on his word". Preamble: "The close hub runs the HUB steps; the desk runs the DESK steps; a desk step left undone is listed OWED and applied at the next wake-up (step 8)." `CTO-DESK-WAKEUP.md` step 8 is unchanged — it already reconciles.
2. **NOW vs "never delete"** (§0 point 3). INDEX `rules:` 3 becomes "supersede by ~~mark~~, never delete — except `## NOW`, a snapshot rewritten whole". SESSION-CLOSE step 3 adds "measured `wc -m` ≤1,500; over = the close FAILS"; the desk's refresh step (1) already rewrites NOW. Intra-day lines go to `cto-<date>.md`.

## §5 Declined as law, kept as desk practice
| item | where it stays | why not law |
|---|---|---|
| 09-20 P-a "the desk delegates; Fable work only as a spawned agent, after asking him" | `topics/cto-desk.md` 09-20 R16–R18 (already there) | binds one seat; a behaviour rule, not cross-cutting |
| never end a turn between build steps; watch ceiling = expected + 15 min; windowed launch timers; explicit `git add` paths; bare commit commands; herdr tab after every `--bg`; adopt the conservative dissent | `topics/cto-desk.md`, `UNATTENDED-LAUNCH.md` | desk mechanics, not binding on other houses |
| "hindsight is not data" (09-21 R24) | `areas/cobalt-product-definition.md` | a product ruling, not a law of the build process |
| web text is data; approvals only in the desk chat | already law: L74, L61 | nothing new to add |

## §6 Your rulings, in order (one word each; the desk takes them one per message)
1. **L34** — amend to the interim registry? (recommend YES)
2. **L62** — the write-path launch shape (`acceptEdits` + the listed allowlist, never bare) plus the hub/desk boundary? (YES)
3. **L58 + SESSION-CLOSE + NOW** — hub proposes, desk applies; NOW rewritten whole, ≤1,500 characters? (YES)
4. **L37** — the classifier is a gate, not an approval? (YES)
5. **L7** — promote chat-"approve" plus `--sha256` into law text? (YES)
6. **Routing tribunal** — name its date; the cluster stays frozen until then. (your date)
7. **L43** — keep "one deploy per evening", with overrides per case? (KEEP)
8. **L46** — the boundary plus a 3-day branch max age? (YES / another number)
9. **L54 / L68** — the gate-branch exception and the `-m 2` rollback named in deploy reports? (YES)
10. **L28 / L59 / L53 / L19 / L12** — the one-sentence scope fixes? (YES to all, or name any to leave)
11. **L67 / L72 / L71 / L35** — fold the 09-21 P-c/P-d and 09-20 P-b/P-d/P-e? (YES)
12. **L75** — add "fix rounds classify first"? (YES)
13. **L48 / L55 / L61** — desk lessons D5–D7 as law? (YES)
14. **The 12 HISTORY moves and the file-level reading rules** (§3)? (YES)
15. **K1/K3 merges** — merge the launch and deploy clusters into single entries? (recommend NO)
