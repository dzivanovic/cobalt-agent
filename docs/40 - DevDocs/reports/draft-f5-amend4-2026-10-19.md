## §0 Headline
- Card 731 amended in place: K4 and K9 `files` cells gain the two test files; row text names each pin line.
- NOT IN THIS JOB F4-owned line reads "except these two pin lines (K4, K9)".
- Pins proven by content at HEAD: `test_modelaccess_config.py:51`, `test_prefill_refresh.py:391`.
- One decision: route order in K4.

## DECISIONS
- ASK DESK: K4 gave no placement for `checkpoint.narrative` in `modelaccess.yaml`; `load_routes` keeps file order (`yaml.safe_load` dict → `ModelAccessConfig.routes`, `src/cobalt/modelaccess/config.py:106-131`), so the pin order follows placement. Default taken: route added after `local.plan`, pin = `["local.plan", "checkpoint.narrative"]`; if the desk wants it before, flip both. [06:59 EDT]

## RECORDS
- Card edited: `docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md` (K4 row, K4 files, K9 row, K9 files, NOT IN THIS JOB). BASE, TIP, CHECK REPORT untouched. [06:59 EDT]
- K9 pin context: `entry.readers == ["com.cobalt.prefill-daily", self.LABEL]` at `tests/cobalt/test_prefill_refresh.py:391`, `LABEL = "com.cobalt.prefill-refresh"` at line 351. [06:59 EDT]
- Not run: tests, git writes. Nothing committed.

DRAFTED · decisions: 1
