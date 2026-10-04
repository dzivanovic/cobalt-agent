#!/usr/bin/env python3
# bare-guard.py — a Claude Code PreToolUse hook (his 2026-10-01 R45 part 1; card 17 A1), extended
# in place as `cobalt-guard` (his 2026-10-03 R32, R33; card 10 rows G1–G11), so the one hook entry
# covers it. Reads the hook's JSON on stdin; exit 0 lets the call through, exit 2 denies it with
# ONE line on stderr naming the route. It never runs a command.
#
# THE SCANNER: tool_input.command is read quote-aware (single quotes, double quotes, $'…' ANSI-C
# quotes, backslash escapes; a `#` comment runs to the newline). OUTSIDE quotes it sees `&&`,
# `||`, a pipe `|`, `;`, a lone `&`, a newline, a `>` or `<` redirect, and -- outside quotes OR
# inside double quotes -- a backtick or `$(`. A command that ends with the exact text
# ` < /dev/null` (the house-probe shape) passes that redirect.
#
# THE SEAT (its kind): the first user record of the transcript is the launch message. A
# `Read '<…>/BUILD-HUB.md'` (CHECK-, DEPLOY-, DEVFIX-) names the kind, and its `CARD: '<path>'`
# is read for WORKTREE, REPORT, CHECK REPORT and the `## ROWS` files. Otherwise the cwd: the repo
# with CTO-DESK-WAKEUP.md = desk, the repo with a prompt under prompts/20*/ = brain, a worktree
# under the worktree root = worker; anything else is UNKNOWN, and an unknown seat meets only the
# kind-free rules G1, G3, G6.
#
# THE RULES, first hit wins. Bash: G3 .env read · G2 production (not deploy) · G4 git shape
# (build, check, devfix, worker) · G7 a second session (any worker kind, deploy too; G9: the
# check's house call, a whole command opening with a CHECK-HUB.md line 10 house string, passes) ·
# G1 one command or a read-only pipe (G11: an `awk` program with `system(`, `>` or `|` is not
# read-only; card 06 B2–B4: nor `sort -o`/`--output`/`--compress-program`, a second `uniq`
# operand or `awk -f`, in a pipe segment or as one command; B1: `sort cut uniq awk` are G3
# readers too). Read: G3. Write / Edit: G6 stop line while dirty · G5 the fence (G10: a check's
# fence adds its own <S>, the card's JOB naming it).
# G8: every deny appends one JSON line to <worktree root>/.ledger/<session_id>.jsonl; a ledger
# error never blocks the deny. Any other error inside the guard -> exit 0: it never blocks work
# because it broke.
# COBALT_WT_ROOT and COBALT_REPO_ROOT stand in for /Users/cobalt/cobalt-wt and /Users/cobalt/cobalt
# in tests/ops/test_bare_guard.py only; the hook entry never sets them.
import datetime
import fnmatch
import json
import os
import re
import shlex
import sys

WT_ROOT = os.path.normpath(os.environ.get("COBALT_WT_ROOT") or "/Users/cobalt/cobalt-wt")
REPO_ROOT = os.path.normpath(os.environ.get("COBALT_REPO_ROOT") or "/Users/cobalt/cobalt")
VAULT_ROOT = "/Users/cobalt/Vault"

PROBE_TAIL = " < /dev/null"
BLOCK = (
    "NOT A REFUSAL. Dejan's rule: one bare command per call, and this call contains {found}. "
    "Resend the SAME commands now, one per call, in order. Do not report this to Dejan as a failure."
)
ROUTE = {
    "G2": "route: production is the deploy hub's; a dev read uses COBALT_ENV=dev",
    "G3": (
        "route: .env is never read; `ls -la <path>/.env` shows it is there, "
        "and the lock scripts copy and remove it"
    ),
    "G4": "route: git add <paths> then commit -m … -- <paths>; a merge is the deploy hub's",
    "G5 fixed": "route: a fixed file changes by a card row",
    "G5 fence": (
        "route: this seat writes only inside its fence (a worker: its worktree and its report; "
        "the brain: reports/ and prompts/20*/; nothing under /Users/cobalt/Vault); "
        "a fixed file changes by a card row"
    ),
    "G6": "route: release the lock (W (f)), then the stop line",
    "G7": "route: the desk launches",
}

HUBS = {
    "BUILD-HUB.md": "build",
    "CHECK-HUB.md": "check",
    "DEPLOY-HUB.md": "deploy",
    "DEVFIX-HUB.md": "devfix",
}
WORKERS = ("build", "check", "devfix", "deploy", "worker")
GIT_SHAPED = ("build", "check", "devfix", "worker")
READ_FILTERS = ("grep", "sed", "cut", "sort", "uniq", "head", "tail", "wc", "awk")
ENV_READERS = ("cat", "grep", "sed", "head", "tail", "less", "sort", "cut", "uniq", "awk")
LAUNCHERS = ("claude", "codex", "grok", "agy")
GIT_DENIED = ("push", "merge", "rebase", "reset", "checkout", "stash", "cherry-pick")
STOP_HEADS = ("BUILT ·", "CHECK DONE ·", "DEPLOYED")
PROD = re.compile(r"COBALT_ENV=production|(?<![\w-])--prod(?![\w-])|cobalt_brain")
ASSIGN = re.compile(r"[A-Za-z_][A-Za-z0-9_]*=")
DOCS = os.path.join("docs", "40 - DevDocs")
SED_WRITES = "`sed` with a `w` or `e` command or flag"
AWK_WRITES = "`awk` with `system(`, `>` or `|` in its program"
AWK_FILE = "`awk -f`, a program the guard cannot read"
SORT_WRITES = "`sort` with `-o`, `--output` or `--compress-program`"
UNIQ_WRITES = "`uniq` with a second operand, a file it writes"
# G9: the three house strings of CHECK-HUB.md line 10, as prefixes of the whole command
HOUSE = re.compile(r"grok |codex exec --skip-git-repo-check -m [A-Za-z0-9._-]+ -s read-only |agy ")
# G10: <S> = <AGY>/scratch/tribunal-bars-0920/<JOB>-check (CHECK-HUB.md line 5)
SCRATCH = os.path.join("agy-trial", "scratch", "tribunal-bars-0920")


def scan(command):
    """Return (what was found, in order of first sight; the quote state at the end; the
    top-level separators as (start, end) spans)."""
    found = []
    cuts = []

    def see(what):
        if what not in found:
            found.append(what)

    quote = None
    i, n = 0, len(command)
    while i < n:
        c = command[i]
        nxt = command[i + 1] if i + 1 < n else ""
        if quote == "'":
            if c == "'":
                quote = None
        elif quote == "$'":
            # ANSI-C quoting: a backslash escapes, `\'` does not close
            if c == "\\":
                i += 2
                continue
            if c == "'":
                quote = None
        elif quote == '"':
            if c == "\\":
                i += 2
                continue
            if c == '"':
                quote = None
            elif c == "`":
                see("a backtick")
            elif c == "$" and nxt == "(":
                see("`$(`")
        elif c == "#" and (i == 0 or command[i - 1] in " \t\n"):
            # a comment runs to the newline: a quote or backslash in it is not one,
            # and the newline that ends it is still seen
            end = command.find("\n", i)
            i = n if end < 0 else end
            continue
        elif c == "\\":
            i += 2
            continue
        elif c == "$" and nxt == "'":
            quote = "$'"
            i += 2
            continue
        elif c in "'\"":
            quote = c
        elif c == "`":
            see("a backtick")
        elif c == "$" and nxt == "(":
            see("`$(`")
        elif c == "&":
            if nxt == "&":
                see("`&&`")
                cuts.append((i, i + 2))
                i += 2
                continue
            see("a background `&`")
            cuts.append((i, i + 1))
        elif c == "|":
            if nxt == "|":
                see("`||`")
                cuts.append((i, i + 2))
                i += 2
                continue
            see("a pipe `|`")
            cuts.append((i, i + 1))
        elif c == ";":
            see("`;`")
            cuts.append((i, i + 1))
        elif c == "\n":
            see("a newline")
            cuts.append((i, i + 1))
        elif c in "<>":
            see("a redirect `%s`" % c)
        i += 1
    return found, quote, cuts


def segments(command, cuts):
    out, start = [], 0
    for a, b in cuts:
        out.append(command[start:a])
        start = b
    out.append(command[start:])
    return out


def words(segment):
    try:
        return shlex.split(segment, comments=True)
    except ValueError:
        return segment.split()


def verb(ws):
    """The command word of a segment past its NAME=value words, as a basename; '' if none."""
    for w in ws:
        if not ASSIGN.match(w):
            return os.path.basename(w)
    return ""


# ---- G1: sed in a pipe is `sed -n`, never -i, never a w / e command or flag ----------------


def sed_delimited(s, i, parts):
    """s[i] is the delimiter; return the index past `parts` closing delimiters, or -1."""
    if i >= len(s) or s[i] in "\n\\":
        return -1
    d = s[i]
    i += 1
    for _ in range(parts):
        while i < len(s) and s[i] != d:
            if s[i] == "\\":
                i += 1
            i += 1
        if i >= len(s):
            return -1
        i += 1
    return i


def sed_address(s, i):
    n = len(s)
    if i >= n:
        return i
    c = s[i]
    if c.isdigit():
        while i < n and s[i].isdigit():
            i += 1
        if i < n and s[i] == "~":
            i += 1
            while i < n and s[i].isdigit():
                i += 1
        return i
    if c == "$":
        return i + 1
    if c in "+~":
        i += 1
        while i < n and s[i].isdigit():
            i += 1
        return i
    if c in "/\\":
        i = sed_delimited(s, i + 1 if c == "\\" else i, 1)
        while 0 <= i < n and s[i] in "IM":
            i += 1
        return i
    return i


def sed_writes(s):
    """True when the script holds a w / W / e command or a w / e flag of `s`, or cannot be read."""
    i, n = 0, len(s)
    while True:
        while i < n and s[i] in " \t\n;":
            i += 1
        if i >= n:
            return False
        i = sed_address(s, i)
        if i < 0:
            return True
        if i < n and s[i] == ",":
            i = sed_address(s, i + 1)
            if i < 0:
                return True
        while i < n and s[i] in " \t!":
            i += 1
        if i >= n:
            return True
        c = s[i]
        i += 1
        if c in "{}":
            continue
        if c in "wWe":
            return True
        if c in "sy":
            i = sed_delimited(s, i, 2)
            if i < 0:
                return True
            if c == "s":
                while i < n and s[i] not in ";\n}":
                    if s[i] in "we":
                        return True
                    if not (s[i].isdigit() or s[i] in "gpiImM \t"):
                        return True
                    i += 1
            continue
        if c in "aicrR:#":
            end = s.find("\n", i)
            i = n if end < 0 else end
            continue
        if c in "btTv":
            while i < n and s[i] not in ";\n":
                i += 1
            continue
        if c in "pPlnNdDgGhHxz=qQF":
            while i < n and (s[i].isdigit() or s[i] in " \t"):
                i += 1
            if i < n and s[i] not in ";\n}":
                return True
            continue
        return True


SED_LONG_OK = (
    "--regexp-extended", "--posix", "--null-data", "--zero-terminated", "--separate",
    "--unbuffered", "--sandbox", "--debug", "--follow-symlinks",
)


def sed_problem(args):
    quiet, scripts, positional = False, [], []
    i, done = 0, False
    while i < len(args):
        a = args[i]
        if done or a == "-" or not a.startswith("-"):
            positional.append(a)
            i += 1
            continue
        if a == "--":
            done = True
            i += 1
            continue
        if a.startswith("--"):
            name, eq, val = a.partition("=")
            if name in ("--quiet", "--silent"):
                quiet = True
            elif name.startswith("--in-place"):
                return "`sed -i`"
            elif name == "--expression":
                if not eq:
                    i += 1
                    if i >= len(args):
                        return "`sed --expression` without its script"
                    val = args[i]
                scripts.append(val)
            elif name == "--file":
                return "`sed -f`, a script the guard cannot read"
            elif name == "--line-length":
                if not eq:
                    i += 1
            elif name not in SED_LONG_OK:
                return "`sed %s`, an option the guard does not know" % name
            i += 1
            continue
        j = 1
        while j < len(a):
            c = a[j]
            if c == "n":
                quiet = True
            elif c == "i":
                return "`sed -i`"
            elif c in "efl":
                rest = a[j + 1:]
                if not rest:
                    i += 1
                    if i >= len(args):
                        return "`sed -%s` without its argument" % c
                    rest = args[i]
                if c == "e":
                    scripts.append(rest)
                elif c == "f":
                    return "`sed -f`, a script the guard cannot read"
                break
            elif c not in "Erszu":
                return "`sed -%s`, an option the guard does not know" % c
            j += 1
        i += 1
    if not scripts:
        if not positional:
            return "`sed` without a script"
        scripts.append(positional[0])
    if not quiet:
        return "`sed` without `-n`"
    if any(sed_writes(s) for s in scripts):
        return SED_WRITES
    return None


def awk_writes(args):
    """G11: True when a word that can be awk program text holds `system(`, `>` or `|`. The
    values of -F and -v and the file of -f are not program text; every other word is read."""
    i, done = 0, False
    while i < len(args):
        a = args[i]
        if not done and a == "--":
            done = True
        elif not done and a[:2] in ("-F", "-v", "-f"):
            if len(a) == 2:
                i += 1
        elif "system(" in a or ">" in a or "|" in a:
            return True
        i += 1
    return False


def awk_file(args):
    """B3: True when the program comes from a file (`-f`, `--file`), which G11 cannot read."""
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--":
            return False
        if a[:2] == "-f" or a == "--file" or a.startswith("--file="):
            return True
        if a in ("-F", "-v"):
            i += 1
        i += 1
    return False


def sort_writes(args):
    """B2, by form: a short-option word holding `o` (`-o out`, `-oout`, `-uo out`), or a long
    option whose name is a prefix of `output`, or (B7) a prefix of `compress-program` at least
    two letters long (`--c` alone is ambiguous with `--check`)."""
    for a in args:
        if a.startswith("--"):
            name = a[2:].partition("=")[0]
            if name and "output".startswith(name):
                return True
            if len(name) >= 2 and "compress-program".startswith(name):
                return True
        elif a.startswith("-") and "o" in a[1:]:
            return True
    return False


def uniq_writes(args):
    """B2: True when uniq has a second operand, its output file. The word after -f, -s or -w,
    and the digits attached in -f1, -s2 or -w3, are values, not operands."""
    operands, i, done = 0, 0, False
    while i < len(args):
        a = args[i]
        if done or a == "-" or not a.startswith("-"):
            operands += 1
        elif a == "--":
            done = True
        elif not a.startswith("--") and a[-1] in "fsw":
            i += 1
        i += 1
    return operands > 1


def filter_problem(ws):
    """B2, B3, G11: what makes a `sort`, `uniq` or `awk` command more than a read, or None."""
    if ws[0] == "sort" and sort_writes(ws[1:]):
        return SORT_WRITES
    if ws[0] == "uniq" and uniq_writes(ws[1:]):
        return UNIQ_WRITES
    if ws[0] == "awk":
        if awk_file(ws[1:]):
            return AWK_FILE
        if awk_writes(ws[1:]):
            return AWK_WRITES
    return None


def pipe_problems(command, cuts):
    problems = []
    for seg in segments(command, cuts):
        ws = words(seg)
        if not ws:
            problems.append("an empty pipe segment")
            continue
        if ws[0] not in READ_FILTERS:
            problems.append("a pipe `|` with `%s`, not a read-only filter" % ws[0])
            continue
        if ws[0] == "sed":
            p = sed_problem(ws[1:])
            if p:
                problems.append(p)
        p = filter_problem(ws)
        if p:
            problems.append(p)
    return problems


def g1(command):
    text = command
    found, quote, cuts = [], None, []
    if command.endswith(PROBE_TAIL):
        text = command[: -len(PROBE_TAIL)]
        found, quote, cuts = scan(text)
    if not command.endswith(PROBE_TAIL) or quote is not None:
        text = command
        found, quote, cuts = scan(command)
    if not found:
        # B4: a lone sort, uniq or awk meets the checks of a pipe segment; its verb is read past
        # NAME=value words and a path, as G3 reads it (a pipe segment of either shape is denied)
        ws = words(text)
        while ws and ASSIGN.match(ws[0]):
            ws = ws[1:]
        p = filter_problem([os.path.basename(ws[0])] + ws[1:]) if ws else None
        return BLOCK.format(found=p) if p else None
    if found == ["a pipe `|`"]:
        problems = pipe_problems(text, cuts)
        if not problems:
            return None
        found = problems
    return BLOCK.format(found=", ".join(found))


# ---- the seat ------------------------------------------------------------------------------


def under(path, root):
    return path == root or path.startswith(root.rstrip("/") + "/")


def worktree_of(cwd):
    if not cwd or not under(cwd, WT_ROOT) or cwd == WT_ROOT:
        return None
    name = cwd[len(WT_ROOT):].lstrip("/").split("/")[0]
    return None if not name or name.startswith(".") else name


def first_message(transcript):
    if not isinstance(transcript, str) or not transcript:
        return ""
    try:
        with open(transcript, encoding="utf-8") as f:
            for k, line in enumerate(f):
                if k > 500:
                    break
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if not isinstance(rec, dict) or rec.get("type") != "user" or rec.get("isMeta"):
                    continue
                msg = rec.get("message")
                content = msg.get("content") if isinstance(msg, dict) else None
                if isinstance(content, str):
                    return content
                if isinstance(content, list):
                    texts = [
                        p["text"]
                        for p in content
                        if isinstance(p, dict) and p.get("type") == "text" and isinstance(p.get("text"), str)
                    ]
                    if texts:
                        return "\n".join(texts)
    except OSError:
        return ""
    return ""


def read_card(path):
    card = {"job": None, "worktree": None, "report": None, "check report": None, "files": []}
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except (OSError, TypeError):
        return card
    for key in ("job", "worktree"):
        m = re.search(r"^%s:[ \t]*([A-Za-z0-9._-]+)[ \t]*$" % key.upper(), text, re.M)
        if m and not m.group(1).startswith("."):
            card[key] = m.group(1)
    for key in ("report", "check report"):
        m = re.search(r"^%s:[ \t]*(\S.*?)[ \t]*$" % key.upper(), text, re.M)
        if m and os.path.isabs(m.group(1)):
            card[key] = os.path.normpath(m.group(1))
    m = re.search(r"^## ROWS[ \t]*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    for line in (m.group(1) if m else "").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if cells:
            card["files"] += re.findall(r"`([^`]+)`", cells[-1])
    return card


def seat(event):
    cwd = event.get("cwd")
    cwd = os.path.normpath(cwd) if isinstance(cwd, str) and os.path.isabs(cwd) else ""
    text = first_message(event.get("transcript_path"))
    m = re.search(r"Read '([^']+)'", text)
    prompt = m.group(1) if m else ""
    m = re.search(r"CARD: '([^']+)'", text)
    card_path = m.group(1) if m else ""
    hub = os.path.basename(prompt)
    in_repo = bool(cwd) and under(cwd, REPO_ROOT)
    wt = worktree_of(cwd)
    if hub in HUBS:
        kind = HUBS[hub]
    elif in_repo and hub == "CTO-DESK-WAKEUP.md":
        kind = "desk"
    elif in_repo and re.search(r"(^|/)prompts/20[^/]*/[^/]+\.md$", prompt):
        kind = "brain"
    elif wt:
        kind = "worker"
    else:
        kind = None
    card = read_card(card_path) if kind in HUBS.values() and card_path else read_card(None)
    return {"kind": kind, "cwd": cwd, "wt": card["worktree"] or wt, "cwd wt": wt, "card": card}


# ---- the Bash rules ------------------------------------------------------------------------


def braces(word):
    """The word's `{a,b}` alternatives, as the shell expands them."""
    m = re.search(r"\{([^{}]*,[^{}]*)\}", word)
    if not m:
        return [word]
    return [x for alt in m.group(1).split(",") for x in braces(word[: m.start()] + alt + word[m.end():])]


def is_env(path):
    """A path that names .env: after brace and glob expansion (a leading dot is matched only by
    a literal one), in any case (the filesystem here is case-insensitive)."""
    for alt in braces(path):
        base = os.path.basename(alt).lower()
        if base.startswith(".") and fnmatch.fnmatchcase(".env", base):
            return True
    return False


def env_words(args):
    """G3's words to test: each operand, and (B8) each option value — the text after the first
    `=` of a `--name=value` word, and the word after `--files0-from` given without `=`."""
    out = list(args)
    for k, a in enumerate(args):
        if a.startswith("--") and "=" in a:
            out.append(a.partition("=")[2])
        elif a == "--files0-from" and k + 1 < len(args):
            out.append(args[k + 1])
    return out


def g3_bash(segs):
    for ws in segs:
        if verb(ws) in ENV_READERS and any(is_env(w) for w in env_words(ws[1:])):
            return ROUTE["G3"]
    return None


def git_problem(ws):
    i = 0
    while i < len(ws) and ASSIGN.match(ws[i]):
        i += 1
    if i >= len(ws) or os.path.basename(ws[i]) != "git":
        return False
    rest = ws[i + 1:]
    if any(w.startswith("--output") for w in rest):
        return True
    j = 0
    while j < len(rest) and rest[j].startswith("-"):
        if rest[j] in ("-C", "-c", "--git-dir", "--work-tree", "--namespace"):
            j += 1
        j += 1
    if j >= len(rest):
        return False
    sub, args = rest[j], rest[j + 1:]
    if sub in GIT_DENIED:
        return True
    if sub == "add":
        # the whole tree by any spelling: `.`, `./`, `:/`, `-A`, `--all`, `--no-ignore-removal`
        return any(
            a in (":/", "--all", "--no-ignore-removal")
            or os.path.normpath(a) == "."
            or (a.startswith("-") and not a.startswith("--") and "A" in a)
            for a in args
        )
    if sub == "commit":
        return "--" not in args
    return False


def bash_rules(command, s):
    found, quote, cuts = scan(command)
    segs = [words(x) for x in segments(command, cuts)]
    kind = s["kind"]
    deny = g3_bash(segs)
    if deny:
        return "G3", deny
    if kind is not None and kind != "deploy" and PROD.search(command):
        return "G2", ROUTE["G2"]
    if kind in GIT_SHAPED and any(git_problem(ws) for ws in segs):
        return "G4", ROUTE["G4"]
    launches = [k for k, ws in enumerate(segs) if verb(ws) in LAUNCHERS]
    if kind == "check" and launches == [0] and HOUSE.match(command):
        launches = []  # G9: the check's one house call, typed as CHECK-HUB.md line 10 lists it
    if kind in WORKERS and launches:
        return "G7", ROUTE["G7"]
    deny = g1(command)
    if deny:
        return "G1", deny
    return None


# ---- the Write / Edit rules ----------------------------------------------------------------


def g6(s, content):
    if not isinstance(content, str):
        return None
    lines = [x.strip() for x in content.splitlines() if x.strip()]
    if not lines or not lines[-1].startswith(STOP_HEADS):
        return None
    names = {x for x in (s["wt"], s["cwd wt"]) if x}
    # the repo's own .env is the lock's source, never its copy: the deploy seat sits there
    if s["cwd"] and s["cwd"] != REPO_ROOT and os.path.exists(os.path.join(s["cwd"], ".env")):
        return ROUTE["G6"]
    if any(os.path.exists(os.path.join(WT_ROOT, x, ".env")) for x in names):
        return ROUTE["G6"]
    try:
        with open(os.path.join(WT_ROOT, ".cobalt_dev.lock", "owner"), encoding="utf-8") as f:
            owner = f.read().strip()
    except OSError:
        owner = ""
    if owner and owner in names:
        return ROUTE["G6"]
    return None


def is_fixed(path):
    # in any case: the filesystem here is case-insensitive
    return os.path.basename(path).lower() == "laws.md" or os.path.dirname(path).lower().endswith(
        ("/" + os.path.join(DOCS, "prompts")).lower()
    )


def g5(s, path):
    kind = s["kind"]
    if kind is None:
        return None
    if is_fixed(path):
        named = kind == "build" and any(
            path.endswith("/" + item.strip().lstrip("/")) for item in s["card"]["files"]
        )
        if not named:
            return ROUTE["G5 fixed"]
        # a named fixed file is still written inside the build's own fence only
    if kind in WORKERS:
        if under(path, VAULT_ROOT):
            return ROUTE["G5 fence"]
        if s["wt"] and under(path, os.path.join(WT_ROOT, s["wt"])):
            return None
        report = s["card"]["check report" if kind == "check" else "report"]
        if report and path == report:
            return None
        job = s["card"]["job"]
        if kind == "check" and job and under(path, os.path.join(WT_ROOT, SCRATCH, job + "-check")):
            return None  # G10: the check's own <S>
        return ROUTE["G5 fence"]
    if kind == "brain":
        docs = os.path.join(REPO_ROOT, DOCS)
        if under(path, os.path.join(docs, "reports")):
            return None
        if re.match(re.escape(os.path.join(docs, "prompts")) + r"/20[^/]*/", path):
            return None
        return ROUTE["G5 fence"]
    return None


# ---- G8 and main ---------------------------------------------------------------------------


def ledger(event, rule, what):
    try:
        sid = re.sub(r"[^A-Za-z0-9._-]", "_", str(event.get("session_id") or "unknown"))
        if sid.startswith("."):
            sid = "_" + sid
        folder = os.path.join(WT_ROOT, ".ledger")
        os.makedirs(folder, exist_ok=True)
        line = {
            "time": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
            "cwd": event.get("cwd") or "",
            "rule": rule,
            "command": what.encode("utf-8")[:200].decode("utf-8", "ignore"),
        }
        with open(os.path.join(folder, sid + ".jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
    except Exception:
        pass


def decide(event):
    """Return (rule, line, what the ledger records) for a deny, or None."""
    tool = event.get("tool_name")
    ti = event.get("tool_input")
    if not isinstance(ti, dict):
        return None
    if tool == "Bash":
        command = ti.get("command")
        if not isinstance(command, str):
            return None
        hit = bash_rules(command, seat(event))
        return hit + (command,) if hit else None
    path = ti.get("file_path")
    if not isinstance(path, str) or not path:
        return None
    if tool == "Read":
        return ("G3", ROUTE["G3"], path) if is_env(path) else None
    if tool in ("Write", "Edit"):
        s = seat(event)
        full = os.path.normpath(path if os.path.isabs(path) else os.path.join(s["cwd"] or "/", path))
        deny = g6(s, ti.get("content") if tool == "Write" else ti.get("new_string"))
        if deny:
            return "G6", deny, path
        deny = g5(s, full)
        if deny:
            return "G5", deny, path
    return None


def main():
    try:
        event = json.loads(sys.stdin.read())
        if not isinstance(event, dict):
            return 0
        hit = decide(event)
        if not hit:
            return 0
        rule, line, what = hit
        ledger(event, rule, what)
        sys.stderr.write(line + "\n")
        return 2
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
