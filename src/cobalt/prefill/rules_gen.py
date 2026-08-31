"""Generate configs/cobalt/rules.yaml from the vault's own Rules.md
("THE 12 RULES" — SLICE 2.1, ruled by Dejan 2026-08-31).

Rules.md, not this repo, is the source of truth. rules.yaml is a
GENERATED artifact — regenerated on every prefill run (daily.py and
drc.py both call `regenerate_rules_config()`, never the old static
`load_rules_config()`, for their live rules block) and carries a header
naming its source plus a sha256 of Rules.md's raw content, so a stale
committed copy is visibly stale, never silently trusted.

Tag contract: each numbered rule line in Rules.md must end with exactly
one recognized Obsidian tag from RECOGNIZED_TAGS. Zero tags, more than
one, or an unrecognized tag all FAIL LOUD, naming the offending line —
there is no default category. Daily.md's old "Trade Rules" list is
explicitly NOT a source (ruled outdated 2026-08-23); only Rules.md's
own numbered lines and `**Label:** *text*` mantra lines are read.
"""

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

from cobalt.vault import resolve_vault_path

from .config import (
    RECOGNIZED_TAGS,
    RULES_CONFIG_PATH,
    GeneratedMeta,
    MantraItem,
    RuleItem,
    RulesConfig,
)

RULES_MD_RELATIVE_PATH = "1 - Trading/5 - Review/Rules.md"

_NUMBERED_LINE_RE = re.compile(r"^\s*\d+\.\s+(.*)$")
_MANTRA_RE = re.compile(r"^\*\*([^*]+):\*\*\s*\*(.+)\*\s*$")
_TAG_TOKEN_RE = re.compile(r"^#\w+$")


class RulesSourceError(RuntimeError):
    """Rules.md missing, unparseable, or a line's tag is missing/wrong — fail loud."""


def _split_trailing_tags(text: str) -> tuple[str, list[str]]:
    """Peel whitespace-delimited #tag tokens off the END of `text`, in
    whatever number actually appears — 0, 1, or many — so the caller can
    enforce "exactly one" itself and report the real count on failure."""
    tokens = text.split()
    tags: list[str] = []
    while tokens and _TAG_TOKEN_RE.match(tokens[-1]):
        tags.insert(0, tokens.pop()[1:])
    return " ".join(tokens), tags


def _slugify(label: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", label.strip().lower()).strip("_")


def _parse_rules_md(text: str) -> tuple[list[RuleItem], list[MantraItem]]:
    rules: list[RuleItem] = []
    mantras: list[MantraItem] = []
    rule_number = 0

    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        m = _NUMBERED_LINE_RE.match(raw_line)
        if m:
            rule_number += 1
            rest, tags = _split_trailing_tags(m.group(1))
            if len(tags) != 1:
                raise RulesSourceError(
                    f"Rules.md line {line_no} (rule #{rule_number}): needs exactly one "
                    f"trailing tag from {RECOGNIZED_TAGS}, found {tags or 'none'}: {raw_line!r}"
                )
            tag = tags[0]
            if tag not in RECOGNIZED_TAGS:
                raise RulesSourceError(
                    f"Rules.md line {line_no} (rule #{rule_number}): trailing tag "
                    f"#{tag} is not one of {RECOGNIZED_TAGS}: {raw_line!r}"
                )
            if not rest.strip():
                raise RulesSourceError(
                    f"Rules.md line {line_no} (rule #{rule_number}): empty rule text "
                    f"after stripping the tag: {raw_line!r}"
                )
            rules.append(RuleItem(id=f"rule_{rule_number:02d}", category=tag, text=rest.strip()))
            continue

        m = _MANTRA_RE.match(raw_line.strip())
        if m:
            label, mantra_text = m.groups()
            mantras.append(MantraItem(id=_slugify(label), text=f"{label.strip()}: {mantra_text.strip()}"))

    if not rules:
        raise RulesSourceError("Rules.md: no numbered rule lines found (expected '1. ... #tag' style lines).")
    return rules, mantras


def _write_rules_yaml(rules_cfg: RulesConfig, path: Path) -> None:
    header = (
        "# GENERATED — do not hand-edit. Source of truth is the vault's own\n"
        f"# {rules_cfg.generated.source}\n"
        "# (\"THE 12 RULES\"). Regenerated on every prefill run — see\n"
        "# src/cobalt/prefill/rules_gen.py. Hand edits here are overwritten on\n"
        "# the next run; edit Rules.md instead.\n"
    )
    body = yaml.safe_dump(
        rules_cfg.model_dump(mode="json"),
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
    )
    path.write_text(header + "\n" + body, encoding="utf-8")


def regenerate_rules_config() -> RulesConfig:
    """Read Rules.md fresh from the vault, parse + validate it, write the
    result to configs/cobalt/rules.yaml, and return the parsed config.
    Raises RulesSourceError (a line's tag is missing/wrong) or
    VaultConfigError (vault unresolvable) — never falls back to a stale
    or default rule set."""
    vault_root = resolve_vault_path()
    source_path = vault_root / RULES_MD_RELATIVE_PATH
    if not source_path.exists():
        raise RulesSourceError(f"Rules.md not found at {source_path} — cannot generate rules.yaml.")

    raw_text = source_path.read_text(encoding="utf-8")
    rules, mantras = _parse_rules_md(raw_text)

    rules_cfg = RulesConfig(
        generated=GeneratedMeta(
            source=str(source_path),
            source_sha256=hashlib.sha256(raw_text.encode("utf-8")).hexdigest(),
            generated_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        ),
        rules=rules,
        mantras=mantras,
    )
    _write_rules_yaml(rules_cfg, RULES_CONFIG_PATH)
    return rules_cfg
