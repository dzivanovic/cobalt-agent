---
status: To Do
priority: P0
module: Ops
phase: 1
complexity: M
tags: [cobalt, task]
created: 2026-02-23
---
# 35 Untethering Tailscale VSCode
# Task: Untethering Tailscale VSCode

**Status**: To Do  
**Priority**: Medium  
**Tags**: infrastructure, development, network  
**Created**: 2026-02-22

## Description

Establish remote development mesh using Tailscale for secure, direct access to development servers without exposing ports to the public internet.

## Objectives

- Configure Tailscale on all development machines
- Set up VSCode Remote-SSH to connect via Tailscale IP
- Configure firewall rules to only allow Tailscale traffic
- Document the connection process

## Tasks

- [ ] Install Tailscale on all development machines
- [ ] Enable SSH on each machine via Tailscale
- [ ] Configure VSCode Remote-SSH plugin
- [ ] Create connection script for quick access
- [ ] Document network configuration in Obsidian

## Success Criteria

- VSCode can connect to development servers by Tailscale IP
- No exposed ports on public firewall
- Connection established in < 30 seconds