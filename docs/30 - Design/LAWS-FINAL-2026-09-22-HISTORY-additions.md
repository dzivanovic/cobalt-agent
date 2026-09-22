# LAWS-HISTORY additions — 2026-09-22 laws sitting (R80–R88)

Staged additions to `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS-HISTORY.md`, in that file's entry shape (moved, never deleted; verbatim wording, date, source line, what replaced it). The desk pastes these in at apply, after the existing `## H-L68-scope` entry (the file's current last entry).

---

## H-L12-retired — L12 Planning hard cap, RETIRED IN FULL 2026-09-22
Source: current LAWS.md L12 (ruled 08-22; amended 09-13, O4), superseding the already-moved clock text at `## H-L12`.
Verbatim: "Standing principle, not a spent one-time clock: when a design/planning phase's cap is hit, ship with what's decided; the rest becomes "decide during build". [amended 09-13, O4] The original 08-22 two-week clock is spent (Product Definition phase closed 09-04, LEDGER:658-659) and does not carry forward automatically — a new design phase does not inherit it; the cap is reasserted per phase by ruling. Original clock text → LAWS-HISTORY H-L12."
Retired by: Dejan, `cto-2026-09-22.md` R84, 17:0x ET — "B" → "L12 RETIRED to LAWS-HISTORY (number never reused); design time is bounded by L67's three-round cap and L73." Number L12 is never reused (R84).

## H-L17-dup — L17's copied 09-07 turn-limit paragraph, removed 2026-09-22 (duplicate of L39)
Source: LAWS.md L17 [amended 09-07, L39] paragraph, as it stood 2026-09-13 → 2026-09-22.
Verbatim: "[amended 09-07, L39] A council answers in ≤3 turns — agree, or vote on turn 3 with dissent recorded in the artifact; no fourth turn; unresolved → Dejan. Council = a hub job type."
Also moved out of L17, the 09-13 resolution note that sat beside it:
Verbatim: "[resolved 09-13, O5] Reading B governs: synthesis on reasoning quality is how a council's recommendation is formed on turns 1–2; L39's turn-3 vote is the termination record for when synthesis does not converge, not a return to vote-tallying. A LAW FILE is never voted at all — an unresolved disagreement about law text is always an OPEN item for Dejan (`prompt-fable-r1.md:7`; see L39)."
Replaced by: `cto-2026-09-22.md` R87 (K6, laws-audit-2026-09-20.md §3): "[amended 2026-09-22, R87 K6] How a council TERMINATES, and the rule that a law file is never voted: L39." The removed text's substance is not lost — it already exists, near-verbatim, as L39's own text (LEDGER:1045) and L39's own [resolved 09-13, O5] paragraph (moved there, not deleted).

## H-L43-headline — L43's original headline "One production deploy per evening.", superseded 2026-09-22
Source: LAWS.md L43, as it stood 09-10 → 2026-09-22 (title "Deploy cadence" and its opening sentence).
Verbatim: "### L43 Deploy cadence (ruled 09-10; amended 09-15, 2026-09-21)
One production deploy per evening."
Replaced by: Dejan, `cto-2026-09-22.md` R83, 17:0x ET — neither the KEEP nor the RETIRE option offered; his words: "The problem that I have with this rule is that every desk assumes when it plans for deployments that it can only do one branch's deployment per night. … I'm okay with one deployment per night. Otherwise, I have a problem with this." → the desk's proposed rewrite, approved verbatim: "L43 One deploy window per evening — carrying every branch that is ready. ONE production deploy EVENT per evening; that one deploy carries EVERY branch built and checked (L67) that day, combined and gated as one stacked set (L68). The count limits deploy events, never branches: no desk or hub plans one branch per night, staggers or defers building to fit the deploy count, or holds a ready branch for a later evening. A branch waits only when it is not built, not checked, or turns the combined gate red — then it is dropped from the set, named, and the rest lands." The 09-15 and 2026-09-21 amendment paragraphs, and the L73 override-path note, are unchanged and not superseded.

## H-L53-cap — L53's unnarrowed config-cap sentence, superseded 2026-09-22
Source: LAWS.md L53, as it stood 09-10/09-12/13 → 2026-09-22.
Verbatim: "Committed config carries engine tunables only — never a cap, rank rule, metric choice or stickiness (those live in the vault pool block)."
Replaced by: `cto-2026-09-22.md` R82 (C4, laws-audit-2026-09-20.md §2 C4): "Committed config carries engine tunables only — never the POOL CAP (the radar pool's name count), rank rule, metric choice or stickiness (those live in the vault pool block). The request ceiling and the scan cadence may sit in committed config only as ruled values that name their ruling in the file (`source: ruling`)." Narrowing evidence: `configs/cobalt/taxonomy/tunables.yaml` carries `radar.finviz_max_rpm` and `radar.scan_interval` as tracked, ruled values (`source: ruling`) — the unnarrowed sentence read as forbidding this in-force practice.

## H-L54-rebase — L54's unscoped "rebase-then-ff on every merge", superseded 2026-09-22
Source: LAWS.md L54 [amended 09-09], as it stood 09-09 → 2026-09-22.
Verbatim: "[amended 09-09] Rebase-then-ff on every merge. Rollback of a merged range is `git revert` of the merge range, never a `reset --hard` to a tag once later work has landed above it."
Replaced by: `cto-2026-09-22.md` R82 (C12, laws-audit-2026-09-20.md §2 C12): "[amended 09-09; scoped 2026-09-22, R82 C12] Rebase-then-ff on every single-branch merge. A gate branch that combines sibling branches (L68) is the one exception: `main` is merged INTO it and it is fast-forwarded, and its rollback is ONE `git revert -m 2` of that merge. Rollback of any other merged range is `git revert` of the merge range, never a `reset --hard` to a tag once later work has landed above it. Every deploy report names which rollback shape its range uses." The gate-branch exception itself was already practiced (L68's own text, `deploy-2026-09-19c`) before this ruling named it as L54's exception in L54's own text.

## H-L55-note — L55's 2026-09-19 status note, retired 2026-09-22
Source: LAWS.md L55, status note as it stood 2026-09-19 → 2026-09-22.
Verbatim: "Status note (not law text): no `git push` ask/deny rule exists in the tracked or user settings files (found 2026-09-19) — the gate today is this law + the auto-mode classifier; whether an ask rule is wanted back is an ops item."
Retired by: `cto-2026-09-22.md` R82 (D7, `topics/cto-desk.md` 2026-09-20 R12): the fact is superseded — since 2026-09-20 R12, `~/cobalt/.claude/settings.local.json` carries the push allow rule (with force/delete/mirror/all/tags shapes denied), so the note's premise ("no rule exists") is no longer true. Replaced by the D7 law text: "[amended 2026-09-22, R82 D7] The desk's push allow rule lives only in `~/cobalt/.claude/settings.local.json` (2026-09-20 R12), with the force / delete / mirror / all / tags shapes denied there. A hub whose working directory is `~/cobalt` inherits that allow, so every hub launch line carries `--disallowedTools "Bash(git push*)"`."

## H-L7-note — L7's status note, promoted into law text 2026-09-22
Source: LAWS.md L7, "Status note" paragraph as it stood 09-16 → 2026-09-22.
Verbatim: "Status note (not law text): no HITL token mechanism exists today — `--hitl` is an unverified free-text label (LEDGER:1288). The law stands; a worker never treats `--hitl <label>` as satisfying it; the enforcement arm is owed (either build token issuance or rename the flag). [amended 2026-09-16, L61] Interim until real tokens and a Cobalt approve path exist: Dejan's spoken or typed "approve" in the desk chat, for the exact action the desk named (file, sha256), IS the HITL approval; the desk logs it with the time in `reports/cto-<date>.md` §4; the hub executes on the desk's relay (first use: 2026-09-16 07:07 ET, `cto-2026-09-16.md` §4 row 3a)."
Replaced by: `cto-2026-09-22.md` R82 (C13, laws-audit-2026-09-20.md §5 agenda item 6): the interim-approval clause is promoted from a "Status note (not law text)" into L7's own law text, and the `--sha256` mechanical-half sentence and "never satisfies this law on its own" sentence are added. No substance is dropped: "no HITL token mechanism exists" is carried as "No HITL token mechanism exists yet"; "the enforcement arm is owed" is not repeated verbatim but is superseded by the same clause's "the day real tokens ship, this clause is amended, not silently bypassed."
