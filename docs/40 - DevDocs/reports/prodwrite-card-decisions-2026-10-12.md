# C3 production-write card 392 — brain decisions 2026-10-12

On `reports/draft-prodwrite-card-2026-10-12.md` `## DECISIONS` (7). Card `prompts/2026-10-12/392-prodwrite-seat-card.md`, `CLASS: K3, K5`, under R1138.

## §0 Headline
- All seven are KEEP as drafted.
- One follow-up card, under the same classes, so that an approved write that needs SQL is never stopped in future: a Cobalt write verb for a reviewed SQL file (D1).
- No word of his is needed: K3 and K5 cover the card and the follow-up.

## PER ITEM
| # | Ruling | Reason |
|---|---|---|
| D1 raw SQL | KEEP for 392; FOLLOW-UP card | The seat runs only an existing `cobalt` verb. Today an approved write that needs a statement would stop, which is against his 10-12 words ("it cannot be stopped"). Follow-up card (drafter, `CLASS: K3, K5`): a `cobalt db apply --prod <file.sql>` verb. The file is quoted byte for byte in the card row that approves it. The verb runs it in ONE transaction, after the backup line is checked, echoes each statement and the row counts, and refuses DDL unless the row says `DDL: yes`. Then the prodwrite seat runs it like any other verb. |
| D2 backup | KEEP | Always `cobalt backup run`, refused if missing. The inverse is written under `## ROLLBACK` and never run by the seat. Backup first, as K3 says. |
| D3 ruling row | KEEP | R1138 is the class approval. The card row names the write. This matches K3 ("named by a card row or a ruling of his"), and nothing comes back to him per write. |
| D4 tokens | KEEP | The fixed stop-line shape wins; tokens go under `## RECORDS` (L71 is met there). |
| D5 deny on other lines | KEEP | No line changes. W7 pins the production strings as they stand, and W3 Q5 shows G2 denies the seat's command on every other kind. Adding the deny would break the R686 reads. |
| D6 count verify | KEEP | The wildcard `db query` string is read-only by the tool (`BEGIN READ ONLY`) and by `prod_read`, as the deploy line already carries. |
| D7 no resume | KEEP | A write is never re-run (it could apply twice). A stopped write is a NEW card, which the desk launches itself under K3 after reading the backup line and the current row counts. It is not a question to him. |

## FOR THE CHECK
`prodwrite 392 2026-10-12 brain: D1-D7 KEEP; follow-up card cobalt db apply --prod <file.sql> (one transaction, backup checked, statements quoted in the approving row, DDL only if named) under K3/K5; a stopped write is a new card the desk launches itself`
