#!/bin/bash

# Configuration
PID_FILE="logs/cobalt.pid"
KEY_FILE="$HOME/.cobalt_key"

case "$1" in
    start)
        if [ -f "$PID_FILE" ]; then
            PID=$(cat "$PID_FILE")
            # Verify if the process is actually running
            if kill -0 "$PID" 2>/dev/null; then
                echo "  Cobalt is already running (PID: $PID)."
                exit 1
            else
                # Stale PID file detected - clean it up
                echo "  Warning: Stale PID file found (PID $PID no longer running). Cleaning up..."
                rm "$PID_FILE"
            fi
        fi
        
        # Inject the Master Key securely
        if [ -f "$KEY_FILE" ]; then
            source "$KEY_FILE"
        else
            echo "  Error: $KEY_FILE not found. Cannot unlock vault."
            exit 1
        fi

        echo "  Initiating Pre-Flight Infrastructure Checks (120s timeout)..."
        TIMEOUT=120

        # 1. Check LM Studio API
        echo "  -> Waiting for LM Studio (Port 1234)..."
        ELAPSED=0
        while ! curl -s http://localhost:1234/v1/models > /dev/null; do
            if [ "$ELAPSED" -ge "$TIMEOUT" ]; then echo "  [X] Fatal: LM Studio offline."; exit 1; fi
            sleep 5; ELAPSED=$((ELAPSED + 5))
        done

        # 2. Check Postgres Database
        echo "  -> Waiting for PostgreSQL (Port 5432)..."
        ELAPSED=0
        while ! nc -z localhost 5432 > /dev/null 2>&1; do
            if [ "$ELAPSED" -ge "$TIMEOUT" ]; then echo "  [X] Fatal: Postgres offline."; exit 1; fi
            sleep 5; ELAPSED=$((ELAPSED + 5))
        done

        # 3. Check Mattermost Server
        echo "  -> Waiting for Mattermost (Port 8065)..."
        ELAPSED=0
        while ! curl -s http://localhost:8065 > /dev/null; do
            if [ "$ELAPSED" -ge "$TIMEOUT" ]; then echo "  [X] Fatal: Mattermost offline."; exit 1; fi
            sleep 5; ELAPSED=$((ELAPSED + 5))
        done

        echo "  [+] All infrastructure green. Igniting Cobalt..."
        mkdir -p logs
        nohup uv run src/cobalt_agent/main.py > logs/mattermost_session.log 2>&1 &
        
        # Save the Process ID
        echo $! > "$PID_FILE"
        echo "  Cobalt started (PID: $(cat $PID_FILE))."
        ;;
        
    stop)
        if [ -f "$PID_FILE" ]; then
            PID=$(cat "$PID_FILE")
            echo "  Sending graceful shutdown signal to Cobalt (PID: $PID)..."
            # kill -15 allows Python to trigger its 'finally' cleanup blocks
            kill -15 "$PID"
            rm "$PID_FILE"
            echo "  Cobalt stopped safely."
        else
            echo "  Cobalt is not running (no PID file found)."
        fi
        ;;
        
    status)
        if [ -f "$PID_FILE" ]; then
            PID=$(cat "$PID_FILE")
            # Verify if the process is actually running using kill -0
            if kill -0 "$PID" 2>/dev/null; then
                echo "  Cobalt is ONLINE (PID: $PID)."
            else
                # Process is dead - clean up stale PID file and report true status
                echo "  Warning: Stale PID file detected (process $PID not running). Removing stale PID..."
                rm "$PID_FILE"
                echo "  Cobalt is OFFLINE."
            fi
        else
            echo "  Cobalt is OFFLINE."
        fi
        ;;
        
    restart)
        $0 stop
        sleep 2
        $0 start
        ;;
        
    *)
        echo "Usage: ./cobalt.sh {start|stop|status|restart}"
        exit 1
esac
