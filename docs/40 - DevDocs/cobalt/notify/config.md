# `src/cobalt/notify/config.py`

## What it does
`configs/cobalt/notify.yaml` → `NotifyConfig` / `MattermostConfig`
(`enabled`, `dm_username`, `vault_key`, `timeout_s`).

## No credential lives here
Only the vault **key name**. The URL and token come from VaultManager,
exactly as the old tree's did.

## No built-in default
A missing config file crashes: an alert channel nobody declared is an
alert channel nobody checks.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

`MattermostConfig.timeout_s` is GONE (ADR-0008 D7). It was the last
threshold in the new core still living in a config file; it is a
`tunables.yaml` row now, like the email channel's two. What is left in
`notify.yaml` is WHO to talk to and WHETHER the channel is on.
