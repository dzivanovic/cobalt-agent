#!/bin/bash
# com.cobalt.mainframe — bring up LM Studio and hold the model in VRAM.
#
# PROVENANCE. This is the last surviving Gemini-era operational artifact.
# It lived at ~/.lmstudio/start_mainframe.sh, outside the repo, outside
# git, and outside every review — the 2026-09-04 nightly-restart
# forensics found it while establishing that the "nightly restart"
# everyone believed in does not exist (there is no cron, no
# StartCalendarInterval before 05:15, no pmset schedule; Gemini-era task
# 45 "Implement automatic restart on process failure" is still
# unchecked). What actually shipped is this RunAtLoad purge. RULING 6
# moved it into ops/ with the other captured LaunchAgents.
#
# TWO DEFECTS FIXED IN THE MOVE, behaviour otherwise identical:
#
# 1. `pkill -9 -f caffeinate` killed EVERY caffeinate on the box, not
#    this script's own. Anything else holding the Mac awake — a backup,
#    a long build, a deliberate `caffeinate` in a terminal — died
#    silently whenever this job restarted. The heartbeat now carries a
#    unique marker in its own command line, its pid is recorded in a
#    pidfile, and only that process tree is killed — after confirming
#    by marker that it is ours (PIDs are recycled).
#
# 2. The 60-second ping loop was unlogged and unsupervised. "Is the
#    model still warm?" had no answer short of asking the API by hand.
#    Every ping now appends its outcome to ops/logs/mainframe.log.
#
#    Logging it immediately earned its keep: within minutes the log
#    showed the 122B model had vanished from LM Studio (~14:45 on
#    2026-09-04, cause unknown — no second script run, nothing in the
#    boot log) and that a ping-only heartbeat can never recover from
#    that. It would have logged FAILED every 60 s forever while the
#    mainframe stayed down; before this change it would have done so
#    silently. The heartbeat now attempts ONE reload per cycle.
#
# The heartbeat exists because the model is evicted from VRAM when idle;
# `caffeinate -i -m` additionally stops the machine idle-sleeping and
# the disk spinning down under it.
#
# 2026-09-09, PROMPT 5 phase A1 — four changes, none of which alter which
# model is served or how it is loaded:
#
# 1. REPO-OWNED CHAT TEMPLATE. LM Studio 1.11.0 forwards neither
#    `enable_thinking` nor `reasoning_effort` from the API into the
#    model's Jinja chat template (proven 2026-09-07 and 2026-09-08), so
#    thinking is unconditionally on and no API parameter can turn it off.
#    The only remaining lever is the template itself, which lives in the
#    model directory — outside the repo, outside git, outside review,
#    exactly like this script did before RULING 6.
#    ops/mainframe/chat_template.jinja is now the source of truth
#    (upstream + one in-band soft-switch block: `/no_think` and
#    `/think_low`), and ops/mainframe/install_template.sh copies it into
#    the model dir on every start and on every heartbeat self-heal. It
#    backs the upstream template up once to chat_template.jinja.orig and
#    refuses to overwrite a template it does not recognise.
#
# 2. SPINNER FILTER. `lms load` prints a TTY progress spinner — braille
#    frames separated by carriage returns, wrapped in ANSI escapes — with
#    no quiet flag available and regardless of having no TTY. That is
#    what made ops/logs/mainframe.log 9.2 MB: 815 spinner lines against
#    10 348 lines of actual log. Both `lms load` calls now go through
#    strip_tty(). Measured on a 20-line sample of the real log: 226 012
#    bytes in, 1 260 bytes out (-99.4%) — and it SURFACES signal the raw
#    log buried mid-line, "Model loaded successfully in 25.64s." becomes
#    its own readable line. The main-path load also stops writing to
#    launchd's stdout, so mainframe-boot.log stops collecting spinner.
#
# 3. LOG ROTATION. There was none; see the 9.2 MB above. One generation
#    only, rotated at start when the log exceeds 5 MB.
#
# 4. TWO HONESTY FIXES. stop_previous_heartbeat() logged "pid N is not
#    one of ours — left alone" even when the pid simply no longer existed
#    (mainframe-swap-2026-09-07.md §12.8); a dead pid now says so. And a
#    post-load `/no_think` probe checks that the installed template is
#    actually in effect — at WARN, never fatal, because NN#16 ranks "the
#    mainframe is down" above "the mainframe thinks when asked not to".

set -u

export PATH="/Users/cobalt/.lmstudio/bin:$PATH"

OPS_DIR="/Users/cobalt/cobalt/ops"
LOG_DIR="$OPS_DIR/logs"
LOG_FILE="$LOG_DIR/mainframe.log"
PID_FILE="$LOG_DIR/mainframe-heartbeat.pid"
# MODEL SWAP 2026-09-07 (was: qwen3.5-122b-a10b, 4-bit MoE, 69.6 GB).
# The 122B segfaulted in LM Studio's node/llmster MLX worker every
# ~330-352 s regardless of load — 820 crash-detections over four days,
# forensics in docs/40 - DevDocs/reports/mainframe-triage-2026-09-07.md.
#
# WARNING — MODEL is a PREFIX match, and three models on this box match
# "qwen3.8-27b": the 8-bit we want, the "-mtp" draft head, and a 4-bit
# build. `lms load` picks "the first one" with no documented ordering,
# so the key alone cannot guarantee which model gets served. MODEL_PATH
# is therefore verified against the served model after load, and the
# script aborts loudly on a mismatch rather than quietly serving a
# 4-bit model to a production trading agent.
MODEL="qwen3.8-27b"
MODEL_PATH="mlx-community/Qwen3.8-27B-8bit"
MODEL_ID="mainframe"
API="http://localhost:1234"

# Served context. The 122B ran 32768 as a VRAM-budget compromise; the
# 27B is far cheaper, so it serves the model's full declared maximum.
# Only 16 of its 64 layers use full attention (the other 48 are linear,
# constant-state), so the KV cache at 262144 is ~17.2 GB — about 47 GB
# all-in against the 122B's 69.6 GB. configs/config.yaml's
# mainframe.context MUST match this value (E4).
CONTEXT_LENGTH=262144

mkdir -p "$LOG_DIR"

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') | $*" >> "$LOG_FILE"; }

# --- 0. rotate the log, ONE generation ---------------------------------
#
# Must run before the first `log` call so the rotation notice is the first
# line of the new file. ONE generation is the rule: mainframe.log.1 is
# overwritten every rotation and nothing older is kept. This log is a
# liveness trace, not an audit trail — anything worth keeping longer is
# quoted into a report under docs/40 - DevDocs/reports/ instead.
# Before the spinner filter (change 2 above) the log grew ~9 MB in five
# days; with it, 5 MB is a long time.
LOG_MAX_BYTES=$((5 * 1024 * 1024))
if [ -f "$LOG_FILE" ]; then
    log_size="$(stat -f %z "$LOG_FILE" 2>/dev/null || echo 0)"
    if [ "$log_size" -gt "$LOG_MAX_BYTES" ]; then
        mv "$LOG_FILE" "$LOG_FILE.1"
        log "rotated: previous log was $log_size bytes (> $LOG_MAX_BYTES) -> $LOG_FILE.1"
    fi
fi

# `lms load` writes a TTY progress spinner even with no TTY attached and
# has no quiet flag (its only flags are --gpu, -c/--context-length,
# --parallel, --ttl, --identifier, --estimate-only, -y/--yes). Each
# spinner burst arrives as ONE physical line of carriage-return-separated
# braille frames wrapped in ANSI escapes, so `tr -d '\r'` would merely
# concatenate ~9 000 characters of frames into a single unreadable line.
# Turning CR into LF instead, then dropping the trailing spinner glyph and
# collapsing the resulting runs, takes a 226 012-byte sample to 1 260
# bytes and leaves "Model loaded successfully in 25.64s." legible.
#
# LC_ALL=C is deliberate: launchd starts this job with no LANG, and the
# spinner glyphs are multibyte UTF-8. In C locale sed matches bytes, and
# `[^[:print:][:space:]]` cleanly catches them without a multibyte
# character range that would behave differently depending on the inherited
# locale. Verified byte-identical under `env -i` (2026-09-09).
strip_tty() {
    tr '\r' '\n' \
        | LC_ALL=C sed -E $'s/\x1b\\[[0-9;?]*[A-Za-z]//g' \
        | LC_ALL=C sed -E 's/[[:space:]]*[^[:print:][:space:]]+[[:space:]]*$//' \
        | grep -v '^[[:space:]]*$' \
        | uniq
}

# Repo-owned chat template installer (change 1 above). Sourced rather than
# inlined because the heartbeat's self-heal reload() needs the same
# function from inside a separate `bash -c` — one implementation, one
# place to edit it. Needs OPS_DIR, MODEL_PATH and log() — all three are
# defined above this point.
INSTALL_TEMPLATE_SH="$OPS_DIR/mainframe/install_template.sh"
if [ ! -f "$INSTALL_TEMPLATE_SH" ]; then
    log "FATAL: missing $INSTALL_TEMPLATE_SH — cannot install the chat template. Aborting."
    exit 1
fi
# shellcheck source=mainframe/install_template.sh
. "$INSTALL_TEMPLATE_SH"

# Unique to THIS script's heartbeat. It appears in the heartbeat's own
# command line, which is what makes "our heartbeat" identifiable without
# resorting to `pkill -f caffeinate` and taking every unrelated
# caffeinate on the box down with it.
HEARTBEAT_MARKER="COBALT_MAINFRAME_HEARTBEAT"

# --- 1. stop OUR previous heartbeat, and nothing else -----------------
#
# `$!` after `caffeinate ... &` is NOT the caffeinate. Measured on this
# machine (2026-09-04): $! was 66399, a bash wrapper, and the actual
# caffeinate was its child 66401. A `comm`-based "is it still a
# caffeinate?" check therefore never matched, logged "left alone", and
# leaked the old heartbeat on every restart — a regression against the
# over-broad pkill it replaced. So: kill the recorded PID's whole tree,
# identify it by our own marker rather than by process name, and sweep
# for orphans by marker as a backstop.
kill_tree() {
    local pid="$1" child
    for child in $(pgrep -P "$pid" 2>/dev/null); do kill_tree "$child"; done
    kill -9 "$pid" 2>/dev/null
}

stop_previous_heartbeat() {
    local old=""
    if [ -f "$PID_FILE" ]; then
        old="$(cat "$PID_FILE" 2>/dev/null || true)"
        rm -f "$PID_FILE"
    fi
    case "$old" in
        ''|*[!0-9]*) : ;;
        *)
            # PIDs are recycled — confirm it is OURS by the marker before
            # signalling anything.
            #
            # The dead-pid case is split out deliberately (2026-09-09). It
            # used to fall into the "not one of ours" branch, which read as
            # "something else owns that pid, we declined to touch it" when
            # the truth was "that pid does not exist". Two very different
            # facts, one misleading line — reported in
            # mainframe-swap-2026-09-07.md §12.8. This is the overwhelmingly
            # common case: launchd `kickstart -k` kills the old heartbeat
            # before this script runs, so its pidfile almost always names a
            # pid that is already gone.
            if ! ps -p "$old" > /dev/null 2>&1; then
                log "previous heartbeat pid $old is gone (nothing to stop)"
            elif ps -p "$old" -o args= 2>/dev/null | grep -q "$HEARTBEAT_MARKER"; then
                kill_tree "$old"
                log "stopped previous heartbeat tree (pid $old)"
            else
                log "heartbeat pid $old is not one of ours — left alone"
            fi
            ;;
    esac
    # Backstop: a heartbeat orphaned by a crash or a `kickstart -k` that
    # removed the pidfile's owner. Scoped to OUR marker — never a bare
    # `pkill -f caffeinate`.
    # This runs BEFORE our own heartbeat is spawned, so nothing here can
    # match this script itself.
    local orphans o
    orphans="$(pgrep -f "$HEARTBEAT_MARKER" 2>/dev/null || true)"
    if [ -n "$orphans" ]; then
        for o in $orphans; do kill_tree "$o"; done
        log "swept orphaned heartbeat pids: $(echo $orphans | tr '\n' ' ')"
    fi
}

log "=== start_mainframe.sh starting (pid $$) ==="

# OS-LEVEL OVERRIDE: remove macOS limits on locking physical RAM
ulimit -l unlimited

log "purging lingering LM Studio processes for warm-boot safety"
lms server stop 2>/dev/null
lms unload --all 2>/dev/null
pkill -9 -f llmster 2>/dev/null          # the core inference engine
pkill -9 -f "node.*lmstudio" 2>/dev/null # the background workers
stop_previous_heartbeat                  # was: pkill -9 -f caffeinate
sleep 2

log "starting LM Studio daemon and server"
lms daemon up
lms server start

log "waiting for LM Studio API on port 1234 (60s timeout)"
TIMEOUT=60
ELAPSED=0
while ! curl -s "$API/v1/models" > /dev/null; do
    if [ "$ELAPSED" -ge "$TIMEOUT" ]; then
        log "ERROR: LM Studio API failed to start within ${TIMEOUT}s. Aborting load."
        exit 1
    fi
    sleep 2
    ELAPSED=$((ELAPSED + 2))
done

# -y is MANDATORY here, not a convenience. Without it `lms load` drops
# into an interactive "Multiple models match — please select one" menu
# whenever MODEL is a prefix of more than one model key. Under launchd
# there is no TTY, so it blocks forever: the model never loads, the
# heartbeat never spawns, and the mainframe is silently DOWN with the
# job still showing as running. Reproduced in production 2026-09-07
# 21:31 during this very swap. The 122B never hit it only because its
# key happened to be unique. `-y` selects the first match, which is why
# the arch/quant verification below is not optional.
#
# The template is installed BEFORE the load, not after: LM Studio reads
# chat_template.jinja when the model is brought into memory, so installing
# it afterwards would leave the previous template serving until the next
# restart. install_template RETURNS non-zero on a missing source or on a
# template in the model dir that is neither upstream nor ours; on the main
# path that is fatal, before anything is loaded.
if ! install_template; then
    log "FATAL: chat template not installed — refusing to load the model. Aborting."
    exit 1
fi

log "API online — loading model into VRAM"
# 2>&1 | strip_tty: see the strip_tty definition above. The exit status
# that matters is `lms load`'s, not the last stage of the pipeline, hence
# PIPESTATUS. This path previously wrote to launchd's stdout
# (mainframe-boot.log); it now goes to the same log as everything else.
lms load "$MODEL" -y --identifier "$MODEL_ID" --gpu max --context-length "$CONTEXT_LENGTH" \
    2>&1 | strip_tty >> "$LOG_FILE"
load_rc=${PIPESTATUS[0]}
# Not fatal on its own: `lms load` has been observed returning non-zero
# after a model was in fact loaded, and the arch/quant verification below
# is the real gate. Logged so a non-zero rc is visible next to the
# verification result rather than discarded, which is what happened before.
if [ "$load_rc" -ne 0 ]; then
    log "WARN: 'lms load' exited $load_rc — continuing to verification"
fi

# --- verify we loaded the model we meant to ---------------------------
#
# MODEL is a prefix match against three "qwen3.8-27b*" models on this
# box (see the MODEL block above). A wrong pick would serve a 4-bit
# model, or the 265 MB MTP draft head, under the identifier the whole
# agent routes to — silently, and with plausible-looking output. That
# is precisely the "plausible-empty artifact" the fail-loud law
# forbids, so a mismatch is fatal here rather than a warning.
#
# Discriminator is arch+quantization, NOT path: /api/v0/models reports
# path=null for any model loaded under a custom --identifier (measured
# 2026-09-07 against the running 122B), so path is unusable here.
# arch+quant separates all three candidates cleanly:
#     qwen3_5     + 8bit  -> the model we want
#     qwen3_5     + 4bit  -> the 4-bit build
#     qwen3_5_mtp + 4bit  -> the MTP draft head
EXPECT_ARCH="qwen3_5"
EXPECT_QUANT="8bit"

read -r got_arch got_quant got_ctx <<EOF
$(curl -s "$API/api/v0/models" | python3 -c "
import json,sys
mid=sys.argv[1]
try:
    for m in json.load(sys.stdin).get('data',[]):
        if m.get('id')==mid:
            print(m.get('arch',''), m.get('quantization',''), m.get('loaded_context_length',''))
            break
except Exception:
    pass
" "$MODEL_ID" 2>/dev/null)
EOF

if [ "$got_arch" != "$EXPECT_ARCH" ] || [ "$got_quant" != "$EXPECT_QUANT" ]; then
    log "FATAL: '$MODEL_ID' should be $EXPECT_ARCH/$EXPECT_QUANT but is '${got_arch:-<none>}'/'${got_quant:-<none>}'"
    log "FATAL: refusing to spawn the heartbeat against the wrong model. Aborting."
    exit 1
fi
# Context mismatch is LOUD BUT NOT FATAL, deliberately. A wrong *model*
# is silent and dangerous, so it aborts above. A clamped *context* still
# serves correct answers, and an over-large prompt fails loudly at the
# point of use anyway — whereas aborting here would leave the mainframe
# down, which NN#16 ("production is always left working") ranks as the
# worse outcome on a trading day. It is logged at WARN so E4 drift is
# visible in the log rather than hidden.
if [ "$got_ctx" != "$CONTEXT_LENGTH" ]; then
    log "WARN: requested context $CONTEXT_LENGTH but server serves '${got_ctx:-<none>}'"
    log "WARN: configs/config.yaml mainframe.context should read '${got_ctx:-?}', not $CONTEXT_LENGTH"
fi
log "verified: '$MODEL_ID' = $got_arch/$got_quant at context $got_ctx"

# --- no-think probe ----------------------------------------------------
#
# install_template put our template in the model dir, but "the file is on
# disk" is not "the template is in effect": LM Studio may have cached the
# previous one, or may render it through minijinja with different
# semantics than the jinja2 the unit tests use
# (tests/cobalt/test_mainframe_template.py). This probe is the only check
# that exercises the real path — send `/no_think` and see whether the
# reply still carries a populated <think> block.
#
# WARN, NOT FATAL, deliberately, and for the same reason as the context
# check above: a mainframe that thinks when asked not to is a degraded
# mainframe, while a mainframe that refused to start is a down one, and
# NN#16 ranks down as strictly worse on a trading day.
probe_reply="$(curl -s --max-time 60 "$API/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"$MODEL_ID\",\"messages\":[{\"role\":\"system\",\"content\":\"/no_think\"},{\"role\":\"user\",\"content\":\"2+2, reply with just the number\"}],\"max_tokens\":16,\"temperature\":0}" 2>&1)"

if [ -z "$probe_reply" ]; then
    log "WARN: nothink probe — no response from $API"
else
    probe_content="$(printf '%s' "$probe_reply" | python3 -c "
import json,sys
try:
    d = json.load(sys.stdin)
except Exception as e:
    print('__PROBE_ERROR__ unparseable response: %s' % e)
    sys.exit(0)
if 'error' in d:
    print('__PROBE_ERROR__ %s' % str(d['error'])[:160])
    sys.exit(0)
try:
    print(d['choices'][0]['message']['content'] or '')
except Exception as e:
    print('__PROBE_ERROR__ unexpected shape: %s' % e)
" 2>/dev/null)"

    case "$probe_content" in
        __PROBE_ERROR__*)
            log "WARN: nothink probe — ${probe_content#__PROBE_ERROR__ }"
            ;;
        *)
            # Thinking is "still on" only if <think> has actual content
            # before </think>. The template's no-think path emits an EMPTY
            # <think></think> pair by design, so an empty one is a PASS.
            if printf '%s' "$probe_content" \
                | python3 -c "
import re,sys
m = re.search(r'<think>(.*?)</think>', sys.stdin.read(), re.DOTALL)
sys.exit(0 if (m and m.group(1).strip()) else 1)
" 2>/dev/null; then
                log "WARN: nothink probe — thinking still on (template not in effect?)"
            else
                log "nothink probe OK: $(printf '%s' "$probe_content" | tr -d '\n' | cut -c1-40)"
            fi
            ;;
    esac
fi

log "model loaded — spawning heartbeat (60s ping, logged, self-healing)"
caffeinate -i -m bash -c '
  MARKER="'"$HEARTBEAT_MARKER"'"   # identifies this process as ours
  LOG_FILE="'"$LOG_FILE"'"
  API="'"$API"'"
  MODEL_ID="'"$MODEL_ID"'"
  MODEL="'"$MODEL"'"
  MODEL_PATH="'"$MODEL_PATH"'"
  # Injected, not inherited: this block runs in a separate `bash -c`
  # under single quotes, so an un-injected $CONTEXT_LENGTH would expand
  # to empty here and every self-heal reload would fail on a bare
  # `--context-length`.
  CONTEXT_LENGTH="'"$CONTEXT_LENGTH"'"
  # Same injection, for the same reason: install_template.sh needs OPS_DIR
  # and MODEL_PATH, and is sourced rather than duplicated here so there is
  # exactly one implementation of "put our chat template in the model dir".
  OPS_DIR="'"$OPS_DIR"'"
  INSTALL_TEMPLATE_SH="'"$INSTALL_TEMPLATE_SH"'"
  export PATH="'"$PATH"'"
  hb() { echo "$(date "+%Y-%m-%d %H:%M:%S") | $*" >> "$LOG_FILE"; }
  # install_template.sh calls log(); in here the logger is hb().
  log() { hb "$@"; }
  strip_tty() {
    tr "\r" "\n" \
      | LC_ALL=C sed -E "s/$(printf "\033")\[[0-9;?]*[A-Za-z]//g" \
      | LC_ALL=C sed -E "s/[[:space:]]*[^[:print:][:space:]]+[[:space:]]*\$//" \
      | grep -v "^[[:space:]]*\$" \
      | uniq
  }
  if [ -f "$INSTALL_TEMPLATE_SH" ]; then
    . "$INSTALL_TEMPLATE_SH"
  else
    hb "WARN: $INSTALL_TEMPLATE_SH missing — heartbeat reloads will not reinstall the template"
    # Returns 0 on purpose, so reloads still happen. The main path already
    # exits 1 when this file is missing, so reaching here means it was
    # deleted AFTER a good start; wedging the heartbeat over that would
    # leave the mainframe down permanently for a repo problem, which is the
    # wrong side of NN#16. The template simply stops being managed, loudly.
    install_template() { hb "WARN: install_template unavailable — template not managed this cycle"; return 0; }
  fi
  reload() {
    hb "heartbeat: attempting reload of $MODEL"
    # Reinstall the template before reloading: a self-heal reload is the
    # other path by which a model enters memory, and it must not bring the
    # model up under a stale or unrecognised template. install_template
    # only ever RETURNS non-zero — it never calls exit — so a refusal
    # cannot take the heartbeat down with it. The reload is SKIPPED on a
    # refusal (architect ruling, ESCALATE 4.1, 2026-09-09): serving a
    # template nobody has reviewed is worse than staying down, and the
    # heartbeat keeps looping so the FATAL is re-logged every 60 s until a
    # human looks at ops/mainframe/.
    if ! install_template; then
      hb "FATAL: template refused — skipping reload; mainframe stays DOWN until ops/mainframe/ is reviewed"
      return 1
    fi
    lms load "$MODEL" -y --identifier "$MODEL_ID" --gpu max --context-length "$CONTEXT_LENGTH" \
      2>&1 | strip_tty >> "$LOG_FILE"
    rc=${PIPESTATUS[0]}
    # OK/FAILED is decided on lms load'\''s status, not the pipeline'\''s: the
    # last stage is `uniq`, which succeeds even when the load did not.
    if [ "$rc" -eq 0 ]; then
      hb "heartbeat: reload OK"
    else
      hb "heartbeat: reload FAILED (rc $rc) — mainframe is DOWN"
    fi
  }
  while true; do
    # LIVENESS: cheap GET /v1/models — proves the LM Studio HTTP daemon
    # itself is up. Fast (~15ms measured) and unaffected by generation
    # length, so unlike the old single generation-based probe it cannot
    # itself time out under load.
    if ! curl -s -o /dev/null --max-time 10 "$API/v1/models"; then
      hb "liveness FAILED: LM Studio HTTP server not responding"
      reload
      sleep 60
      continue
    fi
    # READINESS: mainframe-triage-2026-09-07 proved GET /v1/models and
    # the per-model "state" field on /api/v0/models both read "loaded"
    # straight through a live crash (state only flips once WE issue a
    # reload), so an inference call is the only probe that actually
    # exercises the crashed worker. It stays the reload trigger for that
    # reason (this intentionally differs from a textbook liveness and
    # readiness split, where readiness never restarts anything).
    # --max-time raised 30s -> 120s: measured generations run 33-41s, and
    # a queued heartbeat ping waits behind the in-flight generation ahead
    # of it, not just its own reply time — 30s was shorter than that
    # queue wait and produced false "no response" DOWNs against a
    # healthy, busy model (confirmed 2026-09-07: reproduced live, ping
    # timed out at 30s during a 34s generation, succeeded at 120s against
    # the same one).
    reply=$(curl -s --max-time 120 "$API/v1/chat/completions" \
      -H "Content-Type: application/json" \
      -d "{\"model\":\"$MODEL_ID\",\"messages\":[{\"role\":\"user\",\"content\":\"ping\"}],\"max_tokens\":1}")
    if [ -n "$reply" ] && ! printf "%s" "$reply" | grep -q "\"error\""; then
      hb "heartbeat OK"
    else
      hb "heartbeat FAILED: $(printf "%s" "${reply:-no response}" | tr -d "\n" | cut -c1-160)"
      # SELF-HEAL, once per cycle. A ping alone cannot bring a model
      # back: on 2026-09-04 the 122B model vanished from LM Studio at
      # ~14:45 (cause unknown — no second script run, nothing in the
      # boot log) and the old ping-only heartbeat would have logged
      # FAILED every 60s forever while the mainframe stayed down. The
      # pre-RULING-6 script had the same flaw and no log to show it.
      reload
    fi
    sleep 60
  done
' &

HEARTBEAT_PID=$!
echo "$HEARTBEAT_PID" > "$PID_FILE"
log "heartbeat running as pid $HEARTBEAT_PID (pidfile $PID_FILE)"

# Block on the heartbeat so this job's lifetime is the heartbeat's
# lifetime, exactly as before the move.
wait "$HEARTBEAT_PID"
