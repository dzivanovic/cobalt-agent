# draft-f5-x2-probe — 2026-10-20

## §0 Headline
- Probe prompt `prompts/2026-10-20/914-f5-x2-probe.md` drafted: Sonnet 5.5, CLASS K2, LADDER `S5-P2 · F5`, one dry run run once, report `reports/f5-x2-probe-2026-10-20.md`.
- Its allow line: `Read`, `Write`, `Bash(date*)`, `Bash(COBALT_ENV=production uv run cobalt checkpoint run --slot 0745 --dry-run)`.
- THE LAUNCHER CANNOT LAUNCH IT TODAY. `desk-launch.sh` kind `prompt` (W6) refuses the string, and `bare-guard.py` G2 would deny it in the seat (kind `brain`). DECISION 1 gives the cheapest route: one K5 card.
- PASS = one `Sectors:` line with 11 `<name> <signed>%` entries and no `degraded: finviz-groups` or `degraded: finviz — demand ceiling` line.
- Cost: one gate check, two Finviz GETs (`:242`), one model call (`:779`) when today's note exists. Run once, never retried.

## DECISIONS
1. ASK DESK: how does the one production string reach the probe seat? [12:20 EDT] Default: one K5 card (`CLASS: K5`, L81), no word of his. The card admits exactly `Bash(COBALT_ENV=production uv run cobalt checkpoint run --slot 0745 --dry-run)` for the one prompt file `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/914-f5-x2-probe.md`, at two gates. It has two rows:
   - L1 `ops/desk/desk-launch.sh` kind `prompt`, the W6 judge (`:815`): pass that string byte for byte only when the prompt is that file. Exempt that string from the `uv run` / `COBALT_ENV=` write-string scan (`:836`).
   - G1 `ops/desk/bare-guard.py` G2 (`:1106`): pass that command byte for byte only when the first message's `Read '<…>'` names that file. Model the pass on `prod_read` (`:990-997`). Every other seat and every other string keeps the deny (L81 KEPT).
   - Tests: the string passes for that file; it is refused for any other prompt and for one changed byte. Deploy by the K5 route.
   - Rejected, the deploy hub's `## LAUNCHD` dry run (`desk-launch.sh:1902`, CARD.md `:69`): it builds the string only from an `add|change` line, and that line bootstraps the plist. The 0745 plist is `deferred` (`909-deploy-f5-checkpoints-fr2-card.md:27`), and X2 is owed before load.
   - Rejected, the prodwrite seat: it is K3, it needs a WRITE RULING of his, and it is for a write.
   - Rejected, a `RULINGS:` line: W6 refuses the string whatever `RULINGS` says.
   - Rejected, a relayed permission (L81 (4)) and a new command (R411, R412).

## RECORDS
- `date` → 2026-10-20 12:17 EDT (start), 12:20 EDT (prompt written). Reads only. No network, no production command, no git write, nothing committed. The probe prompt is uncommitted; the desk commits it after the K5 card.
- Read: prompt 913; card 912 whole; `reports/draft-f5-x2-2026-10-20.md` whole; `prompts/2026-10-19/877-cos-probe-card.md` whole; `prompts/2026-10-19/873-cos-gate-run.md` and `prompts/2026-10-20/901-clean-stale-sessions.md` (launch-line shape); `prompts/CARD.md` (grep: `:69` LAUNCHD, `:156-161` prodwrite); `topics/writing-rules.md` whole.
- LAWS.md: L53 (`:293`), L62 (`:322`), L81 (`:406`, KEPT: `COBALT_ENV=production*` deny and G2 stay on every other seat); L36, L74, L79 headings.
- `git show HEAD:ops/desk/desk-launch.sh`:
  - `:130-148` and `:785-841`: kind `prompt` refuses `uv run` and `COBALT_ENV=` unless RULINGS cites HIS RULING + APPROVED rows. W6 refuses every `COBALT_ENV=production` string except exactly `Bash(COBALT_ENV=production uv run cobalt db query *)` (`:815-816`).
  - `:1902-1919`: the LAUNCHD dry run is skipped for `deferred` (`[ "$lmode" != deferred ] || return 0`).
- `git show HEAD:ops/desk/bare-guard.py`:
  - `:788-822` `seat()`: a prompt under `prompts/20*/` with cwd in the repo → kind `brain`.
  - `:1106-1107`: G2 denies production for any kind but `deploy`, except `prod_read` (`:990-997`, `db query` only).
- `~/.claude/settings.json`: the PreToolUse hook runs `bare-guard.py` (`:22`). `git show HEAD:.claude/settings.json`: no `COBALT_ENV=production*` deny string; the deny is W6 plus G2.
- `git show HEAD:src/cobalt/prefill/checkpoints.py`:
  - `:95` `GETS_PER_SLOT = 2`; `:100` `GROUPS = "finviz-groups"`; `:102` `DEMAND_CEILING`; `:104` `GROUPS_URL`; `:111` column names.
  - `:190-221` `_decimal` / `parse_groups`; `:224-235` `fetch_groups` (token `:227`, `return parse_groups(response.text)` `:235`); `:238-256` `fetch_figures` (two GETs `:242`).
  - `:451-490` `render_body`: the `Sectors: ` line, or `degraded: finviz-groups — <reason>`.
  - `:576-584` `check_demand`; `:697-704` gate then fetch; `:747-751` the dry run stops when the note is absent (no figures, no model call); `:779` `narrate`, one model call.
  - `:824` `as_job(..., skip=args.dry_run)`; `:825` `default_stores()`; `:830-832` the report printed.
- `git show HEAD:src/cobalt/vaultwrite/store.py:78-87`: `ensure_schema` runs the vault_writes forward migrations on every run, the dry run included. Its statements are `IF NOT EXISTS` / `SET NOT NULL` / `COMMENT ON` (`git grep` of `vaultwrite/migrations/`). That is the same no-op every vault-writing job runs; the prompt states it.
- `writer.py:272-293`: `WriteResult.report()` prints the unified diff. The diff's context lines are his note, so the prompt quotes only named `+` lines (L32).
- `909-deploy-f5-checkpoints-fr2-card.md:26-29` (git grep): the four checkpoint plists `deferred`, gate X2 among the items.
- Model: Sonnet 5.5. One command, a copy and a count; no judgment calls that need Opus.
- Not traced: whether today's daily note exists (`daymode/note.py:250`). If it does not, the probe FAILs with the `dry run: the note does not exist yet` line, and the prompt says so.

DRAFTED · decisions: 1
