"""The ONE vault write path (LAW L28, 2026-09-03).

Every byte Cobalt puts into an Obsidian note goes through this module.
Nothing under `src/cobalt/` may open a vault file for writing any other
way — grep for `write_text|open(.*"a"|"w")` under src/cobalt to prove it.

What the law buys, mechanically:

1. **create-if-absent only.** `create_if_absent()` renders a template
   into a file that does not exist. An existing file NEVER takes that
   path — not at 05:15, not for a stub, not ever. It takes `upsert_unit`,
   which merges. The old `daily.py` stub-upgrade branch (whole-file
   rewrite that discarded everything above a banner) is deleted, not
   fixed.
2. **Marker-bounded, unit-addressed.** Cobalt writes only between
   `<!-- cobalt:section NAME -->` markers, and everything it writes is a
   `<!-- cobalt:unit ID -->` block. Same id -> update in place. Human
   text inside a section, and every byte outside one, is carried through
   verbatim in position. A human edit to a Cobalt line WINS and is
   recorded as an override.
3. **Audited.** Before/after of the touched section plus full-file
   hashes land in `vault_writes` on every write (30-day retention,
   purged by this writer itself); overrides land in `vault_overrides`,
   which never expires. The file write is atomic (tmp + rename in the
   same directory) behind an mtime+hash guard: if the file changed since
   it was read, the write ABORTS LOUDLY, re-reads, and retries exactly
   once.
4. **Diff-first.** Every result carries the unified diff, and every
   entrypoint has `--dry-run`, which computes the whole thing and writes
   nothing.
5. **Never the wrong vault.** A target under the production vault is
   refused unless `COBALT_ENV=production` is set explicitly, and a
   production-declared process is refused a target outside it. Fail
   loud; never resolve silently to either vault.
6. **Never at the wrong time (F1, 2026-09-04).** Every write entry point
   is gated on `cobalt.session`: inside `market_reset` (20:00-21:00 ET)
   the write is REFUSED with one loud message naming the window, a log
   line, and a `session_blocks` counter row. Two carve-outs, both
   deliberate and both narrow: `--dry-run` (it writes nothing, and
   diagnosing a problem during the window is exactly when you want it)
   and `restore` (the L28 rollback path — a recovery must not be locked
   out for an hour, and it is a human action, not a scheduled one).
   Every write also STAMPS its session into `vault_writes.session`.
"""

import functools
import os
import re
import tempfile
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from difflib import unified_diff
from pathlib import Path
from typing import Callable, Optional

from loguru import logger

from cobalt.session import (
    Session,
    SessionClock,
    assert_writable,
    note_ungated,
    session_clock,
)
from cobalt.session import clock as session_clock_mod
from cobalt.vault import (
    PROD_VAULT_PATH_REFERENCE,
    VaultWriteRefused,
    assert_within_vault,
    is_production,
    is_repo_owned,
)

from .markers import (
    MarkerError,
    SectionBlock,
    all_sections,
    find_section,
    render_section,
    render_unit,
    unit_open,
    validate_name,
)
from .frontmatter import frontmatter_span
from .merge import Override, merge3
from cobalt import obsidian

from .store import VaultWriteStore, sha256_text

__all__ = [
    "AT_END",
    "NoteChangedOnDisk",
    "Placement",
    "VaultWriteError",
    "VaultWriter",
    "WriteResult",
    "after_pattern",
    "assert_write_target",
    "wrap_span",
]


class VaultWriteError(RuntimeError):
    """A vault write could not be performed — refuse, never guess."""


@dataclass(frozen=True)
class _MergeBase:
    """What `merge3` should use as its `base`, and why. See
    `VaultWriter._merge_base`."""

    text: Optional[str]
    missing: bool
    #: The earlier `vault_writes.id` whose output came back on disk. Set
    #: only on a recognised SYNC REVERT; recorded on the write row.
    sync_revert_of: Optional[int] = None
    #: The line that goes into `WriteResult.notes`, so the decision is
    #: visible in the run's own report and not only in the log.
    note: Optional[str] = None


class NoteChangedOnDisk(RuntimeError):
    """The note changed between the read this edit was computed from and
    the moment of the rename. Someone else (Obsidian's editor buffer is
    the prime suspect — it destroyed data twice on 2026-09-02/03) wrote
    in the gap. Abort loudly, re-read, retry once."""


# ---------------------------------------------------------------------------
# Placement: where a section goes the FIRST time it is written
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Placement:
    """Locates the line span a not-yet-existing section should occupy.

    `locate` returns `(start, end)` line indices, or None if the anchor
    isn't in this note. `start == end` is a pure insertion (nothing
    existing is touched at all). `start < end` WRAPS those lines: they
    become the new unit's seed body, so a table Cobalt is about to fill
    keeps every cell the human already typed.

    L28's default when there is no anchor, or the anchor is missing, is
    "append at the end; nothing above it is touched".
    """

    describe: str
    locate: Callable[[list[str]], Optional[tuple[int, int]]]


AT_END = Placement("end of note", lambda lines: (len(lines), len(lines)))


def after_pattern(pattern: re.Pattern, describe: str) -> Placement:
    """Insert immediately after the first line matching `pattern`."""

    def locate(lines: list[str]) -> Optional[tuple[int, int]]:
        for i, line in enumerate(lines):
            if pattern.match(line):
                return (i + 1, i + 1)
        return None

    return Placement(describe, locate)


def wrap_span(locate: Callable[[list[str]], Optional[tuple[int, int]]], describe: str) -> Placement:
    """Wrap an existing span of lines — they become the unit's seed body."""
    return Placement(describe, locate)


# ---------------------------------------------------------------------------
# Safety fences
# ---------------------------------------------------------------------------


def assert_write_target(path: Path) -> None:
    """Refuse a target in the repo, and refuse the WRONG vault.

    The production vault is reachable only from a process that declared
    itself production (`COBALT_ENV=production`), and a process that made
    that declaration may write nowhere else. Both directions fail loud —
    a write never resolves silently into either vault (af83c6f's guard,
    applied to the resolved TARGET, not just to the vault root, because
    callers can and do pass paths directly).

    ONE CARVE-OUT, DECLARED IN CONFIG-FREE CODE: a path inside
    `cobalt.vault.REPO_OWNED_ROOTS` (today: `docs/40 - DevDocs/reports/`)
    is allowed and skips both vault questions, because neither applies
    to it — it is not in a vault, so it cannot be in the wrong one. The
    generated seat-usage report lives there and still comes through this
    writer for the MERGE (its human cells) and the audit row, not for
    the guards. Everything else inside the repo is refused exactly as
    before; the carve-out is a fixed tuple in the code, so a caller
    cannot widen it by passing an argument.
    """
    resolved = Path(path).expanduser().resolve()
    if is_repo_owned(resolved):
        return
    assert_within_vault(resolved)  # never inside the repo working tree

    prod_root = Path(PROD_VAULT_PATH_REFERENCE).expanduser().resolve()
    try:
        resolved.relative_to(prod_root)
        under_prod = True
    except ValueError:
        under_prod = False

    if under_prod and not is_production():
        raise VaultWriteRefused(
            f"REFUSED: write target {resolved} is inside the PRODUCTION vault "
            f"({prod_root}) but this process did not declare COBALT_ENV=production. "
            "Set it explicitly on the process that is meant to write live notes; "
            "there is no implicit fallback."
        )
    if is_production() and not under_prod:
        raise VaultWriteRefused(
            f"REFUSED: COBALT_ENV=production but the write target {resolved} is "
            f"outside the production vault ({prod_root}). A production process "
            "writes only to the production vault — this one is misconfigured or "
            "stale and needs a restart."
        )


# ---------------------------------------------------------------------------
# Snapshot + result types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Snapshot:
    """What the file looked like when this edit was computed from it."""

    exists: bool
    text: Optional[str]
    sha256: Optional[str]
    mtime_ns: Optional[int]

    @property
    def lines(self) -> list[str]:
        return (self.text or "").split("\n")


@dataclass
class WriteResult:
    path: Path
    action: str  # created | updated | unchanged | skipped_exists | skipped | restored
    section: Optional[str] = None
    unit: Optional[str] = None
    diff: str = ""
    dry_run: bool = False
    write_id: Optional[int] = None
    overrides: list[Override] = field(default_factory=list)
    hash_before: Optional[str] = None
    hash_after: Optional[str] = None
    baseline_missing: bool = False
    notes: list[str] = field(default_factory=list)
    # RULING 6.3d: conditions that make a SUCCESSFUL write untrustworthy.
    # Today the only member is "Obsidian is not running, so these bytes
    # will not sync" — the exact failure that made prefill's correct
    # 05:15 write on 2026-09-04 invisible. Printed as ERROR, never NOTE.
    errors: list[str] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return self.hash_before != self.hash_after

    def report(self) -> str:
        """The run-report line for this write, diff included (L28.4)."""
        head = f"[{'DRY-RUN' if self.dry_run else 'WRITE'}] {self.action}: {self.path}"
        if self.section:
            head += f" · section={self.section}"
        if self.unit:
            head += f" · unit={self.unit}"
        if self.write_id is not None:
            head += f" · write_id={self.write_id}"
        parts = [head]
        for err in self.errors:
            parts.append(f"  ERROR: {err}")
        for note in self.notes:
            parts.append(f"  NOTE: {note}")
        if self.baseline_missing:
            parts.append(
                "  NOTE: no baseline on record for this unit (never written, or "
                "purged past 30-day retention) — merged against the on-disk body."
            )
        for ov in self.overrides:
            parts.append(f"  OVERRIDE: {ov.describe()}")
        parts.append(self.diff if self.diff else "  (no diff — nothing changed)")
        return "\n".join(parts)


# ---------------------------------------------------------------------------
# The writer
# ---------------------------------------------------------------------------


def _snapshot(path: Path) -> Snapshot:
    if not path.exists():
        return Snapshot(exists=False, text=None, sha256=None, mtime_ns=None)
    text = path.read_text(encoding="utf-8")
    return Snapshot(
        exists=True,
        text=text,
        sha256=sha256_text(text),
        mtime_ns=path.stat().st_mtime_ns,
    )


def _unified(path: Path, before: Optional[str], after: str) -> str:
    diff = unified_diff(
        (before or "").splitlines(),
        after.splitlines(),
        fromfile=f"{path} (before)",
        tofile=f"{path} (after)",
        lineterm="",
    )
    return "\n".join(diff)


def _ensure_trailing_newline(text: str) -> str:
    return text if text.endswith("\n") else text + "\n"


# Actions that put (or would put) bytes on disk. "unchanged", "skipped"
# and "skipped_exists" wrote nothing, so an absent Obsidian is irrelevant
# to them and must not raise a false alarm.
_BYTES_ACTIONS = frozenset({"created", "updated", "restored"})


def _reports_sync_status(method):
    """Annotate every WriteResult a public writer method returns with the
    Obsidian-sync condition (RULING 6.3d). Applied at the four public
    entry points rather than the ten `return WriteResult(...)` sites, so
    a future return site cannot forget it."""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self._annotate_sync(result)
        return result

    return wrapper


class VaultWriter:
    """One instance per run. `run_id` ties every row this run wrote
    together in `vault_writes`."""

    def __init__(
        self,
        writer: str,
        *,
        store: Optional[VaultWriteStore] = None,
        run_id: Optional[str] = None,
        dry_run: bool = False,
        precommit_hook: Optional[Callable[[Path], None]] = None,
        clock: Optional[SessionClock] = None,
        now: Optional[Callable[[], "datetime"]] = None,
    ):
        self.writer = writer
        self.run_id = run_id or uuid.uuid4().hex[:12]
        self.dry_run = dry_run
        self.store = store
        # F1 seam: tests freeze time by passing `now`; nothing in
        # production passes either of these. `session_clock()` is
        # lru_cached, so this costs one config read per process.
        self.clock = clock or session_clock()
        self._now = now or session_clock_mod.now_utc
        # Test seam ONLY: called after the guard read and before the
        # rename, so a test can simulate a concurrent writer landing in
        # the gap. Never set in production code.
        self._precommit_hook = precommit_hook
        self._purged = False

    # -- plumbing ----------------------------------------------------

    def _require_store(self) -> VaultWriteStore:
        if self.store is None:
            raise VaultWriteError(
                "No vault_writes store configured — L28.3 requires every write "
                "to be persisted before it lands. Refusing to write blind."
            )
        return self.store

    def _session_gate(self, action: str, path: Path) -> Session:
        """LAW L28.6 / Charter F1: refuse a write inside `market_reset`.

        Returns the session so the caller can stamp it on the audit row —
        the SAME resolution that made the allow/refuse decision, so a row
        can never claim a session the gate did not see.

        A dry run is not gated: it writes nothing, and `--dry-run` during
        the window is how you find out what a job WOULD have done.
        """
        session = self.clock.session(self._now())
        if self.dry_run:
            return session
        if is_repo_owned(Path(path)):
            # F1 GUARDS THE VAULT, NOT THE REPO. The market_reset window
            # exists because 20:00-21:00 ET is when the trading day's
            # notes are being reset and a Cobalt write into them races a
            # human one. A generated report in the repo has no human
            # editing it at 20:30, is not synced to any device, and is
            # reviewed in a git diff — refusing it would take the 20:00
            # and 21:00 runs of an hourly job out every single night,
            # fail them, and paint F18 red for the guard doing something
            # it was never asked to do.
            return session
        return assert_writable(
            f"vaultwrite:{self.writer}:{action}",
            target=str(path),
            now=self._now(),
            clock=self.clock,
        )

    def _current_session(self) -> Session:
        """The session to stamp on an audit row when no gate ran (dry
        run, or `restore`'s carve-out)."""
        return self.clock.session(self._now())

    def _annotate_sync(self, result: WriteResult) -> None:
        """RULING 6.3d. Bytes that land in the vault while no Obsidian
        process is running do not reach Sync, do not reach Dejan's other
        devices, and — as 2026-09-04 proved — can be silently overwritten
        by whichever device DOES have Obsidian open. The write succeeded;
        its delivery did not. That is an ERROR line, not a note, and the
        heartbeat reads the same probe so the two can never disagree."""
        if result.action not in _BYTES_ACTIONS:
            return
        try:
            running, message = obsidian.sync_status()
        except obsidian.ObsidianProbeError as e:
            # "the probe broke" is NOT "Obsidian is down" — say which.
            detail = f"Obsidian probe FAILED — sync state UNKNOWN: {e}"
            result.errors.append(detail)
            logger.error(f"{result.path}: {detail}")
            return
        if not running:
            result.errors.append(message)
            logger.error(f"{result.path}: {message}")

    def _purge_once(self) -> None:
        """Retention is the writer's own job (L28.3) — one purge per run.
        A dry run purges nothing: --dry-run writes NOTHING, DB included."""
        if self._purged or self.store is None or self.dry_run:
            return
        self._purged = True
        try:
            removed = self.store.purge_expired()
            if removed:
                logger.info(f"vault_writes: purged {removed} row(s) past 30-day retention")
        except Exception as e:  # never let housekeeping block a write
            logger.error(f"vault_writes purge FAILED (write continues): {type(e).__name__}: {e}")

    def _commit(self, path: Path, snapshot: Snapshot, new_text: str) -> None:
        """Guarded atomic write: re-verify the file still matches the
        snapshot this edit was computed from, then tmp+rename in the same
        directory."""
        if self._precommit_hook is not None:
            self._precommit_hook(path)
        current = _snapshot(path)
        if current.sha256 != snapshot.sha256 or current.mtime_ns != snapshot.mtime_ns:
            raise NoteChangedOnDisk(
                f"ABORT: {path} changed on disk between this run's read and its "
                f"write (sha {snapshot.sha256} -> {current.sha256}). Nothing was "
                "written; the on-disk content is untouched."
            )
        fd, tmp_name = tempfile.mkstemp(dir=str(path.parent), prefix=f".{path.name}.", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(new_text)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp_name, path)
        except BaseException:
            Path(tmp_name).unlink(missing_ok=True)
            raise

    def _persist_and_write(
        self,
        path: Path,
        snapshot: Snapshot,
        new_text: str,
        *,
        section: Optional[str],
        unit: Optional[str],
        before_section: Optional[str],
        after_section: Optional[str],
        overrides: list[Override],
        unit_before: Optional[str] = None,
        unit_after: Optional[str] = None,
        sync_revert_of: Optional[int] = None,
        write_file: bool = True,
    ) -> int:
        store = self._require_store()
        override_rows = [
            {
                "cobalt_text": "\n".join(ov.base),
                "human_text": "\n".join(ov.human),
                "attempted_text": "\n".join(ov.cobalt),
                "conflict": ov.conflict,
            }
            for ov in overrides
        ]
        with store.pending_write(
            note=str(path),
            section=section,
            unit=unit,
            before=before_section,
            after=after_section,
            unit_before=unit_before,
            unit_after=unit_after,
            sync_revert_of=sync_revert_of,
            hash_before=snapshot.sha256,
            hash_after=sha256_text(new_text),
            writer=self.writer,
            run_id=self.run_id,
            session=self._current_session().value,
            overrides=override_rows,
        ) as write_id:
            # An override-only run advances the baseline without touching
            # the file — identical bytes are never re-written (no pointless
            # mtime churn for Obsidian to notice).
            if write_file and new_text != (snapshot.text or ""):
                self._commit(path, snapshot, new_text)
        return write_id

    def _write_with_retry(self, path: Path, build, *, write_file: bool = True):
        """`build(snapshot)` returns (new_text, kwargs-for-persist) or
        None to mean "nothing to do". Retries exactly once after a loud
        abort (L28.3)."""
        last_error: Optional[NoteChangedOnDisk] = None
        for attempt in (1, 2):
            snapshot = _snapshot(path)
            built = build(snapshot)
            if built is None:
                return None, snapshot
            new_text, kwargs = built
            if self.dry_run:
                return (new_text, kwargs, None), snapshot
            try:
                write_id = self._persist_and_write(
                    path, snapshot, new_text, write_file=write_file, **kwargs
                )
            except NoteChangedOnDisk as e:
                last_error = e
                logger.error(f"{e} (attempt {attempt}/2)")
                if attempt == 2:
                    raise
                continue
            return (new_text, kwargs, write_id), snapshot
        raise last_error  # unreachable; keeps the type checker honest

    # -- API ---------------------------------------------------------

    @_reports_sync_status
    def create_if_absent(self, path: Path, template: str) -> WriteResult:
        """L28.1: write a note whole ONLY when it does not exist. An
        existing file is never rewritten from a template — it is left
        untouched and reported as `skipped_exists`."""
        path = Path(path)
        assert_write_target(path)
        self._session_gate("create_if_absent", path)
        self._purge_once()

        if path.exists():
            snapshot = _snapshot(path)
            return WriteResult(
                path=path,
                action="skipped_exists",
                dry_run=self.dry_run,
                diff="",
                hash_before=snapshot.sha256,
                hash_after=snapshot.sha256,
                notes=["file exists — create-if-absent does not rewrite it (L28.1)"],
            )

        if not path.parent.is_dir():
            raise VaultWriteError(
                f"Target directory missing: {path.parent} — refusing to create "
                "vault structure (folder policy is a Vault Session decision)."
            )

        text = _ensure_trailing_newline(template)
        diff = _unified(path, "", text)
        if self.dry_run:
            return WriteResult(
                path=path,
                action="created",
                diff=diff,
                dry_run=True,
                hash_before=None,
                hash_after=sha256_text(text),
            )

        snapshot = _snapshot(path)
        write_id = self._persist_and_write(
            path,
            snapshot,
            text,
            section=None,
            unit=None,
            before_section=None,
            after_section=text,
            overrides=[],
        )
        # Seed one baseline row per unit the template brought with it, so
        # the first upsert_unit has a real `base` leg to merge against.
        self._seed_baselines(path, text)
        return WriteResult(
            path=path,
            action="created",
            diff=diff,
            write_id=write_id,
            hash_before=None,
            hash_after=sha256_text(text),
        )

    def _seed_baselines(self, path: Path, text: str) -> None:
        store = self._require_store()
        lines = text.split("\n")
        for section in all_sections(lines):
            for unit_id, unit in section.units.items():
                body = "\n".join(unit.body(lines))
                with store.pending_write(
                    note=str(path),
                    section=section.name,
                    unit=unit_id,
                    before=None,
                    after=section.text(lines),
                    unit_before=None,
                    unit_after=body,
                    hash_before=None,
                    hash_after=sha256_text(text),
                    writer=self.writer,
                    run_id=self.run_id,
                    session=self._current_session().value,
                ):
                    pass

    @_reports_sync_status
    def upsert_unit(
        self,
        path: Path,
        section: str,
        unit_id: str,
        body: str,
        *,
        placement: Optional[Placement] = None,
        skip_if: Optional[Callable[[str], bool]] = None,
    ) -> WriteResult:
        """L28.2: write `body` into `section`/`unit_id`, merging.

        Same id -> updated in place. New id -> appended inside the
        section. Missing section -> created at `placement` (default: the
        end of the note; nothing above it is touched). Human text is
        preserved verbatim in position, and a human edit to a Cobalt line
        wins and is recorded as an override.
        """
        path = Path(path)
        assert_write_target(path)
        self._session_gate("upsert_unit", path)
        validate_name(section, "section")
        validate_name(unit_id, "unit")
        self._purge_once()

        if not path.exists():
            raise VaultWriteError(
                f"REFUSED: {path} does not exist. upsert_unit never creates a "
                "note — call create_if_absent() with a template first (L28.1)."
            )

        result_notes: list[str] = []
        state: dict = {}

        def build(snapshot: Snapshot):
            text = snapshot.text or ""
            if skip_if is not None and skip_if(text):
                state["skipped"] = True
                return None
            lines = text.split("\n")
            try:
                sec = find_section(lines, section)
            except MarkerError as e:
                raise VaultWriteError(str(e)) from e

            cobalt_lines = body.split("\n") if body != "" else []
            notes: list[str] = []
            baseline_missing = False

            if sec is None:
                place = placement or AT_END
                span = place.locate(lines)
                if span is None:
                    notes.append(
                        f"anchor not found ({place.describe}) — section appended at "
                        "the end of the note; nothing above it was touched (L28)."
                    )
                    span = AT_END.locate(lines)
                assert span is not None
                start, end = span
                seed = lines[start:end]
                human_body = "\n".join(seed)
                merged = merge3(seed, seed, cobalt_lines)
                new_section_lines = render_section(section, render_unit(unit_id, "\n".join(merged.lines)))
                if start == end and start >= len(lines) and lines and lines[-1].strip():
                    new_section_lines = ["", *new_section_lines]
                new_lines = lines[:start] + new_section_lines + lines[end:]
                before_section = None
                overrides = merged.overrides
            else:
                unit = sec.units.get(unit_id)
                if unit is None:
                    human_body = ""
                    merged = merge3([], [], cobalt_lines)
                    unit_lines = render_unit(unit_id, "\n".join(merged.lines))
                    new_lines = lines[: sec.close_line] + unit_lines + lines[sec.close_line :]
                    notes.append(f"unit {unit_id!r} is new — appended inside section {section!r}")
                else:
                    human_lines = unit.body(lines)
                    human_body = "\n".join(human_lines)
                    base = self._merge_base(path, section, unit_id, human_body)
                    if base.missing:
                        baseline_missing = True
                        base_lines = list(human_lines)
                    else:
                        base_lines = base.text.split("\n") if base.text != "" else []
                    if base.note:
                        notes.append(base.note)
                        state["sync_revert_of"] = base.sync_revert_of
                    merged = merge3(base_lines, human_lines, cobalt_lines)
                    unit_lines = render_unit(unit_id, "\n".join(merged.lines))
                    new_lines = (
                        lines[: unit.open_line] + unit_lines + lines[unit.close_line + 1 :]
                    )
                before_section = sec.text(lines)
                overrides = merged.overrides

            new_text = _ensure_trailing_newline("\n".join(new_lines))
            after_sec = find_section(new_text.split("\n"), section)
            after_section = after_sec.text(new_text.split("\n")) if after_sec else None

            merged_body = "\n".join(merged.lines)
            state.update(
                {
                    "overrides": overrides,
                    "baseline_missing": baseline_missing,
                    "merged_body": merged_body,
                }
            )
            result_notes.clear()
            result_notes.extend(notes)

            if new_text == text and not overrides:
                state["unchanged"] = True
                return None

            return new_text, {
                "section": section,
                "unit": unit_id,
                "before_section": before_section,
                "after_section": after_section,
                "unit_before": human_body,
                "unit_after": merged_body,
                "sync_revert_of": state.get("sync_revert_of"),
                "overrides": overrides,
            }

        # An override with no textual change still advances the baseline
        # (so it is recorded exactly once) without touching the file.
        outcome, snapshot = self._write_with_retry(path, build, write_file=True)

        if state.get("skipped"):
            return WriteResult(
                path=path, action="skipped", section=section, unit=unit_id,
                dry_run=self.dry_run, hash_before=snapshot.sha256,
                hash_after=snapshot.sha256,
                notes=["skip_if matched — nothing computed, nothing written"],
            )
        if outcome is None:
            return WriteResult(
                path=path, action="unchanged", section=section, unit=unit_id,
                dry_run=self.dry_run, hash_before=snapshot.sha256,
                hash_after=snapshot.sha256, notes=list(result_notes),
                baseline_missing=state.get("baseline_missing", False),
            )

        new_text, _kwargs, write_id = outcome
        changed = new_text != (snapshot.text or "")
        return WriteResult(
            path=path,
            action="updated" if changed else "unchanged",
            section=section,
            unit=unit_id,
            diff=_unified(path, snapshot.text, new_text),
            dry_run=self.dry_run,
            write_id=write_id,
            overrides=state.get("overrides", []),
            hash_before=snapshot.sha256,
            hash_after=sha256_text(new_text),
            baseline_missing=state.get("baseline_missing", False),
            notes=list(result_notes),
        )

    def _baseline(self, path: Path, section: str, unit_id: str) -> Optional[str]:
        if self.store is None:
            return None
        return self.store.last_after(str(path), section, unit_id)

    #: How far back a body is still recognised as one Cobalt wrote here.
    #: See `VaultWriteStore.recent_afters` — a recognition window, not a
    #: search of the history.
    SYNC_REVERT_WINDOW = 10

    def _merge_base(
        self, path: Path, section: str, unit_id: str, human_body: str
    ) -> "_MergeBase":
        """The `base` leg of the three-way merge, and WHY it is that.

        THE ONE PLACE EITHER WRITE PATH DECIDES THIS. `upsert_unit` and
        `upsert_region` both call it before `merge3`, because the bug it
        exists for is a property of the merge and not of the marker
        shape, and two copies of this reasoning would be one copy too
        many (one-path rule).

        Ordinarily the base is `last_after` — what Cobalt wrote here last
        — and anything else on disk is the human's, which wins.

        THE EXCEPTION, and it cost an hour and forty minutes on
        2026-09-09. The daily note's `heartbeat` unit was stuck on the
        05:54 GREEN block from 06:25 to 08:05. The 06:09 and 06:24 beats
        wrote RED; at 06:25:54 Obsidian Sync carried a stale copy up from
        another device and put the 05:54 text back. Every beat after that
        saw on-disk != baseline, concluded "a human edited this", let the
        human win, and wrote overrides 30-34. Cobalt could not update its
        own status block, and the audit trail said a person had insisted
        on it five times.

        A HUMAN EDIT IS NEW TEXT; A SYNC REVERT IS OLD TEXT COMING BACK,
        and that difference is already recorded — the reverted body is
        byte-identical to something this unit's own history contains. So
        when the on-disk body does not match the baseline but DOES match
        a recent `unit_after`, the base becomes the on-disk text: Cobalt's
        new text then wins cleanly, exactly as it would have if the sync
        had never happened, and no override is recorded because none
        occurred.

        THE FALSE POSITIVE IS ACKNOWLEDGED AND NARROW: a human who
        hand-types a byte-identical copy of one of the last ten things
        Cobalt wrote into this unit is treated as a sync. That is
        indistinguishable in principle — the bytes are the only evidence
        there is — and the reverse mistake is the one that actually
        happened and actually cost something.
        """
        base_text = self._baseline(path, section, unit_id)
        if base_text is None:
            return _MergeBase(text=None, missing=True)
        if human_body == base_text or self.store is None:
            return _MergeBase(text=base_text, missing=False)

        for write_id, after in self.store.recent_afters(
            str(path), section, unit_id, limit=self.SYNC_REVERT_WINDOW
        ):
            if after != human_body:
                continue
            row = self.store.get_write(write_id)
            when = row["ts"] if row else None
            note = (
                f"SYNC REVERT: the text on disk is byte-identical to vault_writes "
                f"id {write_id}"
                + (f" ({when:%Y-%m-%d %H:%M:%S})" if when else "")
                + " — an earlier Cobalt write coming back, not a human edit. "
                "Cobalt's new text wins cleanly; no override recorded."
            )
            logger.warning(
                "vaultwrite: SYNC REVERT in {} [{}/{}] — on-disk body matches "
                "vault_writes id {} ({}). Obsidian Sync is the usual cause. "
                "Taking the on-disk text as the merge base; NOT recording an "
                "override.",
                path,
                section,
                unit_id,
                write_id,
                when,
            )
            return _MergeBase(
                text=human_body, missing=False, sync_revert_of=write_id, note=note
            )

        return _MergeBase(text=base_text, missing=False)

    @_reports_sync_status
    def upsert_region(
        self,
        path: Path,
        section_label: str,
        region_id: str,
        body: str,
        *,
        locate: Callable[[list[str]], Optional[tuple[int, int]]],
    ) -> WriteResult:
        """The ONE marker-less variant, and the ONE place it is legal.

        Obsidian requires YAML frontmatter to be the very first bytes of
        a file: an HTML comment above `---` stops it being frontmatter at
        all, and a comment INSIDE it stops it being YAML. A trade note's
        frontmatter therefore cannot carry markers, so its region is
        located structurally (`locate`) instead of by marker.

        Everything else L28 asks for still applies, unchanged: the same
        three-way merge (human text wins and is recorded as an override),
        the same mtime+hash guard, the same atomic tmp+rename, the same
        before/after + full-file hashes in `vault_writes`, the same
        unified diff, the same dry-run, and the same rollback through
        `restore`. Do NOT reach for this anywhere a marker would work —
        `upsert_unit` is the write path; this is the frontmatter carve-out.
        """
        path = Path(path)
        assert_write_target(path)
        self._session_gate("upsert_region", path)
        self._purge_once()
        if not path.exists():
            raise VaultWriteError(
                f"REFUSED: {path} does not exist. upsert_region never creates a "
                "note — call create_if_absent() first (L28.1)."
            )

        state: dict = {}

        def build(snapshot: Snapshot):
            text = snapshot.text or ""
            lines = text.split("\n")
            span = locate(lines)
            if span is None:
                raise VaultWriteError(
                    f"REFUSED: could not locate the {region_id!r} region in {path} — "
                    "refusing to guess where it starts and ends."
                )
            start, end = span
            human_lines = lines[start:end]
            base = self._merge_base(
                path, section_label, region_id, "\n".join(human_lines)
            )
            baseline_missing = base.missing
            base_lines = list(human_lines) if base.missing else (
                base.text.split("\n") if base.text != "" else []
            )
            cobalt_lines = body.split("\n") if body != "" else []
            merged = merge3(base_lines, human_lines, cobalt_lines)
            new_lines = lines[:start] + merged.lines + lines[end:]
            new_text = _ensure_trailing_newline("\n".join(new_lines))

            state.update({
                "overrides": merged.overrides,
                "baseline_missing": baseline_missing,
                "sync_revert_of": base.sync_revert_of,
                "sync_note": base.note,
            })
            if new_text == text and not merged.overrides:
                return None
            return new_text, {
                "section": section_label,
                "unit": region_id,
                "before_section": "\n".join(human_lines),
                "after_section": "\n".join(merged.lines),
                "unit_before": "\n".join(human_lines),
                "unit_after": "\n".join(merged.lines),
                "sync_revert_of": base.sync_revert_of,
                "overrides": merged.overrides,
            }

        outcome, snapshot = self._write_with_retry(path, build)
        if outcome is None:
            return WriteResult(
                path=path, action="unchanged", section=section_label, unit=region_id,
                dry_run=self.dry_run, hash_before=snapshot.sha256, hash_after=snapshot.sha256,
                baseline_missing=state.get("baseline_missing", False),
                notes=[n for n in [state.get("sync_note")] if n],
            )
        new_text, _kwargs, write_id = outcome
        changed = new_text != (snapshot.text or "")
        return WriteResult(
            path=path,
            action="updated" if changed else "unchanged",
            section=section_label,
            unit=region_id,
            diff=_unified(path, snapshot.text, new_text),
            dry_run=self.dry_run,
            write_id=write_id,
            overrides=state.get("overrides", []),
            hash_before=snapshot.sha256,
            hash_after=sha256_text(new_text),
            baseline_missing=state.get("baseline_missing", False),
            notes=[n for n in [state.get("sync_note")] if n],
        )

    # -- rollback ----------------------------------------------------

    @staticmethod
    def _locate_region(lines: list[str], row: dict) -> tuple[int, int]:
        """Where the MARKER-LESS region this row wrote lives now.

        `upsert_region` is the one write path whose target is located by
        a callable rather than by a marker, and a Python callable cannot
        be persisted — so `restore` cannot re-run the locator that made
        the write. Until 2026-09-09 it did not try: it looked for a
        section marker, found none (frontmatter cannot carry one — see
        vaultwrite/frontmatter.py) and refused. 102 of the ADR-0008
        sprint's vault writes were frontmatter, and a restic snapshot was
        their only rollback.

        Two ways in, in this order, and both are evidence rather than
        inference:

        1. **Structurally**, for the one region shape that HAS a
           structure: `frontmatter_span`. Used when the block it finds
           still holds exactly the bytes this row wrote.
        2. **By content.** `unit_after` IS the text the write left on
           disk, verbatim; a single contiguous run of lines equal to it
           is where the region is. This covers every other `locate`
           shape (the seat-usage report's human cells, and anything
           added later) without a registry of locators to keep in step.

        FAIL LOUD ON ANYTHING ELSE. Zero matches means the region has
        been rewritten since — by a human, or by a later Cobalt write —
        and restoring an old block over it would delete work nobody
        asked to lose. More than one match means the anchor is ambiguous.
        Neither is a case for guessing.
        """
        after = row["unit_after"]
        if after is None:
            raise VaultWriteError(
                f"vault_writes id {row['id']} has no `unit_after` — there is no "
                "record of what this write left on disk, so its region cannot be "
                "located. Refusing."
            )
        after_lines = after.split("\n")

        span = frontmatter_span(lines)
        if span is not None and lines[span[0] : span[1]] == after_lines:
            return span

        n = len(after_lines)
        matches = [
            i for i in range(0, len(lines) - n + 1) if lines[i : i + n] == after_lines
        ]
        if len(matches) == 1:
            return (matches[0], matches[0] + n)
        if not matches:
            raise VaultWriteError(
                f"REFUSED: the marker-less region {row['unit']!r} written by "
                f"vault_writes id {row['id']} is no longer on disk as it was "
                f"written — {row['note']} has changed since. Restoring would "
                "overwrite whatever replaced it. Refusing to guess where it "
                "started and ended."
            )
        raise VaultWriteError(
            f"REFUSED: the text vault_writes id {row['id']} wrote appears "
            f"{len(matches)} times in {row['note']} — the anchor is ambiguous "
            "and a marker-less region has nothing else to locate it by."
        )

    @_reports_sync_status
    def restore(self, write_id: int) -> WriteResult:
        """L28: `cobalt vault restore --write-id N` — put that write back,
        through this same writer (guard, atomic write, its own audit row).

        THREE PATHS, and which one runs is decided by the row, not by a
        flag (2026-09-09, closing ESCALATE items 1 and 2 of the ADR-0008
        report):

        * **a unit row** (`unit` set, `unit_before` not null) — only that
          unit's body is put back, located by its own stable-id marker
          INSIDE the section. Until today this restored the whole
          section from `before`, which silently dropped every sibling
          unit written after the one being undone: the daily note has a
          `heartbeat` unit and a `rules` unit in one section, and rolling
          back a heartbeat write took the morning's rules with it. A
          per-write rollback that cannot be used on any note with two
          units is not a rollback.

          If the write CREATED the unit — its open marker is absent from
          the recorded before-section — the unit is REMOVED rather than
          emptied. Leaving a marker pair around nothing would be a
          Cobalt-owned artifact that the before-state did not have.

        * **a region row** (no section marker in the file) — the
          marker-less `upsert_region` carve-out, restored byte-exact from
          `unit_before` into the span `_locate_region` finds.

        * **a legacy section row** (`unit` null, or `unit_before` null) —
          the original whole-section replace, unchanged. Rows written
          before this change carry no `unit_before` for their unit, and
          the honest thing to do with them is what was always done.
        """
        store = self._require_store()
        row = store.get_write(write_id)
        if row is None:
            raise VaultWriteError(f"No vault_writes row with id {write_id}.")
        if not row["section"]:
            raise VaultWriteError(
                f"vault_writes id {write_id} is a whole-file create (no section) — "
                "there is no before-state to restore. Refusing."
            )
        if row["before"] is None:
            raise VaultWriteError(
                f"vault_writes id {write_id} created section {row['section']!r} "
                "(before-state is NULL) — restoring would mean deleting a section. "
                "Refusing; that is a manual decision."
            )

        path = Path(row["note"])
        assert_write_target(path)
        # NO session gate here, on purpose (L28.6 carve-out). `restore` is
        # the rollback path and a human action; locking recovery out for
        # the 20:00-21:00 window would mean the one hour you most want to
        # undo a bad write is the one hour you cannot. The write is still
        # audited and still stamps the session it happened in.
        #
        # RULED 2026-09-04 (S1-P3): the carve-out costs one loud line and
        # a row in the counter F18 shows. Outside the window this is a
        # no-op. Inside it, a rollback can never be a quiet one.
        note_ungated(
            f"vaultwrite:{self.writer}:restore",
            target=str(path),
            why=f"restoring vault_writes id {write_id} is the rollback path — the "
                "one hour you most want to undo a bad write must not be the one "
                "hour you cannot",
            now=self._now(),
            clock=self.clock,
        )
        self._purge_once()
        if not path.exists():
            raise VaultWriteError(f"REFUSED: {path} no longer exists — nothing to restore into.")

        section_name = row["section"]
        before_state = row["before"]
        unit_id = row["unit"]
        unit_before = row["unit_before"]
        #: A unit row can be put back on its own. A row with no unit, or
        #: one written before `unit_before` was recorded, cannot — and
        #: gets the original whole-section behaviour rather than a guess.
        per_unit = bool(unit_id) and unit_before is not None

        def build(snapshot: Snapshot):
            lines = (snapshot.text or "").split("\n")
            sec: Optional[SectionBlock] = find_section(lines, section_name)

            if sec is None:
                # THE MARKER-LESS CARVE-OUT. `upsert_region` writes into a
                # span located by a callable — frontmatter has no marker
                # and cannot have one — so there is no section to find,
                # and until 2026-09-09 this was where the refusal came
                # from. See `_locate_region`.
                if not per_unit:
                    raise VaultWriteError(
                        f"REFUSED: section {section_name!r} is not in {path} any "
                        "more — refusing to guess where to put the restored text."
                    )
                start, end = self._locate_region(lines, row)
                current_region = "\n".join(lines[start:end])
                restored = unit_before.split("\n") if unit_before != "" else []
                new_lines = lines[:start] + restored + lines[end:]
                new_text = _ensure_trailing_newline("\n".join(new_lines))
                if new_text == (snapshot.text or ""):
                    return None
                return new_text, {
                    "section": section_name,
                    "unit": unit_id,
                    "before_section": current_region,
                    "after_section": unit_before,
                    "unit_before": current_region,
                    "unit_after": unit_before,
                    "overrides": [],
                }

            if per_unit:
                unit = sec.units.get(unit_id)
                if unit is None:
                    raise VaultWriteError(
                        f"REFUSED: unit {unit_id!r} is not in section "
                        f"{section_name!r} of {path} any more — refusing to guess "
                        "where to put the restored text. (The whole section is "
                        "still recoverable from this row's `before` by hand.)"
                    )
                # Did this write CREATE the unit? The recorded
                # before-section is the evidence: if the unit's own open
                # marker is not in it, the unit did not exist, and putting
                # back an empty body would leave a Cobalt marker pair the
                # before-state never had.
                created_it = unit_open(unit_id) not in before_state
                current_unit = "\n".join(unit.body(lines))
                if created_it:
                    new_lines = lines[: unit.open_line] + lines[unit.close_line + 1 :]
                else:
                    new_lines = (
                        lines[: unit.open_line]
                        + render_unit(unit_id, unit_before)
                        + lines[unit.close_line + 1 :]
                    )
                new_text = _ensure_trailing_newline("\n".join(new_lines))
                if new_text == (snapshot.text or ""):
                    return None
                after_sec = find_section(new_text.split("\n"), section_name)
                return new_text, {
                    "section": section_name,
                    "unit": unit_id,
                    "before_section": sec.text(lines),
                    "after_section": (
                        after_sec.text(new_text.split("\n")) if after_sec else None
                    ),
                    # The restored body becomes the next merge's baseline,
                    # so the following ordinary write merges against what
                    # is on disk rather than against the version it undid.
                    "unit_before": current_unit,
                    "unit_after": None if created_it else unit_before,
                    "overrides": [],
                }

            current_section = sec.text(lines)
            new_lines = lines[: sec.open_line] + before_state.split("\n") + lines[sec.close_line + 1 :]
            new_text = _ensure_trailing_newline("\n".join(new_lines))
            if new_text == (snapshot.text or ""):
                return None
            # The restored section becomes the new baseline for its units,
            # so the next ordinary write merges against what is actually
            # on disk rather than against the version it just undid.
            restored_lines = new_text.split("\n")
            restored_sec = find_section(restored_lines, section_name)
            restored_unit = (
                restored_sec.units.get(row["unit"]) if restored_sec and row["unit"] else None
            )
            return new_text, {
                "section": section_name,
                "unit": row["unit"],
                "before_section": current_section,
                "after_section": before_state,
                "unit_before": None,
                "unit_after": (
                    "\n".join(restored_unit.body(restored_lines)) if restored_unit else None
                ),
                "overrides": [],
            }

        saved_writer = self.writer
        self.writer = f"vault.restore<-{saved_writer}"
        try:
            outcome, snapshot = self._write_with_retry(path, build)
        finally:
            self.writer = saved_writer

        if outcome is None:
            return WriteResult(
                path=path, action="unchanged", section=section_name, unit=row["unit"],
                dry_run=self.dry_run, hash_before=snapshot.sha256, hash_after=snapshot.sha256,
                notes=[f"section {section_name!r} already matches vault_writes id {write_id}"],
            )
        new_text, _kwargs, new_write_id = outcome
        return WriteResult(
            path=path,
            action="restored",
            section=section_name,
            unit=row["unit"],
            diff=_unified(path, snapshot.text, new_text),
            dry_run=self.dry_run,
            write_id=new_write_id,
            hash_before=snapshot.sha256,
            hash_after=sha256_text(new_text),
            notes=[f"restored section {section_name!r} to vault_writes id {write_id} before-state"],
        )
