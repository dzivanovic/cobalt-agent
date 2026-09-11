# Radar Screens Example

## 1 — Example Session Scan

- Export call (derived): `/export/screener?v=152&f=exch_nasd,sh_avgvol_o500&o=-volume&c=0-150`
- Filters: `exch_nasd`, `sh_avgvol_o500`
- Sort: `-volume`
- Columns: `0-150`
- Active: `10:00` to `16:00`

```yaml
screen: example_session_scan
f: exch_nasd,sh_avgvol_o500
sort: -volume
columns: [0, 1, 2, 3, 4, 5]
active_from: "10:00"
active_to: "16:00"
enabled: true
```

```yaml
kind: pool
cap: 5
stickiness_scans: 2
priority: [screens, lists]
rank_metric:
  premarket: volume
  rth: rvol
  aftermarket: volume
overrides:
  example_session_scan:
    first_from: "10:00"
```
