# `src/cobalt/db_query.py`

Implements `cobalt db query`: a quote/comment-aware SELECT-only guard plus a server-side read-only transaction, timeout, role assertion, row limit, and unconditional rollback. All connections use `cobalt.db.connect`.

