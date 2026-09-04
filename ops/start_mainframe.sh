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
# The heartbeat exists because the model is evicted from VRAM when idle;
# `caffeinate -i -m` additionally stops the machine idle-sleeping and
# the disk spinning down under it.

set -u

export PATH="/Users/cobalt/.lmstudio/bin:$PATH"

OPS_DIR="/Users/cobalt/cobalt/ops"
LOG_DIR="$OPS_DIR/logs"
LOG_FILE="$LOG_DIR/mainframe.log"
PID_FILE="$LOG_DIR/mainframe-heartbeat.pid"
MODEL_ID="mainframe"
API="http://localhost:1234"

mkdir -p "$LOG_DIR"

log() { echo "$(date '+%Y-%m-%d %H:%M:%S') | $*" >> "$LOG_FILE"; }

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
            if ps -p "$old" -o args= 2>/dev/null | grep -q "$HEARTBEAT_MARKER"; then
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

log "API online — loading model into VRAM"
lms load qwen3.5-122b-a10b --identifier "$MODEL_ID" --gpu max --context-length 32768

log "model loaded — spawning heartbeat (60s ping, logged)"
caffeinate -i -m bash -c '
  MARKER="'"$HEARTBEAT_MARKER"'"   # identifies this process as ours
  LOG_FILE="'"$LOG_FILE"'"
  API="'"$API"'"
  MODEL_ID="'"$MODEL_ID"'"
  while true; do
    reply=$(curl -s --max-time 30 "$API/v1/chat/completions" \
      -H "Content-Type: application/json" \
      -d "{\"model\":\"$MODEL_ID\",\"messages\":[{\"role\":\"user\",\"content\":\"ping\"}],\"max_tokens\":1}")
    if [ -n "$reply" ] && ! printf "%s" "$reply" | grep -q "\"error\""; then
      echo "$(date "+%Y-%m-%d %H:%M:%S") | heartbeat OK" >> "$LOG_FILE"
    else
      echo "$(date "+%Y-%m-%d %H:%M:%S") | heartbeat FAILED: ${reply:-no response}" >> "$LOG_FILE"
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
