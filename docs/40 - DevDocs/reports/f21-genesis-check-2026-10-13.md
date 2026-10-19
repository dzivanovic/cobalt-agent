# f21-genesis-1013 — CHECK (pass 1) · 2026-10-19

## §0 Headline
Check of `f21-genesis-1013`, done 08:41 EDT. Tip `66439da6` → `a19a638a`. House A was grok (1 finding); no house B was needed.
Held 3, fixed 3. O1 = A1: `GenesisStore.replace` ran on `db.connect`'s autocommit connection, so its DELETE committed by itself and a failed insert could leave a partial source. O2: `splitlines()` threw the line ranges off at a form feed or U+2028.
Suites green on `a19a638a`: offline 8686/0, with-DB 5634/0, live-note 147/0; `cobalt_dev: 0013 — F2 = F0`; `.env` removed. RESTARTS: `com.cobalt.radar`.
One decision, not for Dejan: the REVERSE pins of `test_stale_score_db.py` are not tested offline (X3).

## L74
(none yet)

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card 820>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/820-f21-genesis-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/820-f21-genesis-check-card.md" · 0 · daaf70cff1e56f6a17df5e85df6bd9838fd9242b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/820-f21-genesis-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " ".../cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... APPROVES `STANDING-LIST.md` once (`4be06af0`) ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " ".../cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: ... approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. ... | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · ... · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
(two long row texts shortened with `...` in this quote; the tool output is whole in the session.)
House gates: `grep -n "^| R17 "` → `35:| R17 | 07:32 ET | His words: ... STANDING: Bash(grok *) is a PRE-APPROVED string ...` (one row) · `grep -n "^| R19 "` → `37:| R19 | 07:36 ET | ... the four house strings are pre-approved on every hub the desk launches, indefinitely ...` (one row) · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- ...cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`date` → `Mon Oct 19 07:33:53 EDT 2026`.
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card 820>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct 19 07:33:58 EDT 2026
status · git status --short --branch · 0 · ## ops/f21-genesis-1013
head · git log --oneline -1; git log --stat --format=%h 66439da6..HEAD · 0 · (6 lines)
    817a07c3 docs(f21-genesis-1013): build report — 66439da6
    817a07c3
    
     .../reports/f21-genesis-build-2026-10-13.md        | 232 +++++++++++++++++++++
     .../reports/f21-genesis-build-2026-10-13.result    |  15 ++
     2 files changed, 247 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/f21-genesis-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/deploy-gemini-grant/.env
report · tail -n 3 ".../f21-genesis-build-2026-10-13.md" · 0 · BUILT · job: f21-genesis-1013 · tip: 66439da6 | on 40e646ed | migration: 0026, rolled back | offline 8683/0 | with-DB 5631/0 | live-note 147/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 317412
range · git log --oneline 40e646ed..66439da6 · 0 · (2 lines)
    66439da6 feat(f21-genesis-1013): F21 chunk 1 — "user".genesis_chunk (0026), the structural importer, loud import failures, the one search entry, cobalt genesis import|search (G1-G6; L1, L3, L32, L42, L76)
    9f742f73 wip(f21-genesis-1013): red — genesis offline, with-DB and RUN tests, synthetic fixtures (G1-G6)
PREFLIGHT OK
```
Another worktree (`deploy-gemini-grant`) holds `.env` (the lock): waited for at W, not a failure (L76).
THE RANGE typed: `git log --stat --format=%h 40e646ed..66439da6` → 2 commits; `9f742f73` (5 paths: two fixtures, three genesis test files), `66439da6` (37 paths: 8 DevDocs pages, `ops/desk/gate-lists.md`, `src/cobalt/cli.py`, 4 `db_migrations` files, 5 `genesis` modules, 18 moved pin test files). Path union = 42 paths (recorded for `## Scope`).
`ls <S>` → `No such file or directory` (fresh).
House probes (`house-probe.sh --card`, background) → `grok: UP` · `gemini: UP`.
Seats: no `HOUSE A: OpenAI` header line → house A = grok. `HOUSE B: as needed` (not `mandatory`) → **house A: grok · house B: none (not needed)**.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card 820>" "<S>"` → last line `STAGED 47 files · 568397 bytes · commits 2` (commits 2 = PREFLIGHT's range count). Per-file lines (bytes · dest under `<S>`): `STAGED-CARD` 30 · `diff.md` 92844 · `files/820-f21-genesis-check-card.md` 23943 · `files/f21-genesis-build-2026-10-13.md` 33051 · `files/wt/docs/40 - DevDocs/cobalt/`: `cli.md` 7018, `db_migrations/__init__.md` 20689, `db_migrations/placement.md` 4778, `genesis/__init__.md` 458, `genesis/chunk.md` 841, `genesis/cli.md` 505, `genesis/search.md` 590, `genesis/store.md` 643 · `files/wt/ops/desk/gate-lists.md` 7752 · `files/wt/src/cobalt/`: `cli.py` 26057, `db_migrations/0026_genesis_chunk.rollback.sql` 329, `db_migrations/0026_genesis_chunk.sql` 1654, `db_migrations/__init__.py` 12587, `db_migrations/placement.py` 8797, `genesis/__init__.py` 552, `genesis/chunk.py` 4940, `genesis/cli.py` 1528, `genesis/search.py` 1878, `genesis/store.py` 2448 · `files/wt/tests/cobalt/`: `fixtures/genesis/ledger-200.md` 15155, `fixtures/genesis/structure.md` 283, `test_archiver_migrations.py` 28503, `test_assumed_store.py` 15396, `test_dml_roles_offline.py` 2347, `test_drc_d2_fix_r1_db.py` 29038, `test_drc_d3_experiments.py` 4993, `test_drc_k1_store.py` 29108, `test_drc_store.py` 25796, `test_f15_p1_records_offline.py` 7126, `test_genesis_db.py` 6861, `test_genesis_experiments_db.py` 1806, `test_genesis_offline.py` 8337, `test_legs_migration.py` 4506, `test_p4_migrations.py` 28888, `test_radar_handicap_store.py` 11538, `test_radar_migration.py` 5223, `test_radar_price_floor_db.py` 6961, `test_radar_score_migration.py` 24142, `test_seam_drc_s3_registry.py` 2119, `test_stale_score_db.py` 11718, `test_tenancy.py` 31347, `test_voice_store.py` 12920 · `rulings.md` 374.
`stage-copy.sh` (files `## READ` names that the script cannot derive), each `COPIED <bytes> <dest>`: `files/468-f21-card.md` 14209 · `files/wt/docs/30 - Design/F21-ADR-FINAL-2026-10-11.md` 30048 · `files/wt/src/cobalt/db_migrations/0024_strike_alerts.sql` 1795 · `files/wt/src/cobalt/db_migrations/0025_dml_roles.sql` 4257 · `files/wt/src/cobalt/aset/strike.py` 27857 · `files/wt/tests/cobalt/test_dml_roles_db.py` 6830.
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim + card `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole + the Files paragraph). `ls -la <S>` at 07:36 → `diff.md`, `files/`, `HOUSE-INSTRUCTIONS.md` (24586), `rulings.md`, `STAGED-CARD`.
House A grok started 07:36 EDT (`date` 07:36:10), background, timeout 2700000. No house B (not needed).

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: G2 (and X3: a partial source)
CLAIM: `GenesisStore.replace` (`src/cobalt/genesis/store.py:41-48`) runs its DELETE and its INSERTs on the connection `db.connect` returns, which is opened `autocommit=True` (`src/cobalt/db.py:199`), and never sets `conn.autocommit = False` (the house shape for a multi-statement write: `src/cobalt/aset/store.py:119`, `src/cobalt/vaultwrite/store.py:194`, `src/cobalt/db_apply.py:245`) nor opens `conn.transaction()`; so the DELETE commits on its own and `conn.commit()` at `:48` is a no-op: an INSERT that fails leaves that source with no rows or half its rows — not ONE transaction (card 468 G2, DECISION D4). The suite's savepoint proxy (`tests/cobalt/conftest.py:210-247`) hides it: every with-DB test runs inside one outer transaction.
RUN: TEST — `tests/cobalt/test_genesis_offline.py`:
```python
def test_check_o1_replace_is_one_transaction_on_an_autocommit_connection():
    """db.connect() opens autocommit=True (db.py:199): a write the store does
    not wrap commits statement by statement. A failed INSERT must leave the
    source's old rows, so the DELETE may not have committed on its own."""
    from contextlib import contextmanager

    from cobalt.genesis.chunk import read_source
    from cobalt.genesis.store import GenesisStore

    class _Cursor:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def executemany(self, query, rows):
            raise RuntimeError("the connection dropped mid-insert")

    class _AutocommitConnection:
        """psycopg's semantics, reduced: in autocommit a statement outside a
        transaction block commits as it runs."""

        def __init__(self):
            self.autocommit = True
            self.committed: list[str] = []
            self._pending: list[str] = []
            self._depth = 0

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            self.rollback() if exc_type is not None else self.commit()
            return False

        def execute(self, query, params=None):
            stmt = query.split()[0]
            if self.autocommit and not self._depth:
                self.committed.append(stmt)
            else:
                self._pending.append(stmt)
            return self

        def cursor(self):
            return _Cursor()

        def commit(self):
            self.committed += self._pending
            self._pending = []

        def rollback(self):
            self._pending = []

        @contextmanager
        def transaction(self):
            self._depth += 1
            try:
                yield
            except BaseException:
                self._pending = []
                raise
            finally:
                self._depth -= 1
            if self.autocommit and not self._depth:
                self.commit()

    conn = _AutocommitConnection()
    store = GenesisStore("cobalt_dev")
    store._connect = lambda: conn
    with pytest.raises(RuntimeError):
        store.replace(read_source(str(FIXTURES / "structure.md")))
    assert conn.committed == [], "the DELETE committed alone: the source lost its rows and gained none"
```
EXPECT: on the tip `AssertionError: the DELETE committed alone ...` with `assert ['DELETE'] == []`.

FINDING O2
ROW: G2
CLAIM: `chunk_markdown` numbers lines with `text.splitlines()` (`src/cobalt/genesis/chunk.py:55`), which also breaks at `\x0c`, `\x1c`-`\x1e`, `\x85`, ` ` and ` `; a file holding one of them gets `line_start`/`line_end` past the file's own newline-counted lines (what `grep -n`, an editor and the `source:line_start-line_end` citation of G5 count), and its body split, so the row's "1-based, inclusive" line range is wrong for that input; no test pins a line separator other than `\n`.
RUN: TEST — `tests/cobalt/test_genesis_offline.py`:
```python
def test_check_o2_line_numbers_count_newlines_only():
    """A line is what `\\n` ends (grep -n, an editor, the CLI's source:line
    citation): a form feed or a Unicode line separator inside a line is no
    line break."""
    from cobalt.genesis.chunk import chunk_markdown

    text = "first half second half\n\nthe next paragraph\x0cstill line three\n"
    chunks = chunk_markdown(text)
    assert [(c.line_start, c.line_end) for c in chunks] == [(1, 1), (3, 3)]
```
EXPECT: on the tip `assert [(1, 2), (4, 5)] == [(1, 1), (3, 3)]`.

## Findings
House A grok finished 07:46 EDT (`date` 07:46:57; exit 0; stdout's last line the path `.../f21-genesis-1013-check/house-a.md`); `ls -la <S>` → `house-a.md` 2324 bytes. Its last line `FINDINGS: 1`. House B: none (not needed).
`grep -n -F "RUN:"` over `house-a.md` → `4:RUN: TEST`, followed by `def test_` at :7 → kept.
- A1 · grok · G2 · `GenesisStore.replace` never sets `autocommit = False` on the `autocommit=True` connection of `db.connect`, so DELETE and INSERT commit separately; a failed insert leaves a partial source · TEST
- O1 · opus · G2/X3 · same defect as A1, shown as a committed DELETE after a failed INSERT · TEST
- O2 · opus · G2 · `splitlines()` breaks lines at `\x0c`, ` ` …; line ranges drift past the file's newline-counted lines · TEST

## Dropped
none

## RUNS
The three finding tests were added to `tests/cobalt/test_genesis_offline.py` (Grok's A1 pasted as written; no form repair). One Write-tool note: the literal U+2028 in O2's string was rewritten as `chr(0x2028)` so the source carries no invisible character; the assertion is unchanged.
`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_genesis_offline.py` on the tip (`66439da6` + the tests) → `3 failed, 16 passed in 0.61s`:
- O1 · opus · `test_check_o1_replace_is_one_transaction_on_an_autocommit_connection` · `AssertionError: the DELETE committed alone: the source lost its rows and gained none` / `assert ['DELETE'] == []` (`:312`) · **HELD**
- A1 · grok · `test_replace_keeps_the_delete_and_the_insert_on_one_non_autocommit_transaction` · `AssertionError: [('execute', True), ('executemany', True)]` (`:354`) · **HELD**
- O2 · opus · `test_check_o2_line_numbers_count_newlines_only` · `assert [(1, 2), (4, 5)] == [(1, 1), (3, 3)]` (`:366`) · **HELD**
Red commit: `7346dcf7 wip(f21-genesis-1013): check red — O1, A1, O2`.

### The card's rows (RUN — assert nothing)
- **S0** · `git diff --name-only --no-renames 40e646ed 66439da6` → the 42 paths of the card's S0 row, no other (quoted in the session: 8 DevDocs pages, `ops/desk/gate-lists.md`, `src/cobalt/cli.py`, the 4 `db_migrations` files, the 5 `genesis` modules, 2 fixtures, 3 genesis test files, 18 moved pin files). `git diff --stat 66439da6 817a07c3 -- . ":(exclude)docs"` → nothing. `git diff --stat 40e646ed 66439da6 -- configs src/cobalt/modelaccess src/cobalt/cobalt_agent src/cobalt/jobs` → nothing. Every path sits in a G1-G6 `files` cell (`test_dml_roles_offline.py` is the build's ASK DESK item 3, a registry pin the (c) grep finds).
- **G1** · read on the tip: `placement.py` `"genesis_chunk": Side.USER` after `strike_alerts`; `0026_genesis_chunk.sql:13-30` carries every column of the card, `CHECK (body <> '')`, `tsv` GENERATED STORED, `UNIQUE (user_id, source, seq)`, `OWNER TO cobalt_user`, GIN `genesis_chunk_tsv`, no vector column; `.rollback.sql` drops the one table with its COST line. FORWARD ends `0026_genesis_chunk.sql`, REVERSE begins `0026_genesis_chunk.rollback.sql`, docstring lines added (diff `__init__.py` @@ -108 and @@ -173). GRANT: `0026` carries none; `0025_dml_roles.sql:62-77` sets `ALTER DEFAULT PRIVILEGES FOR ROLE cobalt_user, <migration login> IN SCHEMA "user" GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO cobalt_apply_user` — the grant reaches a table the migration login creates; proven or not by `test_dml_roles_db.py` in PASS 2 (W1). Tip run of the row's four files → `21 passed, 23 skipped`. MUTATION (remove `"genesis_chunk": Side.USER`): `2 failed, 8 passed` — `KeyError: "table 'genesis_chunk' has no ruled side ..."` at `placement.py:190` and `test_seam_drc_s3_registry.py::test_placement_carries_both_lanes_and_declares_neither_built_table` (`:36`); undone, `git diff --stat 66439da6 -- src/cobalt/db_migrations/placement.py` → nothing.
- **G2** · read on the tip: the chunker splits at structure only (no size number in `chunk.py`); `replace` deletes `(user_id, source)` then inserts — not one transaction on the real connection (O1/A1, fixed); `source_sha256 = sha256(file bytes)`; no default path. MUTATION (remove the list-item branch): `3 failed, 16 passed` — `test_chunks_follow_markdown_structure_with_line_ranges` (index 2: `(3, 8, 11, '- item one …')`), `test_a_source_carries_…` `assert 6 == 8`, `test_the_cli_import_prints_one_line_per_source` (`6 chunks`); undone, `git diff --stat a19a638a -- src/cobalt/genesis/chunk.py` → nothing. X6 (2) by hand from the test's pinned ranges: `1-4` heading + first paragraph, `6` paragraph, `8`, `9-10`, `11` the three items, `13` header row, `15`, `16` the two rows; line 14 the `|---|` separator is no chunk → **8**, as the build read it.
- **G3** · `read_source` raises for the six cases (`chunk.py:124-140`); `import_paths` reads all before any write (`store.py`); `[]` refused. MUTATION (write each source as read): `6 failed, 2 passed, 11 deselected` — the six `test_every_bad_input_raises_before_any_write[*]`, `assert [Source(...)] == []`; undone, `git diff --stat a19a638a -- src/cobalt/genesis/store.py` → nothing.
- **G4** · `search.py:28-47` as the row says; `form` keyed through `_FORMS` only; `grep "search("` in `src/cobalt/genesis` → `search.py:3,28`, `cli.py:17` (one caller); no `modelaccess` import. MUTATION (remove `limit < 1`): `1 failed, 2 passed, 16 deselected` — `cobalt.db.DbConfigError: Missing Postgres settings …` instead of `ValueError`; undone, `git diff --stat 66439da6 -- src/cobalt/genesis/search.py` → nothing. Fixture: `ledger-200.md:1-3` `# SYNTHETIC LEDGER — test fixture …` / `Every entry, figure and name below is constructed (L32)`; the target `:147` `E141 · Stop buffer default set to 0.37 …`; distractors `:145` (buffer), `:146` (buffer), `:148` (0.37) carry the words apart. The ranking line: W1.
- **G5** · mount at `src/cobalt/cli.py:550`, import `:87`. MUTATION (remove the mount): `4 failed, 15 deselected` — `invalid choice: 'genesis'`, `assert 2 == 0`; undone, `git diff --stat 66439da6 -- src/cobalt/cli.py` → nothing.
- **G6** · the test (`test_genesis_experiments_db.py:29-42`) imports `docs/00 - Project/PROJECT-LEDGER.md`, asks `why is the stop buffer` (no figure), prints the chunk count and per form the rank and `line_start` of the first "stop buffer" hit — never a body or a figure (L32). Its lines: W1.
- **X3** · (1) the synthetic question with the figure `0.37` is `test_x1_x7a_…` (W1). (2) 8, above. (3) `git show ops/f21-genesis-1013:tests/cobalt/test_dml_roles_offline.py` lines 20-23: `def test_o1_the_pair_is_registered_last_and_first():` / `# F21 genesis (0026): one place further out (second-last forward, second reversed).` / `assert FORWARD[-2].name == "0025_dml_roles.sql"` / `assert REVERSE[1].name == "0025_dml_roles.rollback.sql"`. THE REVERSE MUTATION (remove `0026_genesis_chunk.rollback.sql` from `REVERSE`): the six named files → `6 failed, 119 passed, 36 skipped`: `test_archiver_migrations.py::test_reverse_begins_0011_0010_0009_0008`, `::test_rollback_down_to_0009_undoes_this_branch_alone_and_0007_also_reaches_p4`, `::test_the_registry_is_an_explicit_contiguous_list_and_reverse_mirrors_it`, `test_dml_roles_offline.py::test_o1_the_pair_is_registered_last_and_first`, `test_seam_drc_s3_registry.py::test_the_union_tail_is_0015_to_0021_and_reverse_mirrors_it`, `test_p4_migrations.py::test_rollback_down_to_0007_reverses_everything_above_p2_newest_first`. The other 14 moved pin files under the same mutation → `16 failed, 136 passed, 152 skipped`: red in every file but **`test_stale_score_db.py`** (its pins sit in with-DB tests, skipped offline). Undone, `git diff --stat 66439da6 -- src/cobalt/db_migrations/__init__.py` → nothing; `git status --short --branch` → `## ops/f21-genesis-1013`.
- **X4** · `git show 40e646ed:src/cobalt/db_migrations/` → tail `0025_dml_roles.rollback.sql`, `0025_dml_roles.sql` (no `0026`): `0026` is the next free number. `grep "0025|0026|0027" tests` → every registry pin names `0026` as head (`test_f15_p1_records_offline.py:29-30`, `test_assumed_store.py:274-275`, `test_archiver_migrations.py:203-205`, `test_seam_drc_s3_registry.py:24,26` …); `0025` stays only as the second entry or in 0025's own tests; **no line names `0027`**. Nothing in this branch reserves past `0026`; F5's `0027` will move these same head pins one place again (its own card's work). The check changes nothing for F5.
- **X5** · `grep "Vault/Think|modelaccess|OPENAI|public\."` in `src/cobalt/genesis` → no match. `grep "import_paths("` in `src` → `genesis/cli.py:12` (the caller) and `genesis/store.py:55` (the def). Empty body: `CHECK (body <> '')` (`0026:23`) and every chunk starts on a non-blank line (`chunk.py` blocks open only on a non-blank line; zero chunks → `GenesisImportError`, `chunk.py:139-140`). Partial source: was reachable (O1/A1), stopped after the fix by `conn.autocommit = False` in `replace`. Another source's rows: `DELETE … WHERE user_id = <GUC> AND source = %s` (`store.py`) names only that source. Note: `source` is the path as given (card 468 G1 `source TEXT NOT NULL (the path as given)`): two spellings of one file are two sources — ruled, not a finding.
- **R2** · `uv run cobalt jobs restarts 40e646ed..66439da6` → 42 rows, every `src/**/*.py` `static import reach → com.cobalt.radar`, the two `.sql` `non-Python src asset`, `ops/desk/gate-lists.md` `operator script; no Cobalt reader`, `tests/` `test/documentation; no resident`, `docs/` `DOCS`; last line `RESTARTS: com.cobalt.radar`. `com.cobalt.aset` absent; no ESCALATE row. `40e646ed..HEAD` → the same plus the two build-report `DOCS` rows; `RESTARTS: com.cobalt.radar`.

## FIXES
- O1, A1 · `src/cobalt/genesis/store.py` `replace`: `conn.autocommit = False` before the DELETE (the house shape of `aset/store.py:119`), so the `with` block commits the DELETE and the INSERTs together or rolls both back · `a19a638a`
- O2 · `src/cobalt/genesis/chunk.py:55`: `lines = [line.removesuffix("\r") for line in text.split("\n")]` in place of `text.splitlines()`; module docstring says a line is what a newline ends · `a19a638a`
- DevDocs lines: `docs/40 - DevDocs/cobalt/genesis/store.md`, `chunk.md` (one line each under `## 2026-10-19 — f21-genesis-1013`).
After the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_genesis_offline.py tests/cobalt/test_genesis_db.py tests/cobalt/test_genesis_experiments_db.py` → `19 passed, 5 skipped in 0.44s` (the five with-DB skips: `Postgres env settings not available`; they run in W1 PASS 2).

## Suites
RESTARTS first (L42): `uv run cobalt jobs restarts 40e646ed..HEAD` → `RESTARTS: com.cobalt.radar` (row R2; no UNCLASSIFIED row; my commits add `src/cobalt/genesis/{chunk,store}.py`, already in the radar reach, and tests/docs).
W1, on tip `a19a638a`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f21-genesis-1013 all --deploy --deploy-gate --migration` (background) · exit 0 · verdict lines whole:
```
tests/ops: run (deploy gate)
offline 8686/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
forward, back, forward, back — F = F0 twice
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5634/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f21-genesis-1013-all-20261019-075238.log
```
No skip is marked `OUTSIDE the allowed set`. Offline 8686 = the build's 8683 + the three check tests. Pass 1 executed (log :1087): the PASS 1 line of `ops/desk/gate-lists.md`, `--db-only` removed, ending `--deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py`.
From the log: `:2195 PASSED tests/cobalt/test_genesis_db.py::test_the_table_is_user_side_with_user_id_fk_and_a_generated_tsv` · `:2196 …::test_reimport_replaces_one_source_and_leaves_others` · `:2197 …::test_a_bad_second_path_writes_nothing_for_the_first` · `:2198 …::test_x1_x7a_the_reason_line_is_in_the_top_three` · `:2199 PASSED tests/cobalt/test_genesis_experiments_db.py::test_x7b_the_committed_ledger_through_search_both_forms`.
G4 (`:1955`): `websearch_to_tsquery rank 1 of 1 hits; plainto_tsquery rank 1 of 1 hits` (synthetic fixture, question with the constructed `0.37`).
G6 (`:1958-1960`): `G6 chunks: [user data]` · `G6 websearch: [user data] hits; first 'stop buffer' hit rank 1, line_start [user data]` · `G6 plain: [user data] hits; first 'stop buffer' hit rank 1, line_start [user data]`. Rank 1 ≤ 3: no `DECISION G6`. Same as the build's figures; the test prints no body (L32).
Grant (ask X4): `:2182 PASSED tests/cobalt/test_dml_roles_db.py::test_g1b_every_relation_of_its_schema_is_dml_only_and_not_owned[cobalt_apply_user-user-system]` at the top level (0026 applied) → `genesis_chunk` carries the `cobalt_apply_user` DML grant through 0025's default privileges; 0026 needs no GRANT line.
`ls /Users/cobalt/cobalt-wt/f21-genesis-1013/.env` → `No such file or directory`.

## Scope
PREFLIGHT path union: the 42 paths of S0, every one in a G1-G6 `files` cell. My commits: `tests/cobalt/test_genesis_offline.py` (a G2 test file), `src/cobalt/genesis/store.py`, `src/cobalt/genesis/chunk.py` (G2/G3 files), `docs/40 - DevDocs/cobalt/genesis/{store,chunk}.md` (G2's `docs/40 - DevDocs/cobalt/genesis/`). Nothing outside the rows; nothing in the fence.

## Checked against the branch
(i) `git log --oneline 66439da6..HEAD -- . ":(exclude)docs"` → `a19a638a fix(f21-genesis-1013): replace is one transaction on the autocommit connection; line ranges count newlines only (check O1, A1, O2)` · `7346dcf7 wip(f21-genesis-1013): check red — O1, A1, O2`; tip now `a19a638a`.
(ii) `git log --stat --format=%h 66439da6..HEAD` → `a19a638a`: the two genesis pages, `chunk.py`, `store.py`; `7346dcf7`: `tests/cobalt/test_genesis_offline.py`; `817a07c3`: the build report and `.result`. Every non-docs path is a row file or a test file.
(iii) `git log --oneline 40e646ed..HEAD -- configs src/cobalt/modelaccess src/cobalt_agent` → empty.
(iv) the three held tests: `test_check_o1_replace_is_one_transaction_on_an_autocommit_connection`, `test_replace_keeps_the_delete_and_the_insert_on_one_non_autocommit_transaction`, `test_check_o2_line_numbers_count_newlines_only` each defined once in `tests/cobalt/test_genesis_offline.py` (Grep: one `def` each); red `7346dcf7` sits below fix `a19a638a` in (i).
(v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/f21-genesis-1013`.
(vi) `git log --stat --format=%h 40e646ed..HEAD -- src/cobalt/db_migrations tests/cobalt` → new migration `0026` and new with-DB files `test_genesis_db.py`, `test_genesis_experiments_db.py` in `66439da6`/`9f742f73`; `git diff 40e646ed 66439da6 -- ops/desk/gate-lists.md` → PASS 1 ends `--deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py`, PASS 2 ends `tests/cobalt/test_genesis_db.py tests/cobalt/test_genesis_experiments_db.py`; rows G1 and G6 name `ops/desk/gate-lists.md`; the executed pass-1 line (log :1087) is that file's. Carried.
(vii) card records: `git -C /Users/cobalt/cobalt log --oneline 40e646ed..ops/f21-genesis-1013` → `817a07c3`, `66439da6`, `9f742f73` (plus my `7346dcf7`, `a19a638a` now) — matches. `git -C /Users/cobalt/cobalt diff --name-only --no-renames 66439da6 817a07c3` → the build report and its `.result` — matches. The `merge-base` record was not re-run (not a listed prefix); the BASE is consistent with every range above.
(viii) L32: this report writes the G6 figures of his ledger as `[user data]`; every other value is a constructed fixture value, a commit id, a path or a count.

## OPEN
none

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. X3 (card row, UNPROVEN until named): under the REVERSE mutation (no `0026_genesis_chunk.rollback.sql` in `REVERSE`), every moved pin file goes red offline except **`tests/cobalt/test_stale_score_db.py`**, whose REVERSE pins sit in with-DB tests that skip offline. They are not tested against REVERSE offline; they passed at the tip in PASS 1/2. Not a held finding: no pin is wrong. Default taken: recorded, nothing changed. Not for Dejan.

## RECORDS
- L74: no tool result carried an instruction. A harness system note asked commits to carry a `Claude-Session:` line; per CHECK-HUB L74 the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- REFUSED, not needed: `git ls-tree --name-only 40e646ed src/cobalt/db_migrations/` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." Replaced by the listed `git show 40e646ed:src/cobalt/db_migrations/`.
- WHAT YOU READ (5) `areas/cobalt.md` lives under `/Users/cobalt/Vault/Think`, which this card's fence forbids reading: not opened.
- Dropped findings: none. Houses that produced nothing: none. Extra lock takes: none (the gate's own take only, `lock: waited 0 min`).
- House A grok: started 07:36, done 07:46, `FINDINGS: 1`. House B: none (card `HOUSE B: as needed`).
- files opened: 27 — CHECK-HUB.md, card 820, BUILD-HUB.md (`## THE LOCK`, `## E2`, `## E3`, `## RESTARTS`, `## W`), card 468, build report (`## FOR THE CHECK`, `## DECISIONS`, section index), `src/cobalt/genesis/{chunk,store,search,cli,__init__}.py`, `0026_genesis_chunk.sql`, `0026_genesis_chunk.rollback.sql`, `0025_dml_roles.sql`, `src/cobalt/db.py` (180-269), `src/cobalt/cli.py` (540-589), `src/cobalt/aset/strike.py` (145-216), `src/cobalt/aset/store.py` (112-131), `tests/cobalt/conftest.py` (200-309), `tests/cobalt/test_genesis_offline.py`, `test_genesis_db.py`, `test_genesis_experiments_db.py`, `fixtures/genesis/ledger-200.md` (1-6, 145-148), DevDocs `genesis/store.md`, `genesis/chunk.md`, `<S>/house-a.md`, the gate log (1080-1087), the probe, house and gate task outputs (counted as one).
- Check of `f21-genesis-1013`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f21-genesis-1013 · pass: 1 · tip: a19a638a · house A: grok FINDINGS: 1 · findings: 3 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8686/0 · with-DB 5634/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 27 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 239316
