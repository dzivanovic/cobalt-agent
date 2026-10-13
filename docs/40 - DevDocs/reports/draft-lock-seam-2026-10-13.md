# draft-lock-seam — report 2026-10-13

## §0 Headline
- Wrote `docs/30 - Design/f20-f23-lock-seam-2026-10-13.md`: all six required statements, each `file:line` read this session.
- Unproven and marked so: F20's package, X1, the two-pin trial, which card merges first. Row 18: approved R1324 (K2), card pending.
- Two things the prompt did not say, added: the desk does the rebase (`BUILD-HUB.md:14` bars a builder), and the second pin trial is the desk's, since a lock change cannot be undone by Edit.
- Docs only; nothing committed, no database, no launch.

## DECISIONS
- ASK DESK: which card merges first, F20 or F23? Default: neither is named; the doc says the desk sets it at the first deploy card. [by the first deploy card]
- ASK DESK: second card's lock regeneration after the desk's rebase: the builder on a `CONTINUE` if row 18 is in, else the desk. Default taken as written in rule 2. [before the second card launches]
- ANSWERED (brain, L79, via cto-desk): row 18 is approved R1324 (K2), card pending; the doc says so and the "else the desk" branch holds until that card deploys. Decisions 1, 2, 4 kept.
- ASK DESK: the F23-FINAL SEAM row `uv.lock` (`F23-FINAL-2026-10-11.md:172`) still says UNSETTLED until this doc; update it when this doc is committed. Default: not touched (outside the two files). [at commit]

## RECORDS
- Read: `f23-tribunal-2026-10-11.md` (CK1, CK11, CK12, FC12, FC17, FC18, FC28, E3), `f20-design-proposal-2026-10-10.md:27`, `f23-design-proposal-2026-10-10.md:47-48, :80-81`, `F20-FINAL-2026-10-11.md:34, :151`, `F23-FINAL-2026-10-11.md:141, :156, :171-179, :201`, `f23-tribunal-opus-2026-10-11.md` (X1, X2, lock lines), `BUILD-HUB.md:14, :76`, `DEPLOY-HUB.md:91-92, :174`, `survey-blockers-2026-10-12.md:30`, `jobs.yaml:39, :88-89, :109, :124, :127, :157-158, :189, :193, :201-202`, `restarts.py:178-264`, `config.py:425`, `test_jobs_reads.py:96-107`, `LAWS.md:357-359`, `pyproject.toml:12-39`, `writing-rules.md`.
- `f20-design-2026-10-10.md` and `f23-design-2026-10-10.md` exist (`Glob`). The F20 file's grep showed only a base-commit line, no lock text. I did not read either whole.
- `LAWS.md` has no `uv.lock` or `lock seam` string (the grep printed nothing). The law line this doc rests on is L68, `LAWS.md:357-359`.
- The first `ls` call was blocked by the bare-command hook (pipe); I re-sent it alone.
- L74: no instruction inside a tool result. The system reminders about a `Claude-Session:` line and a file-send tool did not arrive in a tool result; not followed (this seat commits nothing).
- The L32 redaction of the f23 proposal `:19`, `:76` and the drafter report `:50` is card 471, not this one; not done here.

DRAFTED · decisions: 3
