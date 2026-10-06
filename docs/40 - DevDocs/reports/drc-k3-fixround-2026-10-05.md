# drc-k3 — K3-F1 fix round 2026-10-05

## What this is
- A pointer record for the K3-F1 fix round of `drc-k3`, built on branch `drc/k3-surfaces-1004`.
- The full build report is `docs/40 - DevDocs/reports/drc-k3-build-2026-10-04.md` on that branch (head `44e8de82`), section `## K3-F1`.
- Why: the first deploy attempt failed at the gate on the two K3-6 tests (`deploy-deploy-k3-1005.md`).

## The fix
- Commit `0ebdf95e`: `tests/cobalt/test_drc_k3.py` only. The two K3-6 rebuild tests carry `requires_db`; the `statements` fixture takes the module `cobalt.drc.build` via `importlib.import_module`, so its spy lands on the build module `imports` calls.
- Gate on `0ebdf95e`, whole `--deploy` (branch report `## K3-F1`): offline 3869/0 · with-DB 4730/0 · live-note 146/0.
- Branch head `44e8de82` adds the build report only.

BUILT · job: drc-k3 · tip: 0ebdf95e | on 979ec797 | migration: none | offline 3869/0 | with-DB 4730/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 11 of 11 | self-check: 2 of 3 | decisions: 9 · for Dejan: 0 · tokens: 167460
