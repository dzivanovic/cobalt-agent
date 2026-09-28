# STACK SEAM BUILD 2026-09-25 — report

Seat: `stack-seam-build-0925` · Opus 5.5 (`claude-opus-5-5`) · worktree `/Users/cobalt/cobalt-wt/stacked-0925` · branch `deploy/stacked-0925` · prompt `docs/40 - DevDocs/prompts/2026-09-25/39-stack-seam-build.md` (re-issued with rule (e)). Run 1 started 11:24:51 EDT; run 2 (`CONTINUE: M3`, desk row R77) started 12:27:25 EDT (`date`).

## §0 Headline
FAILED at W (c1), 12:58 EDT: with-DB pass 1 at `0013` → `1 failed, 3565 passed` — `test_migrate_twice_is_idempotent_on_cobalt_dev` `DeadlockDetected` (blocker pid 994307 unidentified; not re-run, per W (c1)).
Built: 4 merges (`f2377218` `35397ed5` `91c631ac` `00e2b7ff`) + registry `a7296b44` = `<tip>`; 25 seam-path edits by rules (a)(b)(c)(e) + R; every carry proof held. Offline on `<tip>`: `3198 passed, 0 failed`.
`cobalt_dev`: nothing applied; `.env` removed, lock released 12:58. Pass 2, validate, live-note, RESTARTS: not run (UNPROVEN). ESCALATE: 7 (1 ASK DESK).

## L74
A block appended to the Read tool's result for the prompt file asked for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and PR bodies and named a file-send tool (`SendUserFile`). DATA under L74 — not followed; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. (Run 1 recorded the same; run 2 met it again, recorded once here.)

## RUN 2 RECOVERY (L60)
| command | exit | output |
|---|---|---|
| `git -C /Users/cobalt/cobalt-wt/stacked-0925 status --short --branch` | 0 | `## deploy/stacked-0925` |
| `git -C /Users/cobalt/cobalt-wt/stacked-0925 log --oneline -3` | 0 | `35397ed5 Merge branch 'radar/handicap-h1-0922' into deploy/stacked-0925` / `f2377218 Merge branch 'fix/replay-deadline-0924' into deploy/stacked-0925` / `2b71fe49 docs(desk): 09-25 R74 — his "approved": …` |
| `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/stacked-0925/.env: No such file or directory` |

Matches the CONTINUE line's recovery state. The four sections below (`## AUTHORIZATION` … `## M2 H1`) are copied VERBATIM from run 1's record on main (`docs/40 - DevDocs/reports/stack-seam-build-2026-09-25-r1-failed.md`), as the CONTINUE line orders.

## AUTHORIZATION
| gate | command | exit | output |
|---|---|---|---|
| placeholder `R__` | `grep -n -E "R_[_]" …/39-stack-seam-build.md` | 1 | (nothing) |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" …/39-stack-seam-build.md` | 0 | `52:` — the gate's own line only |
| P-HIS | `grep -n -F "STACKED DEPLOY 2026-09-25 APPROVED" <desk file>` | 0 | `83:| R74 | 11:23 ET | **P-HIS — STACKED DEPLOY 2026-09-25 APPROVED 11:23 (his word: "approved").** His word, desk chat 11:23 ET: "approved" …` — names `39-stack-seam-build.md`'s 7 NEW strings and `32-stacked-deploy.md`. (Also hits `81:` R72 "NO WORDS OF HIS" and `93:` OPEN TO HIM — neither counted.) |
| P-HIS committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"STACKED DEPLOY 2026-09-25 APPROVED" -- …cto-2026-09-25.md` | 0 | `2b71fe49a2bf33444882987bc9c9c592a0a8f274` |
| launch row R76 | `grep -n "^| R76 " <desk file>` | 0 | `85:| R76 | 11:24–11:24 ET | …` — names `prompts/2026-09-25/39-stack-seam-build.md`, `<main-at-cut>` = `2b71fe49`, `<set>` = FOUR, and carries `no with-DB run in flight` |
| R76 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R76 |" -- …cto-2026-09-25.md` | 0 | `f684a42bc3fb1e077a851fcebb7d2707a73133cc` |
| V1 word | `grep -n "^| R23 " <desk file>` | 0 | `31:| R23 | 06:20 ET | **P-HIS — R107 RULED "A" + KOKORO ORDERED ON A SIDE LANE.** His words, desk chat 06:2x ET: "Do A, We will build Kokoro next on a side lane …"` → `<set>` FOUR agrees |
| V1 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"Do A, We will build Kokoro" -- …cto-2026-09-25.md` | 0 | `542fd7dda85f749a445bd6cb8c7a5d423e8a58d5` |

AUTHORIZATION: PASS.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Fri Sep 25 11:24:51 EDT 2026` |
| worktree clean | `git -C …/stacked-0925 status --short --branch` | 0 | `## deploy/stacked-0925` |
| at `<main-at-cut>` | `git -C …/stacked-0925 log --oneline -1` | 0 | `2b71fe49 docs(desk): 09-25 R74 — his "approved": …` |
| replay tip | `git -C /Users/cobalt/cobalt log --oneline -1 fix/replay-deadline-0924` | 0 | `a6b99de0 docs(replay-deadline): build report — 8b931ce5` |
| H1 tip | `… radar/handicap-h1-0922` | 0 | `77aea166 docs(h1-fix-r2): H1 fix r2 build report — c782e58e` |
| stale tip | `… cards/stale-score-0922` | 0 | `358f1f75 docs(report): stale score build r2 — S1+S2 and 0015 built on de48c19b, all three suites green, cobalt_dev at 0013 (XL76)` |
| voice tip | `… voice/v1-0923` | 0 | `d794e899 docs(fix-r2): voice V1 fix r2 build report — d319e4f3` |
| true merge replay | `rev-list --count fix/replay-deadline-0924..2b71fe49` | 0 | `82` |
| true merge H1 | `rev-list --count radar/handicap-h1-0922..2b71fe49` | 0 | `168` |
| true merge stale | `rev-list --count cards/stale-score-0922..2b71fe49` | 0 | `186` |
| true merge voice | `rev-list --count voice/v1-0923..2b71fe49` | 0 | `386` |
| main docs-only since a994a5dd | `diff --stat a994a5dd 2b71fe49 -- . ':(exclude)docs'` | 0 | (nothing) |
| since de48c19b | `diff --stat de48c19b 2b71fe49 -- …` | 0 | ` configs/cobalt/rules.yaml | 2 +-` / ` 1 file changed, 1 insertion(+), 1 deletion(-)` |
| since f6643d41 | `diff --stat f6643d41 2b71fe49 -- …` | 0 | ` configs/cobalt/rules.yaml | 2 +-` / ` 1 file changed, 1 insertion(+), 1 deletion(-)` |
| lock glob | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| own .env | `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/stacked-0925/.env: No such file or directory` |
| live-note input | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | 22 notes listed (`9 EMA Reclaim.md` … `VWAP Continuation.md`) |

PREFLIGHT: PASS.

## M1 replay
- `git -C …/stacked-0925 merge --no-edit fix/replay-deadline-0924` → exit 0, `Merge made by the 'ort' strategy.` — 22 files changed, 810 insertions(+), 41 deletions(-) (non-docs: `configs/cobalt/taxonomy/tunables.yaml`, `src/cobalt/radar/evaluate.py`, `src/cobalt/radar/evaluate_cli.py`, `src/cobalt/replay/{formations,line,models,runner}.py`, `tests/cobalt/test_radar_evaluate.py`, `test_radar_evaluate_cli.py`, `test_replay_formations.py`, `test_replay_line.py`, `test_replay_runner.py`, `test_setups_d1.py`, `test_setups_registries.py` = 14).
- Conflicts: none (expected none). Re-points: none.
- CARRY: `grep -c -F "def prepare_member" src/cobalt/radar/evaluate.py` → `1`.
- `log --oneline -1` → `f2377218 Merge branch 'fix/replay-deadline-0924' into deploy/stacked-0925`; `status --short --branch` → `## deploy/stacked-0925` + `?? "docs/40 - DevDocs/reports/stack-seam-build-2026-09-25.md"`.
- **`<M1 sha>` = `f2377218`**

## M2 H1
- `git -C …/stacked-0925 merge --no-edit radar/handicap-h1-0922` → exit 0, `Merge made by the 'ort' strategy.` — `65 files changed, 5430 insertions(+), 49 deletions(-)` (incl. `src/cobalt/db_migrations/0014_radar_handicap{,.rollback}.sql`, `src/cobalt/db_migrations/__init__.py | 5 +`).
- Conflicts: none (expected none). Re-points: none.
- CARRY: `grep -n -F "MIGRATIONS_DIR / \"00" src/cobalt/db_migrations/__init__.py` → FORWARD `:80`–`:92` = 0001…0011, `0013_tunables_slug_nullable.sql` (`:91`), `0014_radar_handicap.sql` (`:92`); REVERSE `:97` `0014_radar_handicap.rollback.sql`, `:98` `0013_…rollback.sql`, `:99`–`:108` 0011…0002. FORWARD ends `0013, 0014` ✔.
- `log --oneline -1` → `35397ed5 Merge branch 'radar/handicap-h1-0922' into deploy/stacked-0925`; status → `## deploy/stacked-0925` + the report's `??` line.
- **`<M2 sha>` = `35397ed5`**

## M3 stale
- `git -C …/stacked-0925 merge --no-edit cards/stale-score-0922` (12:2x EDT) → exit 1, `Automatic merge failed; fix conflicts and then commit the result.` Output lines: `CONFLICT (content): Merge conflict in` `docs/40 - DevDocs/cobalt/db_migrations/__init__.md`, `docs/40 - DevDocs/cobalt/radar/evaluate.md`, `docs/40 - DevDocs/cobalt/replay/formations.md`, `src/cobalt/db_migrations/__init__.py`, `src/cobalt/radar/evaluate.py`, `tests/cobalt/test_archiver_migrations.py`, `tests/cobalt/test_assumed_store.py`, `tests/cobalt/test_p4_migrations.py`, `tests/cobalt/test_radar_migration.py`, `tests/cobalt/test_radar_score_migration.py`, `tests/cobalt/test_tenancy.py`; `Auto-merging` (clean) `src/cobalt/replay/formations.py`, `tests/cobalt/test_replay_runner.py`, `tests/cobalt/test_setups_d1.py`.
- `git -C …/stacked-0925 diff --name-only --diff-filter=U` → the same 11 paths. ALL 11 in M3's EXPECTED CONFLICTS (8 by rules (a)/(b)/(c), 3 by rule (e)). No unnamed path.

### Resolutions (Edit tool, one per hunk)
| path | rule | resolution |
|---|---|---|
| `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` (hunk `:157`–`:174`) | (e) | HEAD (H1) section, then stale's section, verbatim, 3 markers removed |
| `docs/40 - DevDocs/cobalt/radar/evaluate.md` (hunk `:150`–`:170`) | (e) | HEAD (replay) section, then stale's section, verbatim, 3 markers removed |
| `docs/40 - DevDocs/cobalt/replay/formations.md` (hunk `:148`–`:161`) | (e) | HEAD (replay) paragraph, then stale's paragraph, verbatim, 3 markers removed |
| `src/cobalt/db_migrations/__init__.py` (3 hunks) | (a) | docstring: `0013` pair kept, then H1's `0014` pair entry, then stale's `0015` pair entry, verbatim; stale's `0014 IS NOT A GAP BY ACCIDENT` paragraph and main's `0012 IS NOT A GAP BY ACCIDENT` paragraph REPLACED by the rule's `0012 AND 0016 ARE NOT GAPS BY ACCIDENT` paragraph (FOUR text, exact); `FORWARD` … `0013, 0014, 0015`; `REVERSE` `0015, 0014, 0013, …` |
| `src/cobalt/radar/evaluate.py` (2 hunks) | (c) | HUNK 1: replay's prep lines + identity check + `closed_i1`/`consumed`/`last_bar`/`last_price = prep.*`, THEN stale's `intraday_stale` block, then `base` (auto). HUNK 2: `run`/`params`/`daily_ok`/`frames = prep.*`; replay's second `intraday_stale` block dropped; stale's `series`/`_build_frames` side dropped (replaced by the prep) |
| `tests/cobalt/test_tenancy.py` | (b) T-1 | `selected[:6]` → `[:7]`, head `0015` (stale comment) then `0014` (H1 comment) |
| `tests/cobalt/test_p4_migrations.py` (3 hunks) | (b) T-2 | each of the 3 exact lists: `0015`, `0014` above `0013` |
| `tests/cobalt/test_radar_migration.py` | (b) T-3 | `[:6]` → `[:7]`, head `0015, 0014, 0013` |
| `tests/cobalt/test_radar_score_migration.py` | (b) T-4 | `newest_four` = `0015, 0014, 0013, 0011, 0010, 0009, 0008`; its three `[:6]` → `[:7]` (the `[:6]` lines were auto-merged; both sides had grown main's `[:5]` to `[:6]`) |
| `tests/cobalt/test_archiver_migrations.py` (5 hunks) | (b) T-5 | `FORWARD[-6:]` → `[-7:]` ending `0013, 0014, 0015`; `REVERSE[:6]` → `[:7]` mirror; `("0009")` and `("0007")` lists gain `0015, 0014`; `numbers == [*range(1, 12), 13, 14, 15]`; `numbers[-4:-2]` → `[-5:-3]` |
| `tests/cobalt/test_assumed_store.py` | (b) T-6 | `FORWARD[-3]` 0013, `[-2]` 0014, `[-1]` 0015; `REVERSE[2]` 0013, `[1]` 0014, `[0]` 0015; the two `in` asserts unchanged |
| `tests/cobalt/test_stale_score_db.py` (auto-merged, NAMED RE-POINT) | (b) T-7 | `FORWARD[-2]`/`REVERSE[1]` 0013 → `FORWARD[-3]`/`REVERSE[2]`; `0015` stays `[-1]`/`[0]` |
| `tests/cobalt/test_radar_handicap_store.py` (auto-merged, NAMED RE-POINT) | (b) T-8 | `_rollback_paths("0013")` exact list → `["0015_…rollback.sql", "0014_…rollback.sql"]` + the rule's one-line comment; `:60`–`:65` and the with-DB calls untouched |

### Marker proofs (each its own call)
`grep -c -F "<<<<<<< "` and `grep -c -F ">>>>>>> "` on each of the 11 conflicted paths → `0` (22 calls, 22 × `0`).

### Carry proofs
Rule (a), `grep -n -F "MIGRATIONS_DIR / \"00" src/cobalt/db_migrations/__init__.py`:
```
91:    MIGRATIONS_DIR / "0001_schemas.sql",
92:    MIGRATIONS_DIR / "0002_move_tables.sql",
93:    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.sql",
94:    MIGRATIONS_DIR / "0004_radar_pool.sql",
95:    MIGRATIONS_DIR / "0005_heartbeat_note_absent.sql",
96:    MIGRATIONS_DIR / "0006_radar_score.sql",
97:    MIGRATIONS_DIR / "0007_radar_cards.sql",
98:    MIGRATIONS_DIR / "0008_radar_value_movers.sql",
99:    MIGRATIONS_DIR / "0009_picks_missed.sql",
100:    MIGRATIONS_DIR / "0010_archive_progress.sql",
101:    MIGRATIONS_DIR / "0011_archive_incidents.sql",
102:    MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql",
103:    MIGRATIONS_DIR / "0014_radar_handicap.sql",
104:    MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql",
109:    MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql",
110:    MIGRATIONS_DIR / "0014_radar_handicap.rollback.sql",
111:    MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql",
112:    MIGRATIONS_DIR / "0011_archive_incidents.rollback.sql",
113:    MIGRATIONS_DIR / "0010_archive_progress.rollback.sql",
114:    MIGRATIONS_DIR / "0009_picks_missed.rollback.sql",
115:    MIGRATIONS_DIR / "0008_radar_value_movers.rollback.sql",
116:    MIGRATIONS_DIR / "0007_radar_cards.rollback.sql",
117:    MIGRATIONS_DIR / "0006_radar_score.rollback.sql",
118:    MIGRATIONS_DIR / "0005_heartbeat_note_absent.rollback.sql",
119:    MIGRATIONS_DIR / "0004_radar_pool.rollback.sql",
120:    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.rollback.sql",
121:    MIGRATIONS_DIR / "0002_move_tables.rollback.sql",
```
`NOT A GAP BY ACCIDENT` → `0` · `ARE NOT GAPS BY ACCIDENT` → `1` · `0016 reserved for stale-score` → `0` · `THE 0008/0009 GAP IS CLOSED` → `1`. ✔

Rule (c), `src/cobalt/radar/evaluate.py`: `intraday_stale = True` → `1` · `intraday_stale=intraday_stale` → `2` · `intraday_staleness(` → `2` · `prep = prep if prep is not None else prepare_member(` → `1` · `closed_i1 = prep.closed_i1` → `1` · `last_price = prep.last_price` → `1` · `run = prep.run` → `1` · `daily_ok = prep.daily_ok` → `1` · `frames = prep.frames(binds_side_by_frame(td))` → `1` · `class MemberPrep` → `1` · `def prepare_member` → `1` · `grep -n -F "EVALUATOR_VERSION = "` → `163:EVALUATOR_VERSION = "s2p2.3"`. All = expected. ✔
`grep -n -F "def evaluate_member"` → `966:def evaluate_member(`. The range `:966` through `frames = prep.frames` (Read), WHOLE:
```python
def evaluate_member(
    ld: LoadedDef,
    member: MemberInput,
    *,
    tunables: Mapping[str, TunableRow],
    defaults: TaxonomyDefaults,
    scan_interval: int,
    clock,
    prep: MemberPrep | None = None,
) -> MemberEvaluation:
    """`prep`: one member's shared def-independent work (R95); None builds
    it here through `prepare_member`. A prep of another membership or
    instant is refused."""
    td = ld.definition
    minutes = working_minutes(defaults)
    prep = prep if prep is not None else prepare_member(member, tunables=tunables, defaults=defaults, clock=clock)
    if (prep.membership_id, prep.as_of) != (member.membership_id, member.as_of):
        raise EvaluateError(
            f"a member prep for membership {prep.membership_id} at {prep.as_of.isoformat()} handed to "
            f"membership {member.membership_id} at {member.as_of.isoformat()}"
        )
    closed_i1 = prep.closed_i1
    consumed = prep.consumed
    last_bar = prep.last_bar
    last_price = prep.last_price
    if last_bar is None:
        intraday_stale = True
    else:
        intraday_stale = intraday_staleness(
            observed_at=last_bar.ts + timedelta(minutes=1), as_of=member.as_of, scan_interval=scan_interval
        ).stale
    base = dict(
        membership_id=member.membership_id, ticker=member.ticker, slug=ld.slug, md5=ld.md5,
        departed=member.departed, consumed_bars=consumed, last_price=last_price,
        last_bar_ts=last_bar.ts if last_bar else None, intraday_stale=intraday_stale,
    )
    inputs_sha = canonical_sha256({
        "def_md5": ld.md5, "bars": consumed, "as_of": member.as_of.isoformat(),
        "daily": [daily_row(b) for b in member.daily.before(member.trade_date)] if member.daily else None,
        "rvol": member.rvol.model_dump(mode="json") if member.rvol else None,
    })

    def result(evaluation: Evaluation, detail: RadarScoreDetail, **kw) -> MemberEvaluation:
        return MemberEvaluation(**base, evaluation=evaluation, detail=detail, inputs_sha256=inputs_sha, **kw)

    def both(ev: MemberEvaluation) -> MemberEvaluation:
        """A result that does not depend on the side: the same for both frames."""
        return publish_frames(long=ev, short=ev)

    ev = evaluability(td)
    if not ev.evaluable:
        return both(result(
            "not_evaluable", RadarScoreDetail(
                atoms=(), missing_atoms=seam_safe_missing_atoms(ev.missing_atoms), observations=(),
            ),
            direction=None, missing=ev.missing_atoms,
        ))
    refusals = convention_refusals(td, tunables)
    if refusals:
        return both(result(
            "not_evaluable", RadarScoreDetail(
                atoms=(), missing_atoms=seam_safe_missing_atoms(refusals), observations=(),
            ),
            direction=None, missing=refusals, note="a convention row names a rule the code does not implement",
        ))

    run = prep.run
    params = prep.params
    daily_ok = prep.daily_ok
    frames = prep.frames(binds_side_by_frame(td))
```
Note for the check: `minutes = working_minutes(defaults)` (common context, both sides) is now unread in `evaluate_member` — stale's side used it for `working_bars`, which the prep replaced. Not edited (rule (c): "You touch nothing else").

Rule (e) — the two first lines per file (quoted from the hunks; each grep uses the line's backtick-free leading or trailing substring, since the grep rule forbids a backtick in a pattern):
| file | HEAD first line | grep → | incoming first line | grep → |
|---|---|---|---|---|
| `db_migrations/__init__.md` | `` `0014_radar_handicap` (float handicap H1, 2026-09-24; the number settled `` | `(float handicap H1, 2026-09-24; the number settled` → `1` | `` ## 2026-09-24 — `0015_shadow_agreement_stale` (stale-score build, R40 by X30 (A)) `` | `(stale-score build, R40 by X30 (A))` → `1` |
| `radar/evaluate.md` | `` ## 2026-09-25 — one member prep per scan (`cto-2026-09-24.md` R95) `` | `## 2026-09-25 — one member prep per scan (` → `1` | `` ## 2026-09-24 — stale score S1 (STALE-SCORE v2 §2 C steps 1–7; `[F-08]` … `` | `## 2026-09-24 — stale score S1 (STALE-SCORE v2 §2 C steps 1–7; ` → `1` |
| `replay/formations.md` | `` **2026-09-25 — the replay deadline fix (`cto-2026-09-24.md` R95).** `` | `**2026-09-25 — the replay deadline fix (` → `1` | `**2026-09-24 — stale score S1.** SUPPORTED_EVALUATORS is now` | `**2026-09-24 — stale score S1.**` → `1` |
Markers: 0/0 in all three (above). DEVDOC STALE at M3: none found — stale's `db_migrations/__init__.md` numbering sentence ("`0014` belongs to handicap H1; `0016`/`0017`/`0018` belong to DRC D1, voice V1 and DRC K1") agrees with rule (a).

Rule (b) carry (greps quoted per file):
- `test_tenancy.py`: `515: "0015_…rollback.sql", # the stale-score build (R40, X30 (A))` · `516: "0014_…rollback.sql", # the float handicap H1` · `517: "0013_…rollback.sql", # the setups one build (R2-3 = B)`.
- `test_p4_migrations.py`: 0015 `:102`, `:114`, `:122` · 0014 `:103`, `:115`, `:123` · 0013 `:104`, `:116`, `:124`.
- `test_radar_migration.py`: 0015 `:35` · 0014 `:36` · 0013 `:37`.
- `test_radar_score_migration.py`: 0015 `:104` · 0014 `:105` · 0013 `:106`.
- `test_archiver_migrations.py`: 0015 `:87` (FORWARD), `:95`, `:120`, `:127` · 0014 `:86`, `:96`, `:121`, `:128` · 0013 `:85`, `:97`, `:122`, `:129`.
- `test_assumed_store.py`: 0015 `:249` `FORWARD[-1]`, `:250` `REVERSE[0]` · 0014 `:246` `FORWARD[-2]`, `:248` `REVERSE[1]` · 0013 `:242`/`:243` (`in`), `:245` `FORWARD[-3]`, `:247` `REVERSE[2]` (+ with-DB `:269`–`:283`, untouched).
- `test_stale_score_db.py`: 0015 `:159` `FORWARD[-1]`, `:160` `REVERSE[0]` (+ `:191` with-DB, untouched) · 0014: no hit · 0013 `:161` `FORWARD[-3]`, `:162` `REVERSE[2]`.
- `test_radar_handicap_store.py`: 0015 `:85` · 0014 `:35`/`:36` (constants), `:62`, `:64` (adjacency, untouched), `:85` · 0013 `:62`, `:65` (adjacency, untouched).

T-lines at M3:
- T-1: `selected[:7]` = 0015, 0014, 0013, 0011, 0010, 0009, 0008 — same objects as H1 ∪ stale (each side's 6 names + the other side's head), strength = exact.
- T-2: `_rollback_paths("0007")` = 0015, 0014, 0013, 0011, 0010, 0009, 0008; `above_0009` = 0015, 0014, 0013, 0011, 0010; `("0008")` = 0015, 0014, 0013, 0011, 0010, 0009 — same objects as H1 ∪ stale, strength = exact.
- T-3: `[:7]` = 0015, 0014, 0013, 0011, 0010, 0009, 0008; `[-4:]` tail unchanged — same objects as H1 ∪ stale, strength = exact.
- T-4: `newest_four` = 0015, 0014, 0013, 0011, 0010, 0009, 0008 at `[:7]` × 3 — same objects as H1 ∪ stale, strength = exact.
- T-5: `FORWARD[-7:]` = 0008, 0009, 0010, 0011, 0013, 0014, 0015; `REVERSE[:7]` its mirror; `("0009")` = 0015, 0014, 0013, 0011, 0010; `("0007")` = those + 0009, 0008; `numbers == [*range(1, 12), 13, 14, 15]`; `numbers[-5:-3] == [10, 11]` — same objects as H1 ∪ stale, strength = exact.
- T-6: `FORWARD[-3]` 0013, `[-2]` 0014, `[-1]` 0015; `REVERSE[2]` 0013, `[1]` 0014, `[0]` 0015 — same objects as H1 ∪ stale, strength = positional.
- T-7: `FORWARD[-1]`/`REVERSE[0]` 0015; `FORWARD[-3]`/`REVERSE[2]` 0013 — same objects as stale, strength = positional (exact equality).
- T-8: `_rollback_paths("0013")` = [0015, 0014] — same object (0014) as H1 plus the newer 0015 the bound now selects, strength = exact.

Comment edits by rule (b) at M3: `test_archiver_migrations.py` numbers comment — old (HEAD) `# bars/chunk-2-0920 and closes the gap when it lands (L68 seam).` / `# The float handicap H1 adds 0014 (L72 P-b).` and (stale) `# bars/chunk-2-0920 and closes the gap when it lands (L68 seam). The` / `# stale-score build adds 0015 (R40); 0014 is handicap H1's (same seam).` → new `# bars/chunk-2-0920 and closes the gap when it lands (L68 seam).` / `# The float handicap H1 adds 0014 (L72 P-b).` / `# The stale-score build adds 0015 (R40); 0014 is handicap H1's (same seam).`; f-string `"1…11 then 13, 14, got …"` / `"1…11 then 13, 15, got …"` → `"1…11 then 13, 14, 15, got {numbers}"`. `test_radar_handicap_store.py` T-8: comment ADDED (rule text). No other comment changed.

Auto-merged, not edited: `grep -c -F "s2p2.3" src/cobalt/replay/formations.py` → `2`; `grep -c -F "cut_at" tests/cobalt/test_replay_runner.py` → `13`.

- `git -C …/stacked-0925 add <path>` × 13 (the 11 conflicted + T-7 + T-8), each exit 0; `git -C …/stacked-0925 commit --no-edit` → `[deploy/stacked-0925 91c631ac] Merge branch 'cards/stale-score-0922' into deploy/stacked-0925`.
- `log --oneline -1` → `91c631ac Merge branch 'cards/stale-score-0922' into deploy/stacked-0925`; `status --short --branch` → `## deploy/stacked-0925` / `?? "docs/40 - DevDocs/reports/stack-seam-build-2026-09-25.md"` (12:31:23 EDT).
- **`<M3 sha>` = `91c631ac`**

## M4 voice
- `git -C …/stacked-0925 merge --no-edit voice/v1-0923` → exit 1, `Automatic merge failed; fix conflicts and then commit the result.` `CONFLICT (content): Merge conflict in` `docs/40 - DevDocs/cobalt/db_migrations/__init__.md`, `src/cobalt/db_migrations/__init__.py`, `tests/cobalt/test_archiver_migrations.py`, `tests/cobalt/test_p4_migrations.py`, `tests/cobalt/test_radar_migration.py`, `tests/cobalt/test_radar_score_migration.py`, `tests/cobalt/test_tenancy.py`; `Auto-merging tests/cobalt/test_radar_panel_cards.py` (clean — rule (d) not triggered).
- `diff --name-only --diff-filter=U` → the same 7 paths. ALL in M4's EXPECTED CONFLICTS. No unnamed path.

### Resolutions
| path | rule | resolution |
|---|---|---|
| `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` (hunk `:139`–`:187`) | (e) | HEAD side WHOLE (main's `0013` section — absent on voice's base — then H1's `0014` paragraph, then stale's `0015` section), then voice's `## 2026-09-23 — voice V1: 0017 …` section WHOLE; 3 markers removed |
| `src/cobalt/db_migrations/__init__.py` (3 hunks) | (a) | docstring: HEAD's `0013`/`0014`/`0015` entries kept, voice's `0017` pair entry appended verbatim; voice's `0012–0016 ARE NOT A GAP BY ACCIDENT` paragraph DROPPED (replaced by the rule's paragraph, already in HEAD from M3, unchanged); `FORWARD` … `0013, 0014, 0015, 0017`; `REVERSE` `0017, 0015, 0014, 0013, 0011…` — voice's `0017` lines KEPT beside `0013` (never "take theirs") |
| `tests/cobalt/test_tenancy.py` | (b) T-1 | `selected[:8]`, head `0017` (voice comment) `0015` `0014` `0013` |
| `tests/cobalt/test_p4_migrations.py` (3 hunks) | (b) T-2 | each list gains `0017` above `0015, 0014, 0013` |
| `tests/cobalt/test_radar_migration.py` | (b) T-3 | `[:8]`, head `0017, 0015, 0014, 0013`; `[-4:]` unchanged |
| `tests/cobalt/test_radar_score_migration.py` (4 hunks) | (b) T-4 | `newest_four` = 8 names; `[:7]`/`[:5]` → `[:8]` × 3; voice comment `(the list is now the newest five)` → `(the list is now the newest eight)` |
| `tests/cobalt/test_archiver_migrations.py` (6 hunks) | (b) T-5 | `FORWARD[-8:]` = 0008…0011, 0013, 0014, 0015, 0017; `REVERSE[:8]` mirror; `("0009")`/`("0007")` gain `0017`; `numbers == [*range(1, 12), 13, 14, 15, 17]`, `numbers[-6:-4] == [10, 11]`; voice survivor exclusion `:483`–`:484` (`name != "voice_turns"`) kept whole (auto-merged) |
| `tests/cobalt/test_assumed_store.py` (auto-merged, NAMED RE-POINT) | (b) T-6 | `FORWARD[-4]` 0013, `[-3]` 0014, `[-2]` 0015, `[-1]` 0017; `REVERSE[0]` 0017, `[1]` 0015, `[2]` 0014, `[3]` 0013; `in` asserts unchanged |
| `tests/cobalt/test_stale_score_db.py` (NAMED RE-POINT) | (b) T-7 | `0015` → `FORWARD[-2]`/`REVERSE[1]`; `0013` → `FORWARD[-4]`/`REVERSE[3]` |
| `tests/cobalt/test_radar_handicap_store.py` (NAMED RE-POINT) | (b) T-8 | `_rollback_paths("0013")` = `[0017, 0015, 0014]` rollbacks; comment kept |
| `tests/cobalt/test_voice_store.py` (NAMED RE-POINT) | (b) T-9 | `_rollback_paths("0011")` → `("0015")` at `:58` and `:186`; `:58`'s `== ["0017_voice_turns.rollback.sql"]` byte for byte |

### Marker proofs
`<<<<<<< ` / `>>>>>>> ` counts on the 7 conflicted paths → 14 × `0`.

### Carry proofs
Rule (a), `grep -n -F "MIGRATIONS_DIR / \"00" src/cobalt/db_migrations/__init__.py`:
```
95:    MIGRATIONS_DIR / "0001_schemas.sql",
96:    MIGRATIONS_DIR / "0002_move_tables.sql",
97:    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.sql",
98:    MIGRATIONS_DIR / "0004_radar_pool.sql",
99:    MIGRATIONS_DIR / "0005_heartbeat_note_absent.sql",
100:    MIGRATIONS_DIR / "0006_radar_score.sql",
101:    MIGRATIONS_DIR / "0007_radar_cards.sql",
102:    MIGRATIONS_DIR / "0008_radar_value_movers.sql",
103:    MIGRATIONS_DIR / "0009_picks_missed.sql",
104:    MIGRATIONS_DIR / "0010_archive_progress.sql",
105:    MIGRATIONS_DIR / "0011_archive_incidents.sql",
106:    MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql",
107:    MIGRATIONS_DIR / "0014_radar_handicap.sql",
108:    MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql",
109:    MIGRATIONS_DIR / "0017_voice_turns.sql",
114:    MIGRATIONS_DIR / "0017_voice_turns.rollback.sql",
115:    MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql",
116:    MIGRATIONS_DIR / "0014_radar_handicap.rollback.sql",
117:    MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql",
118:    MIGRATIONS_DIR / "0011_archive_incidents.rollback.sql",
119:    MIGRATIONS_DIR / "0010_archive_progress.rollback.sql",
120:    MIGRATIONS_DIR / "0009_picks_missed.rollback.sql",
121:    MIGRATIONS_DIR / "0008_radar_value_movers.rollback.sql",
122:    MIGRATIONS_DIR / "0007_radar_cards.rollback.sql",
123:    MIGRATIONS_DIR / "0006_radar_score.rollback.sql",
124:    MIGRATIONS_DIR / "0005_heartbeat_note_absent.rollback.sql",
125:    MIGRATIONS_DIR / "0004_radar_pool.rollback.sql",
126:    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.rollback.sql",
127:    MIGRATIONS_DIR / "0002_move_tables.rollback.sql",
```
`NOT A GAP BY ACCIDENT` → `0` · `ARE NOT GAPS BY ACCIDENT` → `1` · `0016 reserved for stale-score` → `0` · `THE 0008/0009 GAP IS CLOSED` → `1`. ✔

Rule (e), `db_migrations/__init__.md` at M4 — HEAD first line `` **2026-09-21 — `0013_tunables_slug_nullable` (setups one build STEP-2; `` → grep `(setups one build STEP-2;` → `1`; incoming first line `` ## 2026-09-23 — voice V1: 0017 `voice_turns` `` → grep `## 2026-09-23 — voice V1: 0017 ` → `1`. Markers 0/0.
**DEVDOC STALE: `docs/40 - DevDocs/cobalt/db_migrations/__init__.md:175` — "The number is the desk's L68 assignment: 0012–0016 belong to unmerged branches (bars chunk 2, the setups build, H1, DRC D1, the stale-score reserve), so the registry reads `…, 0011, 0017` until they land"** (`grep -n -F "0012–0016 belong to"` → `175:`). On the stack 0013/0014/0015 are merged, 0015 is stale-score's (not DRC D1's) and 0016 is DRC D1's; the registry reads `…, 0011, 0013, 0014, 0015, 0017`. Kept as written by rule (e).

Rule (b) carry (greps quoted per file, M4):
- `test_tenancy.py`: 0017 `:515` · 0015 `:516` · 0014 `:517` · 0013 `:518`.
- `test_p4_migrations.py`: 0017 `:102`, `:115`, `:124` · 0015 `:103`, `:116`, `:125` · 0014 `:104`, `:117`, `:126` · 0013 `:105`, `:118`, `:127`.
- `test_radar_migration.py`: 0017 `:35` · 0015 `:36` · 0014 `:37` · 0013 `:38`.
- `test_radar_score_migration.py`: 0017 `:104` · 0015 `:105` · 0014 `:106` · 0013 `:107`.
- `test_archiver_migrations.py`: 0017 `:88` (FORWARD), `:96`, `:122`, `:130` (from the survivor grep) · 0015 `:87`, `:97`, `:123`, `:131` · 0014 `:86`, `:98`, `:124`, `:132` · 0013 `:85`, `:99`, `:125`, `:133`.
- `test_assumed_store.py`: 0017 `:251` `FORWARD[-1]`, `:252` `REVERSE[0]` · 0015 `:249` `FORWARD[-2]`, `:250` `REVERSE[1]` · 0014 `:246` `FORWARD[-3]`, `:248` `REVERSE[2]` · 0013 `:242`/`:243` (`in`), `:245` `FORWARD[-4]`, `:247` `REVERSE[3]` (+ with-DB `:271`–`:285`).
- `test_stale_score_db.py`: 0017 none · 0015 `:159` `FORWARD[-2]`, `:160` `REVERSE[1]` (+ `:191` with-DB) · 0014 none · 0013 `:161` `FORWARD[-4]`, `:162` `REVERSE[3]`.
- `test_radar_handicap_store.py`: 0017 `:85` · 0015 `:85` · 0014 `:35`/`:36` (constants), `:62`, `:64` (adjacency, untouched), `:86` · 0013 `:62`, `:65` (adjacency).
- `test_voice_store.py` `_rollback_paths(`: `58: assert [p.name for p in _rollback_paths("0015")] == ["0017_voice_turns.rollback.sql"]` · `186: _apply(conn, _rollback_paths("0015"))`.

T-lines (final, `<set>` FOUR):
- T-1: `selected[:8]` = 0017, 0015, 0014, 0013, 0011, 0010, 0009, 0008; `[-3:]`, `names[-1]`, range asserts unchanged — same objects as main ∪ H1 ∪ stale ∪ voice, strength = exact.
- T-2: `("0007")` = 0017, 0015, 0014, 0013, 0011, 0010, 0009, 0008; `above_0009` = 0017, 0015, 0014, 0013, 0011, 0010; `("0008")` = 0017, 0015, 0014, 0013, 0011, 0010, 0009 — same objects as all four sides, strength = exact.
- T-3: `[:8]` = 0017, 0015, 0014, 0013, 0011, 0010, 0009, 0008; `[-4:]` unchanged — same objects as all sides, strength = exact.
- T-4: `newest_four` = 0017, 0015, 0014, 0013, 0011, 0010, 0009, 0008 at `[:8]` × 3 (name kept) — same objects as all sides, strength = exact.
- T-5: `FORWARD[-8:]` = 0008, 0009, 0010, 0011, 0013, 0014, 0015, 0017; `REVERSE[:8]` = 0017, 0015, 0014, 0013, 0011, 0010, 0009, 0008; `("0009")` = 0017, 0015, 0014, 0013, 0011, 0010; `("0007")` = those + 0009, 0008; `numbers == [*range(1, 12), 13, 14, 15, 17]`; `numbers[-6:-4] == [10, 11]`; survivor exclusion kept — same objects as all sides, strength = exact.
- T-6: `FORWARD[-4..-1]` = 0013, 0014, 0015, 0017; `REVERSE[0..3]` = 0017, 0015, 0014, 0013 — same objects as main ∪ H1 ∪ stale (+ voice's head), strength = positional.
- T-7: 0015 at `FORWARD[-2]`/`REVERSE[1]`, 0013 at `FORWARD[-4]`/`REVERSE[3]` — same objects as stale, strength = positional (exact equality).
- T-8: `_rollback_paths("0013")` = 0017, 0015, 0014 rollbacks — H1's object (0014) plus every newer rollback the bound selects, strength = exact.
- T-9: `_rollback_paths("0015")` = [0017] at `:58`; `:186` reverses exactly 0017 — same object as voice, strength = exact.

Comment edits by rule (b) at M4 (old → new):
- `test_radar_score_migration.py:104` `# voice V1 (the list is now the newest five)` → `# voice V1 (the list is now the newest eight)`.
- `test_archiver_migrations.py:88` `# voice V1; 0012–0016 are unmerged branches' (L68)` → `# voice V1; 0012 and 0016 are unmerged branches' (L68)`.
- `test_archiver_migrations.py` numbers comment: voice's `# Voice V1 adds 0017; 0012–0016 belong to unmerged branches and close` / `# the gap as they land (L68 seam).` → `# Voice V1 adds 0017; 0012 and 0016 belong to unmerged branches and close` / `# the gap as they land (L68 seam).`, appended under HEAD's four comment lines (kept); f-string → `"1…11 then 13, 14, 15, 17, got {numbers}"`.
- `test_assumed_store.py:249` `# the stale-score build (R40) now tops it` → `# the stale-score build (R40)` (the "now tops it" clause is false once 0017 is `[-1]`; clause dropped per rule (b)'s comment clause — a READING, listed for the check).

- `add` × 11 (7 conflicted + T-6, T-7, T-8, T-9), each exit 0; `commit --no-edit` → `[deploy/stacked-0925 00e2b7ff] Merge branch 'voice/v1-0923' into deploy/stacked-0925`.
- `log --oneline -1` → `00e2b7ff Merge branch 'voice/v1-0923' into deploy/stacked-0925`; `status --short --branch` → `## deploy/stacked-0925` / `?? "docs/40 - DevDocs/reports/stack-seam-build-2026-09-25.md"` (12:34:57 EDT).
- **`<M4 sha>` = `00e2b7ff`**

## R THE REGISTRY
Loader proofs at the merged tree (each its own `grep -n -F`, hit quoted):
| grep | hit |
|---|---|
| `CONFIG_PATH = ` voice/config.py | `32:CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "voice.yaml"` |
| `def load_voice_config` voice/config.py | `120:def load_voice_config(path: Path = CONFIG_PATH, *, backup_sources: Optional[list[Path]] = None) -> VoiceConfig:` |
| `_CONFIG = load_voice_config()` voice/web.py | `59:        _CONFIG = load_voice_config()` |
| `CONFIG_PATH = ` voice/registry.py | `23:CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "agents" / "voice.yaml"` |
| `def load_agent` voice/registry.py | `85:def load_agent(path: Path = CONFIG_PATH) -> AgentSpec:` |
| `CONFIG_PATH = ` modelaccess/config.py | `28:CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "modelaccess.yaml"` |
| `def load_routes` modelaccess/config.py | `106:def load_routes(path: Path = CONFIG_PATH) -> ModelAccessConfig:` |
| `load_routes().routes[load_agent().route]` voice/web.py | `176:        plan_timeout = load_routes().routes[load_agent().route].timeout_s` |
| `include_router(voice_web.router)` aset/web.py | `90:app.include_router(voice_web.router)` |
| `exec uv run python -m cobalt.aset` ops/start_aset.sh | `73:exec uv run python -m cobalt.aset` |
| `COBALT_VOICE_` ops/start_aset.sh | `35:export COBALT_VOICE_SCRATCH_DIR="/Users/cobalt/.cobalt/voice-scratch"` · `37:export COBALT_VOICE_MODEL_DIR="/Users/cobalt/.cobalt/voice-models"` |
| `start_aset.sh` ops/com.cobalt.aset.plist | `25:        <string>/Users/cobalt/cobalt/ops/start_aset.sh</string>` |
| `<string>run</string>` ops/com.cobalt.radar.plist | `19:` and `22:` (Read `:17`–`:23`: `uv` `run` `cobalt` `radar` `run`) |
| `nohup uv run` cobalt.sh | `59:        nohup uv run src/cobalt_agent/main.py > logs/mattermost_session.log 2>&1 &` |
All match the drafter's reads. Pre-check: none of the six paths sits in `no_resident_reads` (greps of `pyproject.toml`, `modelaccess.yaml`, `start_aset.sh`, `voice.yaml` in `jobs.yaml` hit only the new lines and one prose comment `:42`).

THE LINES: `jobs.yaml` `com.cobalt.aset` `reads:` += `configs/cobalt/voice.yaml`, `configs/cobalt/agents/voice.yaml`, `configs/cobalt/modelaccess.yaml`, `ops/start_aset.sh`, `pyproject.toml`, `uv.lock`; `com.cobalt.radar` `reads:` += `pyproject.toml`, `uv.lock`. `com.cobalt.agent`: NOT given a line (its `reads: []` is deliberate, `jobs.yaml` "the read-once class", pinned by `test_jobs_reads.py`). No `no_resident_reads` entry added.

THE PIN FLIPPED: `tests/cobalt/test_jobs_restarts.py` `test_a_resident_wrapper_script_is_not_an_operator_script` — old: `assert row.escalate is True` / `assert row.restarts  # the conservative set, until someone rules on it` → new: `# Classified 2026-09-25 (stack seam build): com.cobalt.aset reads it (jobs.yaml) — the ruling this pin waited for.` / `assert row.escalate is False` / `assert row.rule == "resident reads"` / `assert "com.cobalt.aset" in row.restarts` (the rule string proven at `src/cobalt/jobs/restarts.py:204`, read-only).

THE COMMIT: `add configs/cobalt/jobs.yaml` · `add tests/cobalt/test_jobs_restarts.py` · `commit -m "chore(jobs): classify voice V1's six paths — …" -m "Co-Authored-By: …" -- …` → `[deploy/stacked-0925 a7296b44] … 2 files changed, 14 insertions(+), 2 deletions(-)`. `show --stat HEAD` → `configs/cobalt/jobs.yaml | 10 ++++++++++` · `tests/cobalt/test_jobs_restarts.py |  6 ++++--` — EXACTLY those two ✔. `diff HEAD~1 HEAD -- configs/cobalt/jobs.yaml` WHOLE:
```diff
@@ -73,6 +73,14 @@ jobs:
       # (com.cobalt.backup, ops/run_backup.sh:39; status/restore are operator commands) and by heartbeat/probes.py:431
       # (backup_freshness, from runner.py:144 — com.cobalt.heartbeat). One-shots derive nothing. Added there 2026-09-22.
       - "configs/cobalt/backup.yaml"
+      # voice V1's six paths, classified at the stack seam build 2026-09-25 (L42). The sheet serves voice
+      # (aset/web.py:90 include_router(voice_web.router)), so this process runs voice's loaders.
+      - "configs/cobalt/voice.yaml"                # voice/config.py:32 CONFIG_PATH + :120 (load_voice_config); cached per process in voice/web.py:59 _CONFIG, so a change reaches the sheet only by restart
+      - "configs/cobalt/agents/voice.yaml"         # voice/registry.py:23 CONFIG_PATH + :85 (load_agent), called from voice/web.py:176
+      - "configs/cobalt/modelaccess.yaml"          # modelaccess/config.py:28 CONFIG_PATH + :106 (load_routes), called from voice/web.py:176
+      - "ops/start_aset.sh"                        # ops/com.cobalt.aset.plist:25 (the program); its exports (start_aset.sh:35, :37 COBALT_VOICE_*) reach the process only at a restart
+      - "pyproject.toml"                           # ops/start_aset.sh:73 (exec uv run python -m cobalt.aset): uv syncs the environment from it when the process starts
+      - "uv.lock"                                  # ops/start_aset.sh:73 (exec uv run python -m cobalt.aset): uv syncs the environment from it when the process starts
     imports: [cobalt.aset.__main__, cobalt.aset.web]
     what: "the ASET semi-auto sheet on :5010 — the surface he trades beside"
 
@@ -173,6 +181,8 @@ jobs:
     reads:
       - "configs/cobalt/radar.yaml"                # radar/config.py:67 (load_config)
       - "configs/cobalt/taxonomy/tunables.yaml"    # taxonomy/loader.py:79 (load_tunables)
+      - "pyproject.toml"                           # ops/com.cobalt.radar.plist:18–22 (uv run cobalt radar run): uv syncs the environment from it when the process starts
+      - "uv.lock"                                  # ops/com.cobalt.radar.plist:18–22 (uv run cobalt radar run): uv syncs the environment from it when the process starts
     imports: [cobalt.cli]
     what: "the resident radar pool scanner and Finviz i1 bar poller"
```
Only `reads:` entries and their comments ✔.
- **`<R sha>` = `a7296b44`** · **`<tip>` = `a7296b44`** (`rev-parse --short=8 HEAD`).

## O OFFLINE
- `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` → `ls: /Users/cobalt/cobalt-wt/stacked-0925/.env: No such file or directory` ✔.
- `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` (background, on `a7296b44`) → exit 0. Sync lines: `Creating virtual environment at: .venv` · `Installed 253 packages in 853ms`.
- **`<p>`**, the summary WHOLE: `3198 passed, 383 skipped, 1 xfailed, 20 warnings in 567.13s (0:09:27)` → **0 failed, 0 errors** ✔ (done 12:46 EDT).
- Evaluate seam proof (rule (c)): `grep -n -F "def test_a_shared_member_prep_gives_every_def_byte_identical_evaluations" tests/cobalt/test_radar_evaluate.py` → `798:` · `grep -n -F "def test_a_prep_builds_each_frame_pair_once_whatever_the_def_count" …` → `827:` · `ls tests/cobalt/test_stale_score.py` → listed. T1 / T2 / stale T(i): collected and passed in the offline summary above (0 failed).
- COUNT: offline 3198 vs context (replay 2512, H1 fix r2 2624, stale 2518, V1 fix r2 2786) — the stack is the union of four branches' tests, so higher than any one; not a stop.

## W WITH-DB
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (lock FREE, 12:46 EDT). `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0925/.env` → exit 0, no output (by name, never read). `ls -la /Users/cobalt/cobalt-wt/*/.env` → EXACTLY one line: `-rw-------  1 cobalt  staff  2186 Sep 25 12:46 /Users/cobalt/cobalt-wt/stacked-0925/.env` ✔. **L76 lock taken 12:46 EDT.**
- (b) `ls -la …/stacked-0925/.env` (LISTED) → `<FP>` → **`<F0>` = cols `664` · rels `35` · views_md5 `272c95bbb12241e3611e4b36326ccf87`**. `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)`; 29 tables probed, no `CHANGED` line; `voice_turns user - - -` (absent, as at `0013`); `radar_membership … 3 card column(s) added by 0007`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: a7296b44 (DIRTY: 1 path(s))` (the untracked report). `cobalt_dev` at `0013` ✔.
- (c1) PASS 1 at `0013`: `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect …` (the nine ids, byte for byte; background) → **exit 1**. **`<d1>` summary WHOLE: `1 failed, 3565 passed, 6 skipped, 9 deselected, 1 xfailed, 20 warnings in 644.02s (0:10:44)`** — GATE RED.
  - THE RED: `tests/cobalt/test_radar_score_migration.py::test_migrate_twice_is_idempotent_on_cobalt_dev`, at `tests/cobalt/test_radar_score_migration.py:304` `_apply(conn, FORWARD)` → `src/cobalt/db_migrations/cli.py:486` `conn.execute(path.read_text())` while applying `0006_radar_score.sql` (captured stdout: `-- applying 0001_schemas.sql` … `-- applying 0006_radar_score.sql`), verbatim:
    ```
    E           psycopg.errors.DeadlockDetected: deadlock detected
    E           DETAIL:  Process 994327 waits for AccessExclusiveLock on relation 389792 of database 165601; blocked by process 994307.
    E           Process 994307 waits for ShareLock on transaction 2617234; blocked by process 994327.
    E           HINT:  See server log for query details.
    ```
  - `DeadlockDetected` is a red under W (c1) ("the lock was not yours alone — name it, never re-run it here"): NOT re-run. The blocking backend (pid 994307) is NOT identified by this run: the `.env` glob showed ONLY this worktree's copy at (a), but whether 994307 was another session on `cobalt_dev` or a connection left open by an earlier test in this same pytest process is not visible to anything this run read (L35: not claimed either way; L70: cause UNPROVEN).
  - SKIPPED lines (all 6, verbatim): `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.
- (c2) forward migrate: **NOT RUN** — nothing was applied to `cobalt_dev` by this run (no `dev forward: APPLIED` line exists). (d) pass 2, (d2) validate, (e) live-note: NOT RUN (UNPROVEN, L70).
- (f) — failure BEFORE (c2) → step 3 only: `rm /Users/cobalt/cobalt-wt/stacked-0925/.env` → exit 0; `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` → `ls: /Users/cobalt/cobalt-wt/stacked-0925/.env: No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`. **`.env: removed, proven gone (L76 lock released 12:58 EDT)`**. `cobalt_dev`: this run applied nothing (proof-only was READ ONLY; the suite's own migration tests run inside their rolled-back transactions); no `<F2>` read — (f) steps 1–2 do not run before (c2).

## RESTARTS
not run — the run stopped at W (c1).

## FOR THE DEPLOY
- `<main-at-cut>` `2b71fe49` · `<set>` FOUR · merges `<M1 sha>` `f2377218` (replay) → `<M2 sha>` `35397ed5` (H1) → `<M3 sha>` `91c631ac` (stale) → `<M4 sha>` `00e2b7ff` (voice) · `<R sha>` = `<tip>` `a7296b44` · plus ONE wip commit of this report above it (RECOVERY, L60).
- Seam paths (changed beyond auto-merge): `src/cobalt/db_migrations/__init__.py` (a) · `tests/cobalt/test_tenancy.py`, `test_p4_migrations.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_archiver_migrations.py`, `test_assumed_store.py` (b, T-1…T-6) · `tests/cobalt/test_stale_score_db.py` (T-7) · `tests/cobalt/test_radar_handicap_store.py` (T-8) · `tests/cobalt/test_voice_store.py` (T-9) · `src/cobalt/radar/evaluate.py` (c) · `configs/cobalt/jobs.yaml` + `tests/cobalt/test_jobs_restarts.py` (R) · DevDocs (e): `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` (M3 + M4), `docs/40 - DevDocs/cobalt/radar/evaluate.md` (M3), `docs/40 - DevDocs/cobalt/replay/formations.md` (M3). `tests/cobalt/test_radar_panel_cards.py`: auto-merged clean, rule (d) not used. Auto-merged, shared by replay and stale, not edited: `src/cobalt/replay/formations.py`, `tests/cobalt/test_replay_runner.py`, `tests/cobalt/test_setups_d1.py`.
- **DEVDOC STALE: `docs/40 - DevDocs/cobalt/db_migrations/__init__.md:175` — "The number is the desk's L68 assignment: 0012–0016 belong to unmerged branches (bars chunk 2, the setups build, H1, DRC D1, the stale-score reserve), so the registry reads `…, 0011, 0017` until they land"** (the desk's DevDoc refresh item).
- THE REGISTRY LINES (R): `com.cobalt.aset` reads += `configs/cobalt/voice.yaml`, `configs/cobalt/agents/voice.yaml`, `configs/cobalt/modelaccess.yaml`, `ops/start_aset.sh`, `pyproject.toml`, `uv.lock`; `com.cobalt.radar` reads += `pyproject.toml`, `uv.lock`. **com.cobalt.agent runs uv run from ~/cobalt (cobalt.sh:59); it is NOT in the registry lines for pyproject.toml / uv.lock (jobs.yaml agent reads: [] + test_jobs_reads.py:84) — the check's Q4; the desk's item if it holds.**
- FOR `32` G1: not read this run (the build stopped before CLOSE); the `diff --stat <main-at-cut> <tip> -- . ':(exclude)docs'` and `log --merges` reads are owed by the relaunch.
- The with-DB leg was designed as TWO passes (W (c1) / (d)); pass 1 is red on a `DeadlockDetected` (above); pass 2 not run. `32` STEP-G3 (d)'s one-pass shape still carries `stack-seam-draft-2026-09-25.md` ESCALATE 1.
- Rollback (L54): `32` ships this branch as the gate branch; its rollback is `32`'s ONE `git revert -m 2`. The branch is NOT gate-ready: W is red/unproven.

## FOR THE CHECK
- M1 `f2377218`: no conflicts, no edits. M2 `35397ed5`: no conflicts, no edits.
- M3 `91c631ac`: 11 conflicted paths + 2 named re-points, each rule under `## M3 stale` (table); rule (e)'s three DevDocs with their quoted first lines there; DEVDOC STALE at M3: none.
- M4 `00e2b7ff`: 7 conflicted paths + 4 named re-points (`## M4 voice` table); rule (e) first lines there; DEVDOC STALE `db_migrations/__init__.md:175` (above).
- rule (b) T-1…T-9 lines as written under `## M4 voice` (final) and `## M3 stale` (intermediate); comment edits (old → new) listed in both sections. Two are READINGS for the check: `test_assumed_store.py:249` dropped "now tops it" (a position clause, not a count — rule (b) names count/range clauses); `test_archiver_migrations.py` voice's numbers comment rewritten `0012–0016` → `0012 and 0016` (the range the combined list contradicts).
- rule (c)'s `evaluate_member` range quoted under `## M3 stale`, all carry counts = expected; note: `minutes = working_minutes(defaults)` is now unused inside `evaluate_member` (context line, not edited).
- DevDoc reading: `docs/40 - DevDocs/cobalt/radar/evaluate.md` replay's "`EVALUATOR_VERSION` is unchanged" is true of replay's change alone; on the stack the constant is `s2p2.3` (stale's bump). Not listed as DEVDOC STALE (the sentence describes that change); the check decides.
- R: loader greps and the WHOLE jobs.yaml diff under `## R THE REGISTRY`; `test_jobs_restarts.py` re-point old → new there.
- `git show --stat <M<n> sha>` per merge: NOT read this run (owed by the relaunch's CLOSE).
- W (c1) red: `test_migrate_twice_is_idempotent_on_cobalt_dev` `DeadlockDetected` — verbatim under `## W WITH-DB`.

## CONTINUE
next: W — RELAUNCH `CONTINUE: W` after the desk rules on the pass-1 `DeadlockDetected` (who held pid 994307 on `cobalt_dev` at ≈12:47–12:58). Branch state: M1–M4 and R committed (`<tip>` `a7296b44`), plus this report's wip commit; O is GREEN on `a7296b44` (`<p>` above, reusable — the tree is unchanged); `.env` removed, lock free, nothing applied to `cobalt_dev`. The relaunch re-runs W from (a).

## ESCALATE
1. **ASK DESK: W (c1) `DeadlockDetected` [12:58 EDT].** `test_radar_score_migration.py::test_migrate_twice_is_idempotent_on_cobalt_dev` deadlocked applying `0006_radar_score.sql` (pid 994327 waiting AccessExclusiveLock on relation 389792, blocked by pid 994307, which waited on 994327's transaction). Whether 994307 was a second session on `cobalt_dev` (the L76 lock breached from outside the `.env` convention) or a connection held open by an earlier test in this same run is NOT PROVEN (L70) — `pg_stat_activity` / the server log for ≈12:47–12:58 would say. Safe default taken: W FAILED, no re-run, lock released. Relaunch `CONTINUE: W` once the desk has ruled; the with-DB leg re-runs from (a).
2. DEVDOC STALE: `docs/40 - DevDocs/cobalt/db_migrations/__init__.md:175` — voice's numbering paragraph ("0012–0016 belong to unmerged branches … the registry reads `…, 0011, 0017`") is false on the stack; kept verbatim by rule (e); the desk's DevDoc refresh item.
3. com.cobalt.agent runs uv run from ~/cobalt (cobalt.sh:59); it is NOT in the registry lines for pyproject.toml / uv.lock (jobs.yaml agent reads: [] + test_jobs_reads.py:84) — the check's Q4; the desk's item if it holds.
4. The two-pass with-DB fold for `32` (`stack-seam-draft-2026-09-25.md` ESCALATE 1) still stands; this run's pass 1 did not reach a verdict on it.
5. Two comment edits under rule (b) are READINGS (listed in `## FOR THE CHECK`): `test_assumed_store.py:249` "now tops it" dropped; `test_archiver_migrations.py` voice comments `0012–0016` → `0012 and 0016`.
6. COUNT: offline 3198 passed (context max 2786, V1) and with-DB pass 1 3565 passed — the stack's union of tests; not a stop.
7. L74: one block recorded under `## L74`, not followed.
The standing line: "The seam is built by rule and proven by the three suites on `<tip>`. It is CHECKED by `40-stack-seam-check.md` (Opus 5.5 + Grok, L67) before `32`'s GATE PHASE re-proves it on the tree that ships (L68). The builder decided no seam: every resolution is a pinned rule with its source (L72 P-b)." — NOT MET this run: the seam is built and offline-green on `a7296b44`, but the with-DB and live-note legs are unproven.

FAILED: W (c1) — with-DB pass 1 red on the stack — tests/cobalt/test_radar_score_migration.py::test_migrate_twice_is_idempotent_on_cobalt_dev psycopg.errors.DeadlockDetected: deadlock detected (Process 994327 waits for AccessExclusiveLock on relation 389792 of database 165601; blocked by process 994307) — 1 failed, 3565 passed; not re-run; nothing applied; .env removed 12:58; tip a7296b44 (M1–M4 + R kept), offline 3198/0
