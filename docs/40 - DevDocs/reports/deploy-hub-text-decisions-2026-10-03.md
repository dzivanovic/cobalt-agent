# JUDGE — card 02b deploy-hub-text, Grok's 8 findings (2026-10-03, brain; desk clock 19:4x ET)

Aim: deploy 02b tonight as the P7/STEP-T/STEP-C fix ONLY. The "when it lands" sentences (T2–T5) are cut from 02b: they describe the chain's text and belong to the port card `03d`, where they are written against the chain's own clauses. All 8 HOLD.

| # | finding | answer | fix text (02b fix round) |
|---|---|---|---|
| 1 | odd `.sql` names and registry edits slip the pattern | HOLD | P7: `a MIGRATION is any file ending .sql under src/cobalt/db_migrations/ (whatever its name), or a changed line inside FORWARD = (…) of src/cobalt/db_migrations/__init__.py that adds, removes or reorders an entry; every .py under that folder (cli.py, placement.py, dev_rebuild.py), tests and docs are CODE and pass MIGRATIONS: none` |
| 2 | a comment or rewrap inside FORWARD reads as a migration; a `NNNN_*.sql` test fixture reads as one | HOLD | covered by 1's text (entry added/removed/reordered only; no `.sql` fixtures exist under the folder — a RECORDS line says so, re-read by the check) |
| 3 | STEP-T greps `MIGRATIONS_DIR / "00` and misses `0100` | HOLD | STEP-T: `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/src/cobalt/db_migrations/__init__.py` (the `00` dropped) |
| 4 | T6 lets any `ops/<other>/` plist pass; `ops/desk/` with a resident Label passes | HOLD | STEP-C: `a plist ADDED or MODIFIED anywhere under ops/ is refused, except one under ops/desk/ whose Label (the line after <key>Label</key>, read by grep -A1 -F) is not a key of configs/cobalt/jobs.yaml and whose path is not ops/<label>.plist` |
| 5 | T2's gate.sh / gate-clean sentences on a text with no gate.sh stall a red gate with the lock held | HOLD → CUT T2 | removed from 02b; the chain's sentence is 03d's |
| 6 | T3's equal-tree sentence is not the chain's clause | HOLD → CUT T3 | removed; 03d writes the clause as ruled: one TIP branch, docs-only diff from the check's code tip, with-DB count above 0, else the gate whole |
| 7 | T4's (v) sentence is not the chain's (v) | HOLD → CUT T4 | removed; 03d: (v) = empty restart set AND MIGRATIONS none, provisional at P1, the SET re-read at STEP-R |
| 8 | T5 forbids the resend 4.6's one retry needs | HOLD → CUT T5 | removed; 03d's flag exception: `inside the outage a blocked call is resent once as single calls; still blocked → STEP-5` |

FOR THE CHECK (card 02b `## RECORDS`): `Grok's 8 findings answered (reports/deploy-hub-text-decisions-2026-10-03.md): 1–4 fixed in the P7, STEP-T and STEP-C sentences; T2–T5 cut from this card and carried to 03d; the card is the P7/T/C fix only.`
