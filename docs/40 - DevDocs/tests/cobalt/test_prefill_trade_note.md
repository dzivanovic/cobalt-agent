# `tests/cobalt/test_prefill_trade_note.py`

Trade-note cases declare `requires_db` because the single vault-write path persists its audit before touching the `tmp_path` vault.

