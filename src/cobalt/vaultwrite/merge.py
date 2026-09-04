"""Deterministic three-way merge for one unit body (LAW L28.2).

No LLM in the write path — this is `difflib` and nothing else, so the
same three inputs always produce the same output.

The three inputs:

  base    what Cobalt wrote into this unit last time (`vault_writes.after`)
  human   what is in the unit on disk right now
  cobalt  what Cobalt wants the unit to say now

The rules, straight out of L28:

  * a region only Cobalt changed  -> Cobalt's new version wins
    (base == human, cobalt differs)
  * a region only the human changed -> the human's version is kept
    (base == cobalt, human differs)
  * both changed the same region  -> the HUMAN wins, always, and one
    override row is recorded
  * a human-added region (nothing in base) -> carried through in
    position, no override — it is an addition, not an override

An override is recorded whenever the human changed or deleted lines
Cobalt had authored (`base` non-empty and `human != base`), whether or
not Cobalt also wanted to change them. A pure insertion by the human is
not an override.

The merge is LINE-ANCHORED, not region-level. A plain diff3 resolves
whole unstable chunks at once, which conflates two different things: a
line the human EDITED, and a line the human merely typed NEXT TO one
Cobalt changed. That conflation loses real work in both directions — an
added journal line freezes Cobalt's update forever, or a corrected
ticker throws away the rest of the card. So each base line is classified
independently against the human's diff (unchanged / edited / deleted),
Cobalt's diff supplies the text for every line the human left alone, and
the human's insertions are carried at their own anchor points.
"""

from dataclasses import dataclass
from difflib import SequenceMatcher


@dataclass(frozen=True)
class Override:
    """One region where the human's text beat Cobalt's. `conflict` is
    True when Cobalt also wanted to change the same region (both
    edited); False when Cobalt would have left it alone."""

    base: tuple[str, ...]
    human: tuple[str, ...]
    cobalt: tuple[str, ...]
    conflict: bool

    def describe(self) -> str:
        kind = "conflict (both edited)" if self.conflict else "human edit"
        return (
            f"{kind}: cobalt wrote {list(self.base)!r}; "
            f"human has {list(self.human)!r}; "
            f"this run wanted {list(self.cobalt)!r} — human kept."
        )


@dataclass(frozen=True)
class MergeResult:
    lines: list[str]
    overrides: list[Override]

    @property
    def text(self) -> str:
        return "\n".join(self.lines)


def _human_view(base: list[str], human: list[str]):
    """Classify the human's edit of `base`, line by line.

    Returns (inserts_at, group_of, groups) where
      inserts_at[i]  lines the human typed immediately BEFORE base line i
                     (i == len(base) means "appended at the end")
      group_of[i]    the id of the edit group base line i belongs to
      groups[gid]    (b1, b2, human_lines) — the human's replacement for
                     base[b1:b2]; empty human_lines means they deleted it
    """
    inserts_at: dict[int, list[str]] = {}
    group_of: dict[int, int] = {}
    groups: list[tuple[int, int, list[str]]] = []

    for tag, i1, i2, j1, j2 in SequenceMatcher(None, base, human, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        if tag == "insert":
            inserts_at.setdefault(i1, []).extend(human[j1:j2])
            continue
        gid = len(groups)
        groups.append((i1, i2, list(human[j1:j2])))  # replace, or delete (empty)
        for i in range(i1, i2):
            group_of[i] = gid
    return inserts_at, group_of, groups


def merge3(base: list[str], human: list[str], cobalt: list[str]) -> MergeResult:
    inserts_at, group_of, groups = _human_view(base, human)
    out: list[str] = []
    overrides: list[Override] = []
    emitted: set[int] = set()

    def take_inserts(i: int) -> None:
        out.extend(inserts_at.pop(i, []))

    def emit_group(gid: int, cobalt_attempt: list[str]) -> None:
        """The human's version of a group of base lines wins, once."""
        if gid in emitted:
            return
        emitted.add(gid)
        b1, b2, human_lines = groups[gid]
        out.extend(human_lines)
        overrides.append(
            Override(
                base=tuple(base[b1:b2]),
                human=tuple(human_lines),
                cobalt=tuple(cobalt_attempt),
                conflict=list(cobalt_attempt) != list(base[b1:b2]),
            )
        )

    for tag, b1, b2, c1, c2 in SequenceMatcher(None, base, cobalt, autojunk=False).get_opcodes():
        if tag == "equal":
            # Cobalt left these lines alone: the human's verdict decides
            # each one on its own.
            for offset, i in enumerate(range(b1, b2)):
                take_inserts(i)
                gid = group_of.get(i)
                if gid is None:
                    out.append(cobalt[c1 + offset])
                else:
                    emit_group(gid, list(base[groups[gid][0] : groups[gid][1]]))
        elif tag == "insert":
            # Cobalt added lines here. Anything the human typed at this
            # same point comes first, then Cobalt's addition.
            take_inserts(b1)
            out.extend(cobalt[c1:c2])
        else:  # "replace" / "delete" — Cobalt rewrote or dropped base[b1:b2]
            pending: list[str] = []
            for i in range(b1, b2):
                pending.extend(inserts_at.pop(i, []))
            touched = any(i in group_of for i in range(b1, b2))
            if touched:
                # The human edited inside the range Cobalt wanted to
                # rewrite. Human wins the whole range (L28.2).
                attempt = list(cobalt[c1:c2])
                for i in range(b1, b2):
                    gid = group_of.get(i)
                    if gid is None:
                        out.append(base[i])  # he kept this line; Cobalt wanted it gone
                    else:
                        emit_group(gid, attempt)
                out.extend(pending)
            else:
                out.extend(cobalt[c1:c2])
                out.extend(pending)

    # Anything the human appended after the last base line.
    for i in sorted(inserts_at):
        out.extend(inserts_at[i])
    return MergeResult(lines=out, overrides=overrides)


def merge_body(base: str, human: str, cobalt: str) -> MergeResult:
    """String-level wrapper. An absent baseline is the caller's problem
    (writer.py surfaces it as `baseline_missing`), not something this
    function guesses at."""
    return merge3(base.split("\n"), human.split("\n"), cobalt.split("\n"))
