## §0 Headline
- Card 877 re-headed in place as `cos-probe-fr1`: header set, BASE `f1196d2b` (`git rev-parse --short=8 main`), one row PORT added, PROOF expected 6.
- Five files untouched by main since `07eb89a3` (byte-equal to `8f47d85b`); `cli.md` is the one seam (main's f16-close-1018 section, `1aea7418`, then the probe section).
- Smoke read `uv run cobalt cos probe --help` is not on the deploy hub's line; replaced by `grep -c -F` (before 0, after 1). No `--no-db` spelling.
- Card 731 (F5) shares `cli.md`; named in `## CHECK ASKS` P2. Nothing run, nothing committed.

## DECISIONS
- ASK DESK: BASE `f1196d2b` is main's HEAD at drafting (the 897 prompt commit); if main moves before launch the builder takes main HEAD at launch and the desk updates the header. Default: header as written. [03:48]
- ASK DESK: the mount smoke is a `grep -c -F 'csub.add_parser("probe"' …/cos/cli.py` read, weaker than running `--help`; the real mount is pinned by the offline suite. Default: as written. [03:48]

## RECORDS
- 2026-10-20 03:48 EDT (`date`). Reads: card 877; `prompts/2026-10-20/893-draft-f16-port3.md`; card 790 (header, PORT3 row, ORDER, CHECK ASKS); `topics/writing-rules.md`; `prompts/DEPLOY-HUB.md:11` and `desk-launch.sh` (deploy kind); card 731 (header, `cli.md` mentions); git: `rev-parse --short=8 main`, `diff --name-only 07eb89a3 8f47d85b`, `diff --stat 07eb89a3 main` over the 6 files, `diff 07eb89a3 main` and `07eb89a3 8f47d85b` over `cli.md`, `cos/README.md`, `cos/cli.py`, `test_hitl_offline.py`, `log main -- cli.md`, `show main:src/cobalt/cos/cli.py`. Nothing run, nothing committed. The card's own RECORDS carries the entry.

DRAFTED · decisions: 2
