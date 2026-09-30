"""DRC K2 fix r2 — WITH-DB red of F-1r2 (L75; the fix prompt
`prompts/2026-09-25/12-drc-k2-fix-r2-build.md` F2).

THE INPUT (`03`'s `## Checked against the branch` rows 1–2,
`drc-k2-fix-r1-check-2026-09-25.md:161` / `:162`): a `resolve` restated
(`--supersedes`) to an EARLIER day that has no import and no `day` row on
or before it, while the superseded resolve's day IS recorded and its
stored rows carry that resolve's effect. The CLI's rebuild trigger reads
the SUPERSEDED row's day (AMENDED C7 (r2)); the rebuild of the earlier,
unrecorded day is refused loud (`nothing to re-pair ([F-05])`), exit 1,
the statement kept (L7), nothing in `drc_rows` written — never the exit-0
`stated; … has no import yet` (L1; v3 `[F-06]` `:190`).

Everything runs inside `test_drc_store.py`'s never-committed migration
transaction on `cobalt_dev` (L76). Constructed symbols and dates only
(L32 / L45).
"""

from __future__ import annotations

from datetime import date

from cobalt.drc.store import DrcStore

from test_drc_k1_store import (  # noqa: F401 — fixtures are used by name
    D3,
    _cli,
    _printed_hash,
    _row,
    _stated_count,
    _state,
    at_ten,
)
from test_drc_k2_experiments import _snapshot, _stated_rows
from test_drc_k2_fix_r1_store import _resolve_applied_on_d_next, _rows_of
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    migrated,
    requires_db,
    weekday_calendar,
)

#: A constructed weekday before `D` under `weekday_calendar`; nothing is
#: recorded on or before it.
D0 = date(2001, 1, 1)


@requires_db
def test_a_resolve_restated_to_an_earlier_unrecorded_day_is_never_a_silent_exit(
    migrated, capsys, at_ten, weekday_calendar
):
    """F-1r2, THE INPUT (`drc-k2-fix-r1-check-2026-09-25.md:161` HOLD 1,
    `:162` HOLD 2; AMENDED C7 (r2); v3 `[F-06]` `:190`; L1): the dry run
    names the rebuild of the earlier day; `--apply` keeps the statement
    (L7), refuses the rebuild loud (`not rebuilt: … nothing to re-pair
    ([F-05])`), exits 1 and writes nothing in `drc_rows` — the later days'
    stored rows still name the superseded resolve, re-paired when
    2001-01-01's input is recorded (AMENDED C7 (b))."""
    trade, first = _resolve_applied_on_d_next()
    # The premise: the superseded resolve's effect removed the trade from
    # the carried book, so no later seed fails on it.
    assert trade not in _row(migrated, D_NEXT, "book_close")[1]["trade_ids"]
    assert trade not in _row(migrated, D3, "book_close")[1]["trade_ids"]
    assert any(i.get("resolve_id") == first.id for _, _, i, _ in _rows_of(migrated, D_NEXT))

    before_next = _snapshot(migrated, D_NEXT)
    before_3 = _snapshot(migrated, D3)
    books = _stated_count(migrated)
    stated = _stated_rows(migrated)
    assert DrcStore().effect_day(D0, first.id) == D0
    argv = ("--resolve", "2001-01-01", trade, "--supersedes", str(first.id))

    code, out = _cli(capsys, *argv)
    assert code == 0, out
    assert "on --apply: rebuild 2001-01-01 and every later recorded day" in out

    code, out = _cli(capsys, *argv, "--apply", "--sha256", _printed_hash(out))
    assert code == 1, out
    (refused,) = [l for l in out.splitlines() if l.startswith("not rebuilt: ")]
    assert "2001-01-01" in refused
    assert "nothing to re-pair ([F-05])" in out
    assert not any(l.startswith("stated;") for l in out.splitlines())
    assert _stated_count(migrated) == books + 1
    assert _stated_rows(migrated)[: len(stated)] == stated
    assert _snapshot(migrated, D_NEXT) == before_next
    assert _snapshot(migrated, D3) == before_3


@requires_db
def test_a_resolve_restated_to_an_earlier_unrecorded_day_before_any_record_still_says_stated(
    migrated, capsys, at_ten, weekday_calendar
):
    """F-1r2, AMENDED C7 (r2)'s OTHERWISE clause (`drc-k2-fix-r1-check-
    2026-09-25.md:161` / `:162`): with nothing recorded, the superseded
    row's day joins no chain — the restatement to 2001-01-01 is written,
    prints `stated; 2001-01-01 has no import yet` (the effect day) and
    exits 0; no `drc_rows` row exists. A GREEN-as-pin on the base."""
    first = _state(D_NEXT, kind="resolve", positions=[{"trade_id": "DDD-long-2001-01-02T10:00:00-05:00"}])
    books = _stated_count(migrated)
    argv = ("--resolve", "2001-01-01", "DDD-long-2001-01-02T10:00:00-05:00", "--supersedes", str(first.id))

    code, out = _cli(capsys, *argv)
    assert code == 0, out
    assert "on --apply" not in out

    code, out = _cli(capsys, *argv, "--apply", "--sha256", _printed_hash(out))
    assert code == 0, out
    assert "stated; 2001-01-01 has no import yet" in out
    assert _stated_count(migrated) == books + 1
    assert migrated.execute('SELECT count(*) FROM "user".drc_rows').fetchone()[0] == 0
