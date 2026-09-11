# `tests/cobalt/test_radar_runner.py`

Proves idle/reset cycles touch no collector or store, verifies stage order and mirror-failure continuation, and implements O4's six-case market-reset crossing matrix. Transactional fakes call `before_commit` after staging and retain changes only after the gate succeeds, allowing the matrix to check rollback, pre-boundary ticker durability, commit timestamps, scan-id idempotency, and the required next-active-cycle `failed_stage` stamp.
