---
status: Done
priority: P1
module: Tools
phase: 5
complexity: L
tags: [cobalt, playwright, browser, selenium]
created: 2026-02-27
---
# 43 Upgrade Playwright Browser Tool

## Objective
Evolve the basic DSL into an advanced search and analysis engine. Must support multi-step interaction arrays (handling cookie banners, logins), targeted DOM extraction (tables/articles), and clean markdown formatting to allow the Intel Drone to scrape financial sites without a paid API.

## Acceptance Criteria
- [ ] Multi-step interaction arrays (cookie banners, logins)
- [ ] Targeted DOM extraction (tables, articles)
- [ ] Clean markdown formatting
- [ ] Intel Drone can scrape financial sites without paid API

## Tasks
- [ ] Design new browser task DSL for multi-step interactions
- [ ] Implement cookie banner handling
- [ ] Implement login form automation
- [ ] Create targeted DOM extraction engine
- [ ] Implement markdown formatting for extracted content
- [ ] Test with sample financial websites

## Notes
- Replaces basic Selenium-based browser tool
- Supports headless and headed modes
- Integrates with Intel Drone for research tasks