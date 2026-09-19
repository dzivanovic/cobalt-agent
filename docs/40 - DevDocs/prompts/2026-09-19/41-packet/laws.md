# LAWS.md excerpts — verbatim, copied from `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md`

`LAWS.md` is the ONLY canonical current law. These four entries are the ones `38-deploy-p4.md` is measured against. Entry text is reproduced exactly, including its source line.

---

### L43 Deploy cadence (ruled 09-10; amended 09-15)
One production deploy per evening.
[amended 2026-09-15] Production `com.cobalt.radar` restarts only inside the 20:00–21:00 ET market_reset pause, or during overnight idle (after the pause, before the 04:00 premarket window) on a trading day; never while a scanning session is open. `com.cobalt.aset` and one-shot jobs are not bound by this window. Approved for the fold 2026-09-15 (Dejan); applied by the CTO desk at the 2026-09-15 close.
— LEDGER:1153 (held 09-11 LEDGER:1179, 09-13 LEDGER:1287); amendment LEDGER 2026-09-15 appendix

---

### L54 Worktree rule (ruled 09-08, R4; amended 09-09; rollback restated 09-11)
`~/cobalt` IS production; every Code prompt works in `~/cobalt-wt/<branch>` off main; production proofs only after a `--ff-only` merge, from `~/cobalt`, as a named step; merge = deploy. [amended 09-09] Rebase-then-ff on every merge. Rollback of a merged range is `git revert` of the merge range, never a `reset --hard` to a tag once later work has landed above it.
— LEDGER:1058, :1119, :1210. Interacts with L46. (O17: this law says it amends a "09-08 branch rule" that does not appear anywhere in the ledger; source still owed — stands as the earliest text regardless.)

---

### L66 Residents down before the merge (alias PROPOSED-5) (ruled 2026-09-17 21:54 ET, R19 "A") — amends L43's restart clause and L54's "merge = deploy"
No merge into `~/cobalt` while a resident can respawn into it: the deploy stops `com.cobalt.aset` and `com.cobalt.radar` (`launchctl bootout`, or the equivalent that also disarms `KeepAlive`) BEFORE the merge and migration, and restarts them after, all inside the 20:00–21:00 market_reset pause on a trading day (L43). A write to `"user".trader_settings` is refused during the pause, so a deploy that carries one runs that write after 21:00 in overnight idle and restarts the radar then. Evidence: 2026-09-17 19:18–19:21 launchd respawned the radar into merged P2 code three times, outside the pause, before the revert (`deploy-2026-09-17.md` ESCALATE 2). A staged checkout that production follows only at restart (option B) is not built; it may be proposed later as an ops item.
— Source: Dejan, desk chat 21:54 ET, "A", to the desk's A/B; `cto-2026-09-17.md` R19. Close list (e) (settings phase before 20:00) is superseded by this shape and is not folded.

---

### L68 Integrated gate before any merge (ruled 2026-09-19)
No branch merges while a second unmerged branch exists, unless an integrated pre-merge gate on the stacked tree is green — the offline suite and the with-DB suite run on the branch that combines them, before the merge, never after it in `~/cobalt`.
— Evidence: two seams no branch's own suite could see — 09-17 ops-0917's `load_sources(...)` call sites vs P2's new keyword; 09-18 P2's fixture vs ops-0918's mandatory seventh step-down row (`43 failed / 1455 passed / 5 errors` on the stack) — `stack-gate-2026-09-18.md` ESCALATE 2, `cto-2026-09-18.md` §14. Interacts with L46, L54, L66.

---

## Context a reviewer needs for L68, stated as fact, not as an answer

Three unmerged branches exist today: `sprint-2/p4` (lands in this deploy), `ops/2026-09-19` and `archiver/append-0919` (deploy 3, Sunday). The desk read L68's words *"while a second unmerged branch exists"* and *"the branch that combines them"* as requiring all three in the gate, while merging only P4. Dejan's own gloss when he approved L68 (R19, `cto-2026-09-19.md` §4) reads: *"three unmerged branches exist (`sprint-2/p4`, `ops/2026-09-19`, `archiver/append-0919`), so before P4 merges an integrated gate (offline + with-DB suites) runs on a stack branch that combines what is about to land, as deploy 1 did on 09-19"* — "what is about to land" admits the narrower reading. **Whether the gate must stack all three or only what lands is an OPEN question for Dejan, not for a reviewer to settle; say which reading you think the prompt's §1 implements and whether the prompt is sound under each.**
