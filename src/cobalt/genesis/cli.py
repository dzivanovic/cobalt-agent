"""CLI registration for F21 chunk 1 (card 468 G5): `cobalt genesis import|search`."""

from __future__ import annotations

from .search import search
from .store import GenesisStore, import_paths


def _cmd_import(args) -> None:
    # A bad path raises GenesisImportError before any write; cobalt.cli prints
    # it as FAILED and exits 1 (L1).
    for source in import_paths(args.paths, store=GenesisStore()):
        print(f"{source.source} · {len(source.chunks)} chunks · sha256 {source.sha256[:12]}")


def _cmd_search(args) -> None:
    for hit in search(args.question, limit=args.limit):
        first = hit.body.splitlines()[0] if hit.body else ""
        print(f"{hit.source}:{hit.line_start}-{hit.line_end} · {hit.rank:.4f} · {first}")


def add_parser(sub) -> None:
    group = sub.add_parser("genesis", help="F21 recall: import markdown sources, search them (FTS, no model)")
    gsub = group.add_subparsers(dest="command", required=True)
    imp = gsub.add_parser("import", help="Chunk each markdown file and replace its rows (all read before any write)")
    imp.add_argument("paths", nargs="+", help="Markdown files, each stored under the path as given.")
    imp.set_defaults(func=_cmd_import)
    find = gsub.add_parser("search", help="The one recall entry: ranked chunks for a question")
    find.add_argument("question", help="Plain words; websearch_to_tsquery('english', …).")
    find.add_argument("--limit", type=int, required=True, help="Most hits to print.")
    find.set_defaults(func=_cmd_search)
