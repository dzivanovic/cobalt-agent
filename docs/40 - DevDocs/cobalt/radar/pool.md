# `src/cobalt/radar/pool.py`

Pure D3 ranking and membership decision logic. It keeps metric positions separate, applies source priority and first-screen precedence, enforces a hard cap with degraded holds, preserves sticky streaks, manages never-admitted episodes, and closes prior-day episodes at aftermarket close.

The decision boundary accepts validated `PoolOverride` instances and JSON-shaped
override mappings. This matters for replay/test variants built with Pydantic's
non-validating `model_copy(update=...)`; note parsing itself remains strict.
