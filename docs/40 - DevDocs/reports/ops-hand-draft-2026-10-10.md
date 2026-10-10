# ops-hand card · drafter report · 2026-10-10

## §0 Headline
- Card `prompts/2026-10-10/231-ops-hand-card.md` written: 6 rows (H1-H6), 3 red-first (H1, H2, H4; H3 proved by H4's tests), 1 pin (H5), 1 RUN (H6).
- The seat today has no launch: `desk-launch.sh` kind `prompt` passes only `auto`/`plan` (`:452-457`); H4 adds kind `ops-hand`, inert until his row (`«INSTALL` title).
- The bound is the guard, not the classifier: G12 (H2) denies every non-class command before the phone prompt; class = kill of one pid, kickstart of a `com.cobalt.*` label, ps/pgrep/launchctl print.
- 5 DECISIONS for him (D1 L63 text, D2 standing list, D3 class, D4 tap rule, D5 orphan-clean); no desk allow or settings edit needed.

## CHANGES
- NEW `docs/40 - DevDocs/prompts/2026-10-10/231-ops-hand-card.md` (header per prompt; `BASE` `«FILL»`; `TIP`, `CHECK REPORT`, `HOUSE B` empty; `DB` omitted).
- NEW this report.

## DECISIONS
Each took its default; the card's `## DECISIONS FOR HIM` carries D1-D5 for him.
- DESIGN 1: seat kind by the basename `OPS-HAND.md` of the first `Read '…'`, ahead of every cwd rule. Reason: from `prompts/2026-10-10/` in the repo the guard calls it `brain`; from a plain cwd it is `None` and skips G2 and G7 (`bare-guard.py:746,1029,1036`).
- DESIGN 2: cwd `/Users/cobalt/cobalt-wt/.ops-hand`, not the repo, so a tap's persisted "don't ask again" lands outside the desk's `~/cobalt/.claude/settings.local.json`; the launcher refuses while that file exists (D4). `worktree_of` skips a dot name (`:672`), so the guard does not call it a worker.
- DESIGN 3: fixed file + launcher kind, not a `prompt`: the prompt kind's mode gate stays as it is (R411; X3 asks the check to prove it byte-identical).
- DESIGN 4: no file write on the seat; it reports by `SendMessage` to `cto-desk`, and the desk writes its §4 row.
- DESIGN 5: model Sonnet 5.5 (it runs handed commands, judges nothing).
- OPEN, NOT KNOWN: whether `--remote-control` relays a default-mode permission prompt to his phone, and whether the seat holds `SendMessage`. First live proof is the desk's (`kill -0 <aset pid>`), in the card's `## RECORDS`.

## RECORDS
- Prompt read 07:48 ET; `CARD.md` whole; `areas/cobalt.md` `## What Cobalt is`, `## Build rules`-end; `LAWS.md` L36, L37, L41, L61-L64, L74; `cto-2026-10-10.md` R851-R857; `cto-2026-10-10-words.md` R855; `aset-orphan-answer-2026-10-10.md` §0, ROWS, `## MODEL AND ORDER`; `brain-direction-2026-10-02.md:190`; `prompts/2026-10-10/228` header.
- `git -C /Users/cobalt/cobalt show d0a5fbb8:ops/desk/desk-launch.sh` → 219-235 `run_launch`, 308 usage, 314-320 size guard, 411-547 kind prompt, 425 `committed`, 452-457 mode gate (`auto|plan`), 485-486 dialog-tool gate, 489-490 seat gate.
- `git -C /Users/cobalt/cobalt show d0a5fbb8:ops/desk/bare-guard.py` → 77-82 HUBS, 83 WORKERS, 88 LAUNCHERS, 112 PROD, 668-672 `worktree_of`, 731-752 `seat`, 1029 G2, 1036 G7, 1131 `decide`, 1195 `main`.
- `git -C /Users/cobalt/cobalt show d0a5fbb8:ops/desk/stop-guard.py`, `desk-list.sh`, `desk-done.sh`, `job-clean.sh`, `.claude/settings.json` (:15, :19, :20, :29).
- `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 -- <the six files>` → only `.claude/settings.json` differs; `stop-guard.py` lines 112, 386, 405 read from the working file.
- `git -C /Users/cobalt/cobalt show d0a5fbb8:tests/ops/` → `test_bare_guard.py`, `test_stop_guard.py`, `test_desk_launch_brain.py`, `test_desk_launch_devfix.py` present; no `test_desk_launch_ops_hand.py`.
- `~/.claude/settings.json` hooks: PreToolUse Bash → `bare-guard.py`; Stop → `stop-guard.py` (read 07:57 ET).
- main HEAD at draft 07:52 ET: `02893841`.
- RESTARTS: none expected (card row H6 proves it).

OPS HAND CARD DRAFTED · decisions: 5
