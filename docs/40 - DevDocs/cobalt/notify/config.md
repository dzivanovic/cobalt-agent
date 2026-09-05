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
