# SESSION-CLOSE — the standing close routine (ruled 2026-09-15, Dejan)

A session that closes without this routine is not closed. The close hub runs it
from `~/cobalt` on `main`; every step leaves evidence in the file it names (L48).
Memory rules are the memory folder's own (`6 - Permanent/Memory/INDEX.md`
frontmatter `rules:`): one subject per file, every line tagged
`[stated YYYY-MM-DD · origin]`, supersede by `~~marking~~` plus
`(superseded YYYY-MM-DD)` — never delete, INDEX + profile + preferences under
4,000 characters, `_imports/` frozen.

| # | Step | Where | Evidence |
|---|---|---|---|
| 1 | **Ledger appendix** — one dated line per ruling, decision and state change of the session; no prose narration. | `docs/00 - Project/PROJECT-LEDGER.md`, `### YYYY-MM-DD — …` appendix | the appendix block |
| 2 | **LAWS fold or proposals** — separate law from record. Unambiguous amendment: rewrite the entry in place, move replaced wording verbatim to `LAWS-HISTORY.md`. New law: only with its authorized number. Anything contested or unnumbered: list under "Laws fold — PROPOSED, NOT APPLIED" in the close report and stop. Never touch L29's routing substance (routing tribunal). | `6 - Permanent/Memory/LAWS.md`, `LAWS-HISTORY.md`; proposals in `docs/40 - DevDocs/reports/close-<date>.md` | diff of LAWS.md, or the proposals list |
| 2a | **Lessons gate** (ruled 2026-09-25, Dejan — `cto-2026-09-25.md` R27, the desk's card cut) — read the `updated:` date of `topics/cto-desk-contract.md`; every `LESSONS OF …` line, and every other `[stated … · Code]` practice line, of `topics/cto-desk.md` stated on or after that date must map to a `## Checklist` rule of `cto-desk-contract.md` that cites its line (`:N`, and `:N(n)` for each numbered item). List every unmapped line or item under `Checklist — OWED` in the close report, each with the rule it proposes: group, id, ONE imperative line, citation. Read only — the hub PROPOSES, the desk APPLIES under L58 (the laws fold's shape): the desk adds the rules and bumps `updated:`. Nothing unmapped = write `Checklist — OWED: none`. | `6 - Permanent/Memory/topics/cto-desk.md`, `topics/cto-desk-contract.md` (read); proposals in `docs/40 - DevDocs/reports/close-<date>.md` | the `Checklist — OWED` list, or `none` |
| 3 | **Rewrite `## NOW`** in full (never append) — ≤ 1,500 characters at the top of `6 - Permanent/Memory/areas/cobalt.md`: main commit, what is LIVE, what is RED, sprint state, approved designs, pending rulings, ops queue. Every line `[stated <date> · Code]`. State it from live evidence (`git log -1`, heartbeat, job rows), never from the previous NOW. | `areas/cobalt.md` | `awk '/^## NOW/{f=1} /^## Canonical/{f=0} f' areas/cobalt.md \| wc -c` |
| 4 | **Append areas/topics** — the day's rulings and facts, tagged, to the file whose subject they belong to: build/deploy record → `areas/cobalt-sprints.md`; seats, launchers, tribunals → `areas/cobalt-houses.md`; product-definition rulings → `areas/cobalt-product-definition.md`; machines, CLIs, shell facts → `topics/devices.md`; behavior rules → `preferences.md` (terse) with reasons in `topics/working-contract.md`. Superseded lines are marked, not deleted. Bump `updated:` and the INDEX line of every file touched. | `6 - Permanent/Memory/` | the lines appended |
| 4a | **Ladder + backlog status** (ruled 2026-09-19, Dejan — the plan file is never orphaned again) — in `SPRINT-LADDER-v0_1.md`, under the CURRENT sprint's heading, rewrite ONE block `### Status <date>`: per feature / owed prompt `DONE-LIVE · DONE-DARK · BUILT-NOT-MERGED · NOT STARTED` with its evidence (tag, commit, report), the sprint's stop date, `ON TIME / AT RISK / LATE` with the reason, and every sizeable OFF-LADDER item of the day with the ruling that ordered it. Bring `BACKLOG.md`'s rows for the same items in line. Status only — scope, dates and order of the ladder change only by his ruling. | `docs/00 - Project/SPRINT-LADDER-v0_1.md`, `docs/00 - Project/BACKLOG.md` | the status block |
| 5 | **Measure the always-loaded block** — `cd "/Users/cobalt/Vault/Think/6 - Permanent/Memory" && wc -c INDEX.md profile.md preferences.md`; the total must stay under 4,000. Over = the close FAILS: trim preferences, move the cut wording to `topics/working-contract.md`, re-measure. Print before and after in the close report. | memory folder | the two `wc -c` totals |
| 6 | **Commit** — one commit on `main` for the session's docs (ledger, close report, prompts, DevDocs); machine-written files that dirty the tree are committed as-is (L51). `COBALT_ENV=production uv run cobalt validate` exit 0 before the commit. The vault is not git — steps 2–5 leave no commit. | `~/cobalt` | `git log -1` in the close report |
| 7 | **Dejan pushes** — `git push` is his (L55). The close report ends `CLOSE COMMITTED <hash> · PUSH: Dejan · ESCALATE: <n>`; the next opener is delivered in the same message. | chat | the last line of the report |

Wake-up path the close feeds, for every house: `CLAUDE.md` / `AGENTS.md` /
`QWEN.md` → memory `INDEX.md` → `areas/cobalt.md` `## NOW` → `LAWS.md`.

Refuse and report rather than guess when a required source is absent or
unreadable, a citation cannot be verified, a classification or number is
contested, or the block would exceed the cap (LAWS.md, "Fold-at-session-close").

## DIFF
ONE row added, between step 2 and step 3, numbered `2a` in the routine's own shape (the `4a` precedent); every other byte is the live file's (proof: `diff` of the live file against this file minus this section prints one added line).

- BEFORE: (no row between `| 2 | **LAWS fold or proposals** …` and `| 3 | **Rewrite `## NOW`** …`)
- AFTER: `| 2a | **Lessons gate** (ruled 2026-09-25, Dejan — …) — read the updated: date of topics/cto-desk-contract.md; every LESSONS OF … line, and every other [stated … · Code] practice line, of topics/cto-desk.md stated on or after that date must map to a ## Checklist rule … that cites its line …; list every unmapped line or item under Checklist — OWED … with the rule it proposes …; the hub PROPOSES, the desk APPLIES under L58 …; nothing unmapped = Checklist — OWED: none. | … | the Checklist — OWED list, or none |` (full text in the table above).
- Drafter's reading beyond the card's words: "stated ON OR AFTER `updated:`" instead of "after" — a lesson appended on the same day as the cut (the contract's `updated:` is that day) would otherwise never be gated; a line already cited by a rule passes, so same-day lines cost nothing twice.

Apply: the desk replaces `docs/40 - DevDocs/SESSION-CLOSE.md` with everything ABOVE `## DIFF` (the live file has no `## DIFF` section). The file sits outside `prompts/`, so the next `99-close.md` the desk writes names step 2a in its card.
