"""`cobalt taxonomy …` — the vault-backed trade_def commands.

    cobalt taxonomy load                   [--dry-run]
    cobalt taxonomy migrate-strategy-notes --dry-run | --apply [--note SLUG]
    cobalt taxonomy migrate-trade-notes    --dry-run | --apply [--note PATH]
    cobalt taxonomy add-alias SLUG "ALIAS"
    cobalt taxonomy sync-frontmatter       --dry-run | --apply

`load` moves a trader's strategy notes into `"user".trade_defs`.
`migrate-strategy-notes` is the ONE-OFF that puts the 22 notes into the
ADR-0008 D3 shape. `sync-frontmatter` (ruling d) re-derives `class` and
`family` from the loaded units and writes only where they differ — it is
what the loader's frontmatter warnings point at.

`--dry-run` FIRST, ALWAYS, IN THE OPERATOR'S HEAD. `load`'s sync is a
replace: a slug that has left the vault has its row deleted (and its
per-trade tunables with it, by cascade). That is the correct semantics —
a def removed from a note is a def gone from the system — but it is not a
semantics anyone should discover from a row count afterwards. For the two
writing commands there is no default at all: pass `--dry-run` or
`--apply`, because one of them puts bytes in the vault.

EVERY vault write goes through `VaultWriter` and nothing else (L28):
marker-bounded, three-way merged, mtime+hash guarded, atomic, audited in
`vault_writes`, and undoable with `cobalt vault restore --write-id`.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from cobalt.vaultwrite import VaultWriter, VaultWriteStore
from cobalt.vaultwrite.frontmatter import frontmatter_span
from cobalt.vaultwrite.markers import find_section

from .note_migration import (
    FRONTMATTER_REGION,
    FRONTMATTER_SECTION,
    add_alias_to_unit,
    apply_plans,
    edit_frontmatter,
    migrate_strategy_template,
    parse_key_aliases,
    parse_matrix_aliases,
    plan_notes,
    unclaimed_matrix_keys,
    write_tunables_yaml,
)
from .store import TradeDefStore
from .trade_note_migration import (
    apply_trade_notes,
    migrate_trade_template,
    build_alias_index,
    plan_trade_notes,
)
from .validate import print_result
from .vault_loader import load_vault_trade_defs


def _require_mode(args: argparse.Namespace, command: str) -> bool:
    """`--dry-run` or `--apply`, never a default. Returns dry_run."""
    if bool(args.dry_run) == bool(args.apply):
        raise SystemExit(
            f"cobalt taxonomy {command}: pass exactly one of --dry-run or --apply. "
            "There is no default: one of them writes to the vault."
        )
    return bool(args.dry_run)


# ---------------------------------------------------------------------
# load
# ---------------------------------------------------------------------


def cmd_load(args: argparse.Namespace) -> None:
    result = load_vault_trade_defs()
    print_result(result)

    if args.dry_run:
        print(
            f"\nDRY RUN — nothing written. {len(result.defs)} def(s) and "
            f"{len(result.user_tunables)} tunable row(s) would be synced into "
            '"user".trade_defs / "user".tunables. Re-run without --dry-run to apply.'
        )
        return

    store = TradeDefStore()
    store.ensure_schema()
    before = set(store.slugs())
    counts = store.sync(result)
    print("\nsynced:")
    print(counts.report())
    added = sorted({d.slug for d in result.defs} - before)
    if added:
        print(f"  new slugs: {added}")
    print(f"  setup_trade_matrix now has {len(store.matrix())} row(s).")


# ---------------------------------------------------------------------
# migrate-strategy-notes  (one-off, ADR-0008 D3)
# ---------------------------------------------------------------------


def cmd_migrate_strategy_notes(args: argparse.Namespace) -> None:
    dry_run = _require_mode(args, "migrate-strategy-notes")
    aliases = parse_matrix_aliases(args.matrix_alias)
    tunable_aliases = parse_key_aliases(args.tunable_alias, flag="tunable-alias")
    plans, lift = plan_notes(
        only_slug=args.note,
        matrix_aliases=aliases,
        tunable_aliases=tunable_aliases,
    )
    if not plans:
        raise SystemExit(f"no strategy note matches --note {args.note!r}")

    print(
        "cobalt taxonomy migrate-strategy-notes — "
        f"{'DRY RUN' if dry_run else 'APPLY'} on {len(plans)} note(s)\n"
    )

    outcomes = apply_plans(plans, dry_run=dry_run)
    for outcome in outcomes:
        print(f"=== {outcome.slug}  ({outcome.path.name})")
        if outcome.md5:
            print(f"    def content UNCHANGED — canonical md5 {outcome.md5}")
        for note in outcome.notes:
            print(f"    NOTE: {note}")
        for warning in outcome.warnings:
            print(f"    WARNING: {warning}")
        for kind in ("frontmatter", "def", "tunables"):
            if kind not in outcome.actions:
                continue
            wid = outcome.write_ids.get(kind)
            print(
                f"    [{kind}] {outcome.actions[kind]}"
                + (f" · write_id={wid}" if wid is not None else "")
            )
            if outcome.diffs.get(kind):
                print(outcome.diffs[kind])
        print()

    # tunables.yaml only moves when the whole corpus moves: a partial run
    # would leave rows in the file that a note already claims.
    if args.note is None:
        diff = write_tunables_yaml(lift, dry_run=dry_run)
        print("=== configs/cobalt/taxonomy/tunables.yaml")
        for line in lift.notes:
            print(f"    NOTE: {line}")
        for line in lift.rekeyed:
            print(f"    NOTE: re-keyed {line}")
        print(diff or "    (no change)")
    else:
        print(
            "=== configs/cobalt/taxonomy/tunables.yaml — NOT touched (--note run). "
            "The rows move only on a full-corpus run."
        )

    if args.note is None:
        _path, template_diff = migrate_strategy_template(dry_run=dry_run)
        print("\n=== 5 - Templates/Strategy.md  (human-tree file, plain edit)")
        print(template_diff)

    # Printed only on a run that still has the authored ids to match on.
    # A matrix key is claimed by a note's slug OR by the id its YAML unit
    # authored, and the migration REMOVES that id — so after it has run,
    # the set would grow by a key that is no longer anybody's question.
    # The per-note WARNINGs above still name every draft that wants a row.
    needs_rows = any(
        "no setup x trade matrix row" in w for o in outcomes for w in o.warnings
    )
    if args.note is None and needs_rows and any(p.yaml_id for p in plans):
        unclaimed = unclaimed_matrix_keys(plans, matrix_aliases=aliases)
        if unclaimed:
            print(
                f"\nUNCLAIMED setup x trade matrix key(s): {unclaimed}. No note's "
                "slug spells any of these, so their rows were NOT seeded anywhere. "
                "Pairing one to a note is a ruling; this command will not guess it."
            )

    changed = sum(1 for o in outcomes for a in o.actions.values() if a == "updated")
    print(
        f"\n{len(outcomes)} note(s), {changed} write(s) "
        f"{'that WOULD change bytes' if dry_run else 'applied'}."
    )


# ---------------------------------------------------------------------
# add-alias  (ADR-0008 D4 — an alias is how a free-text value finds a slug)
# ---------------------------------------------------------------------


def cmd_add_alias(args: argparse.Namespace) -> None:
    from cobalt.vault import resolve_vault_path

    from .vault_loader import DEFINITION_SECTION, DEF_UNIT_PREFIX, STRATEGIES_DIR

    root = resolve_vault_path()
    matches = [
        path
        for path in sorted((root / STRATEGIES_DIR).glob("*.md"))
        if (split := _frontmatter_of(path)) and split.get("trade_def") == args.slug
    ]
    if len(matches) != 1:
        raise SystemExit(
            f"expected exactly one strategy note with trade_def: {args.slug!r}, "
            f"found {len(matches)}"
        )
    path = matches[0]
    lines = path.read_text(encoding="utf-8").splitlines()
    section = find_section(lines, DEFINITION_SECTION)
    unit = section.units.get(f"{DEF_UNIT_PREFIX}{args.slug}") if section else None
    if unit is None:
        raise SystemExit(f"{path.name}: no {DEF_UNIT_PREFIX}{args.slug} unit")

    body = "\n".join(unit.body(lines))
    new_body, notes = add_alias_to_unit(body, args.alias)

    store = VaultWriteStore()
    store.ensure_schema()
    writer = VaultWriter("taxonomy.add_alias", store=store, dry_run=args.dry_run)
    result = writer.upsert_unit(
        path, DEFINITION_SECTION, f"{DEF_UNIT_PREFIX}{args.slug}", new_body
    )
    for note in notes:
        print(f"NOTE: {note}")
    print(result.report())


def _frontmatter_of(path):
    from cobalt.vaultwrite.frontmatter import split_frontmatter

    fm, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    return fm or {}


# ---------------------------------------------------------------------
# migrate-trade-notes  (ADR-0008 D4)
# ---------------------------------------------------------------------


def cmd_migrate_trade_notes(args: argparse.Namespace) -> None:
    dry_run = _require_mode(args, "migrate-trade-notes")
    index = build_alias_index()
    run = plan_trade_notes(only_note=args.note, index=index)

    print(
        "cobalt taxonomy migrate-trade-notes — "
        f"{'DRY RUN' if dry_run else 'APPLY'} on {len(run.plans)} note(s)\n"
    )
    outcomes = apply_trade_notes(run, dry_run=dry_run)

    for outcome in outcomes:
        if outcome.action.startswith("skip"):
            continue
        print(
            f"=== {outcome.path.name}\n"
            f"    strategy={outcome.strategy_value!r} -> "
            f"trade_def={outcome.slug or '(blank)'}"
            + (f" · write_id={outcome.write_id}" if outcome.write_id else "")
        )
        if outcome.diff:
            print(outcome.diff)
        print()

    print("=== tally (strategy value -> slug -> n)")
    matched = blank = 0
    for label, (slug, n) in sorted(run.tally.items(), key=lambda x: (-x[1][1], x[0])):
        print(f"    {label!r:<44} -> {slug or '(blank)':<24} n={n}")
        if slug:
            matched += n
        else:
            blank += n
    print(f"    matched {matched} note(s); {blank} left blank")

    for problem in run.problems:
        print(f"    PROBLEM: {problem}")
    skipped = sum(1 for o in outcomes if o.action == "skip_has_trade_def")
    if skipped:
        print(f"    {skipped} note(s) already carried `trade_def:` — skipped")

    if args.note is None:
        _path, template_diff = migrate_trade_template(dry_run=dry_run)
        print("\n=== 5 - Templates/Individual Trade Template.md  (plain edit)")
        print(template_diff)

    changed = sum(1 for o in outcomes if o.action == "updated")
    print(
        f"\n{len(outcomes)} note(s), {changed} write(s) "
        f"{'that WOULD change bytes' if dry_run else 'applied'}."
    )


# ---------------------------------------------------------------------
# sync-frontmatter  (ruling d)
# ---------------------------------------------------------------------


def cmd_sync_frontmatter(args: argparse.Namespace) -> None:
    from cobalt.vault import resolve_vault_path

    dry_run = _require_mode(args, "sync-frontmatter")
    result = load_vault_trade_defs()
    vault_root = resolve_vault_path()

    store = VaultWriteStore()
    store.ensure_schema()
    writer = VaultWriter("taxonomy.sync_frontmatter", store=store, dry_run=dry_run)

    wanted: dict[Path, tuple[Optional[str], list[str]]] = {}
    for loaded in result.defs:
        wanted[vault_root / loaded.note_path] = (
            loaded.definition.trade_class.value,
            [f.value for f in loaded.definition.family],
        )
    for draft in result.drafts:
        wanted[vault_root / draft.note_path] = (None, [])

    changed = 0
    for path, (trade_class, families) in sorted(wanted.items()):
        lines = path.read_text(encoding="utf-8").splitlines()
        span = frontmatter_span(lines)
        if span is None:
            print(f"SKIP {path.name}: no frontmatter block")
            continue
        current = "\n".join(lines[span[0]:span[1]])
        body, _notes = edit_frontmatter(
            lines[span[0]:span[1]], trade_class=trade_class, families=families
        )
        if body == current:
            continue
        changed += 1
        result_row = writer.upsert_region(
            path, FRONTMATTER_SECTION, FRONTMATTER_REGION, body,
            locate=frontmatter_span,
        )
        print(result_row.report())

    if changed:
        print(
            f"\nsync-frontmatter: {changed} note(s) differ from their def "
            f"({'nothing written — dry run' if dry_run else 'written'})."
        )
    else:
        print(
            "\nsync-frontmatter: every note's class/family already matches its def "
            "— 0 changes."
        )


# ---------------------------------------------------------------------


def add_parser(sub) -> None:
    group = sub.add_parser(
        "taxonomy", help="Trade definitions, read from the vault (ADR-0008 D3)"
    )
    gsub = group.add_subparsers(dest="command", required=True)

    load = gsub.add_parser(
        "load",
        help='Load every strategy note into "user".trade_defs / "user".tunables.',
    )
    load.add_argument(
        "--dry-run", action="store_true", help="Read and report; write nothing."
    )
    load.set_defaults(func=cmd_load)

    migrate = gsub.add_parser(
        "migrate-strategy-notes",
        help="ONE-OFF: put the strategy notes into the ADR-0008 D3 shape.",
    )
    migrate.add_argument("--dry-run", action="store_true")
    migrate.add_argument("--apply", action="store_true")
    migrate.add_argument("--note", help="Limit the run to one slug.")
    migrate.add_argument(
        "--matrix-alias",
        action="append",
        metavar="MATRIX_KEY=SLUG",
        help=(
            "Pair a setup x trade matrix key with the note that owns it, for the "
            "keys no rule derives. Repeatable. A RULING, passed in rather than "
            "written down here — see parse_matrix_aliases()."
        ),
    )
    migrate.add_argument(
        "--tunable-alias",
        action="append",
        metavar="OLD_KEY=SLUG",
        help=(
            "Pair a per_trade tunable key with the note that owns it. Repeatable. "
            "Needed only when re-running over a corpus whose units have already "
            "dropped their authored id — a first run reads the pairing from the "
            "notes themselves."
        ),
    )
    migrate.set_defaults(func=cmd_migrate_strategy_notes)

    trade = gsub.add_parser(
        "migrate-trade-notes",
        help="ONE-OFF: give every trade note a `trade_def:` (ADR-0008 D4).",
    )
    trade.add_argument("--dry-run", action="store_true")
    trade.add_argument("--apply", action="store_true")
    trade.add_argument("--note", help="Limit the run to one note (file name or path).")
    trade.set_defaults(func=cmd_migrate_trade_notes)

    alias = gsub.add_parser(
        "add-alias",
        help="Add one alias to a strategy note's aliases[] (idempotent).",
    )
    alias.add_argument("slug")
    alias.add_argument("alias")
    alias.add_argument("--dry-run", action="store_true")
    alias.set_defaults(func=cmd_add_alias)

    sync = gsub.add_parser(
        "sync-frontmatter",
        help="Re-align each note's class/family with its loaded def (ruling d).",
    )
    sync.add_argument("--dry-run", action="store_true")
    sync.add_argument("--apply", action="store_true")
    sync.set_defaults(func=cmd_sync_frontmatter)


__all__ = [
    "add_parser",
    "cmd_add_alias",
    "cmd_load",
    "cmd_migrate_trade_notes",
    "cmd_migrate_strategy_notes",
    "cmd_sync_frontmatter",
]
