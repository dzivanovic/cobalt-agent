# Draft owed file — 2026-10-13

## §0 Headline
- Card 496: DF1's step C now writes `data/deploy/bootstrap-owed.json` as well as printing `BOOTSTRAP OWED:`. BO1 removes the entry once the label is loaded.
- OW1 is rewritten. K18 and `watchdog.sweep` both read the file and report a listed label as `OWED (deferred bootstrap)`; unlisted labels stay red. There is no `--deploy-report` flag. OW1 builds after DF1.
- 496's `RESTARTS` header says it is derived at the build, with the builder's report and the deploy card carrying it. 503: P6 text, the NOT IN THIS JOB line and the FOR THE CHECK line only.
- 2 decisions below. Tests were not run.

## DECISIONS
1. ASK DESK: the brain's red test "entry removed and still unloaded → both red" cannot be red on BASE. BASE has no file, so a label with no entry is already red, and the test is green on BASE. Default: card 496 test (w) is written as a PIN, green before and after, and says so. [12:05]
2. ASK DESK: the header wording. Neither card had a derived-value style for a header, and every other `RESTARTS:` header in `prompts/2026-10-12` and `2026-10-13` is a literal set or `none`. The only existing style is "derived" in RECORDS and in 503's X2. Default: `RESTARTS: derived at the build by `cobalt jobs restarts BASE..HEAD`; the builder writes the derived line into its report and the deploy card carries it`, with no angle token. No `ops/desk` script greps `RESTARTS:` (`grep` empty). [12:05]

## RECORDS
- Files edited: `prompts/2026-10-13/496-plist-step-c-card.md` (header `RESTARTS`; DF1 and its test (o); BO1 and its test (t); OW1 rewritten with tests u–z; READ; a FOR THE CHECK line; RECORDS) and `prompts/2026-10-13/503-f23-card.md` (P6 text, NOT IN THIS JOB line, a FOR THE CHECK line). Nothing committed.
- Anchors read on the working tree, `git -C /Users/cobalt/cobalt status --short` over `src/cobalt/jobs src/cobalt/smoke tests/cobalt/test_jobs.py tests/cobalt/test_smoke.py configs/cobalt/smoke .gitignore data` empty, so they equal HEAD: `watchdog.py:385-398` (the `not status.loaded` branch, `:397` the `Finding`); `test_jobs.py:885`; `checks.py:415-435`; `.gitignore:6` is `data/`. `data/backups` exists on disk and `data/deploy` does not; DF1's script creates it. `git show HEAD:<file>` was blocked by the bare-command hook (it refuses a pipe); the clean status stands in for it.
- RESTARTS class homes named in 496's RECORDS, read from `src/cobalt/jobs/restarts.py:198-264`, not run: `src/cobalt/smoke/checks.py` → static import reach (`:216-220`) via `cli.py:76` and radar `imports: [cobalt.cli]`; `src/cobalt/jobs/watchdog.py` → static import reach, its reach to a resident not read (no `watchdog` in `src/cobalt/cli.py`); `s2.yaml` → `:251-255`; `tests/` → `:245-246`; `ops/desk/deploy-step-c.sh` → `:230`; `data/deploy/bootstrap-owed.json` → gitignored, never in a diff. 496 no longer changes `smoke/cli.py` or `models.py`.
- BASE, TIP and the other header lines are untouched. No placeholder token added.

DRAFTED · decisions: 2
