# draft-cos-cutover-tooling-amend · 2026-10-20

## §0 Headline
Card 931 amended in place for preflight round 1: fail 2 and notes 4, 5, 7 fixed; notes 3, 6, 8 and `RULINGS` untouched.
T1c now has (f)-(h) (`:53` (e), `:155` (f), `:160`), proven on `main`; the exception list, the test and DEPLOY PROOF (`after 8`) follow.
Nothing run, nothing committed.

## DECISIONS
None.

## RECORDS
- 2026-10-20 17:55 EDT from `date`.
- Read: prompt 942; card 931; `reports/cos-cutover-tooling-preflight-2026-10-20.md`; `Vault/Think/6 - Permanent/Memory/topics/writing-rules.md`.
- `git -C /Users/cobalt/cobalt grep -n … main -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (the file is under `docs/40 - DevDocs/prompts/`, not `prompts/`): `:53` (e) holds `cobalt.sh status` → ONLINE and "(e) false … run STEP-5 (3) NOW"; `:155` (f) holds `RESTARTS:` minus deferred and not-loaded `= STEP-R's <restart set>`; `:160` holds `agent OFFLINE at tail 3` in the RED list. All three trace.
- Line starts: `- THE ONE RESUME` (`:53`), ``- (f) `COBALT_ENV=production uv run cobalt validate` `` (`:155`; `- (f) ` alone also starts `:108`, so the full start is used), `RED = a resident` (`:160`).
- Edits (card 931 only): T1c row (f)-(h), test starts, line-count wording, `eight times`, files cell; T1b(ii) neither-state fail; NOT IN THIS JOB list; DEPLOY PROOF `after 8` plus a one-line marker-count note (no `· before` / `· after`, so it is not read as a marker).

DRAFTED · decisions: 0
