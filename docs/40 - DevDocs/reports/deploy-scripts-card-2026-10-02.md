# Deploy card draft — set `scripts` — 2026-10-02 (drafter `deploy-scripts-draft`, 16:34 ET)

## §0 Headline
1. Card written: `prompts/2026-10-02/25-deploy-scripts-card.md`, JOB `scripts-1002`, nine ships, `MIGRATIONS: none`, restart set `com.cobalt.aset com.cobalt.radar`. The desk commits it.
2. `11` and `13` are left out: the hub's P7 refuses them (`src/cobalt/db_migrations` changes under `MIGRATIONS: none`), and their two branches conflict at STEP-T (DECISION 1).
3. `06` is left out: its check was still running at 16:34 ET.
4. R135 does not name this card's JOB, which P1 (iv) requires. The desk binds it to `scripts-1002` before the launch, or launches at 20:00 under P1 (i) (DECISION 2).

## DECISIONS
1. `11` dev-rebuild and `13` slot-guard are NOT IN THIS SET. Safe default taken: both rows left out; they ship tomorrow.
   - P7 and STEP-T: `git -C /Users/cobalt/cobalt diff --stat main...ops/slot-guard-1002 -- src/cobalt/db_migrations` → `src/cobalt/db_migrations/cli.py`, `src/cobalt/db_migrations/dev_rebuild.py`. The same read on `ops/dev-rebuild-1002` names the same two files. `DEPLOY-HUB.md` P7 accepts only the files of `MIGRATIONS` (NOTHING when `none`), and so does STEP-T. With either head on the card, the result is `FAILED PREFLIGHT: migration` for the whole set. Neither file is a migration.
   - The stack is broken: `git -C /Users/cobalt/cobalt merge-base --is-ancestor 68dddee3 ops/slot-guard-1002` → exit 1. `13` stands on `1df251b9` and does not carry `11`'s check fixes (`c9960106`, `68dddee3`, `07cc965f`).
   - A conflict at STEP-T: both branches insert after line 18 of `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md` (`07cc965f` and `7eafd308`) and after line 172 of `tests/cobalt/test_dev_rebuild_db.py` (`c9960106` and `b6a3219b`). `git -C /Users/cobalt/cobalt diff -U0 1df251b9 <branch> -- <file>` shows it for each.
   - The judge seat answers (R41). It needs two things: a restack of `13` onto `68dddee3` that resolves those two inserts, and a hub rule that admits a non-migration file under `src/cobalt/db_migrations` on a `MIGRATIONS: none` card. The adoption card is the natural place for the rule.
2. The window row does not name the JOB. P1 (iv) requires "a row of `RULINGS` that overrules L66 / L43 for THIS deploy and names this card's `JOB`". R135 (`cto-2026-10-02.md` line 142) names no JOB. The precedent R32 (line 39) applied R10 and R14 to JOB `aset-interim-close-1002` by name.
   - Safe default: the card cites `2026-10-02 R37, 2026-10-02 R135`, as ordered. Before the launch, the desk writes and commits a row in R32's shape, `HIS RULING (R135 as applied by the desk, L78): L73 override of L43 / L66 for THIS deploy, JOB scripts-1002 …` with `HIS RULING · APPROVED`, and adds its number to `RULINGS`.
   - Without that row, a launch before 20:00 ET may end `FAILED PREFLIGHT: window`. The report would then exist, and a relaunch needs a new `REPORT` name. From 20:00 ET, P1 (i) or (ii) holds with no new row.
3. UNPROVEN — needs STEP-T's merges. I read every shared file hunk by hunk (card `## RECORDS`, "FILES TWO SHIPS BOTH CHANGE"). No hunk overlaps. The closest pair is `22`'s `DEPLOY-HUB.md` line 109 and `16`'s lines 111–113, with one unchanged line between them. Only the hub's merge proves the merge is clean (L68). A conflict ends `FAILED: merge` with nothing touched.
4. UNPROVEN — needs `uv run pytest tests/ops` on the merged tree. `tests/ops/` is new in this set, and STEP-G runs only `tests/cobalt tests/taxonomy`. Each check ran its branch's `tests/ops` files. No run covers the nine merged together. The hub has no listed string for this run, so the card does not ask for it. `ops/desk/` is read by no resident (`15`'s rule).

## RECORDS
- Read whole: `brain-direction-2026-10-02.md` (with its uncommitted `## TOMORROW` rows), `CARD.md`, the precedent cards `14` and `10`, and `DEPLOY-HUB.md` lines 1–128 and the heading index.
- Headers: a `grep -h -E "^(JOB|BRANCH|BASE|TIP|CHECK REPORT|WORKTREE|RULINGS):"` over the twelve cards.
- Stop lines: `tail -n 2` of the twelve check reports, at 16:28 ET. All ten finished checks read `held unfixed: 0` and `ready: YES`. `06` read `(run in progress — next step under ## CONTINUE)` at 16:28, 16:32 and 16:34 ET (`tail -n 1`).
- Heads: `git -C /Users/cobalt/cobalt log -1 --format=%h <branch>` ×12. Past-tip commits: `git -C /Users/cobalt/cobalt log --oneline --stat <tip>..<branch>`, docs only for `15`, `16`, `22`, `11`, `13` and `06`.
- Stacks: `merge-base --is-ancestor` for `46712ab4`, `63649058` and `68dddee3` against their dependants. Overlaps: `diff --stat` of each branch over its base, and `diff -U0` of every shared file.
- `main` movement: `git -C /Users/cobalt/cobalt log --oneline <base>..main` for bases `446ff64d`, `a0188b69` and `53a85f27`. `git -C /Users/cobalt/cobalt show -U0 5bf129ae`.
- Migrations: `log --oneline main..<branch> -- src/cobalt/db_migrations`, EMPTY for `05`, `17`, `18`, `19`, `21` (carries `15`, `16`, `12`) and `22`. Not empty for `13` (carries `11`): `7eafd308`, `1df251b9`.
- Production schema level 0022: `deploy-2026-10-02-1.md` line 241. Its stop line reads `DEPLOYED deploy-2026-10-02-1 0f154bb5 | set: asetclose | migrations: none …`.
- Rulings: `grep -n -E "^\| R(…) \|" cto-2026-10-02.md`. `git log -1 --format=%h -S"| R135 |"` → `4a9360d2`; `-S"| R37 |"` → `4e3fa8d8`.
- Markers: before values read on `main` at 16:30 ET: `grep -c -F` returned `0` for every new string, `1` for `127.0.0.1`, and `ls` returned No such file for every new path. After values come from the branch diffs.
- Check reports committed: `log -1 --format=%h -- <path>`, all nine non-empty. `git diff --stat -- "docs/40 - DevDocs/reports"` lists `brain-direction-2026-10-02.md`, `dev-rebuild-check-2026-10-02.md` and `seat-usage.md` as dirty. None of these is a ship's check report.
- Names free: card `## RECORDS`.
- The card has no `«FILL` token (`grep -c` → 0). Its only `%` characters are in two `--format=%h` records under `## RECORDS`. `## SMOKE READS` has none.
- One edit to the card after the first write: his quoted R135 words were removed from `## RECORDS` (writing-rules: no quotes on a read path).

DEPLOY CARD DRAFTED · set: scripts · ships: 9 · migrations: none · decisions: 4 · for Dejan: 0
