## §0 Headline
- Card drafted: `prompts/2026-10-10/251-tribunal-guard-card.md`, one row T, `BASE` left as `«FILL»`.
- G9 extends to a tribunal hub by prompt name; `HOUSE` and `claude` denial unchanged.
- One line number corrected: `seat()` ends at `:753`, not `:751`.
- Follow-up row (`seat()` brain for any `prompts/20*/` seat) sits in `## NOT IN THIS JOB`, not built.

## CHANGES
- Wrote `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/251-tribunal-guard-card.md` (header, `## ROWS`, `## NOT IN THIS JOB`, `## READ`, `## CHECK ASKS`, `## RECORDS`).
- Wrote this report. No other file touched.

## DECISIONS
1. `DB: none`, not omitted: `CARD.md` reads `none` as "no `cobalt_dev` lock", and both files sit under `ops/` and `tests/ops/`; omitting it would take a lock for nothing.
2. Tribunal name match is `(^|/)prompts/20[^/]*/[0-9]+-(?!draft)[a-z0-9-]*-tribunal(-r[0-9]+)?\.md$`, not `*-tribunal*.md`: that glob would also admit the drafter (236), the Opus seat (238), the derive (239) and the preflight (249). Real hub names include `-r2` (`17-f15-tribunal-r2.md`).
3. The flag is a new `seat()` field `tribunal`, not a new kind: the hub stays `worker`, so G1-G6 apply unchanged.
4. Red set: only test 1 is red on `BASE`; the denial and fence tests are written green to pin them.
5. Astra probe: 237 line 9 has no ` < /dev/null`, line 43 has it; the card allows both, matching 237 over the row.
6. RESTARTS left UNPROVEN at drafting (no `uv` in this seat's allow list); the build hub runs it.

## RECORDS
- `git -C /Users/cobalt/cobalt show d0a5fbb8:ops/desk/bare-guard.py`, read in full: `:83`, `:88`, `:124-125`, `:731-753`, `:746-747`, `:748-749`, `:1015-1041`, `:1033-1037` as the card lists.
- `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- ops/desk/bare-guard.py tests/ops/test_bare_guard.py`: no output.
- Read: `237-f4-tribunal.md` lines 1, 9, 37-43; `CHECK-HUB.md` line 10 (`grep -n` found `codex exec --skip-git-repo-check`); `tests/ops/test_bare_guard.py` `:150-279`, `:1180-1289`; `ls` of `prompts/2026-10-10/`, `2026-09-29/`, `2026-09-22/`; `CARD.md` and `writing-rules.md` whole.
- `rev-parse --short=8 HEAD` printed `fccbb258` (main HEAD; the code commit is `d0a5fbb8`).

TRIBUNAL-GUARD CARD DRAFTED · decisions: 6
