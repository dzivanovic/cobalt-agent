#!/bin/bash
export PATH="/Users/cobalt/.lmstudio/bin:$PATH"

# OS-LEVEL OVERRIDE: Remove macOS limits on locking physical RAM
ulimit -l unlimited

echo "Purging lingering processes for warm-boot safety..."
lms server stop 2>/dev/null
lms unload --all 2>/dev/null
pkill -9 -f llmster 2>/dev/null        # Nuke the core inference engine
pkill -9 -f "node.*lmstudio" 2>/dev/null # Nuke the background workers
pkill -9 -f caffeinate 2>/dev/null     # Nuke the old heartbeat
sleep 2

echo "Starting LM Studio daemon and server..."
lms daemon up
lms server start

echo "Waiting for LM Studio API on Port 1234 (60-second timeout)..."
TIMEOUT=60
ELAPSED=0

# Ping the API. If it fails, wait 2 seconds and try again, up to 60 seconds.
while ! curl -s http://localhost:1234/v1/models > /dev/null; do
    if [ "$ELAPSED" -ge "$TIMEOUT" ]; then
        echo "ERROR: LM Studio API failed to start within ${TIMEOUT} seconds. Aborting load."
        exit 1
    fi
    sleep 2
    ELAPSED=$((ELAPSED + 2))
done

echo "API confirmed online. Loading 122B Mainframe model into 88GB VRAM limit..."
lms load qwen3.5-122b-a10b --identifier "mainframe" --gpu max --context-length 32768

echo "Model loaded. Spawning background heartbeat to prevent memory eviction..."
caffeinate -i -m bash -c '
  while true; do
    curl -s http://localhost:1234/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '\''{
      "model": "mainframe",
      "messages": [{"role": "user", "content": "ping"}],
      "max_tokens": 1
    }''\' > /dev/null
    sleep 60
  done
'
