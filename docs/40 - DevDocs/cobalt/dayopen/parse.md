# `src/cobalt/dayopen/parse.py`

Pure regex parsers over the real `logs/heartbeat.log` plain console
block (`HEARTBEAT GREEN|RED — ... (TIMESTAMP TZ)` headers and
`OK|RED  radar  <detail>` probe lines), `logs/heartbeat.err`'s loguru
lines, and `docs/30 - Design/archiver-runs.md`'s markdown table(s).

`newest_radar_probe_line` / `newest_beat_header` scan from the end of
the file for C3. `all_beat_headers` and `failed_lines` feed C6: the
latter is a SUBSTRING match on "FAILED", not a log-level filter — a
genuine `job_run` wrapper crash logs `... FAILED — <Exception>: ...` at
ERROR level, but so does a normal RED beat's own
`heartbeat: RED — N job(s)` line, and only the first contains the
literal word. `last_markdown_table_row` returns the LAST `|`-table in a
file (archiver-runs.md carries two, split by the "Database column
added" ruling) — header and last data row, by column name, so an added
or reordered column never mis-maps a value.

None of this parses the markdown-table-diff rendering of the same beat
that heartbeat.log also carries (the vault daily-note's before/after
diff) — same information, second format, not needed.
