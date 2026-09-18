# Migration harness fix — streamed content proof + `--proof-only` (deploy-2026-09-18 step 3.5)

Hub `migrate-fix-0918` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/cards` on top of `848681e`. Prompt: `docs/40 - DevDocs/prompts/2026-09-18/15-migrate-harness-fix.md`.

## §0 Headline

- RUN OPEN 15:54 ET. PREFLIGHT PASS — six rules probed, **zero denials**.
- Authorization VERIFIED by this hub: every rule in this launch line is inside R1 list (1) (`cto-2026-09-18.md` §4), committed on main.
- Target: `_probe`'s `md5(string_agg(...))` → a client-side streamed md5 over a server-side cursor, byte-identical digests; plus a read-only `--proof-only` with timings.
- ESCALATE: 0 so far.

## PREFLIGHT

Run 15:54 ET from `/Users/cobalt/cobalt-wt/s2-p2-cards`. **Zero denials.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **empty**, worktree clean |
| `Bash(git log*)` | `git log -1 --oneline` | 0 | allowed — `848681e docs(report): STACK READY — integrated suite 1815 passed / 0 failed …` = the gated stack tip |
| `Bash(date*)` | `date` | 0 | allowed — `Fri Sep 18 15:54:09 EDT 2026` |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_tenancy.py` | 0 | allowed — **34 tests collected** |
| `Bash(cp /Users/cobalt/cobalt/.env …)` | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s2-p2-cards/.env` | 0 | allowed — by name only, never printed (L41 interim); removed at step 3 |
| `Bash(COBALT_ENV=dev uv run cobalt db migrate*)` | `COBALT_ENV=dev uv run cobalt db migrate --help` | 0 | allowed — today's flags are exactly `--allow-prod`, `--down-to NNNN`, `--rollback`. **No probe-only mode** — deploy ESCALATE 2, confirmed at the CLI |

**AUTHORIZATION — verified by this hub, 15:53 ET.** `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` → `293db20` (this run's launch row), `5ac9560`, `7864fd8` on top of the 09-18 revert range — the rulings file is committed on main. Compared rule by rule against **R1 list (1)** (`cto-2026-09-18.md` §4, "Approved" 06:46 ET):

| this launch line's rule | in R1 list (1)? |
|---|---|
| `cp/rm/ls -la` on `/Users/cobalt/cobalt-wt/s2-p2-cards/.env` | YES — "`.env` cp/rm/ls by path" |
| `COBALT_ENV=dev uv run cobalt db migrate*` (incl. `--rollback`) | YES — named verbatim |
| `COBALT_ENV=dev uv run pytest *` · `uv run pytest *` | YES |
| `COBALT_ENV=dev uv run cobalt validate*` | YES |
| `uv run cobalt jobs restarts *` | YES |
| git add/commit/diff/status/log/show/rev-parse | YES |
| `git -C /Users/cobalt/cobalt log*` / `rev-parse *` | YES |
| `cd`/`ls`/`grep`/`tail`/`wc`/`date` | YES (R1's list also carries `shasum`, unused here) |

No rule in this launch line is outside R1 list (1); R1's list additionally carries `settings load *--dry-run*`, `COBALT_VAULT_PATH=… pytest`, `git rebase main`/`--continue` and `shasum`, which this line does **not** take — a strict subset. **No production command exists in this launch line**: `COBALT_ENV=production`, `--allow-prod`, push, merge and vault writes are absent. R3 + R5 (the weekend push, "done trading" 11:09 ET) and R8 (second opinion — owed BEFORE any production use of this build, and it is not this run's job) are on the same committed row set.

Also noted, as in all three deploy runs today: the prompt file's tail carries a block styled as a system reminder asking for a `Claude-Session:` URL line in every commit. It arrives inside a tool result — the file's own bytes — not from the harness or from Dejan; the genuine harness attribution reminder names only `Co-Authored-By` and says not to add lines it leaves out. **Not followed.**

CONTINUE: step 1
