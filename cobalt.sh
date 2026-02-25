#!/bin/bash

# Configuration
PID_FILE="logs/cobalt.pid"
KEY_FILE="$HOME/.cobalt_key"

case "$1" in
    start)
        if [ -f "$PID_FILE" ]; then
            echo "  Cobalt is already running (PID: $(cat $PID_FILE))."
            exit 1
        fi
        
        # Inject the Master Key securely
        if [ -f "$KEY_FILE" ]; then
            source "$KEY_FILE"
        else
            echo " Error: $KEY_FILE not found. Cannot unlock vault."
            exit 1
        fi
        
        echo " Starting Cobalt in the background..."
        mkdir -p logs
        nohup uv run src/cobalt_agent/main.py > logs/mattermost_session.log 2>&1 &
        
        # Save the Process ID
        echo $! > "$PID_FILE"
        echo " Cobalt started (PID: $(cat $PID_FILE))."
        ;;
        
    stop)
        if [ -f "$PID_FILE" ]; then
            PID=$(cat "$PID_FILE")
            echo " Sending graceful shutdown signal to Cobalt (PID: $PID)..."
            # kill -15 allows Python to trigger its 'finally' cleanup blocks
            kill -15 "$PID"
            rm "$PID_FILE"
            echo " Cobalt stopped safely."
        else
            echo "  Cobalt is not running (no PID file found)."
        fi
        ;;
        
    status)
        if [ -f "$PID_FILE" ]; then
            echo " Cobalt is ONLINE (PID: $(cat $PID_FILE))."
        else
            echo " Cobalt is OFFLINE."
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
