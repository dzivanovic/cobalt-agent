# Cobalt AI Infrastructure: SRE Boot Sequence

The Cobalt ecosystem utilizes a 3-stage automated boot sequence designed to gracefully handle cold-boot race conditions and prevent macOS from offloading the LLM to swap memory.

## Stage 1: The Base Layer (Docker)
PostgreSQL and Mattermost run in Docker containers and boot natively via the Docker Daemon.
* **Requirement:** Docker Desktop must be set to "Open at Login" in macOS System Settings.
* **Container Configuration:** Containers must be flagged with the `--restart unless-stopped` policy.
* **Recovery Command:** If containers fail to auto-start, re-apply the policy:
  `docker update --restart unless-stopped postgres cobalt-mattermost-1`

## Stage 2: The Mainframe Brain (LM Studio)
macOS uses `launchd` to fire the 122B model into VRAM immediately upon user login. The bash script applies an 88GB memory limit and spawns a background heartbeat loop to prevent the kernel from compressing the weights into SSD swap.

* **Target Script:** `/Users/cobalt/.lmstudio/start_mainframe.sh`
* **Agent Location:** `~/Library/LaunchAgents/com.cobalt.mainframe.plist`
* **Recovery / Rebuild:**
  If the configuration is deleted, recreate it by pasting this into the terminal:
  ```bash
  cat << 'EOF' > ~/Library/LaunchAgents/com.cobalt.mainframe.plist
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd](http://www.apple.com/DTDs/PropertyList-1.0.dtd)">
  <plist version="1.0">
  <dict>
      <key>Label</key>
      <string>com.cobalt.mainframe</string>
      <key>ProgramArguments</key>
      <array>
          <string>/Users/cobalt/.lmstudio/start_mainframe.sh</string>
      </array>
      <key>RunAtLoad</key>
      <true/>
      <key>StandardOutPath</key>
      <string>/Users/cobalt/.lmstudio/mainframe_boot.log</string>
      <key>StandardErrorPath</key>
      <string>/Users/cobalt/.lmstudio/mainframe_boot.err</string>
  </dict>
  </plist>
  EOF

Activate: launchctl load ~/Library/LaunchAgents/com.cobalt.mainframe.plist

## Stage 3: The Cobalt Agent

macOS launches the Cobalt python agent simultaneously with LM Studio. The ./cobalt.sh script contains a 120-second loop that polls Port 1234, intentionally stalling Cobalt until the 122B Mainframe is fully loaded and responsive.

* **Target Script:** /Users/cobalt/cobalt/cobalt.sh
* **Agent Location:** ~/Library/LaunchAgents/com.cobalt.agent.plist
* **Recovery / Rebuild:**
    If the configuration is deleted, recreate it by pasting this into the terminal:
    ```Bash

    cat << 'EOF' > ~/Library/LaunchAgents/com.cobalt.agent.plist
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd](http://www.apple.com/DTDs/PropertyList-1.0.dtd)">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.cobalt.agent</string>
        <key>EnvironmentVariables</key>
        <dict>
            <key>PATH</key>
            <string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/cobalt/.local/bin</string>
        </dict>
        <key>ProgramArguments</key>
        <array>
            <string>/Users/cobalt/cobalt/cobalt.sh</string>
            <string>start</string>
        </array>
        <key>WorkingDirectory</key>
        <string>/Users/cobalt/cobalt</string>
        <key>RunAtLoad</key>
        <true/>
        <key>AbandonProcessGroup</key>
        <true/>
        <key>StandardOutPath</key>
        <string>/Users/cobalt/cobalt_agent_boot.log</string>
        <key>StandardErrorPath</key>
        <string>/Users/cobalt/cobalt_agent_boot.err</string>
    </dict>
    </plist>
    EOF

Activate: launchctl load ~/Library/LaunchAgents/com.cobalt.agent.plist

