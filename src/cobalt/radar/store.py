"""System-side radar membership and pool-row transactions."""

from __future__ import annotations

import json
from datetime import datetime
from typing import Callable

from cobalt import db, env
from cobalt.db import Side
from cobalt.session import assert_writable

from .pool import Action, Transition
from zoneinfo import ZoneInfo

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


__all__ = ["RadarStore"]
