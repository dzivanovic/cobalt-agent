#!/usr/bin/env bash
#
# cto-desk.sh — bring the always-on CTO desk back with one command.
#
# Owed by R11 (2026-09-17 07:04 ET, Dejan): "I suggest we always have you
# running in Herder and on remote control. And you relaunch yourself and
# attach to those two all the time."  A desk is ALWAYS both: a background
# session exposed as remote control `cto-desk`, AND visible in exactly one
# herdr tab labelled "CTO" whose pane runs `claude attach <id>`.
#
# WHAT IT DOES
#   1. Asks the session registry (`claude agents --json`) whether a desk is
#      alive: a background row whose cwd is the repo and whose launch
#      carries the desk's remote-control name.
#   2. Desk alive  -> makes sure the "CTO" tab exists and its viewer is
#      running; re-attaches only if the tab is missing or the viewer died.
#   3. No desk     -> launches one with the launch line PARSED OUT OF
#      docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md, then does (2).
#
# WHAT IT NEVER DOES
#   Stops, kills, exits or closes ANYTHING. No `claude stop`, no `kill`, no
#   `herdr tab close`. A second desk is reported and left alone for a human
#   to resolve (two desks must never write memory at once — L58). It holds
#   no secrets and prints none.
#
# IDEMPOTENT: on a healthy desk it runs three reads and changes nothing.
#
#   ops/cto-desk.sh            # do it
#   ops/cto-desk.sh --dry-run  # print every action, run none
#
set -euo pipefail

REPO="/Users/cobalt/cobalt"
WAKEUP="${REPO}/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"
TAB_LABEL="CTO"
TAB_WORKSPACE="w2"

DRY_RUN=0
for arg in "$@"; do
    case "$arg" in
        --dry-run) DRY_RUN=1 ;;
        -h|--help) sed -n '2,30p' "$0"; exit 0 ;;
        *) echo "cto-desk.sh: unknown argument '$arg' (only --dry-run)" >&2; exit 2 ;;
    esac
done

say()  { printf '%s\n' "$*"; }
note() { printf '  %s\n' "$*"; }

# Every state-changing command in this script goes through `act`, so
# --dry-run is a property of ONE function and cannot be forgotten at a call
# site. Reads are never wrapped: a dry run that did not look would be
# reporting on a machine it never asked about.
act() {
    if [[ $DRY_RUN -eq 1 ]]; then
        printf 'WOULD RUN: %s\n' "$*"
        return 0
    fi
    printf 'RUN: %s\n' "$*"
    "$@"
}

require() {
    command -v "$1" >/dev/null 2>&1 || {
        echo "cto-desk.sh: '$1' is not on PATH — cannot proceed." >&2
        exit 1
    }
}
require claude
require herdr
require python3

# ---------------------------------------------------------------------------
# The launch line, from the wake-up file — never a second copy of it (L3).
# ---------------------------------------------------------------------------
# The wake-up file's line 1 carries the desk's whole launch: model,
# permission mode, remote-control name, denied dialog tools, --add-dir.
# Copying it here would make this script a second source of truth for how
# the desk starts, and the two would drift on the first ruling that changes
# a flag. So it is READ, between the first `claude --bg` and the backtick
# that closes that code span.
desk_launch_line() {
    [[ -f "$WAKEUP" ]] || {
        echo "cto-desk.sh: wake-up file not found: $WAKEUP" >&2
        exit 1
    }
    python3 - "$WAKEUP" <<'PY'
import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
start = text.find("claude --bg")
if start < 0:
    sys.exit("cto-desk.sh: no `claude --bg` launch line in the wake-up file")
end = text.find("`", start)
if end < 0:
    sys.exit("cto-desk.sh: the launch line is not closed by a backtick")
line = text[start:end].strip()
if "--remote-control" not in line:
    sys.exit("cto-desk.sh: the parsed launch line carries no --remote-control")
print(line)
PY
}

LAUNCH_LINE="$(desk_launch_line)"
# The remote-control name comes out of that same line, so renaming the desk
# is one edit in the wake-up file and none here.
RC_NAME="$(printf '%s\n' "$LAUNCH_LINE" | sed -n 's/.*--remote-control[= ]\([^ ]*\).*/\1/p')"
[[ -n "$RC_NAME" ]] || { echo "cto-desk.sh: could not read --remote-control from the launch line" >&2; exit 1; }

# ---------------------------------------------------------------------------
# Is a desk alive?
# ---------------------------------------------------------------------------
# `claude agents --json` is the registry (ruled 2026-09-16, R4). A row is
# THE DESK when its working directory is the repo AND the desk's
# remote-control name appears in the row, and its state is not terminal.
# A `done` row is a finished session, not a live desk — the 09-17 ops
# prompt lost a whole item to counting one (cto-2026-09-17.md ESCALATE 1).
# PROVEN 2026-09-18, and the reason this is not a plain pipe: `claude
# agents --json` (CLI 2.1.276) writes its 1.8 KB of JSON to a FILE just
# fine (exit 0) and writes NOTHING AT ALL into a pipe. Piping it straight
# into a parser yields an empty document and, without this, a script that
# concludes "no desk is alive" and launches a second one. So it goes
# through a temp file, always.
# The registry goes to a FILE and the parser is handed its PATH. Not a
# pipe: the parser's program arrives on stdin as a heredoc, so stdin is
# already spoken for and a piped document would be silently discarded —
# which reads exactly like "no desk is alive" and launches a second one.
desk_row() {
    local tmp="${TMPDIR:-/tmp}/cto-desk-registry.$$.json"
    # stderr kept in the same file: if the CLI is telling us why it printed
    # nothing, that message is the diagnosis, not noise to discard.
    claude agents --json >"$tmp" 2>>"$tmp" || true
    python3 - "$REPO" "$RC_NAME" "$DRY_RUN" "$tmp" <<'PY'
import json, sys

repo, rc_name, dry, path = sys.argv[1], sys.argv[2], sys.argv[3] == "1", sys.argv[4]
raw = open(path, encoding="utf-8", errors="replace").read()
try:
    doc = json.loads(raw)
except Exception as e:                       # a registry we cannot read is
    print(f"PARSE_ERROR={e}")                # reported, never guessed past
    head = " ".join(raw.split())[:400] or "(no output at all)"
    print(f"RAW_HEAD={head}")
    sys.exit(0)

def rows(node):
    if isinstance(node, list):
        for item in node:
            yield from rows(item)
    elif isinstance(node, dict):
        if any(k in node for k in ("id", "sessionId", "session_id")):
            yield node
        else:
            for value in node.values():
                yield from rows(value)

CWD_KEYS = ("cwd", "workingDirectory", "working_directory", "dir", "path")
ID_KEYS = ("id", "sessionId", "session_id")
STATE_KEYS = ("state", "status")
KIND_KEYS = ("kind", "type", "mode")
NAME_KEYS = ("name", "peerName", "peer_name", "label", "title")
TERMINAL = {"done", "failed", "stopped", "exited", "error", "cancelled"}
#: What counts as "a background session". `kind` is reported as
#: `background` by CLI 2.1.276; the others are here so a renamed value
#: does not silently make every row a non-candidate.
BACKGROUND = {"background", "bg", "daemon", "headless"}

def first(row, keys):
    for k in keys:
        if k in row and row[k] not in (None, ""):
            return k, row[k]
    return None, None

all_rows = list(rows(doc))
print(f"ROWS={len(all_rows)}")
if dry:
    if all_rows:
        print("FIELDS=" + ",".join(sorted(all_rows[0])))
    for row in all_rows:
        _, ident = first(row, ID_KEYS)
        _, kind = first(row, KIND_KEYS)
        _, state = first(row, STATE_KEYS)
        _, cwd = first(row, CWD_KEYS)
        _, name = first(row, NAME_KEYS)
        short = str(cwd or "").replace("/Users/cobalt/", "~/")
        print(f"ROW={ident} kind={kind} state={state} cwd={short} name={name}")

# WHAT IDENTIFIES THE DESK, and what does not (established 2026-09-18 from
# a real `claude agents --json`, CLI 2.1.276). The row's fields are:
#     cwd, id, kind, name, sessionId, startedAt, state
# There is NO remote-control field. `--remote-control cto-desk` is a launch
# flag the registry does not report, and `name` is the session's peer name
# ("cto desk wakeup process"), not the remote-control name — so matching on
# `cto-desk` finds nothing and would conclude, wrongly, that no desk is
# alive. The discriminator is the one CTO-DESK-WAKEUP.md STEP 0 already
# uses: a BACKGROUND row whose cwd is the repo itself. Every hub works in
# `~/cobalt-wt/<branch>` (L54), so only the desk ever has this cwd.
hits = []
for row in all_rows:
    cwd_key, cwd = first(row, CWD_KEYS)
    if not cwd or str(cwd).rstrip("/") != repo.rstrip("/"):
        continue
    state_key, state = first(row, STATE_KEYS)
    if str(state).lower() in TERMINAL:
        continue
    kind_key, kind = first(row, KIND_KEYS)
    if kind is not None and str(kind).lower() not in BACKGROUND:
        continue
    _, ident = first(row, ID_KEYS)
    _, name = first(row, NAME_KEYS)
    # Recorded, never required: if a future CLI does surface the
    # remote-control name anywhere in the row, say so.
    rc_seen = rc_name in json.dumps(row)
    matched = f"{cwd_key}={cwd}+{kind_key}={kind}" + (f"+{rc_name} seen in row" if rc_seen else "")
    started = str(row.get("startedAt") or row.get("started_at") or "")
    hits.append((started, ident, matched, state, state_key, name))

# NEWEST WINS, and the older rows are reported, not touched. A stale row
# survives in the registry long after its session stopped doing anything
# (`c0194cb6`, a 09-16 "check claude version" session, was still listed
# `blocked` with cwd `~/cobalt` on 09-18). Erroring out on it would make
# this script refuse to work on the very machine it is meant to fix, and
# stopping it is a human's call. So: the desk is the most recently started
# candidate — which is what CTO-DESK-WAKEUP.md STEP 0 already says,
# "the background row with cwd ~/cobalt STARTED NOW".
def _age_key(started):
    # `startedAt` is epoch MILLISECONDS (1789728845765) in CLI 2.1.276, but
    # sort numerically only when it really is a number — an ISO string must
    # not be compared against an int.
    return (1, int(started)) if str(started).isdigit() else (0, str(started))

hits.sort(key=lambda h: _age_key(h[0]), reverse=True)
print(f"HITS={len(hits)}")
for i, (started, ident, matched, state, state_key, name) in enumerate(hits):
    if i == 0:
        print(f"DESK_ID={ident}")
        print(f"MATCHED_FIELD={matched}+newest startedAt={started}")
        print(f"DESK_STATE={state_key}={state}; name={name}")
    else:
        print(f"STALE={ident} {state_key}={state} startedAt={started} name={name}")
PY
    rm -f "$tmp"
}

DESK_ID=""
MATCHED_FIELD=""
DESK_STATE=""
HITS=0
ROWS=0
PARSE_ERROR=""
RAW_HEAD=""
STALE=""
while IFS= read -r line; do
    case "$line" in
        FIELDS=*)        note "registry row fields: ${line#FIELDS=}" ;;
        ROW=*)           note "${line}" ;;
        ROWS=*)          ROWS="${line#ROWS=}" ;;
        HITS=*)          HITS="${line#HITS=}" ;;
        DESK_ID=*)       [[ -z "$DESK_ID" ]] && DESK_ID="${line#DESK_ID=}" ;;
        MATCHED_FIELD=*) [[ -z "$MATCHED_FIELD" ]] && MATCHED_FIELD="${line#MATCHED_FIELD=}" ;;
        DESK_STATE=*)    [[ -z "$DESK_STATE" ]] && DESK_STATE="${line#DESK_STATE=}" ;;
        PARSE_ERROR=*)   PARSE_ERROR="${line#PARSE_ERROR=}" ;;
        RAW_HEAD=*)      RAW_HEAD="${line#RAW_HEAD=}" ;;
        STALE=*)         STALE="${STALE:+$STALE
  }${line#STALE=}" ;;
    esac
done < <(desk_row)

if [[ -n "$PARSE_ERROR" ]]; then
    echo "cto-desk.sh: could not parse \`claude agents --json\`: $PARSE_ERROR" >&2
    echo "  what it printed: ${RAW_HEAD:-(nothing)}" >&2
    if [[ $DRY_RUN -eq 1 ]]; then
        # A dry run exists to be diagnosable — reads only, no actions.
        echo "  claude binary   : $(command -v claude || echo '(not found)')" >&2
        echo "  claude --version: $(claude --version 2>&1 | head -n 1)" >&2
    fi
    echo "Refusing to launch a second desk on an unreadable registry." >&2
    exit 1
fi

say "registry : ${ROWS} session row(s); ${HITS} live desk row(s) (cwd ${REPO}, remote control ${RC_NAME})"

if [[ -n "$STALE" ]]; then
    # Reported, never resolved here: ending a session is a human's call, and
    # two desks writing memory at once is what L58 forbids — so an older row
    # that is genuinely still alive has to be SEEN, not quietly ignored.
    say "older    : $((HITS - 1)) further background row(s) with this cwd — NOT the desk, NOT touched:"
    note "$STALE"
    note "if one of those is really a second desk, stop it by hand (\`claude stop <id>\`)."
fi

# ---------------------------------------------------------------------------
# No desk -> launch one.
# ---------------------------------------------------------------------------
if [[ -z "$DESK_ID" ]]; then
    say "desk     : NONE alive -> launching from ${WAKEUP##*/} line 1"
    note "$LAUNCH_LINE"
    if [[ $DRY_RUN -eq 1 ]]; then
        printf 'WOULD RUN: cd %s && %s\n' "$REPO" "$LAUNCH_LINE"
        say "dry run  : stopping here — the new id is only known after a real launch."
        exit 0
    fi
    cd "$REPO"
    # `eval` because the launch line is one shell command WITH its quoting,
    # read from the file that owns it.
    eval "$LAUNCH_LINE"
    # Re-ask the registry rather than scraping the launch output: the
    # registry is the one place that knows the id (R4).
    DESK_ID=""
    while IFS= read -r line; do
        case "$line" in
            DESK_ID=*)       [[ -z "$DESK_ID" ]] && DESK_ID="${line#DESK_ID=}" ;;
            MATCHED_FIELD=*) MATCHED_FIELD="${line#MATCHED_FIELD=}" ;;
            DESK_STATE=*)    DESK_STATE="${line#DESK_STATE=}" ;;
        esac
    done < <(desk_row)
    [[ -n "$DESK_ID" ]] || { echo "cto-desk.sh: launched, but no desk row appeared in the registry." >&2; exit 1; }
    say "desk     : launched ${DESK_ID}"
fi

say "desk     : ${DESK_ID} alive (matched on registry field '${MATCHED_FIELD}', ${DESK_STATE})"

# ---------------------------------------------------------------------------
# Exactly one "CTO" tab, with a live viewer.
# ---------------------------------------------------------------------------
# `herdr tab list` / `herdr pane list` answer with ONE line of JSON:
#   {"id":"cli:tab:list","result":{"tabs":[{"label":"CTO","tab_id":"w2:tF",
#    "workspace_id":"w2","pane_count":1,"agent_status":"done",...}],...}}
# so they are parsed, never split on whitespace — a label with a space in
# it ("Local Terminal", "P2 Reship B") breaks any awk field guess.
herdr_select() {
    # herdr_select <subcommand> <match-key> <match-value> <emit-key>
    local sub="$1" mkey="$2" mval="$3" ekey="$4"
    local tmp="${TMPDIR:-/tmp}/cto-desk-herdr.$$.json"
    # Same temp-file rule as the registry: never read a CLI through a pipe
    # when it may decide it is not talking to a terminal.
    herdr "$sub" list >"$tmp" 2>>"$tmp" || true
    python3 - "$tmp" "$mkey" "$mval" "$ekey" <<'PY'
import json, sys
path, mkey, mval, ekey = sys.argv[1:5]
try:
    doc = json.load(open(path, encoding="utf-8"))
except Exception:
    sys.exit(0)                      # unreadable -> no matches, said by silence

def walk(node):
    if isinstance(node, list):
        for item in node:
            yield from walk(item)
    elif isinstance(node, dict):
        yield node
        for value in node.values():
            yield from walk(value)

for row in walk(doc):
    if str(row.get(mkey, "")) == mval and row.get(ekey):
        print(row[ekey])
PY
    rm -f "$tmp"
}

tab_ids()      { herdr_select tab  label   "$TAB_LABEL" tab_id; }
pane_for_tab() { herdr_select pane tab_id  "$1"         pane_id | head -n 1; }

if [[ $DRY_RUN -eq 1 ]]; then
    say "herdr    : tabs labelled '${TAB_LABEL}': $(tab_ids | tr '\n' ' ')"
fi

viewer_alive() {
    pgrep -f "claude attach ${DESK_ID}" >/dev/null 2>&1
}

# Plain `while read` rather than `mapfile`: /bin/bash on macOS is 3.2 and
# this script has to run from whatever shell a wake-up lands in.
TABS=""
TAB_COUNT=0
while IFS= read -r t; do
    [[ -n "$t" ]] || continue
    TABS="${TABS:+$TABS }$t"
    TAB_COUNT=$((TAB_COUNT + 1))
done < <(tab_ids)
TAB="${TABS%% *}"

if [[ "$TAB_COUNT" -gt 1 ]]; then
    # Reported, not closed: this script never closes a tab.
    say "viewer   : WARNING — ${TAB_COUNT} tabs labelled '${TAB_LABEL}' (${TABS}). Using ${TAB};"
    note "close the spare by hand (\`herdr tab close <tab>\`) — this script closes nothing."
fi

if [[ -z "$TAB" ]]; then
    say "viewer   : no '${TAB_LABEL}' tab -> creating one"
    act herdr tab create --workspace "$TAB_WORKSPACE" --cwd "$REPO" --label "$TAB_LABEL" --no-focus
    if [[ $DRY_RUN -eq 1 ]]; then
        printf 'WOULD RUN: herdr pane run <new pane> "claude attach %s"\n' "$DESK_ID"
        say "desk ${DESK_ID} alive — viewer would be attached in a new '${TAB_LABEL}' tab"
        exit 0
    fi
    TAB=""
    while IFS= read -r t; do
        [[ -n "$t" && -z "$TAB" ]] && TAB="$t"
    done < <(tab_ids)
    [[ -n "$TAB" ]] || { echo "cto-desk.sh: created the tab but cannot find it in \`herdr tab list\`." >&2; exit 1; }
fi

PANE="$(pane_for_tab "$TAB")"
if [[ -z "$PANE" ]]; then
    echo "cto-desk.sh: tab ${TAB} has no pane in \`herdr pane list\` — nothing to attach into." >&2
    exit 1
fi

if viewer_alive; then
    say "viewer   : tab ${TAB} pane ${PANE}, \`claude attach ${DESK_ID}\` running"
    say "desk ${DESK_ID} alive — viewer ok"
    exit 0
fi

say "viewer   : tab ${TAB} pane ${PANE}, no live \`claude attach ${DESK_ID}\` -> re-attaching"
act herdr pane run "$PANE" "claude attach ${DESK_ID}"
say "desk ${DESK_ID} alive — viewer re-attached"
