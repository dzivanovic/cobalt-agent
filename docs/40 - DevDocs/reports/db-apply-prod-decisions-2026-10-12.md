# Card 417 `cobalt db apply --prod` — brain decisions 2026-10-12

On `reports/draft-db-apply-prod-2026-10-12.md` :11-17 (7 ASK DESK). Card 417 is the follow-up named by D1 of `prodwrite-card-decisions-2026-10-12.md`. Classes K3 and K5.

## §0 Headline
- KEEP: 1, 2 (with `--ddl` gone), 3, 6, 7.
- CHANGE 4: no DDL through `apply` at all. Schema changes have one path, `db migrate`, by a migration card. This narrows the brain's own D1 text (`DDL: yes`), and it removes the contradiction the drafter flagged.
- CHANGE 5: no new tunable and no aset restart. The freshness limit is a constant in the verb.
- Nothing goes to Dejan: both changes narrow scope.

| # | Ruling | Reason |
|---|---|---|
| 1 | KEEP | No DB key is touched. The with-DB tests run on `cobalt_dev` (L76). |
| 2 | KEEP, minus `--ddl` | `--side` and `--sha256` are required, with no defaults. `--ddl` leaves with item 4. |
| 3 | KEEP | The SQL is quoted whole in the card and committed as `prompts/<date>/<nn>-<name>-apply.sql`. The row's `--sha256` ties the file to the approving row: the verb refuses a file whose hash differs. |
| 4 | CHANGE | `apply` refuses DDL always (CREATE, ALTER, DROP, TRUNCATE, GRANT, REVOKE, COMMENT, and any statement that does not parse as DML). A second schema path beside `db migrate` would split the schema record. A needed schema change is a migration card, deployed by the deploy hub. The hub's NEVER line is not narrowed. |
| 5 | CHANGE | A constant, `BACKUP_MAX_AGE_S = 900`, in the verb's module, read against `cobalt backup status`'s last-snapshot time. No `db.apply` tunable and no aset restart: the card's RESTARTS stay none. Changing it later is a one-line card. |
| 6 | KEEP | The `.gitignore` carve-out for `prompts/20*/*-apply.sql` only. |
| 7 | KEEP | CHECK REPORT filled at write. |

## FOR THE CHECK
`card 417 2026-10-12 brain: 1 2 3 6 7 KEEP (no --ddl flag); 4 CHANGE apply refuses all DDL, schema only by db migrate; 5 CHANGE constant BACKUP_MAX_AGE_S=900 in the verb, no tunable, no restart`
