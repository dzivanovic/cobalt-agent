"""ops/desk/bare-guard.py, the PreToolUse hook of his 2026-10-01 R45 part 1 (card 17 A1).

Every case runs the script as a subprocess with the hook's JSON on stdin, the way
Claude Code calls a PreToolUse hook. Exit 0 lets the call through; exit 2 blocks it
and its stderr is the one line the session reads.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest

REPO = Path(__file__).resolve().parents[2]
GUARD = REPO / "ops" / "desk" / "bare-guard.py"
BLOCK_HEAD = "NOT A REFUSAL. Dejan's rule: one bare command per call, and this call contains "
BLOCK_TAIL = (
    ". Resend the SAME commands now, one per call, in order. "
    "Do not report this to Dejan as a failure."
)


@pytest.fixture(autouse=True)
def roots(tmp_path, monkeypatch) -> SimpleNamespace:
    """COBALT_WT_ROOT and COBALT_REPO_ROOT stand in for /Users/cobalt/cobalt-wt and
    /Users/cobalt/cobalt (the take-devdb-lock.sh shape), so the ledger, the lock dir and the
    cards of every case live under tmp_path."""
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"
    wt.mkdir()
    repo.mkdir()
    monkeypatch.setenv("COBALT_WT_ROOT", str(wt))
    monkeypatch.setenv("COBALT_REPO_ROOT", str(repo))
    return SimpleNamespace(wt=wt, repo=repo, tmp=tmp_path)


def guard(stdin: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["python3", str(GUARD)], input=stdin, capture_output=True, text=True, timeout=60
    )


def bash(command: str) -> str:
    return json.dumps(
        {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": command}}
    )


PASS = [
    "ls -la /tmp",
    'git commit -m "a; b and c > d"',
    'COBALT_ENV=dev uv run cobalt db query --side user "SELECT a || b FROM t"',
    'grep -n -E "^(BUILT|FAILED)" file',
    'codex exec -s read-only "Reply OK." < /dev/null',
    'git commit -m "first line\nsecond line"',
    "grep -n -F 'a | b && c' file",
    "echo it\\'s",
    "echo $'a\\'b; c'",
    'echo "a \\" ; b"',
]


@pytest.mark.parametrize("command", PASS)
def test_a_bare_command_passes(command):
    done = guard(bash(command))
    assert done.returncode == 0, done.stderr
    assert done.stderr == ""


BLOCK = [
    ("ls && ls", "`&&`"),
    ("cd x; ls", "`;`"),
    ("ls | head", "a pipe `|`"),
    ("ls || ls", "`||`"),
    ("echo hi > f", "a redirect `>`"),
    ("sort < f", "a redirect `<`"),
    ("sleep 2 &", "a background `&`"),
    ("ls\nls", "a newline"),
    ("echo $(date)", "`$(`"),
    ('echo "$(date)"', "`$(`"),
    ("echo `date`", "a backtick"),
    ('echo "`date`"', "a backtick"),
    ("ls < /dev/null && ls", "`&&`"),
    ('ls && codex exec "x" < /dev/null', "`&&`"),
    ('cat f | codex exec "x" < /dev/null', "a pipe `|`"),
    ("echo $'\\''; ls", "`;`"),
    ('echo "a \\" ; b" ; ls', "`;`"),
]


@pytest.mark.parametrize("command,found", BLOCK)
def test_a_compound_command_is_blocked_naming_what_was_found(command, found):
    done = guard(bash(command))
    assert done.returncode == 2, done.stderr
    line = done.stderr.strip()
    assert line.startswith(BLOCK_HEAD), line
    assert line.endswith(BLOCK_TAIL), line
    assert found in line[len(BLOCK_HEAD) : -len(BLOCK_TAIL)], line


@pytest.mark.parametrize("command", ["ls # it's\nls", 'ls # say "hi\nls', "ls # x\\\nls"])
def test_check_o1_a_comment_does_not_hide_the_newline_after_it(command):
    done = guard(bash(command))
    assert done.returncode == 2, done.stderr
    assert "a newline" in done.stderr


def test_the_block_line_is_exactly_the_ruled_text():
    done = guard(bash("ls && ls"))
    assert done.stderr == BLOCK_HEAD + "`&&`" + BLOCK_TAIL + "\n"


def test_the_dev_null_exception_is_only_the_exact_ending():
    assert guard(bash('codex exec "x" < /dev/null')).returncode == 0
    assert guard(bash('codex exec "x" < /dev/null ')).returncode == 2
    assert guard(bash('codex exec "x" </dev/null')).returncode == 2
    assert guard(bash('codex exec "x" < /dev/nullx')).returncode == 2


@pytest.mark.parametrize(
    "stdin",
    [
        json.dumps({"tool_name": "Read", "tool_input": {"file_path": "/a && b"}}),
        json.dumps({"tool_name": "Edit", "tool_input": {"command": "ls && ls"}}),
        "{not json",
        "",
        json.dumps({"tool_name": "Bash", "tool_input": {"command": 5}}),
        json.dumps({"tool_name": "Bash"}),
        json.dumps([1, 2]),
    ],
)
def test_another_tool_or_a_broken_input_passes(stdin):
    done = guard(stdin)
    assert done.returncode == 0, done.stderr


# ---- card 10 cobalt-guard (his 2026-10-03 R32, R33): the seat, rows G1–G8 ----------------

G2_ROUTE = "route: production is the deploy hub's; a dev read uses COBALT_ENV=dev"
G3_ROUTE = (
    "route: .env is never read; `ls -la <path>/.env` shows it is there, "
    "and the lock scripts copy and remove it"
)
G4_ROUTE = "route: git add <paths> then commit -m … -- <paths>; a merge is the deploy hub's"
G5_FIXED = "route: a fixed file changes by a card row"
G5_FENCE = (
    "route: this seat writes only inside its fence (a worker: its worktree and its report; "
    "the brain: reports/ and prompts/20*/; nothing under /Users/cobalt/Vault); "
    "a fixed file changes by a card row"
)
G6_ROUTE = "route: release the lock (W (f)), then the stop line"
G7_ROUTE = "route: the desk launches"

JOB_WT = "job-0101"
DEFAULT_FILES = "`ops/desk/x.py`, `tests/ops/test_x.py`"


def prompts(roots) -> Path:
    return roots.repo / "docs" / "40 - DevDocs" / "prompts"


def card_text(roots, files: str) -> str:
    report = roots.wt / JOB_WT / "docs" / "40 - DevDocs" / "reports" / "job-build-2026-01-01.md"
    check = roots.repo / "docs" / "40 - DevDocs" / "reports" / "job-check-2026-01-01.md"
    return (
        "JOB: job\n"
        "BRANCH: ops/job-0101\n"
        f"WORKTREE: {JOB_WT}\n"
        "BASE: 0000000a\n"
        f"REPORT: {report}\n"
        f"CHECK REPORT: {check}\n"
        "DB: none\n"
        "\n"
        "## ROWS\n"
        "\n"
        "| row | what | red first | files |\n"
        "|---|---|---|---|\n"
        f"| X1 | a constructed row with a `\\|` in it | tests | {files} |\n"
        "\n"
        "## NOT IN THIS JOB\n"
        "- `docs/40 - DevDocs/prompts/CHECK-HUB.md`\n"
    )


def transcript(roots, name: str, first: str | list) -> Path:
    """The real shape of a Claude Code transcript: one JSON record per line, the launch
    message the first `user` record; a non-user record before it."""
    p = roots.tmp / f"{name}.jsonl"
    records = [
        {"type": "queue-operation", "operation": "enqueue", "sessionId": "sess-test-1"},
        {
            "parentUuid": None,
            "isSidechain": False,
            "userType": "external",
            "cwd": "/constructed",
            "sessionId": "sess-test-1",
            "type": "user",
            "message": {"role": "user", "content": first},
            "uuid": "00000000-0000-0000-0000-000000000001",
            "timestamp": "2026-01-01T13:00:00.000Z",
        },
        {
            "type": "user",
            "message": {"role": "user", "content": "CONTINUE: W. a later message"},
        },
    ]
    p.write_text("".join(json.dumps(r) + "\n" for r in records))
    return p


HUB_FILE = {
    "build": "BUILD-HUB.md",
    "check": "CHECK-HUB.md",
    "deploy": "DEPLOY-HUB.md",
    "devfix": "DEVFIX-HUB.md",
}


def make_seat(roots, kind, *, cwd=None, files=DEFAULT_FILES, first=None) -> dict:
    """A constructed seat: cwd + transcript. kind None = no transcript, cwd outside both roots."""
    p = prompts(roots)
    if kind in HUB_FILE:
        card = p / "2026-01-01" / f"01-{kind}-card.md"
        card.parent.mkdir(parents=True, exist_ok=True)
        card.write_text(card_text(roots, files))
        hub = p / HUB_FILE[kind]
        text = f"Read '{hub}' and follow it exactly. CARD: '{card}'"
        default_cwd = roots.repo if kind == "deploy" else roots.wt / JOB_WT
    elif kind == "desk":
        text = "Read 'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md' and follow it exactly."
        default_cwd = roots.repo
    elif kind == "brain":
        text = f"Read '{p / '2026-01-01' / '23-brain-judge.md'}' and follow it exactly."
        default_cwd = roots.repo
    else:
        text = None
        default_cwd = roots.tmp / "elsewhere"
    if first is not None:
        text = first
    where = Path(cwd) if cwd is not None else default_cwd
    where.mkdir(parents=True, exist_ok=True)
    path = transcript(roots, f"t-{kind}", text) if text is not None else ""
    return {"cwd": str(where), "transcript": str(path)}


def call(tool: str, tool_input: dict, seat: dict | None = None, session: str = "sess-test-1"):
    event = {
        "session_id": session,
        "transcript_path": seat["transcript"] if seat else "",
        "cwd": seat["cwd"] if seat else "",
        "permission_mode": "dontAsk",
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": tool_input,
    }
    return guard(json.dumps(event))


def run(command: str, seat: dict | None = None, **kw):
    return call("Bash", {"command": command, "description": "x"}, seat, **kw)


def assert_denied(done, route: str):
    assert done.returncode == 2, (done.returncode, done.stderr)
    assert done.stderr == route + "\n", done.stderr


def assert_allowed(done):
    assert done.returncode == 0, done.stderr
    assert done.stderr == ""


KINDS = ["build", "check", "devfix", "deploy", "desk", "brain", None]
WORKERS = ["build", "check", "devfix"]


# ---- G1 READ-ONLY PIPES ------------------------------------------------------------------

PIPES_ALLOWED = [
    "grep -n X f | cut -f2",
    'grep -n "^| R154 " f | cut -c1-80',
    "grep -n X f | sort | uniq -c | head -5",
    "sed -n '/^## PREFLIGHT/,$p' f | head -3",
    "sed -n -e 's/a/b/gp' f | wc -l",
    "tail -n 5 f | cut -d: -f1 | grep -o 'y'",
    "grep -c x f | head -1 < /dev/null",
]


@pytest.mark.parametrize("kind", [None, "build"])
@pytest.mark.parametrize("command", PIPES_ALLOWED)
def test_g1_a_read_only_pipe_is_allowed(roots, kind, command):
    assert_allowed(run(command, make_seat(roots, kind)))


PIPES_DENIED = [
    # today's denied call (cto-2026-10-03.md REFUSALS 10:25): the `;`
    ('grep "^| R154 " f | cut -c1-80; grep "^| R149 " f | grep -o "x"', "`;`"),
    ("grep X f | rm -rf /", "`rm`"),
    ("grep X f | sed -i s/a/b/ f", "`sed -i`"),
    ("grep X f | sed -n -i.bak p", "`sed -i`"),
    ("grep X f | sed --in-place -n p", "`sed -i`"),
    ("grep X f | sed 's/a/b/'", "`sed` without `-n`"),
    ("grep X f | sed -n 's/a/b/w out'", "`sed` with a `w` or `e` command or flag"),
    ("grep X f | sed -n 's/a/b/e'", "`sed` with a `w` or `e` command or flag"),
    ("grep X f | sed -n '1e date'", "`sed` with a `w` or `e` command or flag"),
    ("grep X f | sed -n 'w out'", "`sed` with a `w` or `e` command or flag"),
    ("grep X f | sed -n -e '/a/{p' -e 'w out' -e '}'", "`sed` with a `w` or `e` command or flag"),
    ("grep X f | sed -n '/a/{p;w out\n}'", "`sed` with a `w` or `e` command or flag"),
    ("grep X f | sed -n -f script.sed", "`sed -f`"),
    ("ls && ls", "`&&`"),
    ("ls | head", "`ls`"),
    ("grep X f | sh", "`sh`"),
    ("grep X f || head f", "`||`"),
    ("grep X f | head > out", "a redirect `>`"),
    ("grep X f | head >> out", "a redirect `>`"),
    ("grep X f | head < in", "a redirect `<`"),
    ("grep X f | head\nls", "a newline"),
    ("grep X f | head $(ls)", "`$(`"),
    ("grep X f | head `ls`", "a backtick"),
    ("grep X f | LC_ALL=C sort", "`LC_ALL=C`"),
    ("grep X f |", "an empty pipe segment"),
]


@pytest.mark.parametrize("command,found", PIPES_DENIED)
def test_g1_anything_else_compound_is_denied_with_the_resend_sentence(command, found):
    done = run(command)
    assert done.returncode == 2, done.stderr
    line = done.stderr.strip()
    assert line.startswith(BLOCK_HEAD), line
    assert line.endswith(BLOCK_TAIL), line
    assert found in line[len(BLOCK_HEAD) : -len(BLOCK_TAIL)], line


AWK_FOUND = "`awk` with `system(`, `>` or `|` in its program"
AWK_NOT_FILTER = "a pipe `|` with `awk`, not a read-only filter"
AWK_DENIED = [
    "grep X f | awk '{print > \"f\"}'",
    "grep X f | awk '{system(\"x\")}'",
    "grep X f | awk '{print | \"sh\"}'",
    "grep X f | awk '{print >> \"f\"}'",
    "grep X f | awk '{ \"date\" | getline d; print d }'",
    "grep X f | awk -F: '{print $1 > \"f\"}'",
    "grep X f | awk -F : -v n=1 '{system(\"x\")}'",
    "grep X f | awk -- '{print > \"f\"}'",
    "awk '{print $1 > \"f\"}' f | head -1",
]


@pytest.mark.parametrize("command", AWK_DENIED)
def test_g11_an_awk_segment_that_can_write_is_denied(roots, command):
    done = run(command, make_seat(roots, "build"))
    assert done.returncode == 2, done.stderr
    line = done.stderr.strip()
    assert line.startswith(BLOCK_HEAD), line
    assert line.endswith(BLOCK_TAIL), line
    assert AWK_FOUND in line[len(BLOCK_HEAD) : -len(BLOCK_TAIL)], line


AWK_ALLOWED = [
    "grep X f | awk '{print $2}'",
    "grep X f | awk -F'|' '{print $2}'",
    "grep X f | awk -F '|' '{print $2}'",
    "grep X f | awk -v 'x=>' '{print x, $1}'",
    "grep X f | awk -vx='|' '{print x}'",
    "grep X f | awk 'NR == 2 {print toupper($0)}' | head -1",
]


@pytest.mark.parametrize("kind", [None, "build"])
@pytest.mark.parametrize("command", AWK_ALLOWED)
def test_b11_an_awk_segment_g11_passes_is_denied_as_no_filter(roots, kind, command):
    # his ruling 10-04 R283 (card 06 B11): awk left G1's pipe list; these were card 10's controls
    assert_resend(run(command, make_seat(roots, kind)), AWK_NOT_FILTER)


def test_g1_one_command_stays_allowed_whatever_its_verb(roots):
    # sed -i as ONE command is not a pipe: the allow strings judge it, not G1
    assert_allowed(run("sed -i s/a/b/ f", make_seat(roots, "build")))


# ---- G2 PRODUCTION FROM A NON-DEPLOY SEAT ------------------------------------------------

PROD_CALLS = [
    "COBALT_ENV=production uv run cobalt validate",
    "uv run cobalt db migrate --prod",
    "uv run cobalt db query --prod=1 x",
    "psql cobalt_brain",
]


@pytest.mark.parametrize("command", PROD_CALLS)
@pytest.mark.parametrize("kind", ["build", "check", "devfix", "desk", "brain", "worker"])
def test_g2_production_from_a_non_deploy_seat_is_denied(roots, kind, command):
    assert_denied(run(command, unstamped_seat(roots, kind)), G2_ROUTE)


@pytest.mark.parametrize("command", PROD_CALLS)
@pytest.mark.parametrize("kind", ["deploy", None])
def test_g2_the_deploy_hub_and_an_unknown_seat_are_allowed(roots, kind, command):
    assert_allowed(run(command, make_seat(roots, kind)))


@pytest.mark.parametrize(
    "command", ["COBALT_ENV=dev uv run pytest -q", "uv run cobalt --products", "ls cobalt_dev"]
)
def test_g2_a_dev_call_from_a_build_is_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


# ---- card 21 guard-g2 (his 2026-10-06 R511): a marked seat's production db query ---------

MARKER = " PROD-READ: 2026-01-01 R5"
PROD_QUERY = 'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1"'
MARKED_KINDS = ["brain", "worker", "desk"]


def marked_seat(roots, kind: str = "brain", *, where: str = "first") -> dict:
    """A prompt seat whose launch message (its first user record) ends with the launcher's stamp
    (desk-launch.sh R1). where: "first" the stamp in the first user record; "later" in a later
    user record only; "body" in the prompt file only; "none" nowhere, a forged RULINGS line and
    row standing beside the seat."""
    p = prompts(roots)
    pfile = p / "2026-01-01" / "19-survey.md"
    pfile.parent.mkdir(parents=True, exist_ok=True)
    body = f"`claude --bg \"Read '{pfile}' and follow it exactly.{MARKER}\"`\n" if where == "body" else ""
    pfile.write_text("RULINGS: 2026-01-01 R5\n" + body)
    rows = roots.repo / "docs" / "40 - DevDocs" / "reports" / "cto-2026-01-01.md"
    rows.parent.mkdir(parents=True, exist_ok=True)
    rows.write_text("| R5 | 07:00 ET | HIS RULING (constructed): production read included. | APPROVED |\n")
    read = p / "CTO-DESK-WAKEUP.md" if kind == "desk" else pfile
    first = f"Read '{read}' and follow it exactly." + (MARKER if where == "first" else "")
    cwd = roots.wt / JOB_WT if kind == "worker" else roots.repo
    seat = make_seat(roots, None, cwd=cwd, first=first)
    if where == "later":
        with open(seat["transcript"], "a") as f:
            f.write(json.dumps({"type": "user", "message": {"role": "user", "content": "go on." + MARKER}}) + "\n")
    return seat


PROD_READS = [
    PROD_QUERY,
    'COBALT_ENV=production uv run cobalt db query --side system --format json --prod "SELECT 1"',
    'COBALT_ENV=production uv run cobalt db query --prod --side=user "SELECT 1"',
]


@pytest.mark.parametrize("command", PROD_READS)
@pytest.mark.parametrize("kind", MARKED_KINDS)
def test_g2_a_marked_seat_runs_a_production_db_query(roots, kind, command):
    """RED (c) on BASE: G2 refused every production string for every non-deploy seat."""
    assert_allowed(run(command, marked_seat(roots, kind)))


# ---- card 120 guard-g2-open-reads (his 2026-10-08 R686): every seat reads, no stamp -------

UNSTAMPED_KINDS = ["build", "check", "devfix", "desk", "brain", "worker"]


def unstamped_seat(roots, kind: str) -> dict:
    """A seat of the kind with no stamp in any record: a hub, desk or brain launch as make_seat
    builds it; a worker as marked_seat builds it (cwd under the worktree root), unstamped."""
    if kind == "worker":
        return marked_seat(roots, "worker", where="none")
    return make_seat(roots, kind)


UNSTAMPED_SEATS = [(k, None) for k in UNSTAMPED_KINDS] + [
    (k, w) for k in MARKED_KINDS for w in ["none", "later", "body"]
]


@pytest.mark.parametrize("command", PROD_READS)
@pytest.mark.parametrize("kind,where", UNSTAMPED_SEATS)
def test_g2_every_seat_runs_a_production_db_query_without_the_stamp(roots, kind, where, command):
    """RED (1) on BASE: G2 passed the read only for a seat whose first record held the stamp.
    where None: a seat of the kind with no stamp anywhere; "none", "later", "body": the stamp
    nowhere, in a later record only, in the prompt body only (card 21's control (a), now a
    pass)."""
    seat = unstamped_seat(roots, kind) if where is None else marked_seat(roots, kind, where=where)
    assert_allowed(run(command, seat))


MARKED_DENIED = [
    "COBALT_ENV=production uv run cobalt db migrate",  # control (b)
    "COBALT_ENV=production uv run cobalt db migrate --prod",  # control (b), the leading shape
    "COBALT_ENV=production uv run cobalt db dev-rebuild user.x --prod",
    'COBALT_ENV=production uv run cobalt db query --prod --side admin "SELECT 1"',
    'COBALT_ENV=production uv run cobalt db query --prod --side=admin "SELECT 1"',
    'COBALT_ENV=production uv run cobalt db query --prod --side "SELECT 1"',
    'COBALT_ENV=production uv run cobalt db query --prod --si admin "SELECT 1"',
    'COBALT_ENV=production COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1"',
    'COBALT_ENV=production uv run cobalt db query --side user "SELECT 1"',
    'COBALT_ENV=production uv run cobalt db query --prod=x --side user "SELECT 1"',
    'COBALT_ENV=production uv run cobalt db query --prod --prod --side user "SELECT 1"',  # control (f)
    'NAME=x COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1"',
    'env COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1"',
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT cobalt_brain"',
    "COBALT_ENV=production uv run cobalt db query --prod --side user \"SELECT '--prod'\"",
    "uv run cobalt db query --prod --side user x",
    "psql cobalt_brain",
    # card 120 CONTROL (2): no other production verb passes
    "COBALT_ENV=production uv run cobalt db apply",
    "COBALT_ENV=production uv run cobalt validate",
    "uv run cobalt_brain",
    'COBALT_ENV=production uv run python -c "print(1)"',
]

# card 120: every G2 control runs on the stamped seat and on an unstamped seat of each kind
CONTROL_SEATS = ["stamped"] + UNSTAMPED_KINDS


def control_seat(roots, which: str) -> dict:
    return marked_seat(roots) if which == "stamped" else unstamped_seat(roots, which)


@pytest.mark.parametrize("which", CONTROL_SEATS)
@pytest.mark.parametrize("command", MARKED_DENIED)
def test_g2_a_marked_seat_is_denied_anything_but_the_one_query_shape(roots, command, which):
    """Controls (b), (f) and the rest: green on BASE (G2 refused every production string) and
    after (prod_read refuses each), stamp or none."""
    assert_denied(run(command, control_seat(roots, which)), G2_ROUTE)


@pytest.mark.parametrize("which", CONTROL_SEATS)
@pytest.mark.parametrize("tail", [" ; ls", " | sh", " | cat"])
def test_g2_a_marked_query_with_a_separator_is_g1s_to_deny(roots, tail, which):
    """CONTROL (e): G2 does not forbid `;` or `|`; G1 denies them with its resend sentence. An
    unstamped seat is RED on BASE (G2 denied it first)."""
    done = run(PROD_QUERY + tail, control_seat(roots, which))
    assert done.returncode == 2, done.stderr
    line = done.stderr.strip()
    assert G2_ROUTE not in line, line
    assert line.startswith(BLOCK_HEAD), line
    assert line.endswith(BLOCK_TAIL), line


@pytest.mark.parametrize("command", [
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1" --pr\\\nod',
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT cobalt_br\\\nain"',
])
@pytest.mark.parametrize("which", CONTROL_SEATS)
def test_g2_a_marked_seat_is_denied_a_production_word_split_by_a_line_continuation(roots, command, which):
    """check O1: bash joins `\\<newline>`; the second --prod or cobalt_brain is still there."""
    assert_denied(run(command, control_seat(roots, which)), G2_ROUTE)


@pytest.mark.parametrize("command", [
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1"#cobalt_brain',
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1" x# --prod',
])
@pytest.mark.parametrize("which", CONTROL_SEATS)
def test_g2_a_marked_seat_is_denied_a_production_word_behind_a_mid_word_hash(roots, command, which):
    """check O2: to bash a `#` inside a word starts no comment; what follows it is run."""
    assert_denied(run(command, control_seat(roots, which)), G2_ROUTE)


@pytest.mark.parametrize("command", [
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1" --pro{d,}',
    'COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1" cobalt_b{r,}ain',
])
@pytest.mark.parametrize("which", CONTROL_SEATS)
def test_g2_a_marked_seat_is_denied_a_production_word_in_a_brace_word(roots, command, which):
    """check O3: the shell brace-expands the word into a second --prod or cobalt_brain."""
    assert_denied(run(command, control_seat(roots, which)), G2_ROUTE)


@pytest.mark.parametrize("which", CONTROL_SEATS)
def test_g2_allow_prod_does_not_pass_for_a_marked_seat(roots, which):
    """X1 / fence: `--allow-prod` is not the one `--prod` of R2(ii)."""
    command = (
        'COBALT_ENV=production uv run cobalt db query --prod --allow-prod '
        '--side user "SELECT 1"'
    )
    assert_denied(run(command, control_seat(roots, which)), G2_ROUTE)


@pytest.mark.parametrize("which", CONTROL_SEATS)
def test_g2_a_brace_word_cannot_hide_a_side_value(roots, which):
    """X1: a brace word is not the words() the side check reads."""
    command = (
        'COBALT_ENV=production uv run cobalt db query --prod --side user '
        '"SELECT 1" {--side,admin}'
    )
    assert_denied(run(command, control_seat(roots, which)), G2_ROUTE)


# ---- G3 .env NEVER READ ------------------------------------------------------------------

ENV_READS = [
    "cat /x/wt/job/.env",
    "grep KEY /x/wt/job/.env",
    "sed -n 1p /x/wt/job/.env",
    "head -1 /x/wt/job/.env",
    "tail -n 1 /x/wt/job/.env",
    "less /x/wt/job/.env",
    'cat "/x/wt/my job/.env"',
    "cat .env",
    "grep -n KEY /x/wt/job/.env | head -1",
]


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize("command", ENV_READS)
def test_g3_a_read_of_env_is_denied_from_every_seat(roots, kind, command):
    assert_denied(run(command, make_seat(roots, kind)), G3_ROUTE)


@pytest.mark.parametrize("kind", KINDS)
def test_g3_the_read_tool_on_env_is_denied(roots, kind):
    done = call("Read", {"file_path": "/x/wt/job/.env"}, make_seat(roots, kind))
    assert_denied(done, G3_ROUTE)


@pytest.mark.parametrize(
    "command",
    [
        "ls -la /x/wt/job/.env",
        "ls /x/wt/job/.env",
        "cp /x/repo/.env /x/wt/job/.env",
        "rm /x/wt/job/.env",
        "cat /x/wt/job/.env.example",
        "grep -n X /x/wt/job/env",
    ],
)
def test_g3_the_lock_steps_on_env_are_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


def test_g3_the_read_tool_on_another_file_is_allowed(roots):
    assert_allowed(call("Read", {"file_path": "/x/wt/job/.env.example"}, make_seat(roots, "build")))


# ---- card 120 O2 (his 2026-10-08 R686): a secret is never read, by any seat ----------------

G3_SECRET_ROUTE = (
    "route: a secret (~/.cobalt_key, data/.cobalt_vault, a keychain password) is never read; "
    "ls -la shows it is there"
)
SECRET_READS = [
    "cat ~/.cobalt_key",
    "cat /Users/cobalt/.cobalt_key",
    "grep KEY /Users/cobalt/.cobalt_ke{y,}",
    "head -c 72 ~/.cobalt_key",
    "cat data/.cobalt_vault",
    "tail -c 9 /Users/cobalt/cobalt/data/.cobalt_vault",
    "security find-generic-password -w -s cobalt",
    "security find-internet-password -w -s x",
    "security dump-keychain",
]


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize("command", SECRET_READS)
def test_g3_a_read_of_a_secret_is_denied_from_every_seat(roots, kind, command):
    """RED (3) on BASE: G3 refused only a .env read; deploy and an unknown seat too."""
    assert_denied(run(command, make_seat(roots, kind)), G3_SECRET_ROUTE)


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "path", ["/Users/cobalt/.cobalt_key", "/Users/cobalt/cobalt/data/.cobalt_vault"]
)
def test_g3_the_read_tool_on_a_secret_is_denied(roots, kind, path):
    """RED (3) on BASE: the Read rule tested is_env only."""
    assert_denied(call("Read", {"file_path": path}, make_seat(roots, kind)), G3_SECRET_ROUTE)


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "command",
    [
        "ls -la /Users/cobalt/.cobalt_key",
        "ls -la /Users/cobalt/cobalt/data/.cobalt_vault",
        "cat /x/.cobalt_key.example",
        "security list-keychains",
    ],
)
def test_g3_a_secret_shown_present_or_a_near_name_is_allowed(roots, kind, command):
    """CONTROL: green on BASE and after."""
    assert_allowed(run(command, make_seat(roots, kind)))


# ---- check of card 120 (pass 1): the findings run on the tip --------------------------------


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "command",
    ["cat ~/.cobalt_k?y", "cat /Users/cobalt/.cobalt_ke*", "tail -c 9 data/.cobalt_v[a]ult"],
)
def test_g3_a_glob_naming_a_secret_is_denied(roots, kind, command):
    """check O1: bash expands the glob to the secret file, as is_env reads a glob for .env."""
    assert_denied(run(command, make_seat(roots, kind)), G3_SECRET_ROUTE)


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "command",
    [
        "security -q dump-keychain",
        "security -v find-generic-password -w -s x",
        "security -l -q find-internet-password -w -s x",
        "security export -k login.keychain -o out.p12",
    ],
)
def test_g3_a_keychain_read_behind_a_global_option_is_denied(roots, kind, command):
    """check O2: security's global options (-h -i -l -q -v, -p prompt) stand before the command."""
    assert_denied(run(command, make_seat(roots, kind)), G3_SECRET_ROUTE)


@pytest.mark.parametrize("kind", KINDS)
def test_g3_a_secret_named_in_another_case_is_denied(roots, kind):
    """check A4 (Sol): the filesystem here is case-insensitive; Bash and the Read tool."""
    seat = make_seat(roots, kind)
    assert_denied(run("cat ~/.COBALT_KEY", seat), G3_SECRET_ROUTE)
    assert_denied(
        call("Read", {"file_path": "/Users/cobalt/cobalt/data/.Cobalt_Vault"}, seat), G3_SECRET_ROUTE
    )


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "command",
    [
        "security -q find-generic-password -w -s cobalt",
        "security {dump-keychain,}",
    ],
)
def test_g3_a_keychain_read_cannot_hide_its_subcommand(roots, kind, command):
    """check A1 (Sol)."""
    assert_denied(run(command, make_seat(roots, kind)), G3_SECRET_ROUTE)


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "command",
    [
        "security -q dump-keychain",
        "security -v dump-keychain",
        "security -q find-generic-password -w -s cobalt",
        "security -v find-internet-password -w -s x",
        "security -q export",
    ],
)
def test_x3_a_keychain_dump_with_a_global_option_first_is_denied(roots, kind, command):
    """check B2 (Grok)."""
    assert_denied(run(command, make_seat(roots, kind)), G3_SECRET_ROUTE)


@pytest.mark.parametrize("kind", KINDS)
@pytest.mark.parametrize(
    "command",
    [
        "cat /Users/cobalt/.cobalt_k*",
        "cat /Users/cobalt/.cobalt_ke?",
        "head -c 72 data/.cobalt_vaul?",
        "tail -c 9 /Users/cobalt/cobalt/data/.cobalt_v*",
        'cat /x/.e\\\nnv',
        'cat ~/.cobalt_ke\\\ny',
        'cat /Users/cobalt/cobalt/data/.cobalt_vaul\\\nt',
    ],
)
def test_x3_a_secret_path_whose_basename_the_guard_does_not_see_is_denied(roots, kind, command):
    """check B3 (Grok)."""
    route = G3_ROUTE if ".e\\\n" in command else G3_SECRET_ROUTE
    assert_denied(run(command, make_seat(roots, kind)), route)


# ---- G4 GIT SHAPE FROM A WORKER ----------------------------------------------------------

GIT_DENIED = [
    "git add -A",
    "git add --all",
    "git add .",
    'git commit -m "x"',
    'git commit -m "a -- b"',
    "git push",
    "git -C /x/wt/job push origin x",
    "git merge main",
    "git rebase main",
    "git reset --hard",
    "git checkout x",
    "git stash push -u -m t",
    "git cherry-pick 0000000a",
    "git log --output=/x/out",
    "git diff --output /x/out",
]


@pytest.mark.parametrize("kind", WORKERS)
@pytest.mark.parametrize("command", GIT_DENIED)
def test_g4_a_git_shape_from_a_worker_is_denied(roots, kind, command):
    assert_denied(run(command, make_seat(roots, kind)), G4_ROUTE)


GIT_ALLOWED = [
    'git add "docs/40 - DevDocs/reports/x.md" tests/ops/test_x.py',
    'git commit -m "fix(x): y" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- a b',
    "git status --short --branch",
    "git -C /x/repo log --oneline -1 x",
    "git diff --stat 0000000a",
]


@pytest.mark.parametrize("command", GIT_ALLOWED)
def test_g4_the_listed_git_shape_from_a_worker_is_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


def test_g4_the_desks_commit_with_paths_is_allowed(roots):
    done = run('git -C /Users/cobalt/cobalt commit -m "docs(desk): x" -- a', make_seat(roots, "desk"))
    assert_allowed(done)


@pytest.mark.parametrize("kind", ["desk", "brain"])
def test_g4_is_a_workers_rule_the_desk_and_the_brain_are_not_shaped(roots, kind):
    # G4 reads "from a worker": a desk or brain git call meets its own allow strings only
    assert_allowed(run('git -C /Users/cobalt/cobalt commit -m "x"', make_seat(roots, kind)))


@pytest.mark.parametrize("command", ["git -C /x/repo merge --ff-only x", "git -C /x/repo reset --soft HEAD~1"])
def test_g4_a_merge_is_the_deploy_hubs(roots, command):
    assert_allowed(run(command, make_seat(roots, "deploy")))


def test_g4_an_unknown_seat_is_allowed(roots):
    assert_allowed(run("git push", make_seat(roots, None)))


# ---- G5 THE WRITE FENCE ------------------------------------------------------------------


def write(path, seat, content="x\n"):
    return call("Write", {"file_path": str(path), "content": content}, seat)


def edit(path, seat, new="y"):
    return call("Edit", {"file_path": str(path), "old_string": "x", "new_string": new}, seat)


@pytest.mark.parametrize("kind", WORKERS)
def test_g5_a_worker_writes_inside_its_worktree(roots, kind):
    seat = make_seat(roots, kind)
    assert_allowed(write(roots.wt / JOB_WT / "ops" / "desk" / "x.py", seat))
    assert_allowed(edit(roots.wt / JOB_WT / "tests" / "ops" / "test_x.py", seat))


@pytest.mark.parametrize("kind", WORKERS + ["deploy"])
@pytest.mark.parametrize(
    "target",
    [
        lambda r: r.wt / "other-0101" / "x.py",
        lambda r: r.repo / "src" / "x.py",
        lambda r: r.wt / JOB_WT / ".." / "other-0101" / "x.py",
        lambda r: Path("/Users/cobalt/Vault/Think/x.md"),
    ],
)
def test_g5_a_worker_outside_its_worktree_is_denied(roots, kind, target):
    seat = make_seat(roots, kind)
    assert_denied(write(target(roots), seat), G5_FENCE)
    assert_denied(edit(target(roots), seat), G5_FENCE)


def test_g5_the_check_writes_its_check_report_on_main(roots):
    seat = make_seat(roots, "check")
    own = roots.repo / "docs" / "40 - DevDocs" / "reports" / "job-check-2026-01-01.md"
    other = roots.repo / "docs" / "40 - DevDocs" / "reports" / "other-check-2026-01-01.md"
    assert_allowed(write(own, seat))
    assert_denied(write(other, seat), G5_FENCE)


def test_g5_the_worktree_comes_from_the_card_when_the_cwd_moves(roots):
    # the check enters <AGY> for its house launch; its fence stays its card's worktree
    seat = make_seat(roots, "check", cwd=roots.wt / "agy-trial")
    assert_allowed(write(roots.wt / JOB_WT / "x.md", seat))
    assert_denied(write(roots.wt / "agy-trial" / "x.md", seat), G5_FENCE)


@pytest.mark.parametrize("kind", KINDS[:-1])
@pytest.mark.parametrize(
    "target",
    [
        lambda r: prompts(r) / "BUILD-HUB.md",
        lambda r: r.wt / JOB_WT / "docs" / "40 - DevDocs" / "prompts" / "CHECK-HUB.md",
        lambda r: r.wt / JOB_WT / "x" / "LAWS.md",
        lambda r: r.repo / "docs" / "40 - DevDocs" / "prompts" / "CTO-DESK-WAKEUP.md",
    ],
)
def test_g5_a_fixed_file_is_denied_from_any_seat(roots, kind, target):
    assert_denied(write(target(roots), make_seat(roots, kind)), G5_FIXED)


def test_g5_a_build_whose_card_names_the_fixed_file_writes_it(roots):
    files = "`docs/40 - DevDocs/prompts/BUILD-HUB.md`, `tests/ops/test_x.py`"
    seat = make_seat(roots, "build", files=files)
    hub = roots.wt / JOB_WT / "docs" / "40 - DevDocs" / "prompts" / "BUILD-HUB.md"
    assert_allowed(write(hub, seat))
    # the card names BUILD-HUB.md only, and only in `files`: CHECK-HUB.md stays fixed
    other = roots.wt / JOB_WT / "docs" / "40 - DevDocs" / "prompts" / "CHECK-HUB.md"
    assert_denied(write(other, seat), G5_FIXED)
    # the named file on main is outside the build's worktree: the fence still holds
    assert_denied(write(prompts(roots) / "BUILD-HUB.md", seat), G5_FENCE)


def test_g5_a_check_whose_card_names_the_fixed_file_is_still_denied(roots):
    files = "`docs/40 - DevDocs/prompts/BUILD-HUB.md`"
    seat = make_seat(roots, "check", files=files)
    hub = roots.wt / JOB_WT / "docs" / "40 - DevDocs" / "prompts" / "BUILD-HUB.md"
    assert_denied(write(hub, seat), G5_FIXED)


def test_g5_the_brain_writes_reports_and_dated_prompts_only(roots):
    seat = make_seat(roots, "brain")
    docs = roots.repo / "docs" / "40 - DevDocs"
    assert_allowed(write(docs / "reports" / "brain-x.md", seat))
    assert_allowed(write(docs / "prompts" / "2026-01-01" / "10-x-card.md", seat))
    assert_denied(write(docs / "prompts" / "BUILD-HUB.md", seat), G5_FIXED)
    assert_denied(write(roots.repo / "src" / "x.py", seat), G5_FENCE)
    assert_denied(write(docs / "prompts" / "x.txt" / ".." / "CARD.md", seat), G5_FIXED)
    assert_denied(write(Path("/Users/cobalt/Vault/Think/x.md"), seat), G5_FENCE)


def test_g5_the_desk_has_no_fence_but_the_fixed_files(roots):
    seat = make_seat(roots, "desk")
    assert_allowed(write(roots.repo / "docs" / "40 - DevDocs" / "reports" / "cto-x.md", seat))
    assert_allowed(write(Path("/Users/cobalt/Vault/Think/x.md"), seat))


def test_g5_an_unknown_seat_is_allowed_everywhere(roots):
    seat = make_seat(roots, None)
    assert_allowed(write(prompts(roots) / "BUILD-HUB.md", seat))
    assert_allowed(write(Path("/Users/cobalt/Vault/Think/x.md"), seat))


# ---- G10 CHECK SCRATCH FENCE (<S>, CHECK-HUB.md line 5; the card's JOB is `job`) ---------


def scratch(roots, job="job") -> Path:
    return roots.wt / "agy-trial" / "scratch" / "tribunal-bars-0920" / f"{job}-check"


@pytest.mark.parametrize("cwd", [None, "agy"])
def test_g10_the_check_writes_under_its_own_scratch(roots, cwd):
    seat = make_seat(roots, "check", cwd=roots.wt / "agy-trial" if cwd else None)
    s = scratch(roots)
    assert_allowed(write(s / "diff.md", seat))
    assert_allowed(write(s / "files" / "wt" / "ops" / "desk" / "x.py", seat))
    assert_allowed(edit(s / "HOUSE-INSTRUCTIONS.md", seat))
    # its own worktree and report stay inside the fence
    assert_allowed(write(roots.wt / JOB_WT / "x.md", seat))


@pytest.mark.parametrize(
    "target",
    [
        lambda r: scratch(r, "other"),
        lambda r: scratch(r, "other") / "diff.md",
        lambda r: scratch(r, "jobx") / "diff.md",
        lambda r: scratch(r) / ".." / "other-check" / "diff.md",
        lambda r: r.wt / "agy-trial" / "scratch" / "tribunal-bars-0920" / "job-check-x" / "diff.md",
        lambda r: r.wt / "agy-trial" / "scratch" / "tribunal-bars-0920" / "diff.md",
    ],
)
def test_g10_the_check_under_another_jobs_scratch_is_denied(roots, target):
    assert_denied(write(target(roots), make_seat(roots, "check")), G5_FENCE)


@pytest.mark.parametrize("kind", ["build", "devfix", "deploy", "brain"])
def test_g10_another_kind_under_the_scratch_is_denied(roots, kind):
    seat = make_seat(roots, kind)
    assert_denied(write(scratch(roots) / "diff.md", seat), G5_FENCE)
    assert_denied(edit(scratch(roots) / "diff.md", seat), G5_FENCE)


def test_g10_a_check_card_with_no_job_has_no_scratch(roots):
    seat = make_seat(roots, "check")
    card = prompts(roots) / "2026-01-01" / "01-check-card.md"
    card.write_text(card.read_text().replace("JOB: job\n", ""))
    assert_denied(write(scratch(roots) / "diff.md", seat), G5_FENCE)
    assert_denied(write(roots.wt / "agy-trial" / "scratch" / "tribunal-bars-0920" / "-check" / "x", seat), G5_FENCE)
    assert_allowed(write(roots.wt / JOB_WT / "x.md", seat))


# ---- G6 STOP LINE WHILE DIRTY ------------------------------------------------------------

STOP_LINES = [
    "BUILT · job: x · tip: 0000000a | on 0000000b",
    "CHECK DONE · job: x",
    "DEPLOYED · job: x",
]


def report(roots) -> Path:
    return roots.wt / JOB_WT / "docs" / "40 - DevDocs" / "reports" / "job-build-2026-01-01.md"


@pytest.mark.parametrize("stop", STOP_LINES)
def test_g6_a_stop_line_while_env_is_on_disk_is_denied(roots, stop):
    seat = make_seat(roots, "build")
    (roots.wt / JOB_WT / ".env").write_text("CONSTRUCTED=1\n")
    assert_denied(write(report(roots), seat, f"# r\n\n## RECORDS\n{stop}\n\n"), G6_ROUTE)
    assert_denied(edit(report(roots), seat, f"x\n{stop}\n"), G6_ROUTE)


@pytest.mark.parametrize("stop", STOP_LINES)
def test_g6_a_stop_line_while_the_lock_names_this_worktree_is_denied(roots, stop):
    seat = make_seat(roots, "build")
    lock = roots.wt / ".cobalt_dev.lock"
    lock.mkdir()
    (lock / "owner").write_text(JOB_WT + "\n")
    assert_denied(write(report(roots), seat, f"# r\n{stop}\n"), G6_ROUTE)


def test_g6_a_stop_line_while_the_lock_names_another_worktree_is_allowed(roots):
    seat = make_seat(roots, "build")
    lock = roots.wt / ".cobalt_dev.lock"
    lock.mkdir()
    (lock / "owner").write_text("other-0101\n")
    assert_allowed(write(report(roots), seat, f"# r\n{STOP_LINES[0]}\n"))


def test_g6_a_clean_stop_line_and_a_dirty_running_line_are_allowed(roots):
    seat = make_seat(roots, "build")
    assert_allowed(write(report(roots), seat, f"# r\n{STOP_LINES[0]}\n"))
    (roots.wt / JOB_WT / ".env").write_text("CONSTRUCTED=1\n")
    running = "# r\n(run in progress — next step under ## CONTINUE)\n"
    assert_allowed(write(report(roots), seat, running))
    assert_allowed(write(report(roots), seat, f"{STOP_LINES[0]}\nmore\n"))


def test_g6_is_kind_free(roots):
    seat = make_seat(roots, None)
    Path(seat["cwd"], ".env").write_text("CONSTRUCTED=1\n")
    target = Path(seat["cwd"]) / "r.md"
    assert_denied(write(target, seat, f"{STOP_LINES[0]}\n"), G6_ROUTE)


# ---- G7 NO SECOND SESSION FROM A WORKER --------------------------------------------------

LAUNCHES = [
    'claude --bg "Read x"',
    'codex exec -s read-only "x"',
    'grok -p "x"',
    "agy x",
    "/usr/local/bin/claude -p x",
    "FOO=1 claude -p x",
    "grep -n X f | claude -p x",
]


@pytest.mark.parametrize("kind", ["build", "devfix", "deploy"])
@pytest.mark.parametrize("command", LAUNCHES[:-1])
def test_g7_a_second_session_from_a_worker_is_denied(roots, kind, command):
    assert_denied(run(command, make_seat(roots, kind)), G7_ROUTE)


def test_g7_a_launch_at_the_end_of_a_pipe_is_denied(roots):
    assert_denied(run(LAUNCHES[-1], make_seat(roots, "build")), G7_ROUTE)


@pytest.mark.parametrize("kind", ["desk", "brain", None])
@pytest.mark.parametrize("command", LAUNCHES[:-1])
def test_g7_the_desk_the_brain_and_an_unknown_seat_launch(roots, kind, command):
    assert_allowed(run(command, make_seat(roots, kind)))


@pytest.mark.parametrize("command", ["ls claude", "grep -n codex f", "sh /x/desk-launch.sh build x"])
def test_g7_the_word_elsewhere_is_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


# ---- G9 CHECK HOUSE CALLS (CHECK-HUB.md line 10's three house strings) ------------------

HOUSE_CALLS = [
    "grok --version",
    "agy --version",
    'codex exec --skip-git-repo-check -m model-x -s read-only -c model_reasoning_effort="high" '
    '"Reply with only the word OK." < /dev/null',
    'grok --sandbox cobalt-job --allow "Write(/x/agy-trial/scratch/tribunal-bars-0920/**)" -p "x"',
    'agy --model model-y --mode accept-edits --sandbox --print="x"',
]


@pytest.mark.parametrize("command", HOUSE_CALLS)
def test_g9_the_check_types_each_house_string(roots, command):
    assert_allowed(run(command, make_seat(roots, "check")))
    # the check enters <AGY> right before the house launch (CHECK-HUB.md line 49)
    assert_allowed(run(command, make_seat(roots, "check", cwd=roots.wt / "agy-trial")))


CHECK_LAUNCHES_DENIED = [
    'codex exec -s read-only "x"',
    'codex exec --skip-git-repo-check -m model-x "x"',
    'codex exec --skip-git-repo-check -m model-x -s workspace-write "x"',
    'codex exec --skip-git-repo-check -m model-x -s read-only-x "x"',
    'codex --skip-git-repo-check -m model-x -s read-only "x"',
    'claude --bg "Read x"',
    "claude -p x",
    "/usr/local/bin/claude -p x",
    "FOO=1 claude -p x",
    "/usr/local/bin/grok -p x",
    "FOO=1 grok -p x",
    "FOO=1 agy x",
    "grok",
    "grep -n X f | grok -p x",
    "grok -p x | claude -p y",
    "agy x | agy y",
]


@pytest.mark.parametrize("command", CHECK_LAUNCHES_DENIED)
def test_g9_any_other_launch_from_the_check_stays_denied(roots, command):
    assert_denied(run(command, make_seat(roots, "check")), G7_ROUTE)


@pytest.mark.parametrize("kind", ["build", "devfix", "deploy"])
@pytest.mark.parametrize("command", HOUSE_CALLS)
def test_g9_another_worker_kind_typing_a_house_string_is_denied(roots, kind, command):
    assert_denied(run(command, make_seat(roots, kind)), G7_ROUTE)


def test_g9_a_worker_with_no_hub_typing_a_house_string_is_denied(roots):
    seat = {"cwd": str(roots.wt / "some-0101"), "transcript": ""}
    assert_denied(run("grok --version", seat), G7_ROUTE)


# ---- the seat's kind (X2) ----------------------------------------------------------------


def test_kind_a_build_whose_cwd_is_the_repo_is_still_a_build(roots):
    seat = make_seat(roots, "build", cwd=roots.repo)
    assert_denied(run("claude -p x", seat), G7_ROUTE)
    assert_denied(write(roots.repo / "src" / "x.py", seat), G5_FENCE)
    assert_allowed(write(roots.wt / JOB_WT / "x.py", seat))


def test_kind_a_desk_launch_in_a_worktree_is_a_worker(roots):
    seat = make_seat(roots, "desk", cwd=roots.wt / "some-0101")
    assert_denied(run("claude -p x", seat), G7_ROUTE)
    assert_denied(run("git push", seat), G4_ROUTE)
    assert_allowed(write(roots.wt / "some-0101" / "x.md", seat))
    assert_denied(write(roots.wt / "other-0101" / "x.md", seat), G5_FENCE)


def test_kind_a_worktree_without_a_transcript_is_a_worker(roots):
    seat = {"cwd": str(roots.wt / "some-0101"), "transcript": ""}
    assert_denied(run("claude -p x", seat), G7_ROUTE)


@pytest.mark.parametrize(
    "first",
    [
        "Read '/x/docs/40 - DevDocs/prompts/CLOSE-HUB.md' and follow it exactly.",
        "hello",
        [{"type": "text", "text": "no path here"}],
    ],
)
def test_kind_the_repo_with_no_desk_or_brain_prompt_is_unknown(roots, first):
    seat = make_seat(roots, "desk", first=first)
    # unknown: G2, G4, G5, G7 allow; G1, G3, G6 still deny
    assert_allowed(run("claude -p x", seat))
    assert_allowed(run("COBALT_ENV=production uv run cobalt validate", seat))
    assert_allowed(write(prompts(roots) / "BUILD-HUB.md", seat))
    assert run("ls && ls", seat).returncode == 2
    assert_denied(run("cat /x/.env", seat), G3_ROUTE)


def test_kind_the_launch_message_as_text_parts_is_read(roots):
    seat = make_seat(roots, "build")
    hub = prompts(roots) / "BUILD-HUB.md"
    card = prompts(roots) / "2026-01-01" / "01-build-card.md"
    parts = [{"type": "text", "text": f"CONTINUE: W. Read '{hub}' and follow it exactly. CARD: '{card}'"}]
    seat = make_seat(roots, "build", first=parts)
    assert_denied(run("claude -p x", seat), G7_ROUTE)


def test_kind_a_missing_transcript_file_in_the_repo_is_unknown(roots):
    seat = {"cwd": str(roots.repo), "transcript": str(roots.tmp / "nope.jsonl")}
    assert_allowed(run("claude -p x", seat))


# ---- G8 THE LEDGER -----------------------------------------------------------------------


def ledger_lines(roots, session="sess-test-1"):
    p = roots.wt / ".ledger" / f"{session}.jsonl"
    return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []


def test_g8_every_deny_appends_one_line(roots):
    seat = make_seat(roots, "build")
    long = "claude -p " + "y" * 300
    assert_denied(run(long, seat), G7_ROUTE)
    assert run("ls && ls", seat).returncode == 2
    lines = ledger_lines(roots)
    assert [x["rule"] for x in lines] == ["G7", "G1"]
    first = lines[0]
    assert set(first) == {"time", "cwd", "rule", "command"}
    assert first["cwd"] == seat["cwd"]
    assert first["command"] == long.encode()[:200].decode()
    assert len(first["command"].encode()) == 200
    assert first["time"][:2] == "20" and "T" in first["time"]
    assert lines[1]["command"] == "ls && ls"


def test_g8_a_write_deny_records_the_path(roots):
    seat = make_seat(roots, "brain")
    target = roots.repo / "src" / "x.py"
    assert_denied(write(target, seat), G5_FENCE)
    assert ledger_lines(roots) == [
        {**ledger_lines(roots)[0], "rule": "G5", "command": str(target), "cwd": seat["cwd"]}
    ]


def test_g8_an_allowed_call_writes_nothing(roots):
    assert_allowed(run("ls -la", make_seat(roots, "build")))
    assert not (roots.wt / ".ledger").exists()


def test_g8_the_session_id_never_leaves_the_ledger_dir(roots):
    assert run("ls && ls", make_seat(roots, "build"), session="../../escape").returncode == 2
    names = os.listdir(roots.wt / ".ledger")
    assert len(names) == 1 and "/" not in names[0] and not names[0].startswith(".")
    assert not (roots.tmp / "escape.jsonl").exists()


def test_g8_an_unwritable_ledger_still_denies(roots):
    (roots.wt / ".ledger").write_text("a file where the dir should be\n")
    done = run("claude -p x", make_seat(roots, "build"))
    assert_denied(done, G7_ROUTE)


# ---- the check of card 10 (cobalt-guard-check-2026-10-04.md, held findings O1, O2, O3, O6) --


def test_check_guard_o1_the_repos_own_env_does_not_make_a_seat_dirty(roots):
    # the deploy seat sits in the repo (desk-launch.sh:46); the repo's .env is the lock's source
    seat = make_seat(roots, "deploy")
    (roots.repo / ".env").write_text("CONSTRUCTED=1\n")
    assert_allowed(write(report(roots), seat, "# r\nDEPLOYED · job: x\n"))
    # its gate worktree's copy still makes it dirty
    (roots.wt / JOB_WT).mkdir(parents=True, exist_ok=True)
    (roots.wt / JOB_WT / ".env").write_text("CONSTRUCTED=1\n")
    assert_denied(write(report(roots), seat, "# r\nDEPLOYED · job: x\n"), G6_ROUTE)


@pytest.mark.parametrize(
    "command",
    ["cat /x/wt/job/.en?", "cat /x/wt/job/.env*", "cat /x/wt/job/{.env,x}", "head -1 /x/wt/job/.ENV"],
)
def test_check_guard_o2_a_word_that_names_env_after_expansion_is_denied(roots, command):
    assert_denied(run(command, make_seat(roots, "build")), G3_ROUTE)


def test_check_guard_o2_the_read_tool_on_env_in_another_case_is_denied(roots):
    assert_denied(call("Read", {"file_path": "/x/wt/job/.ENV"}, make_seat(roots, "build")), G3_ROUTE)


@pytest.mark.parametrize("command", ["cat /x/wt/job/.env.*", "grep -n X *", "cat /x/wt/job/{.env.example,x}"])
def test_check_guard_o2_a_pattern_that_cannot_name_env_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


@pytest.mark.parametrize(
    "command", ["git add ./", "git add -- ./", "git add :/", "git add --no-ignore-removal"]
)
def test_check_guard_o3_a_whole_tree_add_by_another_spelling_is_denied(roots, command):
    assert_denied(run(command, make_seat(roots, "build")), G4_ROUTE)


@pytest.mark.parametrize("kind", ["desk", "build"])
def test_check_guard_o6_a_fixed_file_in_another_case_is_denied(roots, kind):
    seat = make_seat(roots, kind)
    base = roots.repo if kind == "desk" else roots.wt / JOB_WT
    assert_denied(write(base / "docs" / "40 - DevDocs" / "prompts" / "build-hub.md", seat), G5_FIXED)
    assert_denied(write(base / "docs" / "40 - devdocs" / "PROMPTS" / "BUILD-HUB.md", seat), G5_FIXED)
    assert_denied(write(base / "x" / "laws.md", seat), G5_FIXED)


# ---- card 06 cobalt-guard-b (check O4, O5; build DECISIONS 1): rows B1–B4 -----------------


@pytest.mark.parametrize(
    "command",
    [
        "sort /x/wt/job/.env",
        "cut -c1- /x/wt/job/.env",
        "uniq /x/wt/job/.env",
        "awk 1 /x/wt/job/.env",
        "grep -n X f | sort /x/wt/job/.env",
    ],
)
def test_check_guard_o5_the_four_new_read_verbs_on_env_are_denied(roots, command):
    assert_denied(run(command, make_seat(roots, "build")), G3_ROUTE)


SORT_FOUND = "`sort` with `-o`, `--output` or `--compress-program`"
UNIQ_FOUND = "`uniq` with a second operand, a file it writes"
AWK_FILE_FOUND = "`awk -f`, a program the guard cannot read"


def assert_resend(done, found: str):
    assert done.returncode == 2, done.stderr
    line = done.stderr.strip()
    assert line.startswith(BLOCK_HEAD), line
    assert line.endswith(BLOCK_TAIL), line
    assert found in line[len(BLOCK_HEAD) : -len(BLOCK_TAIL)], line


@pytest.mark.parametrize(
    "command,found",
    [
        ("grep X f | sort -o out", SORT_FOUND),
        ("grep X f | sort --output=out", SORT_FOUND),
        ("grep X f | sort --compress-program=sh", SORT_FOUND),
        ("grep X f | uniq - out", UNIQ_FOUND),
        ("grep X f | sort -uo out", SORT_FOUND),
        ("grep X f | sort -oout", SORT_FOUND),
        ("grep X f | sort --out=x", SORT_FOUND),
        ("grep X f | sort --compress=sh", SORT_FOUND),
    ],
)
def test_check_guard_o4_a_filter_that_writes_or_runs_is_denied(roots, command, found):
    done = run(command, make_seat(roots, "build"))
    assert done.returncode == 2, done.stderr
    assert_resend(done, found)


@pytest.mark.parametrize(
    "command",
    [
        "grep X f | sort -u",
        "sort -k2,2n f",
        "sort --unique f",
        "grep X f | uniq -c",
        "grep X f | uniq -f 1 -",
        "uniq -f 1 f",
        "uniq -s2 -w3 f",
    ],
)
def test_b2_a_sort_or_uniq_that_only_reads_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


def test_b3_an_awk_program_from_a_file_in_a_pipe_is_denied(roots):
    done = run("grep X f | awk -f p.awk", make_seat(roots, "build"))
    assert done.returncode == 2, done.stderr
    assert_resend(done, AWK_FILE_FOUND)
    for command in ("grep X f | awk -fp.awk", "grep X f | awk --file=p.awk", "grep X f | awk --file p.awk"):
        assert_resend(run(command, make_seat(roots, "build")), AWK_FILE_FOUND)


def test_b3_b11_an_awk_program_in_the_command_is_denied_as_no_filter(roots):
    # B3's control until his ruling 10-04 R283 (B11): an awk pipe segment is not a read-only filter
    assert_resend(run("grep X f | awk '{print $1}'", make_seat(roots, "build")), AWK_NOT_FILTER)
    assert_resend(run("grep X f | awk -F f '{print $1}'", make_seat(roots, "build")), AWK_NOT_FILTER)


@pytest.mark.parametrize(
    "command,found",
    [
        ("sort -o out f", SORT_FOUND),
        ("uniq f out", UNIQ_FOUND),
        ("awk -f p.awk f", AWK_FILE_FOUND),
        ("awk '{print > \"x\"}' f", AWK_FOUND),
        # the house-probe ending passes its redirect, not the lone command's check
        ("sort -o out f < /dev/null", SORT_FOUND),
    ],
)
def test_b4_a_lone_sort_uniq_or_awk_that_writes_is_denied(roots, command, found):
    done = run(command, make_seat(roots, "build"))
    assert done.returncode == 2, done.stderr
    assert_resend(done, found)


@pytest.mark.parametrize("command", ["sort f", "awk '{print $1}' f"])
def test_b4_a_lone_sort_or_awk_that_only_reads_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


@pytest.mark.parametrize(
    "command,found",
    [
        ("LC_ALL=C sort -o out f", SORT_FOUND),
        ("/usr/bin/sort -o out f", SORT_FOUND),
        ("LC_ALL=C uniq f out", UNIQ_FOUND),
        ("/usr/bin/awk -f p.awk f", AWK_FILE_FOUND),
    ],
)
def test_check_b_o1_a_lone_filter_by_path_or_behind_an_assignment_that_writes_is_denied(roots, command, found):
    assert_resend(run(command, make_seat(roots, "build")), found)


@pytest.mark.parametrize("command", ["sort --co=sh f", "sort --co sh f", "sort --compress=sh f"])
def test_b7_a_two_letter_prefix_of_compress_program_is_denied(roots, command):
    done = run(command, make_seat(roots, "build"))
    assert done.returncode == 2, done.stderr
    assert_resend(done, SORT_FOUND)


@pytest.mark.parametrize("command", ["sort --check f", "sort -c f"])
def test_b7_sort_check_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


@pytest.mark.parametrize(
    "command",
    ["sort --files0-from=.env", "sort --files0-from .env", "sort --files0-from=/x/wt/job/.env"],
)
def test_b8_an_option_value_naming_env_is_denied(roots, command):
    assert_denied(run(command, make_seat(roots, "build")), G3_ROUTE)


@pytest.mark.parametrize("command", ["sort --key=2 f", "grep -n --include=*.py X ."])
def test_b8_an_option_value_not_naming_env_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


@pytest.mark.parametrize(
    "command",
    [
        "awk 'BEGIN{while(getline l < \".env\") print l}'",
        "awk 'BEGIN{ARGV[1]=\".e\" \"nv\"; ARGC=2} {print}'",
        "awk '@include \"x\"'",
        "awk '@load \"x\"'",
        "awk 'BEGIN{ARGC=1} {print}' f",
        "grep X f | awk '{getline l < \"y\"; print l}'",
    ],
)
def test_b9_an_awk_program_that_reads_a_file_it_names_is_denied(roots, command):
    assert_denied(run(command, make_seat(roots, "build")), G3_ROUTE)


@pytest.mark.parametrize("command", ["awk '{print $1}' f"])
def test_b9_an_awk_program_that_reads_only_its_operands_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


WRAPPED_FOUND = "a wrapper whose command the guard cannot find"


@pytest.mark.parametrize(
    "command,found",
    [
        ("time sort -o out f", SORT_FOUND),
        ("nice -n 5 sort -o out f", SORT_FOUND),
        ("env A=1 sort -o out f", SORT_FOUND),
        ("command sort -o out f", SORT_FOUND),
        ("xargs awk -f p.awk", AWK_FILE_FOUND),
        ("time nice sort -o out f", SORT_FOUND),
        ("timeout 5 sort -o out f", SORT_FOUND),
        ("timeout -s KILL 5 uniq f out", UNIQ_FOUND),
        ("stdbuf -oL sort -o out f", SORT_FOUND),
        ("nohup uniq f out", UNIQ_FOUND),
        ("/usr/bin/env -i A=1 /usr/bin/sort -o out f", SORT_FOUND),
        ("xargs -0 -n 1 awk '{print > \"x\"}'", AWK_FOUND),
        ("time", WRAPPED_FOUND),
        ("xargs", WRAPPED_FOUND),
        ("timeout 5", WRAPPED_FOUND),
        ("env A=1", WRAPPED_FOUND),
        ("env -S 'sort -o out f'", WRAPPED_FOUND),
        ("nice --foo sort f", WRAPPED_FOUND),
    ],
)
def test_b10_a_wrapped_command_is_judged_as_the_command_it_runs(roots, command, found):
    done = run(command, make_seat(roots, "build"))
    assert done.returncode == 2, done.stderr
    assert_resend(done, found)


@pytest.mark.parametrize(
    "command,route",
    [
        ("time cat /x/wt/job/.env", G3_ROUTE),
        ("xargs sort --files0-from=.env", G3_ROUTE),
        ("env A=1 awk 'BEGIN{getline l < \"y\"}'", G3_ROUTE),
        ("time git push", G4_ROUTE),
        ("nohup claude -p x", G7_ROUTE),
    ],
)
def test_b10_every_guard_rule_judges_the_wrapped_command(roots, command, route):
    assert_denied(run(command, make_seat(roots, "build")), route)


@pytest.mark.parametrize(
    "command", ["time sort f", "nice -n 5 sort f", "env A=1 sort -u f", "timeout 5 grep -n X f", "time -p wc -l f"]
)
def test_b10_a_wrapped_read_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


@pytest.mark.parametrize("command", ["grep X f | time sort", "grep -l X f | xargs grep -n Y"])
def test_b10_a_wrapper_in_a_pipe_stays_denied(roots, command):
    done = run(command, make_seat(roots, "build"))
    assert done.returncode == 2, done.stderr
    assert_resend(done, "not a read-only filter")


@pytest.mark.parametrize(
    "command",
    [
        "grep X f | awk '{print $1}'",
        "awk '{print $1}' f | head -1",
        "grep X f | sort | awk 'NF > 1'",
        # card 10's G1 control until his ruling 10-04 R283 (B11)
        "awk '{print $1}' f | sort -u",
    ],
)
def test_b11_an_awk_pipe_segment_is_denied(roots, command):
    done = run(command, make_seat(roots, "build"))
    assert done.returncode == 2, done.stderr
    assert_resend(done, AWK_NOT_FILTER)


@pytest.mark.parametrize("command", ["grep X f | awk '{print > \"f\"}'", "grep X f | awk -f p.awk"])
def test_b11_g11_and_b3_stay_as_defence_on_an_awk_segment(roots, command):
    done = run(command, make_seat(roots, "build"))
    assert_resend(done, AWK_NOT_FILTER)
    assert_resend(done, AWK_FOUND if "-f" not in command else AWK_FILE_FOUND)


@pytest.mark.parametrize("command", ["grep X f | cut -f2", "grep X f | sort -u | head -3"])
def test_b11_a_pipe_without_awk_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))


# ---- check r3 of cobalt-guard-b ------------------------------------------------------------


@pytest.mark.parametrize(
    "command,found",
    [
        ("sort {-o,out} f", SORT_FOUND),
        ("grep X f | sort {-o,out}", SORT_FOUND),
        ("uniq {f,out}", UNIQ_FOUND),
        ("grep X f | uniq {-,out}", UNIQ_FOUND),
    ],
)
def test_check_b_r3_o1_a_brace_word_that_expands_to_a_write_is_denied(roots, command, found):
    assert_resend(run(command, make_seat(roots, "build")), found)


@pytest.mark.parametrize(
    "command,found",
    [
        # bash: `-{n..p}` is `-n -o -p`, `{1..2}` is `1 2`
        ("sort -{n..p} f", SORT_FOUND),
        ("uniq {1..2}", UNIQ_FOUND),
    ],
)
def test_check_b_r3_o1_a_brace_sequence_that_expands_to_a_write_is_denied(roots, command, found):
    assert_resend(run(command, make_seat(roots, "build")), found)


def test_check_b_r3_o1_a_brace_sequence_naming_env_is_denied(roots):
    # bash: `.{d..f}nv` is `.denv .eenv .fenv`
    assert_denied(run("sort /x/wt/job/.{d..f}nv", make_seat(roots, "build")), G3_ROUTE)


@pytest.mark.parametrize("command", ["sort $'-o' out f", "grep X f | sort $'\\x2do' out"])
def test_check_b_r3_o2_an_ansi_c_quoted_sort_output_is_denied(roots, command):
    assert_resend(run(command, make_seat(roots, "build")), SORT_FOUND)


@pytest.mark.parametrize(
    "command", ["sort {a,b}", "sort -{n,u} f", "sort $'-u' f", "grep X f | uniq $'-c'", "uniq {f,}"]
)
def test_check_b_r3_a_brace_or_ansi_c_read_stays_allowed(roots, command):
    assert_allowed(run(command, make_seat(roots, "build")))
