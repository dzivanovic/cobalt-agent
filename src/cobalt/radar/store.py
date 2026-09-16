"""System-side radar membership and pool-row transactions."""

from __future__ import annotations

import json
from collections.abc import Callable
from datetime import date, datetime
from zoneinfo import ZoneInfo

from cobalt import db, env
from cobalt.db import Side
from cobalt.session import assert_writable

from .pool import Action, Transition

ET = ZoneInfo("America/New_York")


class RadarStore:
    SIDE = Side.SYSTEM

    def __init__(self, db_name: str | None = None, *, connect=None):
        self.db_name = db_name or (None if connect else env.resolve_db_name())
        self._factory = connect

    def _connect(self):
        return self._factory() if self._factory else db.connect(self.db_name, side=self.SIDE)

    def open_members(self, pool_key: str) -> list[dict]:
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT ticker, sources, entered_at, below_cap_streak, last_rank, trade_date "
                "FROM radar_membership WHERE pool_key = %s AND left_at IS NULL",
                (pool_key,),
            )
            columns = [item.name for item in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def pool_row(self, pool_key: str) -> dict | None:
        with self._connect() as conn:
            cursor = conn.execute("SELECT * FROM radar_pool WHERE pool_key = %s", (pool_key,))
            row = cursor.fetchone()
            return dict(zip([item.name for item in cursor.description], row)) if row else None

    def members_for_day(self, pool_key: str, trade_date: date) -> list[dict]:
        """Return every membership episode for one pool and trading day.

        This intentionally includes open, departed, and never-admitted
        episodes.  Admission is represented by ``entered_at IS NOT NULL``;
        callers must not mistake every open row for a pool member.
        """
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT id, pool_key, ticker, trade_date, first_seen_at, "
                "entered_at, left_at, source, sources, rank_at_entry, last_rank, "
                "below_cap_streak, excluded_by, session, opened_scan_id, "
                "last_scan_id, closed_scan_id FROM radar_membership "
                "WHERE pool_key = %s AND trade_date = %s ORDER BY id",
                (pool_key, trade_date),
            )
            columns = [item.name for item in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def apply_membership(
        self,
        *,
        pool_key: str,
        transitions: list[Transition],
        scan_id: int,
        now: datetime,
        session: str,
        before_commit: Callable[[], None] | None = None,
    ) -> None:
        assert_writable("radar.membership", target=pool_key, now=now)
        conn = self._connect()
        conn.autocommit = False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO radar_pool (pool_key,state,session,members) "
                    "VALUES (%s,'scanning',%s,0) ON CONFLICT (pool_key) DO NOTHING",
                    (pool_key, session),
                )
                for item in transitions:
                    if item.action in {Action.RETAIN, Action.HOLD}:
                        cur.execute(
                            "UPDATE radar_membership SET sources=%s::jsonb, last_rank=%s, "
                            "below_cap_streak=%s, last_scan_id=%s "
                            "WHERE pool_key=%s AND ticker=%s AND left_at IS NULL "
                            "AND last_scan_id < %s",
                            (json.dumps(item.sources), item.rank, item.below_cap_streak, scan_id, pool_key, item.ticker, scan_id),
                        )
                    elif item.action is Action.LEAVE:
                        cur.execute(
                            "UPDATE radar_membership SET left_at=%s, closed_scan_id=%s, "
                            "last_scan_id=%s, below_cap_streak=%s, "
                            "excluded_by=COALESCE(%s,excluded_by) "
                            "WHERE pool_key=%s AND ticker=%s AND left_at IS NULL "
                            "AND last_scan_id < %s",
                            (item.left_at or now, scan_id, scan_id, item.below_cap_streak, item.excluded_by.value if item.excluded_by else None, pool_key, item.ticker, scan_id),
                        )
                    else:
                        entered = now if item.action is Action.ADMIT else None
                        if item.action is Action.ADMIT:
                            # Promotion is a new admitted episode.  Close a
                            # prior never-admitted episode first so the partial
                            # unique index still enforces one open episode.
                            cur.execute(
                                "UPDATE radar_membership SET left_at=%s, closed_scan_id=%s, "
                                "last_scan_id=%s WHERE pool_key=%s AND ticker=%s "
                                "AND left_at IS NULL AND entered_at IS NULL AND last_scan_id < %s",
                                (now, scan_id, scan_id, pool_key, item.ticker, scan_id),
                            )
                        if item.action is Action.EXCLUDE:
                            cur.execute(
                                "UPDATE radar_membership SET sources=%s::jsonb, last_rank=%s, "
                                "excluded_by=%s, last_scan_id=%s WHERE pool_key=%s AND ticker=%s "
                                "AND left_at IS NULL AND entered_at IS NULL AND last_scan_id < %s",
                                (json.dumps(item.sources), item.rank,
                                 item.excluded_by.value if item.excluded_by else None,
                                 scan_id, pool_key, item.ticker, scan_id),
                            )
                            if cur.rowcount:
                                continue
                        cur.execute(
                            "INSERT INTO radar_membership "
                            "(pool_key,ticker,trade_date,first_seen_at,entered_at,source,sources,"
                            "rank_at_entry,last_rank,below_cap_streak,excluded_by,session,opened_scan_id,last_scan_id) "
                            "VALUES (%s,%s,%s,%s,%s,%s,%s::jsonb,%s,%s,%s,%s,%s,%s,%s) "
                            "ON CONFLICT (pool_key, opened_scan_id, ticker) DO NOTHING",
                            (
                                pool_key, item.ticker, now.astimezone(ET).date(), now, entered,
                                item.source or (item.sources[0] if item.sources else "unknown"),
                                json.dumps(item.sources), item.rank if entered else None, item.rank,
                                item.below_cap_streak,
                                item.excluded_by.value if item.excluded_by else None,
                                session, scan_id, scan_id,
                            ),
                        )
            if before_commit:
                before_commit()
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    def put_pool(
        self,
        row: dict,
        *,
        before_commit: Callable[[], None] | None = None,
        now: datetime,
    ) -> None:
        assert_writable("radar.pool_row", target=row["pool_key"], now=now)
        conn = self._connect()
        conn.autocommit = False
        try:
            conn.execute(
                "INSERT INTO radar_pool "
                "(pool_key,state,degraded,degraded_sources,failed_stage,failed_detail,sources,session,"
                "cap,members,last_scan_id,last_scan_at,last_scan_ms,last_poll_at,poll_failures,budget,updated_at) "
                "VALUES (%(pool_key)s,%(state)s,%(degraded)s,%(degraded_sources)s::jsonb,%(failed_stage)s,"
                "%(failed_detail)s,%(sources)s::jsonb,%(session)s,%(cap)s,%(members)s,%(last_scan_id)s,"
                "%(last_scan_at)s,%(last_scan_ms)s,%(last_poll_at)s,%(poll_failures)s::jsonb,%(budget)s::jsonb,%(updated_at)s) "
                "ON CONFLICT (pool_key) DO UPDATE SET state=EXCLUDED.state,degraded=EXCLUDED.degraded,"
                "degraded_sources=EXCLUDED.degraded_sources,failed_stage=EXCLUDED.failed_stage,"
                "failed_detail=EXCLUDED.failed_detail,sources=EXCLUDED.sources,session=EXCLUDED.session,"
                "cap=EXCLUDED.cap,members=EXCLUDED.members,last_scan_id=EXCLUDED.last_scan_id,"
                "last_scan_at=EXCLUDED.last_scan_at,last_scan_ms=EXCLUDED.last_scan_ms,"
                "last_poll_at=EXCLUDED.last_poll_at,poll_failures=EXCLUDED.poll_failures,budget=EXCLUDED.budget,"
                "updated_at=EXCLUDED.updated_at WHERE radar_pool.last_scan_id IS NULL "
                "OR radar_pool.last_scan_id < EXCLUDED.last_scan_id",
                {
                    **row,
                    "degraded_sources": json.dumps(row.get("degraded_sources", [])),
                    "sources": json.dumps(row.get("sources", [])),
                    "poll_failures": json.dumps(row.get("poll_failures", [])),
                    "budget": json.dumps(row.get("budget")) if row.get("budget") is not None else None,
                },
            )
            if before_commit:
                before_commit()
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    def stamp_failure(
        self,
        pool_key: str,
        *,
        failed_stage: str,
        failed_detail: str,
        now: datetime,
        poll_failures: list[dict] | None = None,
        before_commit: Callable[[], None] | None = None,
    ) -> None:
        assert_writable("radar.pool_row", target=pool_key, now=now)
        conn = self._connect()
        conn.autocommit = False
        try:
            conn.execute(
                "UPDATE radar_pool SET failed_stage=%s, failed_detail=%s, "
                "poll_failures=COALESCE(%s::jsonb,poll_failures), updated_at=%s "
                "WHERE pool_key=%s",
                (
                    failed_stage,
                    failed_detail,
                    json.dumps(poll_failures) if poll_failures is not None else None,
                    now,
                    pool_key,
                ),
            )
            if before_commit:
                before_commit()
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    def stamp_poll(
        self,
        pool_key: str,
        *,
        polled_at: datetime,
        poll_failures: list[dict],
        preserve_failure: bool = False,
        before_commit: Callable[[], None] | None = None,
    ) -> None:
        """Persist S4 freshness, clearing only a recovered bars failure.

        ``preserve_failure`` keeps a reset-crossing failure visible for the
        complete cycle in which the resident first succeeds in stamping it.
        """
        assert_writable("radar.bars", target=pool_key, now=polled_at)
        conn = self._connect()
        conn.autocommit = False
        try:
            detail = f"poll failures: {len(poll_failures)}" if poll_failures else None
            conn.execute(
                "UPDATE radar_pool SET last_poll_at=%s, poll_failures=%s::jsonb, "
                "failed_stage=CASE WHEN %s THEN failed_stage WHEN %s THEN 'bars' "
                "WHEN failed_stage='bars' THEN NULL ELSE failed_stage END, "
                "failed_detail=CASE WHEN %s THEN failed_detail WHEN %s THEN %s "
                "WHEN failed_stage='bars' THEN NULL ELSE failed_detail END, updated_at=%s "
                "WHERE pool_key=%s",
                (
                    polled_at, json.dumps(poll_failures), preserve_failure,
                    bool(poll_failures), preserve_failure, bool(poll_failures),
                    detail, polled_at, pool_key,
                ),
            )
            if before_commit:
                before_commit()
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()


    # -- S5 evaluate: the system-side seam (S2-P2 STEP-4) ----------------
    #
    # SYSTEM PAYLOAD ONLY (L32, Astra R1-1): the rows written here carry a
    # trade_def md5, generic atoms/observations validated by
    # `cobalt.radar.seam`, hashes, and nullable numeric copies of a card's
    # values — never a slug, def text, WHY prose or settings content. The
    # stored inputs live user-side in the receipt.

    def admitted_members(self, pool_key: str) -> list[dict]:
        """Open, ADMITTED membership episodes, by id (the S5 cohort)."""
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT id, ticker, trade_date, entered_at, left_at, last_rank FROM radar_membership "
                "WHERE pool_key = %s AND left_at IS NULL AND entered_at IS NOT NULL ORDER BY id",
                (pool_key,),
            )
            columns = [item.name for item in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def memberships(self, ids: list[int]) -> list[dict]:
        if not ids:
            return []
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT id, ticker, trade_date, entered_at, left_at, last_rank FROM radar_membership "
                "WHERE id = ANY(%s) ORDER BY id",
                (list(ids),),
            )
            columns = [item.name for item in cursor.description]
            rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        missing = sorted(set(ids) - {row["id"] for row in rows})
        if missing:
            raise RuntimeError(f"radar_membership rows {missing} referenced by open radar cards do not exist")
        return rows

    def i1_bars(self, ticker: str, start: datetime, end: datetime) -> list:
        """Stored i1 bars in [start, end), oldest first."""
        from cobalt.archiver.models import Bar, Interval

        with self._connect() as conn:
            rows = conn.execute(
                "SELECT ticker, interval, ts, open, high, low, close, volume FROM bars "
                "WHERE ticker = %s AND interval = 'i1' AND ts >= %s AND ts < %s ORDER BY ts",
                (ticker, start, end),
            ).fetchall()
        return [
            Bar(ticker=r[0], interval=Interval(r[1]), ts=r[2], open=r[3], high=r[4], low=r[5], close=r[6], volume=r[7])
            for r in rows
        ]

    def latest_run_id(self, pool_key: str) -> int | None:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT max(id) FROM radar_score_run WHERE pool_key = %s", (pool_key,)
            ).fetchone()
        return int(row[0]) if row and row[0] is not None else None

    def _tx(self, label: str, target: str, now: datetime, work, before_commit):
        assert_writable(label, target=target, now=now)
        conn = self._connect()
        conn.autocommit = False
        try:
            with conn.cursor() as cur:
                result = work(cur)
            if before_commit:
                before_commit()
            conn.commit()
            return result
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    def abandon_running_runs(self, pool_key: str, *, now: datetime, before_commit=None) -> list[int]:
        """A run still `running` at the start of a new one never published
        (a crash, or a market_reset drop): it is marked failed, named."""
        def work(cur):
            cur.execute(
                "UPDATE radar_score_run SET status = 'failed', finished_at = %s, "
                "failed_detail = 'abandoned: the run never published (crash or market_reset drop)' "
                "WHERE pool_key = %s AND status = 'running' RETURNING id",
                (now, pool_key),
            )
            return [int(r[0]) for r in cur.fetchall()]

        return self._tx("radar.evaluate", pool_key, now, work, before_commit)

    def open_score_run(self, row: dict, *, before_commit=None) -> int:
        def work(cur):
            cur.execute(
                "INSERT INTO radar_score_run (pool_key, scan_id, previous_run_id, session, started_at, status, "
                "cards_enabled, evaluator_version, formula_sha256, tunables_sha256, settings_sha256, cohort_sha256) "
                "VALUES (%(pool_key)s, %(scan_id)s, %(previous_run_id)s, %(session)s, %(started_at)s, 'running', "
                "%(cards_enabled)s, %(evaluator_version)s, %(formula_sha256)s, %(tunables_sha256)s, "
                "%(settings_sha256)s, %(cohort_sha256)s) RETURNING id",
                row,
            )
            return int(cur.fetchone()[0])

        return self._tx("radar.evaluate", row["pool_key"], row["started_at"], work, before_commit)

    def put_scores(self, run_id: int, rows: list[dict], *, before_commit=None) -> dict[tuple[int, str], int]:
        from .seam import DeskShadow, RadarScoreDetail

        # The closed seam models are the gate, re-applied at the write.
        for row in rows:
            RadarScoreDetail.model_validate(row["detail"])
            DeskShadow.model_validate(row["desk_shadow"])

        def work(cur):
            out: dict[tuple[int, str], int] = {}
            for row in rows:
                cur.execute(
                    "INSERT INTO radar_score (run_id, membership_id, ticker, trade_def_md5, direction, evaluation, "
                    "detail, desk_shadow, inputs_sha256) VALUES (%s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb, %s) "
                    "RETURNING id",
                    (run_id, row["membership_id"], row["ticker"], row["trade_def_md5"], row["direction"],
                     row["evaluation"], json.dumps(row["detail"]), json.dumps(row["desk_shadow"]),
                     row["inputs_sha256"]),
                )
                out[(row["membership_id"], row["trade_def_md5"])] = int(cur.fetchone()[0])
            return out

        from cobalt.session.clock import now_utc

        return self._tx("radar.evaluate", str(run_id), now_utc(), work, before_commit)

    def copy_card_values(self, copies: list[dict], *, before_commit=None) -> None:
        def work(cur):
            for copy in copies:
                cur.execute(
                    "UPDATE radar_score SET proximity = %s, conviction = %s, card_score = %s, "
                    "suppressed_reason = %s WHERE id = %s",
                    (copy["proximity"], copy["conviction"], copy["card_score"], copy["suppressed_reason"],
                     copy["score_id"]),
                )
                if cur.rowcount != 1:
                    raise RuntimeError(f"radar_score {copy['score_id']} not found for the card value copy")

        from cobalt.session.clock import now_utc

        self._tx("radar.evaluate", "radar_score", now_utc(), work, before_commit)

    def finish_run(self, run_id: int, *, status: str, finished_at: datetime, detail: str | None,
                   before_commit=None) -> None:
        if status not in {"complete", "failed"}:
            raise ValueError(f"a run finishes complete or failed, not {status!r}")

        def work(cur):
            cur.execute(
                "UPDATE radar_score_run SET status = %s, finished_at = %s, failed_detail = %s "
                "WHERE id = %s AND status = 'running'",
                (status, finished_at, detail, run_id),
            )
            if cur.rowcount != 1:
                raise RuntimeError(f"radar_score_run {run_id} was not running — refusing to re-publish it")

        self._tx("radar.evaluate", str(run_id), finished_at, work, before_commit)

    def board(self, pool_key: str) -> list[dict]:
        with self._connect() as conn:
            cursor = conn.execute(
                "SELECT * FROM radar_board_v WHERE pool_key = %s ORDER BY membership_id, trade_def_md5",
                (pool_key,),
            )
            columns = [item.name for item in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def members_for_replay(self, pool_key: str, trade_date: date) -> list[dict]:
        """Admitted episodes of one day (read-only dry-run input)."""
        return [row for row in self.members_for_day(pool_key, trade_date) if row["entered_at"] is not None]


__all__ = ["RadarStore"]
