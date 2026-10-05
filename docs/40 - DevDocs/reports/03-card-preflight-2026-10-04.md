# Card 03 drc-d5 — preflight, 2026-10-04 (read-only)

BASE paths below are read in `/Users/cobalt/cobalt-wt/drc-k3-1004`, whose `HEAD` is `3e40359ac99508105d7bed5dc849ca336f3bd1b3` (= BASE).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `tail -n 3 drc-k3-check-2026-10-04.md` | last line: `CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · house B: Grok … · ready: YES` | OK |
| 1b | `git rev-parse drc/k3-surfaces-1004` | `3e40359ac99508105d7bed5dc849ca336f3bd1b3` | OK |
| 1c | `git diff --stat 3e40359a drc/k3-surfaces-1004` | empty (branch head = BASE) | OK |
| 1d | `git merge-base --is-ancestor main 3e40359a` | exit 1 — `main` is NOT an ancestor of BASE. `merge-base main 3e40359a` = `979ec797`; `log 3e40359a..main` = 41 commits (all `docs(desk)` / `docs(close)` / `docs(report)`, top `a1c846ff`); `diff --stat 979ec797 main -- src tests` = empty | FAIL |
| 2a | `git rev-parse --verify drc/d5-reconcile-1004` | `fatal: Needed a single revision` (exit 128) | OK |
| 2b | `ls /Users/cobalt/cobalt-wt/drc-d5-1004` | `No such file or directory` | OK |
| 3a | files-column paths at BASE (`ls` in the BASE worktree) | exist: `src/cobalt/drc/{build,units,imports}.py`, `src/cobalt/aset/drc_page.py`, `docs/40 - DevDocs/prompts/{BUILD-HUB,DEPLOY-HUB}.md`, `docs/40 - DevDocs/cobalt/drc/`. `reconcile.py` and the tests / `reconcile.md` are new or DOC | OK |
| 3b | `units.py` | `202:def reconcile(day_row: dict) -> str:` · `206:    return "\n".join(["legs: not built", "adjustment pending (legs writer not built)"])` (card: `:189`, `:193`) | OK — NOTE N1 |
| 3c | `build.py` names | `454:def plan_note(…)` · `494:    matched: dict[str, dict] = {}` · `620:    day_derived = {` · `768:    lines.append(f"R: planned … · realized not computed (D5)")` (card `:627`) · `876:    repaired = sorted(…)` / `878:        rebuild_notes(repaired, …)` in `run_drc_build` `:869` (card `:704`) | OK — NOTE N1 |
| 3d | `cli.py` | `275:        if args.dry_run:` · `279:            print(build.plan_note(args.date, deps=planning, event=event, check=True).report())` · `280:            return` (card `:288`–`:292`) | OK — NOTE N1 |
| 3e | `cards/legs.py` | `160:def _check_source` · `246:def insert_entry_leg(` · `274:   … source_import_id=None, held_stated=None,` · `409:    session = assert_writable("cards.leg.exit", …, now=now)` · `431:   … at=now, flag=flag,` · `381:def record_exit(` · `480:def record_correction(` · `520:        raise LegRefused("shares", f"REFUSED: a leg holds shares > 0, got {shares!r}…` (`519` is the `if shares is not None and int(shares) <= 0:`) · `285:def running_shares` · `323`–`328`: `if entry is not None:` … `base, basis = int(card["shares"]), BASIS_SHARES` · `677:def realized_r` · `713:def read_position` | OK |
| 3f | `src/cobalt/db_migrations/0021_legs.sql` | `63:    CHECK ((source = 'trading_log') = (source_import_id IS NOT NULL)),` · `93:CREATE OR REPLACE VIEW "user".legs_current_v AS`. The card writes `0021_legs.sql:63` with no directory: it is under `src/cobalt/db_migrations/` | OK |
| 3g | v2 design lines | `:80` `**Reconcile step (R67, F33) …`; `:96` `**Seam with v3 C1/C2 (R67) — S-C1, S-C2 …`; `:117` `[F-19] Grok (i)…Realized R stores fn_version = realized_r.1`; `:179` `\| D5 Reconcile writes to legs (R67) \|…`; `:181` `This slice: 5 chunks … D5 after v3 C2 is merged`; `:203` `\| X11 \| D5 (R2-1) \| Fable seat, verbatim…`; `:235` `## OPEN — ROUND 2 (R2-1)…`; `:247` `> Waits on the answer: D5's CLOSED-card path only…`; (`:79` `[F-09]` dry-run line also holds) | OK |
| 4 | RESTARTS class home | the card's `## RECORDS` names `RESTARTS: derived (drc/*, aset/* → com.cobalt.aset per v2 [F-27]; quote cobalt jobs restarts)`; `drc/*` and `aset/drc_page.py` are the only code paths | OK |
| 5a | `cto-2026-09-22.md` R67 / R90 | R67 (`:99`): `S3 EXITS R2-2 … the DAS trading-log import RECONCILES — DAS is the truth`; R90 (`:75`): `"If export has opened, leave it opened, and give me way to resolve in DRC." → the DRC IS BUILT` | OK |
| 5b | `s3-reread-draft-2026-10-04.md` `## DECISIONS` (`:53`) | D5-a `:54`, D5-b `:55`, D5-c `:56`, D5-d `:57`, each `ASK DESK … Default taken`; the card's defaults match | OK |
| 5c | `grep -n "^\| R233 "` etc. in `cto-2026-10-03.md` | R233 `:239` `D5 card 03 re-cut STACKED on 01+02 checked tips … ship in one deploy Mon 10-05 night`; R236 `:242` `only drafters write cards and prompts … drafter re-read before preflight`; R244 `:250` `brain judge: D5-a..d KEEP, no card change` | OK |
| 5d | `git show 3e40359a:tests/cobalt/test_legs_c2_db.py` | present (`S3 exits C2 as built … apply_0021 …`); the real-forward fixture is `aset` (`apply_0021`), X7 at the real `0021` | OK |
| 6 | `grep -n "^\| R219 "` | `225:\| R219 \| 10-04 15:01 ET \| HIS RULING: S3's K3, F15 P2, D5 run on the new workflow … \| HIS RULING · APPROVED \|` | OK |
| 7 | rows' red first | X: `RUN — asserts nothing; quoted`; D5-1 `red: the unit still prints legs: not built …`; D5-2 `red: with-DB, a card with ½ off tapped … negative control: --dry-run`; D5-3 `red: the X11 shape …`; D5-4 `red: the line still reads not computed (D5) …`; T: `git diff <BASE> -- <both hub files> shows only these ids added`; DOC: `—`. No K25 section in the card | OK |
| 8 | `grep -c -F "«FILL" 03-drc-d5-card.md` | `0`; `TIP:` (`:6`), `CHECK REPORT:` (`:8`), `HOUSE B:` (`:9`) are empty | OK |

## ISSUES

- Check 1d FAIL: `main` is not an ancestor of BASE `3e40359a`. `main` has moved on 41 docs-only commits since K3's base `979ec797` (`git diff --stat 979ec797 main -- src tests` is empty), so `src` / `tests` on `main` equal K3's base. The stacked deploy is unaffected in code; the desk decides whether the card's check reads `979ec797` as the merge-base or `main` is merged first.

## NOTES

- N1: the card's line numbers for `units.py`, `build.py` and `drc/cli.py` are the pre-K3 numbers; at BASE they moved (K3 added code above). The BASE lines are: `units.py` `reconcile` `:189`→`:202`, `legs: not built` `:193`→`:206`; `build.py` `realized not computed (D5)` `:627`→`:768`, `run_drc_build` re-pair `:704`→`:876`–`:878`; `cli.py` `:288`–`:292`→`:275`–`:280`. No name is missing. The `cards/legs.py`, `0021_legs.sql` and v2 design cites hold as stated.
- N2: `build.py` `matched` is a local in `plan_note` (`:494`), not a module name; `day_derived` is at `:620`.
- N3: K3's A31 section `drc-open-items/open_positions` (`units.py` `OPEN_ITEMS`), `drc_page.py` `_resolve_forms` (`:122`, K3-7's RESOLVE) and `imports.py` `day_view` (`:1018`) all exist at BASE, so D5-3's targets are real. `inputs.carried_from` is read at `build.py:395` and `:783`.
- N4: the dry-run negative control holds in the code: `--dry-run` calls `plan_note` alone (`cli.py:279`) and returns at `:280`.

PREFLIGHT DONE · card: 03 · checks: 8 · fails: 1 · ready: NO
