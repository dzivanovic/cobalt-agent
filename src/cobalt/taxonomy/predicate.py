"""The §10.5 IF/Then condition grammar, parsed (S2-P2 STEP-2, ruling R3).

Until S2-P2 a precondition's `expr` was a raw string nobody read. R3:
parse the existing strings into a typed AST AT LOAD, leave the notes
untouched, fail loud on anything that does not parse. `TradeDef`
validation calls `parse_predicate` for every `expr` it holds (via
`Predicate`), so a def that loads is a def whose every expression has a
tree; the vault loader turns a failure into note path + line + slug +
expression (`vault_loader._locate_predicate_errors`).

WHAT THE GRAMMAR COVERS (Astra R1-4: an incomplete grammar is a
whole-taxonomy first-run failure, so it was inventoried against every
expr position before it was written):

    expr      := or
    or        := and (OR and)*
    and       := not (AND not)*
    not       := NOT not | qualified
    qualified := relation ( (on|after|against) additive
                          | between additive and additive )*
    relation  := additive [ cmp additive | IN (set | additive)
                          | (touched|near|close_through|inside) additive ]
    additive  := term (('+'|'-') term)*
    term      := unary (('*'|'/') unary)*
    unary     := '-' unary | postfix
    postfix   := primary [unit]            unit: min bars days sec pct atr cents
    primary   := number | string | null | cfg(key) | event(name, args...)
               | '{' additive (',' additive)* '}' | '(' expr ')'
               | [that] ref
    ref       := segment ('.' segment)*
    segment   := ident [ '(' [arg (',' arg)*] ')' ]
    arg       := [ident ':'] (words | expr)          words: 2+ bare identifiers

`cmp` is `== != >= <= > <` (`≥`/`≤` accepted). AND/OR/NOT/IN are
keywords in either all-caps or all-lower spelling. A relation or
qualifier word immediately followed by `(` is an ordinary call —
`touched(Leg(pullback), VWAP)` and `Leg(pullback) touched VWAP` both
parse. A bare word on the right of `==`/`!=` or inside `{}` is a
`Symbol` (an enum value such as `culminating`), never an atom.

ATOMS. `required_atoms(ast)` names what a detector must supply: the
canonical text of every outermost reference (`Extension.state`,
`RangeBreak(HTF).day_count`, `opposite(Gap.direction)` — a call is one
atom, whole), every `event(...)`, and every relation/qualifier word
(`touched`, `on`, …), because each needs evaluator support. `cfg()`
keys, numbers and symbols are not atoms. The radar's detector registry
(`cobalt.radar.anatomy.registry`) compares against this set; the
difference is the "not evaluable: missing atoms […]" line (R2).

`text` predicates are human and never reach this module.
"""

from __future__ import annotations

import re
from decimal import Decimal
from typing import Annotated, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

#: A `cfg()` key — the same character class the loader's token scan uses
#: (loader._CFG_TOKEN_PATTERN), with empty segments refused.
CFG_KEY_RE = re.compile(r"^[A-Za-z0-9_]+(\.[A-Za-z0-9_]+)*$")

UNITS = frozenset({"min", "bars", "days", "sec", "pct", "atr", "cents"})
RELATION_WORDS = frozenset({"touched", "near", "close_through", "inside"})
QUALIFIER_WORDS = frozenset({"on", "after", "against"})
KEYWORDS = frozenset({"AND", "OR", "NOT", "IN"})
COMPARISONS = ("==", "!=", ">=", "<=", ">", "<")


class PredicateSyntaxError(ValueError):
    """An expression that does not parse. Carries the text and column."""

    def __init__(self, expr: str, column: int, reason: str):
        self.expr = expr
        self.column = column
        self.reason = reason
        super().__init__(
            f"predicate syntax error at column {column}: {reason} in {expr!r}"
        )


# ---------------------------------------------------------------------------
# AST — frozen Pydantic, discriminated on `kind`
# ---------------------------------------------------------------------------


class _Node(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class Number(_Node):
    kind: Literal["number"] = "number"
    value: Decimal


class String(_Node):
    kind: Literal["string"] = "string"
    value: str


class Null(_Node):
    kind: Literal["null"] = "null"


class Symbol(_Node):
    kind: Literal["symbol"] = "symbol"
    name: str


class Cfg(_Node):
    kind: Literal["cfg"] = "cfg"
    key: str


class Words(_Node):
    kind: Literal["words"] = "words"
    words: tuple[str, ...]


class Quantity(_Node):
    kind: Literal["quantity"] = "quantity"
    value: Node
    unit: str


class Arg(_Node):
    name: str | None = None
    value: Node


class Segment(_Node):
    name: str
    #: None = no parentheses; () = empty call.
    args: tuple[Arg, ...] | None = None


class Ref(_Node):
    kind: Literal["ref"] = "ref"
    segments: tuple[Segment, ...]
    demonstrative: bool = False


class EventAtom(_Node):
    kind: Literal["event"] = "event"
    name: str
    args: tuple[Arg, ...] = ()


class SetLiteral(_Node):
    kind: Literal["set"] = "set"
    items: tuple[Node, ...]


class Arith(_Node):
    kind: Literal["arith"] = "arith"
    op: Literal["+", "-", "*", "/"]
    left: Node
    right: Node


class Negate(_Node):
    kind: Literal["negate"] = "negate"
    operand: Node


class Compare(_Node):
    kind: Literal["compare"] = "compare"
    op: Literal["==", "!=", ">=", "<=", ">", "<"]
    left: Node
    right: Node


class InTest(_Node):
    kind: Literal["in"] = "in"
    left: Node
    right: Node


class Relation(_Node):
    kind: Literal["relation"] = "relation"
    op: Literal["touched", "near", "close_through", "inside"]
    left: Node
    right: Node


class Qualified(_Node):
    kind: Literal["qualified"] = "qualified"
    op: Literal["on", "after", "against"]
    subject: Node
    anchor: Node


class Between(_Node):
    kind: Literal["between"] = "between"
    subject: Node
    start: Node
    end: Node


class Not(_Node):
    kind: Literal["not"] = "not"
    operand: Node


class And(_Node):
    kind: Literal["and"] = "and"
    operands: tuple[Node, ...]


class Or(_Node):
    kind: Literal["or"] = "or"
    operands: tuple[Node, ...]


Node = Annotated[
    Union[
        Number, String, Null, Symbol, Cfg, Words, Quantity, Ref, EventAtom,
        SetLiteral, Arith, Negate, Compare, InTest, Relation, Qualified,
        Between, Not, And, Or,
    ],
    Field(discriminator="kind"),
]

for _model in (
    Quantity, Arg, Segment, Ref, EventAtom, SetLiteral, Arith, Negate,
    Compare, InTest, Relation, Qualified, Between, Not, And, Or,
):
    _model.model_rebuild()


# ---------------------------------------------------------------------------
# Tokenizer
# ---------------------------------------------------------------------------

_TOKEN_RE = re.compile(
    r"""
    (?P<ws>\s+)
  | (?P<num>\d+(?:\.\d+)?)
  | (?P<str>"[^"]*"|'[^']*')
  | (?P<ident>[A-Za-z_][A-Za-z0-9_]*)
  | (?P<op>==|!=|>=|<=|≥|≤|[<>*·/+\-(){},:.])
    """,
    re.VERBOSE,
)

_OP_ALIASES = {"≥": ">=", "≤": "<=", "·": "*"}


class _Tok:
    __slots__ = ("kind", "value", "col")

    def __init__(self, kind: str, value: str, col: int):
        self.kind, self.value, self.col = kind, value, col

    def is_op(self, *values: str) -> bool:
        return self.kind == "op" and self.value in values

    def word(self) -> str | None:
        return self.value if self.kind == "ident" else None


def _tokenize(expr: str) -> list[_Tok]:
    tokens: list[_Tok] = []
    pos = 0
    while pos < len(expr):
        if expr.startswith("cfg(", pos) and (pos == 0 or not (expr[pos - 1].isalnum() or expr[pos - 1] == "_")):
            close = expr.find(")", pos + 4)
            if close == -1:
                raise PredicateSyntaxError(expr, pos + 1, "expected ')' after cfg key")
            key = expr[pos + 4:close].strip()
            if not CFG_KEY_RE.match(key):
                raise PredicateSyntaxError(expr, pos + 5, f"invalid cfg key {key!r}")
            tokens.append(_Tok("cfg", key, pos + 1))
            pos = close + 1
            continue
        match = _TOKEN_RE.match(expr, pos)
        if match is None:
            raise PredicateSyntaxError(expr, pos + 1, f"unexpected character {expr[pos]!r}")
        kind = match.lastgroup
        text = match.group()
        if kind != "ws":
            if kind == "op":
                text = _OP_ALIASES.get(text, text)
            elif kind == "str":
                text = text[1:-1]
            tokens.append(_Tok(kind, text, pos + 1))
        pos = match.end()
    tokens.append(_Tok("eof", "", len(expr) + 1))
    return tokens


def _keyword(tok: _Tok) -> str | None:
    """AND/OR/NOT/IN in all-caps or all-lower spelling."""
    if tok.kind != "ident":
        return None
    upper = tok.value.upper()
    if upper in KEYWORDS and tok.value in (upper, upper.lower()):
        return upper
    return None


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------


class _Parser:
    def __init__(self, expr: str):
        self.expr = expr
        self.tokens = _tokenize(expr)
        self.i = 0

    # -- helpers ----------------------------------------------------------
    def peek(self, offset: int = 0) -> _Tok:
        return self.tokens[min(self.i + offset, len(self.tokens) - 1)]

    def advance(self) -> _Tok:
        tok = self.peek()
        self.i += 1
        return tok

    def fail(self, reason: str, tok: _Tok | None = None) -> PredicateSyntaxError:
        return PredicateSyntaxError(self.expr, (tok or self.peek()).col, reason)

    def expect_op(self, value: str) -> None:
        if not self.peek().is_op(value):
            raise self.fail(f"expected {value!r}")
        self.advance()

    def _word_not_call(self, words: frozenset[str]) -> str | None:
        tok = self.peek()
        if tok.kind == "ident" and tok.value in words and not self.peek(1).is_op("("):
            return tok.value
        return None

    # -- grammar ----------------------------------------------------------
    def parse(self) -> Node:
        if not self.expr.strip():
            raise PredicateSyntaxError(self.expr, 1, "empty expression")
        node = self.parse_or()
        if self.peek().kind != "eof":
            raise self.fail(f"unexpected token {self.peek().value!r}")
        return node

    def parse_or(self) -> Node:
        operands = [self.parse_and()]
        while _keyword(self.peek()) == "OR":
            self.advance()
            operands.append(self.parse_and())
        return operands[0] if len(operands) == 1 else Or(operands=tuple(operands))

    def parse_and(self) -> Node:
        operands = [self.parse_not()]
        while _keyword(self.peek()) == "AND":
            self.advance()
            operands.append(self.parse_not())
        return operands[0] if len(operands) == 1 else And(operands=tuple(operands))

    def parse_not(self) -> Node:
        if _keyword(self.peek()) == "NOT":
            self.advance()
            return Not(operand=self.parse_not())
        return self.parse_qualified()

    def parse_qualified(self) -> Node:
        node = self.parse_relation()
        while True:
            op = self._word_not_call(QUALIFIER_WORDS)
            if op is not None:
                self.advance()
                node = Qualified(op=op, subject=node, anchor=self.parse_additive())
                continue
            if self._word_not_call(frozenset({"between"})):
                self.advance()
                start = self.parse_additive()
                if _keyword(self.peek()) != "AND":
                    raise self.fail("expected 'and' in between … and …")
                self.advance()
                node = Between(subject=node, start=start, end=self.parse_additive())
                continue
            return node

    def parse_relation(self) -> Node:
        left = self.parse_additive()
        tok = self.peek()
        if tok.kind == "op" and tok.value in COMPARISONS:
            self.advance()
            right = self.parse_additive()
            if tok.value in ("==", "!=") and _is_bare_word(right):
                right = Symbol(name=right.segments[0].name)
            return Compare(op=tok.value, left=left, right=right)
        if _keyword(tok) == "IN":
            self.advance()
            right = self.parse_set() if self.peek().is_op("{") else self.parse_additive()
            return InTest(left=left, right=right)
        op = self._word_not_call(RELATION_WORDS)
        if op is not None:
            self.advance()
            return Relation(op=op, left=left, right=self.parse_additive())
        return left

    def parse_additive(self) -> Node:
        node = self.parse_term()
        while self.peek().is_op("+", "-"):
            op = self.advance().value
            node = Arith(op=op, left=node, right=self.parse_term())
        return node

    def parse_term(self) -> Node:
        node = self.parse_unary()
        while self.peek().is_op("*", "/"):
            op = self.advance().value
            node = Arith(op=op, left=node, right=self.parse_unary())
        return node

    def parse_unary(self) -> Node:
        if self.peek().is_op("-"):
            self.advance()
            return Negate(operand=self.parse_unary())
        return self.parse_postfix()

    def parse_postfix(self) -> Node:
        node = self.parse_primary()
        tok = self.peek()
        if (
            tok.kind == "ident"
            and tok.value in UNITS
            and not self.peek(1).is_op("(", ".")
        ):
            self.advance()
            return Quantity(value=node, unit=tok.value)
        return node

    def parse_set(self) -> SetLiteral:
        self.expect_op("{")
        items: list[Node] = []
        while True:
            item = self.parse_additive()
            items.append(Symbol(name=item.segments[0].name) if _is_bare_word(item) else item)
            if self.peek().is_op(","):
                self.advance()
                continue
            if not self.peek().is_op("}"):
                raise self.fail("expected '}'")
            self.advance()
            return SetLiteral(items=tuple(items))

    def parse_primary(self) -> Node:
        tok = self.peek()
        if tok.kind == "num":
            self.advance()
            return Number(value=Decimal(tok.value))
        if tok.kind == "str":
            self.advance()
            return String(value=tok.value)
        if tok.kind == "cfg":
            self.advance()
            return Cfg(key=tok.value)
        if tok.is_op("("):
            self.advance()
            node = self.parse_or()
            self.expect_op(")")
            return node
        if tok.is_op("{"):
            return self.parse_set()
        if tok.kind == "ident":
            if tok.value.lower() == "null" and not self.peek(1).is_op("(", "."):
                self.advance()
                return Null()
            if tok.value == "event" and self.peek(1).is_op("("):
                return self.parse_event()
            if _keyword(tok) is not None or (
                tok.value in RELATION_WORDS | QUALIFIER_WORDS | {"between"}
                and not self.peek(1).is_op("(")
            ):
                raise self.fail("expected an operand")
            if tok.value == "that" and self.peek(1).kind == "ident":
                self.advance()
                ref = self.parse_ref()
                return Ref(segments=ref.segments, demonstrative=True)
            return self.parse_ref()
        raise self.fail("expected an operand")

    def parse_event(self) -> EventAtom:
        from .trade_def import Event

        open_tok = self.advance()  # `event`
        args = self.parse_args()
        if not args or args[0].name is not None or not _is_bare_word(args[0].value):
            raise self.fail("event() takes an event name first", open_tok)
        name = args[0].value.segments[0].name
        known = {e.value for e in Event}
        if name not in known:
            raise self.fail(
                f"unknown event {name!r} (known: {', '.join(sorted(known))})", open_tok
            )
        return EventAtom(name=name, args=args[1:])

    def parse_ref(self) -> Ref:
        segments = [self.parse_segment()]
        while self.peek().is_op("."):
            self.advance()
            segments.append(self.parse_segment())
        return Ref(segments=tuple(segments))

    def parse_segment(self) -> Segment:
        tok = self.peek()
        if tok.kind != "ident":
            raise self.fail("expected a name")
        self.advance()
        args = self.parse_args() if self.peek().is_op("(") else None
        return Segment(name=tok.value, args=args)

    def parse_args(self) -> tuple[Arg, ...]:
        self.expect_op("(")
        if self.peek().is_op(")"):
            self.advance()
            return ()
        args: list[Arg] = []
        while True:
            name = None
            if self.peek().kind == "ident" and self.peek(1).is_op(":"):
                name = self.advance().value
                self.advance()
            args.append(Arg(name=name, value=self.parse_arg_value()))
            if self.peek().is_op(","):
                self.advance()
                continue
            self.expect_op(")")
            return tuple(args)

    def _plain_word_at(self, offset: int) -> bool:
        tok = self.peek(offset)
        return (
            tok.kind == "ident"
            and _keyword(tok) is None
            and tok.value not in RELATION_WORDS | QUALIFIER_WORDS | UNITS | {"between"}
            and not self.peek(offset + 1).is_op("(", ".", ":")
        )

    def parse_arg_value(self) -> Node:
        count = 0
        while self._plain_word_at(count):
            count += 1
        if count >= 2:
            words = tuple(self.advance().value for _ in range(count))
            return Words(words=words)
        return self.parse_or()


def _is_bare_word(node: Node) -> bool:
    return (
        isinstance(node, Ref)
        and not node.demonstrative
        and len(node.segments) == 1
        and node.segments[0].args is None
    )


def parse_predicate(expr: str) -> Node:
    """Parse one §10.5 expression. Raises `PredicateSyntaxError`."""
    return _Parser(expr).parse()


# ---------------------------------------------------------------------------
# Canonical rendering — the atom spelling, and a stable round trip
# ---------------------------------------------------------------------------

_PRIMARY = 10


def _precedence(node: Node) -> int:
    if isinstance(node, Or):
        return 1
    if isinstance(node, And):
        return 2
    if isinstance(node, Not):
        return 3
    if isinstance(node, (Qualified, Between)):
        return 4
    if isinstance(node, (Compare, InTest, Relation)):
        return 5
    if isinstance(node, Arith):
        return 6 if node.op in ("+", "-") else 7
    if isinstance(node, Negate):
        return 8
    if isinstance(node, Quantity):
        return 9
    return _PRIMARY


def _arg(arg: Arg) -> str:
    value = render(arg.value)
    return f"{arg.name}: {value}" if arg.name is not None else value


def render(node: Node, minimum: int = 0) -> str:
    """Canonical text. `parse_predicate(render(ast)) == ast`."""
    text = _render(node)
    return f"({text})" if _precedence(node) < minimum else text


def _render(node: Node) -> str:
    if isinstance(node, Number):
        return format(node.value, "f")
    if isinstance(node, String):
        return f'"{node.value}"'
    if isinstance(node, Null):
        return "null"
    if isinstance(node, Symbol):
        return node.name
    if isinstance(node, Cfg):
        return f"cfg({node.key})"
    if isinstance(node, Words):
        return " ".join(node.words)
    if isinstance(node, Quantity):
        return f"{render(node.value, _PRIMARY)} {node.unit}"
    if isinstance(node, Ref):
        body = ".".join(
            seg.name + ("" if seg.args is None else f"({', '.join(_arg(a) for a in seg.args)})")
            for seg in node.segments
        )
        return f"that {body}" if node.demonstrative else body
    if isinstance(node, EventAtom):
        return f"event({', '.join([node.name, *(_arg(a) for a in node.args)])})"
    if isinstance(node, SetLiteral):
        return "{" + ", ".join(render(item, 6) for item in node.items) + "}"
    if isinstance(node, Arith):
        level = _precedence(node)
        return f"{render(node.left, level)} {node.op} {render(node.right, level + 1)}"
    if isinstance(node, Negate):
        return f"-{render(node.operand, 8)}"
    if isinstance(node, Compare):
        return f"{render(node.left, 6)} {node.op} {render(node.right, 6)}"
    if isinstance(node, InTest):
        return f"{render(node.left, 6)} IN {render(node.right, 6)}"
    if isinstance(node, Relation):
        return f"{render(node.left, 6)} {node.op} {render(node.right, 6)}"
    if isinstance(node, Qualified):
        return f"{render(node.subject, 4)} {node.op} {render(node.anchor, 6)}"
    if isinstance(node, Between):
        return (
            f"{render(node.subject, 4)} between {render(node.start, 6)} "
            f"and {render(node.end, 6)}"
        )
    if isinstance(node, Not):
        return f"NOT {render(node.operand, 3)}"
    if isinstance(node, And):
        return " AND ".join(render(op, 3) for op in node.operands)
    if isinstance(node, Or):
        return " OR ".join(render(op, 2) for op in node.operands)
    raise TypeError(f"not a predicate node: {type(node).__name__}")


# ---------------------------------------------------------------------------
# Atoms
# ---------------------------------------------------------------------------


def required_atoms(node: Node) -> frozenset[str]:
    """Everything a detector must supply for `node` to be evaluated."""
    found: set[str] = set()
    _collect(node, found)
    return frozenset(found)


def _collect(node: Node, found: set[str]) -> None:
    if isinstance(node, (Ref, EventAtom)):
        found.add(render(node))
    elif isinstance(node, Quantity):
        _collect(node.value, found)
    elif isinstance(node, SetLiteral):
        for item in node.items:
            _collect(item, found)
    elif isinstance(node, (Arith, Compare, InTest)):
        _collect(node.left, found)
        _collect(node.right, found)
    elif isinstance(node, Relation):
        found.add(node.op)
        _collect(node.left, found)
        _collect(node.right, found)
    elif isinstance(node, Qualified):
        found.add(node.op)
        _collect(node.subject, found)
        _collect(node.anchor, found)
    elif isinstance(node, Between):
        found.add("between")
        for child in (node.subject, node.start, node.end):
            _collect(child, found)
    elif isinstance(node, (Not, Negate)):
        _collect(node.operand, found)
    elif isinstance(node, (And, Or)):
        for child in node.operands:
            _collect(child, found)


__all__ = [
    "And", "Arg", "Arith", "Between", "CFG_KEY_RE", "Cfg", "Compare",
    "EventAtom", "InTest", "Negate", "Node", "Not", "Null", "Number", "Or",
    "PredicateSyntaxError", "Qualified", "Quantity", "Ref", "Relation",
    "Segment", "SetLiteral", "String", "Symbol", "Words", "parse_predicate",
    "render", "required_atoms",
]
