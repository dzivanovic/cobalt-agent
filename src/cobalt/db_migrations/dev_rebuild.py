"""`rebuild_table` — free a dev table's dropped column slots, provably.

WHY THIS EXISTS (2026-10-02). Postgres never reuses a dropped column's
`attnum`: the slot is freed only when the relation is rebuilt. Every real
forward and rollback of `0007` on `cobalt_dev` adds and then drops 29
columns on `"user".aset_sizings`, and on 2026-10-01 that table reached
`max_attnum 1581` of the 1600 hard limit (`deploy-2026-10-01-1.md`,
`## L68 GATE` (c) and `## DECISIONS` 2). One table was rebuilt by a one-off
script that day (`devdb-rebuild-2026-10-02.md`). This module turns that
script into the standard, for any `system` / `"user"` table.

THE RULE. In the caller's ONE transaction, under a savepoint:

    BEFORE = read_state()   max(attnum), dropped, live, rows, row digest,
                            and a pg_catalog digest by section
    rebuild                 a fresh table with the live columns in order,
                            everything that hangs off the old one re-made
    AFTER  = read_state()
    keep it only if every AFTER value equals BEFORE, except
    `max_attnum` = live and dropped = 0.

Anything else raises `RebuildMismatch` naming each differing field, and
the savepoint is rolled back: NOTHING IS KEPT. `dry_run=True` rolls the
savepoint back after the compare whatever it shows. The caller commits;
this module never does.

THE ROW DIGEST is the migrate proof's own per-table digest
(`cli._content_digest`, L3) over the whole `to_jsonb(t)` — every column,
in primary-key order, independent of column order.

A SHAPE THIS MODULE DOES NOT HANDLE IS REFUSED, never guessed (L1):
anything but a plain permanent table, rules, inheritance or partitioning,
publication membership, extended statistics, security labels, a
serial-style owned sequence, a virtual generated column, a dependent that
is not a plain view, a table or index outside the default tablespace.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field

import psycopg
from psycopg import sql

from .cli import _content_digest

#: The schemas a rebuild may touch. `public` holds nothing new-core.
SCHEMAS = ("system", "user")

#: Postgres's hard limit on a table's column slots (`MaxHeapAttributeNumber`).
SLOT_LIMIT = 1600

#: Free slots below which the with-DB suite refuses to start (slot-guard
#: S2): the largest committed churn of one suite run plus the 33 a
#: rolled-back test adds inside its transaction
#: (`test_radar_score_migration.py:497`–`506` re-adds `0007` after
#: `0021` / `0022`).
SLOT_FAIL_HEADROOM = 64


class RebuildRefused(RuntimeError):
    """A precondition or a table shape this rebuild does not handle."""


class RebuildMismatch(RuntimeError):
    """AFTER differs from BEFORE outside the rule. Nothing was kept."""

    def __init__(self, fields, *, before: "TableState", after: "TableState"):
        self.fields = tuple(fields)
        self.before = before
        self.after = after
        super().__init__("AFTER differs from BEFORE in: " + ", ".join(self.fields))

    def detail_lines(self) -> list[str]:
        """`- <line>` gone and `+ <line>` new, per differing section."""
        out = []
        for name in self.fields:
            b = self.before.sections.get(name)
            a = self.after.sections.get(name)
            if b is None and a is None:
                out.append(f"{name}: BEFORE {getattr(self.before, name)} "
                           f"AFTER {getattr(self.after, name)}")
                continue
            b, a = b or (), a or ()
            out.append(f"{name}:")
            out.extend(f"  - {line}" for line in b if line not in a)
            out.extend(f"  + {line}" for line in a if line not in b)
        return out


def _md5_lines(lines) -> str:
    return hashlib.md5("\n".join(lines).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class TableState:
    max_attnum: int
    dropped: int
    live: int
    rows: int
    row_digest: str
    #: section name -> its lines, built from pg_catalog BY NAME so a
    #: BEFORE and an AFTER of two different relations are comparable.
    sections: dict = field(default_factory=dict)

    @property
    def catalog_digest(self) -> str:
        return _md5_lines(f"{k}:{_md5_lines(v)}" for k, v in self.sections.items())

    def line(self) -> str:
        return (
            f"max_attnum {self.max_attnum} · dropped {self.dropped} · live {self.live}"
            f" · rows {self.rows} · row digest {self.row_digest}"
            f" · catalog digest {self.catalog_digest}"
        )


@dataclass(frozen=True)
class RebuildResult:
    before: TableState
    after: TableState
    dry_run: bool


# --------------------------------------------------------------------------
# catalog reads
# --------------------------------------------------------------------------
def _acl_sql(expr: str) -> str:
    """A stable, sorted text rendering of an aclitem[] (NULL = default)."""
    return (
        f"CASE WHEN {expr} IS NULL THEN '<default>' ELSE coalesce(("
        "SELECT string_agg(s, ',' ORDER BY s) FROM ("
        "SELECT pg_get_userbyid(x.grantor) || '>' || "
        "CASE WHEN x.grantee = 0 THEN 'PUBLIC' ELSE pg_get_userbyid(x.grantee) END"
        " || ':' || x.privilege_type || CASE WHEN x.is_grantable THEN '*' ELSE '' END AS s"
        f" FROM aclexplode({expr}) x) q), '<empty>') END"
    )


def _rows(conn, query: str, params=None) -> list[tuple]:
    return conn.execute(query, params).fetchall()


def _one(conn, query: str, params=None):
    row = conn.execute(query, params).fetchone()
    return row[0] if row else None


def _table_oid(conn, schema: str, table: str) -> int:
    oid = _one(
        conn,
        "SELECT c.oid FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace"
        " WHERE n.nspname = %s AND c.relname = %s",
        (schema, table),
    )
    if oid is None:
        raise RebuildRefused(f"{schema}.{table} not found")
    return int(oid)


def _dependent_views(conn, oid: int) -> list[tuple]:
    """(oid, qualified name, relkind, depth) for every relation whose rewrite
    rule depends, directly or through other views, on the table; ordered for
    creation."""
    return _rows(
        conn,
        """
        WITH RECURSIVE dep(oid, depth) AS (
            SELECT r.ev_class, 1
              FROM pg_depend d JOIN pg_rewrite r ON r.oid = d.objid
             WHERE d.classid = 'pg_rewrite'::regclass
               AND d.refclassid = 'pg_class'::regclass
               AND d.refobjid = %(oid)s AND r.ev_class <> %(oid)s
            UNION
            SELECT r.ev_class, dep.depth + 1
              FROM dep
              JOIN pg_depend d ON d.refobjid = dep.oid
                              AND d.refclassid = 'pg_class'::regclass
                              AND d.classid = 'pg_rewrite'::regclass
              JOIN pg_rewrite r ON r.oid = d.objid
             WHERE r.ev_class <> dep.oid
        )
        SELECT c.oid, quote_ident(n.nspname) || '.' || quote_ident(c.relname),
               c.relkind, max(dep.depth) AS depth
          FROM dep JOIN pg_class c ON c.oid = dep.oid
          JOIN pg_namespace n ON n.oid = c.relnamespace
         GROUP BY c.oid, n.nspname, c.relname, c.relkind
         ORDER BY depth, 2
        """,
        {"oid": oid},
    )


_TABLE_SHAPE = """
    SELECT c.relkind, c.relpersistence, c.relhasrules, c.relispartition,
           (SELECT count(*) FROM pg_inherits WHERE inhrelid = c.oid OR inhparent = c.oid),
           (SELECT count(*) FROM pg_publication_rel WHERE prrelid = c.oid),
           (SELECT count(*) FROM pg_statistic_ext WHERE stxrelid = c.oid),
           (SELECT count(*) FROM pg_seclabel WHERE objoid = c.oid
                                             AND classoid = 'pg_class'::regclass),
           c.reltablespace,
           (SELECT count(*) FROM pg_index x JOIN pg_class i ON i.oid = x.indexrelid
             WHERE x.indrelid = c.oid AND i.reltablespace <> 0)
      FROM pg_class c WHERE c.oid = %s"""


def read_state(conn, schema: str, table: str) -> TableState:
    """BEFORE / AFTER: the numbers, the row digest, the catalog by section."""
    oid = _table_oid(conn, schema, table)
    rows, row_digest = _content_digest(conn, schema, table, sql.SQL("to_jsonb(t)"))
    s: dict[str, list[tuple]] = {}
    s["table"] = _rows(
        conn,
        """SELECT pg_get_userbyid(c.relowner), array_to_string(c.reloptions, ','),
                  c.relrowsecurity, c.relforcerowsecurity, c.relreplident,
                  obj_description(c.oid, 'pg_class'),
                  (SELECT amname FROM pg_am WHERE oid = c.relam),
                  (SELECT 'toast:' || coalesce(array_to_string(t.reloptions, ','), '')
                     FROM pg_class t WHERE t.oid = c.reltoastrelid)
             FROM pg_class c WHERE c.oid = %s""",
        (oid,),
    ) + _rows(conn, _TABLE_SHAPE, (oid,))
    s["grants"] = _rows(
        conn, f"SELECT 'table', {_acl_sql('c.relacl')} FROM pg_class c WHERE c.oid = %s", (oid,)
    ) + _rows(
        conn,
        f"""SELECT 'column ' || a.attname, {_acl_sql('a.attacl')}
              FROM pg_attribute a
             WHERE a.attrelid = %s AND a.attnum > 0 AND NOT a.attisdropped
               AND a.attacl IS NOT NULL
             ORDER BY a.attname""",
        (oid,),
    )
    s["columns"] = _rows(
        conn,
        """SELECT row_number() OVER (ORDER BY a.attnum), a.attname,
                  format_type(a.atttypid, a.atttypmod),
                  CASE WHEN a.attcollation <> t.typcollation THEN co.collname END,
                  a.attnotnull, pg_get_expr(d.adbin, d.adrelid), a.attidentity, a.attgenerated,
                  a.attstattarget, a.attstorage, a.attcompression,
                  array_to_string(a.attoptions, ','), col_description(a.attrelid, a.attnum)
             FROM pg_attribute a JOIN pg_type t ON t.oid = a.atttypid
             LEFT JOIN pg_collation co ON co.oid = a.attcollation
             LEFT JOIN pg_attrdef d ON d.adrelid = a.attrelid AND d.adnum = a.attnum
            WHERE a.attrelid = %s AND a.attnum > 0 AND NOT a.attisdropped
            ORDER BY a.attnum""",
        (oid,),
    )
    s["constraints"] = _rows(
        conn,
        """SELECT con.conname, con.contype, pg_get_constraintdef(con.oid), con.convalidated,
                  obj_description(con.oid, 'pg_constraint')
             FROM pg_constraint con WHERE con.conrelid = %s ORDER BY con.conname""",
        (oid,),
    )
    s["fks_out"] = [r for r in s["constraints"] if r[1] == "f"]
    s["fks_in"] = _rows(
        conn,
        """SELECT con.conrelid::regclass::text, con.conname, pg_get_constraintdef(con.oid),
                  con.convalidated, obj_description(con.oid, 'pg_constraint')
             FROM pg_constraint con
            WHERE con.confrelid = %s AND con.contype = 'f' AND con.conrelid <> %s
            ORDER BY 1, 2""",
        (oid, oid),
    )
    s["indexes"] = _rows(
        conn,
        """SELECT i.relname, pg_get_indexdef(x.indexrelid), x.indisclustered, x.indisreplident,
                  x.indisvalid,
                  (SELECT con.conname FROM pg_constraint con
                    WHERE con.conindid = x.indexrelid AND con.conrelid = x.indrelid
                      AND con.contype IN ('p', 'u', 'x')),
                  obj_description(i.oid, 'pg_class'),
                  (SELECT string_agg(a.attnum || ':' || a.attstattarget, ',' ORDER BY a.attnum)
                     FROM pg_attribute a
                    WHERE a.attrelid = i.oid AND a.attstattarget IS NOT NULL AND a.attstattarget <> -1)
             FROM pg_index x JOIN pg_class i ON i.oid = x.indexrelid
            WHERE x.indrelid = %s ORDER BY i.relname""",
        (oid,),
    )
    s["triggers"] = _rows(
        conn,
        """SELECT t.tgname, pg_get_triggerdef(t.oid), t.tgenabled, obj_description(t.oid, 'pg_trigger')
             FROM pg_trigger t WHERE t.tgrelid = %s AND NOT t.tgisinternal ORDER BY t.tgname""",
        (oid,),
    )
    s["policies"] = _rows(
        conn,
        """SELECT p.polname, p.polpermissive, p.polcmd,
                  array_to_string(ARRAY(SELECT CASE WHEN r = 0 THEN 'PUBLIC' ELSE pg_get_userbyid(r) END
                                          FROM unnest(p.polroles) WITH ORDINALITY u(r, o) ORDER BY o), ','),
                  pg_get_expr(p.polqual, p.polrelid), pg_get_expr(p.polwithcheck, p.polrelid),
                  obj_description(p.oid, 'pg_policy')
             FROM pg_policy p WHERE p.polrelid = %s ORDER BY p.polname""",
        (oid,),
    )
    s["sequences"] = []
    for r in _rows(
        conn,
        f"""SELECT quote_ident(sn.nspname) || '.' || quote_ident(s.relname), d.deptype, a.attname,
                   pg_get_userbyid(s.relowner), {_acl_sql('s.relacl')}, format_type(sq.seqtypid, NULL),
                   sq.seqstart, sq.seqincrement, sq.seqmax, sq.seqmin, sq.seqcache, sq.seqcycle,
                   obj_description(s.oid, 'pg_class')
              FROM pg_depend d
              JOIN pg_class s ON s.oid = d.objid AND s.relkind = 'S'
              JOIN pg_namespace sn ON sn.oid = s.relnamespace
              JOIN pg_sequence sq ON sq.seqrelid = s.oid
              JOIN pg_attribute a ON a.attrelid = d.refobjid AND a.attnum = d.refobjsubid
             WHERE d.classid = 'pg_class'::regclass AND d.refclassid = 'pg_class'::regclass
               AND d.refobjid = %s AND d.deptype IN ('a', 'i')
             ORDER BY 1""",
        (oid,),
    ):
        last = _rows(conn, f"SELECT last_value, is_called FROM {r[0]}")[0]
        s["sequences"].append(tuple(r) + tuple(last))
    s["views"] = []
    for v_oid, v_name, _relkind, _depth in _dependent_views(conn, oid):
        s["views"].extend(
            (v_name,) + tuple(r)
            for r in _rows(
                conn,
                f"""SELECT c.relkind, pg_get_userbyid(c.relowner), {_acl_sql('c.relacl')},
                           array_to_string(c.reloptions, ','), pg_get_viewdef(c.oid),
                           obj_description(c.oid, 'pg_class'),
                           (SELECT count(*) FROM pg_rewrite WHERE ev_class = c.oid AND rulename <> '_RETURN'),
                           (SELECT string_agg(t.tgname || ':' || pg_get_triggerdef(t.oid) || ':' || t.tgenabled::text, ';' ORDER BY t.tgname)
                              FROM pg_trigger t WHERE t.tgrelid = c.oid AND NOT t.tgisinternal),
                           (SELECT string_agg(a.attname || ':' || coalesce(col_description(c.oid, a.attnum), '') || ':' || {_acl_sql('a.attacl')}
                                              || ':' || coalesce((SELECT pg_get_expr(d.adbin, d.adrelid) FROM pg_attrdef d
                                                                   WHERE d.adrelid = c.oid AND d.adnum = a.attnum), ''),
                                              ';' ORDER BY a.attnum)
                              FROM pg_attribute a WHERE a.attrelid = c.oid AND a.attnum > 0 AND NOT a.attisdropped)
                      FROM pg_class c WHERE c.oid = %s""",
                (v_oid,),
            )
        )
    return TableState(
        max_attnum=_one(conn, "SELECT max(attnum) FROM pg_attribute WHERE attrelid = %s AND attnum > 0", (oid,)),
        dropped=_one(conn, "SELECT count(*) FROM pg_attribute WHERE attrelid = %s AND attnum > 0 AND attisdropped", (oid,)),
        live=_one(conn, "SELECT count(*) FROM pg_attribute WHERE attrelid = %s AND attnum > 0 AND NOT attisdropped", (oid,)),
        rows=rows,
        row_digest=row_digest,
        sections={
            k: tuple("|".join("" if x is None else str(x) for x in r) for r in v)
            for k, v in s.items()
        },
    )


def differences(before: TableState, after: TableState) -> list[str]:
    """The rule. Empty means AFTER may be kept."""
    fields = [f for f in ("live", "rows", "row_digest") if getattr(before, f) != getattr(after, f)]
    if after.max_attnum != after.live:
        fields.append("max_attnum")
    if after.dropped != 0:
        fields.append("dropped")
    names = list(before.sections) + [k for k in after.sections if k not in before.sections]
    fields.extend(k for k in names if before.sections.get(k) != after.sections.get(k))
    return fields


# --------------------------------------------------------------------------
# the rebuild
# --------------------------------------------------------------------------
_ACL_ENTRY_COLS = (
    "pg_get_userbyid(x.grantor), "
    "CASE WHEN x.grantee = 0 THEN 'PUBLIC' ELSE quote_ident(pg_get_userbyid(x.grantee)) END, "
    "x.privilege_type, x.is_grantable"
)
_TRIGGER_STATE = {"D": "DISABLE TRIGGER", "R": "ENABLE REPLICA TRIGGER", "A": "ENABLE ALWAYS TRIGGER"}
_POLCMD = {"*": "ALL", "r": "SELECT", "a": "INSERT", "w": "UPDATE", "d": "DELETE"}
_STORAGE = {"p": "PLAIN", "e": "EXTERNAL", "m": "MAIN", "x": "EXTENDED"}
_COMPRESSION = {"p": "pglz", "l": "lz4"}


def _lit(conn, value) -> str:
    return "NULL" if value is None else sql.Literal(value).as_string(conn)


def _rel_acl(conn, oid: int) -> tuple[bool, list[tuple]]:
    null_acl = _one(conn, "SELECT relacl IS NULL FROM pg_class WHERE oid = %s", (oid,))
    return bool(null_acl), _rows(
        conn, f"SELECT {_ACL_ENTRY_COLS} FROM pg_class c, aclexplode(c.relacl) x WHERE c.oid = %s", (oid,)
    )


def _col_acls(conn, oid: int) -> list[tuple]:
    """(quoted column, entries) for every column with a non-null ACL."""
    return [
        (attq, _rows(
            conn,
            f"SELECT {_ACL_ENTRY_COLS} FROM pg_attribute a, aclexplode(a.attacl) x"
            " WHERE a.attrelid = %s AND a.attnum = %s",
            (oid, attnum),
        ))
        for attnum, attq in _rows(
            conn,
            "SELECT attnum, quote_ident(attname) FROM pg_attribute"
            " WHERE attrelid = %s AND attnum > 0 AND NOT attisdropped AND attacl IS NOT NULL"
            " ORDER BY attnum",
            (oid,),
        )
    ]


def _restore_acl(conn, objkw: str, target: str, owner: str, owner_q: str,
                 null_acl: bool, entries: list[tuple], column: str | None = None) -> None:
    if null_acl:
        return
    col = f" ({column})" if column else ""
    if column is None:
        # A fresh relation already carries the schema's DEFAULT PRIVILEGES
        # for the creating role; those are revoked too, so the ACL that
        # results is the captured one and nothing more.
        present = [
            r[0] for r in _rows(
                conn,
                "SELECT DISTINCT CASE WHEN x.grantee = 0 THEN 'PUBLIC'"
                " ELSE quote_ident(pg_get_userbyid(x.grantee)) END"
                " FROM pg_class c, aclexplode(c.relacl) x WHERE c.oid = %s::regclass",
                (target,),
            )
        ]
        for grantee_q in sorted(set(present) | {owner_q}):
            conn.execute(f"REVOKE ALL ON {objkw} {target} FROM {grantee_q}")
    for grantor, grantee_q, priv, grantable in sorted(entries, key=lambda e: e[0] != owner):
        stmt = f"GRANT {priv}{col} ON {objkw} {target} TO {grantee_q}"
        if grantable:
            stmt += " WITH GRANT OPTION"
        if grantor == owner:
            conn.execute(stmt)
        else:
            conn.execute(f"SET ROLE {_one(conn, 'SELECT quote_ident(%s)', (grantor,))}")
            conn.execute(stmt)
            conn.execute("RESET ROLE")


def _with_opts(reloptions) -> str:
    return f" WITH ({', '.join(reloptions)})" if reloptions else ""


def _capture_view(conn, v_oid: int, v_name: str) -> dict:
    relkind, owner, owner_q, reloptions, defn, comment, extra_rules = _rows(
        conn,
        """SELECT c.relkind, pg_get_userbyid(c.relowner), quote_ident(pg_get_userbyid(c.relowner)),
                  c.reloptions, pg_get_viewdef(c.oid), obj_description(c.oid, 'pg_class'),
                  (SELECT count(*) FROM pg_rewrite WHERE ev_class = c.oid AND rulename <> '_RETURN')
             FROM pg_class c WHERE c.oid = %s""",
        (v_oid,),
    )[0]
    if relkind != "v":
        raise RebuildRefused(f"dependent {v_name} has relkind {relkind!r}; only plain views are handled")
    if extra_rules:
        raise RebuildRefused(f"dependent view {v_name} has {extra_rules} extra rule(s); not handled")
    null_acl, entries = _rel_acl(conn, v_oid)
    return {
        "name": v_name, "owner": owner, "owner_q": owner_q, "reloptions": reloptions,
        "def": defn, "comment": comment, "null_acl": null_acl, "acl": entries,
        "col_acls": _col_acls(conn, v_oid),
        "col_comments": _rows(
            conn,
            "SELECT quote_ident(attname), col_description(attrelid, attnum) FROM pg_attribute"
            " WHERE attrelid = %s AND attnum > 0 AND NOT attisdropped"
            " AND col_description(attrelid, attnum) IS NOT NULL ORDER BY attnum",
            (v_oid,),
        ),
        "col_defaults": _rows(
            conn,
            "SELECT quote_ident(a.attname), pg_get_expr(d.adbin, d.adrelid)"
            " FROM pg_attrdef d JOIN pg_attribute a ON a.attrelid = d.adrelid AND a.attnum = d.adnum"
            " WHERE d.adrelid = %s ORDER BY a.attnum",
            (v_oid,),
        ),
        "triggers": _rows(
            conn,
            "SELECT quote_ident(tgname), pg_get_triggerdef(oid), tgenabled, obj_description(oid, 'pg_trigger')"
            " FROM pg_trigger WHERE tgrelid = %s AND NOT tgisinternal ORDER BY tgname",
            (v_oid,),
        ),
    }


def _capture(conn, schema: str, table: str) -> dict:
    """Everything the rebuild re-makes, read before any change."""
    oid = _table_oid(conn, schema, table)
    (relkind, persistence, hasrules, ispartition, n_inh, n_pub, n_stx, n_lbl,
     tablespace, n_idx_ts) = _rows(conn, _TABLE_SHAPE, (oid,))[0]
    if (relkind != "r" or persistence != "p" or hasrules or ispartition
            or n_inh or n_pub or n_stx or n_lbl or tablespace or n_idx_ts):
        raise RebuildRefused(
            f"unhandled table shape: relkind={relkind} persistence={persistence} rules={hasrules}"
            f" partition={ispartition} inherits={n_inh} publications={n_pub}"
            f" ext_stats={n_stx} security_labels={n_lbl} tablespace={tablespace}"
            f" index_tablespaces={n_idx_ts}"
        )
    owner, owner_q, reloptions, rls, force_rls, replident, comment, am_q, toast_options = _rows(
        conn,
        """SELECT pg_get_userbyid(c.relowner), quote_ident(pg_get_userbyid(c.relowner)),
                  c.reloptions, c.relrowsecurity, c.relforcerowsecurity, c.relreplident,
                  obj_description(c.oid, 'pg_class'),
                  (SELECT quote_ident(amname) FROM pg_am WHERE oid = c.relam),
                  (SELECT t.reloptions FROM pg_class t WHERE t.oid = c.reltoastrelid)
             FROM pg_class c WHERE c.oid = %s""",
        (oid,),
    )[0]
    null_acl, acl = _rel_acl(conn, oid)
    cols = _rows(
        conn,
        """SELECT quote_ident(a.attname), format_type(a.atttypid, a.atttypmod),
                  CASE WHEN a.attcollation <> t.typcollation
                       THEN quote_ident(cn.nspname) || '.' || quote_ident(co.collname) END,
                  a.attnotnull, pg_get_expr(d.adbin, d.adrelid), a.attidentity, a.attgenerated,
                  a.attstattarget, a.attstorage, t.typstorage, a.attcompression, a.attoptions,
                  col_description(a.attrelid, a.attnum)
             FROM pg_attribute a JOIN pg_type t ON t.oid = a.atttypid
             LEFT JOIN pg_collation co ON co.oid = a.attcollation
             LEFT JOIN pg_namespace cn ON cn.oid = co.collnamespace
             LEFT JOIN pg_attrdef d ON d.adrelid = a.attrelid AND d.adnum = a.attnum
            WHERE a.attrelid = %s AND a.attnum > 0 AND NOT a.attisdropped
            ORDER BY a.attnum""",
        (oid,),
    )
    if any(c[6] not in ("", "s") for c in cols):
        raise RebuildRefused("a virtual generated column exists; only STORED is handled")
    seqs = {}
    for s in _rows(
        conn,
        """SELECT s.oid, quote_ident(sn.nspname) || '.' || quote_ident(s.relname), d.deptype,
                  quote_ident(a.attname), sq.seqstart, sq.seqincrement, sq.seqmax, sq.seqmin,
                  sq.seqcache, sq.seqcycle, obj_description(s.oid, 'pg_class'),
                  pg_get_userbyid(s.relowner), quote_ident(pg_get_userbyid(s.relowner))
             FROM pg_depend d
             JOIN pg_class s ON s.oid = d.objid AND s.relkind = 'S'
             JOIN pg_namespace sn ON sn.oid = s.relnamespace
             JOIN pg_sequence sq ON sq.seqrelid = s.oid
             JOIN pg_attribute a ON a.attrelid = d.refobjid AND a.attnum = d.refobjsubid
            WHERE d.classid = 'pg_class'::regclass AND d.refclassid = 'pg_class'::regclass
              AND d.refobjid = %s AND d.deptype IN ('a', 'i')""",
        (oid,),
    ):
        if s[2] != "i":
            raise RebuildRefused("a serial-style owned sequence exists; only identity sequences are handled")
        last_value, is_called = _rows(conn, f"SELECT last_value, is_called FROM {s[1]}")[0]
        s_null_acl, s_acl = _rel_acl(conn, s[0])
        seqs[s[3]] = {
            "oid": s[0], "name": s[1], "start": s[4], "inc": s[5], "max": s[6], "min": s[7],
            "cache": s[8], "cycle": s[9], "comment": s[10], "owner": s[11], "owner_q": s[12],
            "last_value": last_value, "is_called": is_called, "null_acl": s_null_acl, "acl": s_acl,
        }
    if any(c[5] and c[0] not in seqs for c in cols):
        raise RebuildRefused("an identity column has no owned sequence")
    return {
        "oid": oid, "owner": owner, "owner_q": owner_q, "reloptions": reloptions,
        "am_q": am_q, "toast_options": toast_options,
        "index_stats": _rows(
            conn,
            """SELECT quote_ident(i.relname), a.attnum, a.attstattarget
                 FROM pg_index x JOIN pg_class i ON i.oid = x.indexrelid
                 JOIN pg_attribute a ON a.attrelid = i.oid
                WHERE x.indrelid = %s AND a.attstattarget IS NOT NULL AND a.attstattarget <> -1
                ORDER BY 1, 2""",
            (oid,),
        ),
        "rls": rls, "force_rls": force_rls, "replident": replident, "comment": comment,
        "null_acl": null_acl, "acl": acl, "col_acls": _col_acls(conn, oid),
        "cols": cols, "seqs": seqs,
        "constraints": _rows(
            conn,
            """SELECT quote_ident(conname), contype, pg_get_constraintdef(oid),
                      obj_description(oid, 'pg_constraint')
                 FROM pg_constraint WHERE conrelid = %s
                ORDER BY CASE contype WHEN 'p' THEN 0 WHEN 'u' THEN 1 WHEN 'x' THEN 2
                                      WHEN 'c' THEN 3 WHEN 'f' THEN 4 ELSE 5 END, conname""",
            (oid,),
        ),
        "indexes": _rows(
            conn,
            """SELECT i.oid, quote_ident(i.relname), pg_get_indexdef(x.indexrelid), x.indisclustered,
                      x.indisreplident, obj_description(i.oid, 'pg_class'),
                      EXISTS (SELECT 1 FROM pg_constraint con
                               WHERE con.conindid = x.indexrelid AND con.conrelid = x.indrelid
                                 AND con.contype IN ('p', 'u', 'x'))
                 FROM pg_index x JOIN pg_class i ON i.oid = x.indexrelid
                WHERE x.indrelid = %s ORDER BY i.relname""",
            (oid,),
        ),
        "triggers": _rows(
            conn,
            """SELECT quote_ident(tgname), pg_get_triggerdef(oid), tgenabled, obj_description(oid, 'pg_trigger')
                 FROM pg_trigger WHERE tgrelid = %s AND NOT tgisinternal ORDER BY tgname""",
            (oid,),
        ),
        "policies": _rows(
            conn,
            """SELECT quote_ident(p.polname), p.polpermissive, p.polcmd,
                      array_to_string(ARRAY(SELECT CASE WHEN r = 0 THEN 'PUBLIC' ELSE quote_ident(pg_get_userbyid(r)) END
                                              FROM unnest(p.polroles) WITH ORDINALITY u(r, o) ORDER BY o), ', '),
                      pg_get_expr(p.polqual, p.polrelid), pg_get_expr(p.polwithcheck, p.polrelid),
                      obj_description(p.oid, 'pg_policy')
                 FROM pg_policy p WHERE p.polrelid = %s ORDER BY p.polname""",
            (oid,),
        ),
        "fks_in": _rows(
            conn,
            """SELECT con.conrelid::regclass::text, quote_ident(con.conname), pg_get_constraintdef(con.oid),
                      obj_description(con.oid, 'pg_constraint')
                 FROM pg_constraint con
                WHERE con.confrelid = %s AND con.contype = 'f' AND con.conrelid <> %s
                ORDER BY 1, 2""",
            (oid, oid),
        ),
        "views": [_capture_view(conn, v[0], v[1]) for v in _dependent_views(conn, oid)],
    }


def _restore_grants(conn, cap: dict, qt: str) -> None:
    """The table's own ACL and its column ACLs."""
    _restore_acl(conn, "TABLE", qt, cap["owner"], cap["owner_q"], cap["null_acl"], cap["acl"])
    for attq, entries in cap["col_acls"]:
        _restore_acl(conn, "TABLE", qt, cap["owner"], cap["owner_q"], False, entries, column=attq)


def _rebuild(conn, schema: str, table: str) -> None:
    cap = _capture(conn, schema, table)
    qs = sql.Identifier(schema).as_string(conn)
    qt = sql.Identifier(schema, table).as_string(conn)
    old = f"zz_rebuild_old_{cap['oid']}"
    seqs = cap["seqs"]

    # ---- detach: dependent views, inbound FKs; park the old table's names
    if cap["views"]:
        conn.execute("DROP VIEW " + ", ".join(v["name"] for v in cap["views"]))
    for rel, conname, _def, _c in cap["fks_in"]:
        conn.execute(f"ALTER TABLE {rel} DROP CONSTRAINT {conname}")
    for i_oid, iname, *_ in cap["indexes"]:
        conn.execute(f"ALTER INDEX {qs}.{iname} RENAME TO zz_rebuild_old_idx_{i_oid}")
    for s in seqs.values():
        conn.execute(f"ALTER SEQUENCE {s['name']} RENAME TO zz_rebuild_old_seq_{s['oid']}")
    conn.execute(f"ALTER TABLE {qt} RENAME TO {old}")

    # ---- the new table: live columns only, same order
    defs, copy_cols = [], []
    for (name, typ, coll, notnull, default, identity, generated, *_rest) in cap["cols"]:
        d = f"{name} {typ}"
        if coll:
            d += f" COLLATE {coll}"
        if generated == "s":
            d += f" GENERATED ALWAYS AS ({default}) STORED"
        elif default is not None:
            d += f" DEFAULT {default}"
        if identity:
            s = seqs[name]
            d += (
                f" GENERATED {'ALWAYS' if identity == 'a' else 'BY DEFAULT'} AS IDENTITY"
                f" (SEQUENCE NAME {s['name']} START WITH {s['start']}"
                f" INCREMENT BY {s['inc']} MINVALUE {s['min']} MAXVALUE {s['max']}"
                f" CACHE {s['cache']} {'CYCLE' if s['cycle'] else 'NO CYCLE'})"
            )
        if notnull:
            d += " NOT NULL"
        defs.append(d)
        if generated != "s":
            copy_cols.append(name)
    conn.execute(
        f"CREATE TABLE {qt} (\n    " + ",\n    ".join(defs) + f"\n) USING {cap['am_q']}"
        f"{_with_opts(cap['reloptions'])}"
    )
    if cap["toast_options"]:
        conn.execute(f"ALTER TABLE {qt} SET ({', '.join('toast.' + o for o in cap['toast_options'])})")
    conn.execute(f"ALTER TABLE {qt} OWNER TO {cap['owner_q']}")

    collist = ", ".join(copy_cols)
    overriding = " OVERRIDING SYSTEM VALUE" if seqs else ""
    conn.execute(f"INSERT INTO {qt} ({collist}){overriding} SELECT {collist} FROM {qs}.{old}")
    for s in seqs.values():
        if s["last_value"] is not None:
            conn.execute(
                f"SELECT setval({_lit(conn, s['name'])}::regclass, {s['last_value']},"
                f" {'true' if s['is_called'] else 'false'})"
            )

    for (name, _t, _c, _n, _d, _i, _g, stattarget, storage, typstorage, compression,
         attoptions, _cm) in cap["cols"]:
        if stattarget is not None and stattarget != -1:
            conn.execute(f"ALTER TABLE {qt} ALTER COLUMN {name} SET STATISTICS {stattarget}")
        if storage != typstorage:
            conn.execute(f"ALTER TABLE {qt} ALTER COLUMN {name} SET STORAGE {_STORAGE[storage]}")
        if compression in _COMPRESSION:
            conn.execute(f"ALTER TABLE {qt} ALTER COLUMN {name} SET COMPRESSION {_COMPRESSION[compression]}")
        if attoptions:
            conn.execute(f"ALTER TABLE {qt} ALTER COLUMN {name} SET ({', '.join(attoptions)})")

    # the old table goes, and its parked indexes and sequences with it
    conn.execute(f"DROP TABLE {qs}.{old}")

    # constraints (NOT NULL constraints of PG18+ come from the column definitions)
    for conname, contype, cdef, _c in cap["constraints"]:
        if contype not in ("n", "t"):
            conn.execute(f"ALTER TABLE {qt} ADD CONSTRAINT {conname} {cdef}")
    for _i, _n, idef, _cl, _ri, _c, backs_constraint in cap["indexes"]:
        if not backs_constraint:
            conn.execute(idef)
    for _i, iname, _d, clustered, repl, _c, _b in cap["indexes"]:
        if clustered:
            conn.execute(f"ALTER TABLE {qt} CLUSTER ON {iname}")
        if repl and cap["replident"] == "i":
            conn.execute(f"ALTER TABLE {qt} REPLICA IDENTITY USING INDEX {iname}")
    for iname, attnum, stattarget in cap["index_stats"]:
        conn.execute(f"ALTER INDEX {qs}.{iname} ALTER COLUMN {attnum} SET STATISTICS {stattarget}")
    if cap["replident"] in ("f", "n"):
        conn.execute(f"ALTER TABLE {qt} REPLICA IDENTITY {'FULL' if cap['replident'] == 'f' else 'NOTHING'}")

    for tname, tdef, tenabled, _c in cap["triggers"]:
        conn.execute(tdef)
        if tenabled in _TRIGGER_STATE:
            conn.execute(f"ALTER TABLE {qt} {_TRIGGER_STATE[tenabled]} {tname}")

    if cap["rls"]:
        conn.execute(f"ALTER TABLE {qt} ENABLE ROW LEVEL SECURITY")
    if cap["force_rls"]:
        conn.execute(f"ALTER TABLE {qt} FORCE ROW LEVEL SECURITY")
    for pname, permissive, cmd, roles, qual, wcheck, _c in cap["policies"]:
        stmt = (f"CREATE POLICY {pname} ON {qt} AS {'PERMISSIVE' if permissive else 'RESTRICTIVE'}"
                f" FOR {_POLCMD[cmd]} TO {roles}")
        if qual is not None:
            stmt += f" USING ({qual})"
        if wcheck is not None:
            stmt += f" WITH CHECK ({wcheck})"
        conn.execute(stmt)

    _restore_grants(conn, cap, qt)
    for s in seqs.values():
        _restore_acl(conn, "SEQUENCE", s["name"], s["owner"], s["owner_q"], s["null_acl"], s["acl"])

    if cap["comment"] is not None:
        conn.execute(f"COMMENT ON TABLE {qt} IS {_lit(conn, cap['comment'])}")
    for row in cap["cols"]:
        if row[12] is not None:
            conn.execute(f"COMMENT ON COLUMN {qt}.{row[0]} IS {_lit(conn, row[12])}")
    for conname, _t, _d, c in cap["constraints"]:
        if c is not None:
            conn.execute(f"COMMENT ON CONSTRAINT {conname} ON {qt} IS {_lit(conn, c)}")
    for _i, iname, _d, _cl, _ri, c, _b in cap["indexes"]:
        if c is not None:
            conn.execute(f"COMMENT ON INDEX {qs}.{iname} IS {_lit(conn, c)}")
    for tname, _d, _e, c in cap["triggers"]:
        if c is not None:
            conn.execute(f"COMMENT ON TRIGGER {tname} ON {qt} IS {_lit(conn, c)}")
    for pname, *_rest, c in cap["policies"]:
        if c is not None:
            conn.execute(f"COMMENT ON POLICY {pname} ON {qt} IS {_lit(conn, c)}")
    for s in seqs.values():
        if s["comment"] is not None:
            conn.execute(f"COMMENT ON SEQUENCE {s['name']} IS {_lit(conn, s['comment'])}")

    # ---- reattach: inbound FKs, then the dependent views in dependency order
    for rel, conname, cdef, c in cap["fks_in"]:
        conn.execute(f"ALTER TABLE {rel} ADD CONSTRAINT {conname} {cdef}")
        if c is not None:
            conn.execute(f"COMMENT ON CONSTRAINT {conname} ON {rel} IS {_lit(conn, c)}")
    for v in cap["views"]:
        conn.execute(f"CREATE VIEW {v['name']}{_with_opts(v['reloptions'])} AS {v['def']}")
        conn.execute(f"ALTER VIEW {v['name']} OWNER TO {v['owner_q']}")
        for attq, default in v["col_defaults"]:
            conn.execute(f"ALTER VIEW {v['name']} ALTER COLUMN {attq} SET DEFAULT {default}")
        _restore_acl(conn, "TABLE", v["name"], v["owner"], v["owner_q"], v["null_acl"], v["acl"])
        for attq, entries in v["col_acls"]:
            _restore_acl(conn, "TABLE", v["name"], v["owner"], v["owner_q"], False, entries, column=attq)
        if v["comment"] is not None:
            conn.execute(f"COMMENT ON VIEW {v['name']} IS {_lit(conn, v['comment'])}")
        for attq, c in v["col_comments"]:
            conn.execute(f"COMMENT ON COLUMN {v['name']}.{attq} IS {_lit(conn, c)}")
        for tname, tdef, tenabled, c in v["triggers"]:
            conn.execute(tdef)
            if tenabled in _TRIGGER_STATE:
                conn.execute(f"ALTER TABLE {v['name']} {_TRIGGER_STATE[tenabled]} {tname}")
            if c is not None:
                conn.execute(f"COMMENT ON TRIGGER {tname} ON {v['name']} IS {_lit(conn, c)}")

    conn.execute(f"ANALYZE {qt}")


# --------------------------------------------------------------------------
# the slot read (slot-guard S1, S2)
# --------------------------------------------------------------------------
_SLOT_REPORT = """
    SELECT n.nspname, c.relname, max(a.attnum),
           count(*) FILTER (WHERE a.attisdropped),
           count(*) FILTER (WHERE NOT a.attisdropped)
      FROM pg_catalog.pg_attribute a
      JOIN pg_catalog.pg_class c ON c.oid = a.attrelid
      JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
     WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p') AND a.attnum > 0
     GROUP BY n.nspname, c.relname
     ORDER BY 3 DESC, 1, 2"""


def slot_report(conn) -> list[tuple[str, str, int, int, int]]:
    """`(schema, table, max_attnum, dropped, live)` for every table in
    `system` / `"user"`, highest `max_attnum` first. ONE read, catalog only;
    `cobalt db migrate` (S1) and the with-DB suite's start (S2) both call it
    (L3)."""
    return [
        (schema, table, int(max_attnum), int(dropped), int(live))
        for schema, table, max_attnum, dropped, live in conn.execute(_SLOT_REPORT).fetchall()
    ]


def slot_lines(rows, warn_at: int) -> list[str]:
    """One `SLOTS WARN` line per table at or above `warn_at`, else ONE
    `SLOTS ok` line naming the highest."""
    warn = [
        f"SLOTS WARN {s}.{t} max_attnum {m} of {SLOT_LIMIT} · dropped {d} · live {l}"
        f" · fix: cobalt db dev-rebuild {s}.{t} (dev only)"
        for s, t, m, d, l in rows
        if m >= warn_at
    ]
    if warn:
        return warn
    if not rows:
        return ['SLOTS ok · no table in system / "user"']
    s, t, m, _d, _l = max(rows, key=lambda r: r[2])
    return [f"SLOTS ok · highest {s}.{t} {m} of {SLOT_LIMIT}"]


def slot_verdict(rows, warn_at: int, fail_headroom: int) -> str:
    """`fail` when any table has fewer than `fail_headroom` free slots,
    `warn` when any is at or above `warn_at`, else `ok`."""
    if any(SLOT_LIMIT - r[2] < fail_headroom for r in rows):
        return "fail"
    if any(r[2] >= warn_at for r in rows):
        return "warn"
    return "ok"


def rebuild_table(conn, schema: str, table: str, *, dry_run: bool) -> RebuildResult:
    """Rebuild `schema.table` in the caller's open transaction; see the module
    docstring for the rule. Returns BEFORE and AFTER; never commits.

    The ACCESS EXCLUSIVE lock is taken OUTSIDE the savepoint, so it is held
    until the caller's transaction ends — one transaction, one lock span —
    and a rolled-back savepoint leaves the original table untouched.
    """
    if schema not in SCHEMAS:
        raise RebuildRefused(f"schema {schema!r} is not one of {', '.join(SCHEMAS)}")
    if conn.autocommit:
        raise RebuildRefused(
            "rebuild_table runs inside the caller's ONE transaction; this connection "
            "is in autocommit, so every statement would commit on its own"
        )
    conn.execute(sql.SQL("LOCK TABLE {} IN ACCESS EXCLUSIVE MODE").format(sql.Identifier(schema, table)))
    with conn.transaction():
        before = read_state(conn, schema, table)
        _rebuild(conn, schema, table)
        after = read_state(conn, schema, table)
        fields = differences(before, after)
        if fields:
            raise RebuildMismatch(fields, before=before, after=after)
        if dry_run:
            raise psycopg.Rollback()
    return RebuildResult(before=before, after=after, dry_run=dry_run)


__all__ = [
    "RebuildMismatch",
    "RebuildRefused",
    "RebuildResult",
    "SCHEMAS",
    "SLOT_FAIL_HEADROOM",
    "SLOT_LIMIT",
    "TableState",
    "differences",
    "read_state",
    "rebuild_table",
    "slot_lines",
    "slot_report",
    "slot_verdict",
]
