# S3 exits C4 fix r2 — drafter report (2026-09-29)

Seat `s3-exits-c4-fix-r2-draft-0929` (Opus 5.5, auto). Start `date` → `Tue Sep 29 20:39:05 EDT 2026`. AUTHORIZATION (K23), each its own call: `grep -n "^| R154 "` → `163:` carries `U2`; `grep -n "^| R155 "` → `164:` names `36-draft-s3-exits-c4-fix-r2.md`; `git log -1 -S"36-draft-s3-exits-c4-fix-r2.md"` → `80856785f3f7b226d9cf54eb59975589df662dfe`. Branch tip read 20:39: `git log --oneline -3 s3/exits-c4` → `e49fe6a2` over `01d0fbb9` over `b493c09c`, as expected. Code read at `01d0fbb9` by `git show`.
Short names: `<r2>` = `reports/s3-exits-c4-fix-r1-check-2026-09-29.md` (round 2); `<b1>` = the fix r1 build report on `s3/exits-c4`; `<o>` / `<g>` = `opus-check.md` / `grok-check.md` in `agy-trial/scratch/tribunal-bars-0920/s3-exits-c4-fix-r1/`.

## §0 Headline
- U2 → **FIX, one row B1**, in C4's own `src/cobalt/prefill/trade_note.py` (not `vaultwrite/`). The merge re-renders his whole frontmatter from a YAML dict: `5.10` → `"5.1"`, and a typed `exit_time: 10:31` → `"631"`, which changes the value itself. B1 writes his lines back byte for byte. Red first on `01d0fbb9`, with a negative control and two mutations.
- X3 → **OUT OF SCOPE** again. It is a separate mechanism: `VaultWriter`'s merge baseline on `main`, which this branch leaves untouched. The deploy set can lawfully ship C4 with it open (`## X3 AND THE DEPLOY SET`).
- U1's unprinted refusal text → UNPROVEN → RUN U3.
- FIX 1 · NOT REAL 10 · UNPROVEN 1 · OUT OF SCOPE 1 · OWNER ITEM 0. Wrote `37` (build) and `38` (round 3 of ≤3, the last; seats Opus · Sol · Grok). No new rule string. ESCALATE 7.

## L74
A system-reminder block came appended to the first tool result (the read of this prompt file). It asks for a `Claude-Session:` line in commits and PR bodies and names a file-send tool. Recorded once here; not followed. I commit nothing and sent no file.

## Classification
Each class comes from `<r2>`'s file-check column (`## Checked against the branch`, `:114-125`) or from its `## FOR THE CLASSIFIER` (`:135-140`) and `## ESCALATE` (`:142-147`).

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | U2: his typed `exit_price: 5.10` comes back as `exit_price: "5.1"` after the close write (Opus CHECK-line item `U2`; FOR THE CLASSIFIER 5; ESCALATE 2) | `<r2>:122` (HOLDS as a run result), `:140`, `:144`; `<b1>:63-64`, `:225`; `<o>:31`; `<g>:7` | FIX → **B1** | L28 ("human text preserved verbatim"); v3 §7 `S3-EXITS-v3-2026-09-22.md:224` "Once he types a value, it is never touched"; R35 (3) (`cto-2026-09-28.md:43`: "O5 / O6 = A: fills only while blank (L28)"); the module's own docstring `trade_note.py:15-16` ("read back and kept verbatim"). **Render site: `trade_note.py`, not `vaultwrite/frontmatter.py`.** `frontmatter.py:47` (`yaml.safe_load`) is the lossy READ; it is shared and read-only, and it stays. The bytes change at `trade_note.py:282-293`: a dict built from that read is re-rendered by `_render_frontmatter(merged, every_key=False)` through `_render_value` (`:113-118`, which quotes every key but `date` / `symbol` / `trade_def`, in `FIELD_ORDER`). My own run (`uv run python -c` with `yaml.safe_load`, 20:4x): `a: 5.10` → `5.1`, `b: 10:31` → `631`, `f: [x, y]` → a list, `h: -120.50` → `-120.5`. So a typed `exit_time: 10:31` would come back `"631"`, a changed VALUE and not only changed bytes. | The merge branch (`:276-295`) builds the block LINE BY LINE from his raw lines, in his order. Only a Cobalt-owned key's entry is replaced by its rendered line, and a key of his is replaced only while blank and filled (R35 (3) unchanged). A block the merge cannot map is refused, with nothing written. One helper, `_merge_frontmatter_lines`. Red first on `01d0fbb9`: B1-1 his key typed first; B1-2 a machine-filled key he then edits; B1-3 `exit_time`; B1-4 his extra keys, comments, list shapes and order; B1-5 the `/size` call shape; B1-6 the unmappable block; B1-7 with-DB through the close (`web.py:1569`) and the retry (`cards/cli.py:149`). N is the negative control (Cobalt's five still refreshed and a blank still filled). It is green on base and red under M1, and B1-1 … B1-5 go red under M2 (K25 (1)). |
| 2 | X3, human wins once: Opus's `ready: NO` rests on it; the seats split on ready (ESCALATE 1; Opus CHECK-line `EXCEPT X3`; Grok "X3 does not decide ready") | `<r2>:143`, `:96`; `<o>:44`, `:50`; `<g>:7` | OUT OF SCOPE | Re-classified on this round's evidence (`## X3 AND THE DEPLOY SET`). It is not U2's mechanism: U2 is C4's own renderer (`trade_note.py:113-118`, `:293`), while X3 is `VaultWriter`'s merge baseline (`vaultwrite/writer.py:724-733`, `unit_after` = the merged body `:766`, `:969`). `git log --oneline c1dc476d..s3/exits-c4 -- src/cobalt/vaultwrite` → EMPTY: that code is `main`'s, shared by every Cobalt unit writer. The rule is settled (L28, v3 §7 `:226`); the mechanism is routed outside C4 (v3 X3 row `:306`; `26` E1 X3 "C4 builds nothing to fix it"). It fails L67's owner test (a design question the houses settle), so it is not an owner item. It is owed as its own vault-writer item (R104). | Not built (L75: nothing widens). B1 needs no writer change: once Cobalt's lines for his keys equal his lines, `merge3` has nothing to take from him, whatever the baseline. R35 (3) is untouched (L77). |
| 3 | The render-site pointer: Opus names `trade_note.py:113-118`, while round 1's classifier and `<b1>` named `vaultwrite/frontmatter.py` (ESCALATE 2, second half) | `<r2>:144`, `:122`; `<o>:31` | NOT REAL | A pointer correction that HOLDS (`<r2>:122`: "the fix site Opus names … is where the quoting is") | Carried into B1: the fix site is `trade_note.py`, and `frontmatter.py` is not touched. |
| 4 | U1: `NaN` / `-1` on `/fill` → 200, and whether the page carries a refusal is not printed (Opus (iii) U1 row) | `<o>:30`; `<b1>:116`, `:218` | UNPROVEN | L70: no seat or hub printed the body past 200 characters. Read: `web.py:1147-1151` renders a caught `SizingError` as `_failed(...)` on a 200 | RUN **U3** in `37` (E2, lock take 1, with-DB). It prints every body line with `FAILED` / `REFUSED` / `Nothing written`, or `NO REFUSAL TEXT`. A silent page → `ESCALATE U3` for the desk (C1's route), not fixed here. |
| 5 | Opus (a) env note: the offline guard test needs the dev-vault trades folder (`vault_writer.py:32`) | `<r2>:124`; `<o>:40` | NOT REAL | Hub HOLDS "not a defect: it fails loud, it never passes falsely" | A record. |
| 6 | The guard wraps the one resolver and fails loud at teardown (FC 1) | `<r2>:136`, `:117-118` | NOT REAL | HOLDS in both seats and the hub | A confirmation of F1. |
| 7 | Every fill-posting test resolves inside `tmp_path` (FC 2) | `<r2>:137`, `:121` | NOT REAL | HOLDS | A confirmation. |
| 8 | The two developer-vault listings are equal before and after (FC 3; Grok NOT CHECKABLE, Opus a summary) | `<r2>:138`, `:123`; `<g>:7` | NOT REAL | The hub's own `ls -la` HOLDS (767 B / 665 B, `Sep 29 09:35`) | Resolved by the hub. `37` / `38` keep the desk listing plus the hub `ls`. |
| 9 | NOTHING WIDENED, no `src/` (FC 4) | `<r2>:139`, `:125` | NOT REAL | HOLDS | A confirmation. |
| 10 | Sol did not check (METER, back Oct 4 2:06 PM) (ESCALATE 3) | `<r2>:145` | NOT REAL | L67 floor met (Opus + Grok); safe default NO | A record. `38` seats Opus · Sol · Grok, and Opus + Grok while Sol is on METER (K22). |
| 11 | L74 (ESCALATE 4) | `<r2>:146` | NOT REAL | L74 | A record. |
| 12 | The standing line (ESCALATE 5) | `<r2>:147` | NOT REAL | L39, L67, L75 | A record. `38` carries round 3's line (THE LAST). |
| 13 | Grok's CHECK line `BUILD STANDS · ready: YES` | `<g>:13`; `<r2>:96` | NOT REAL | Every Grok item HOLDS in `<r2>` | A confirmation. |

Each seat's CHECK-line item: Opus `EXCEPT X3` = row 2 and `U2` = row 1; Grok `BUILD STANDS` = row 13; Sol METER = row 10.

Totals: FIX 1 (→ row B1) · NOT REAL 10 · UNPROVEN 1 (→ RUN U3) · OUT OF SCOPE 1 · OWNER ITEM 0.

## X3 AND THE DEPLOY SET
X3 and U2 are not one mechanism. U2 is C4's own frontmatter renderer: it re-renders his values from a lossy YAML read (`trade_note.py:113-118`, `:282-293`). B1 fixes it in that file alone, and no line of the writer changes. X3 is `VaultWriter`'s merge baseline: after his edit of a Cobalt line wins once, `unit_after` holds the merged body, so the next Cobalt write sees no human change and overwrites his edit without an override row (`vaultwrite/writer.py:724-733`, `:766`; the frontmatter region is the same, `:943-951`, `:969`). That code is `main`'s. It is shared by every Cobalt unit writer, and this branch has no commit under `src/cobalt/vaultwrite` past the merge-base `c1dc476d`. The rule is already settled (L28 "human wins"; v3 §7 `:226`). The approved design routes the mechanism outside C4 (v3 X3 row `:306`; `26` E1 X3: "C4 builds nothing to fix it"). The houses can settle the design, so it fails L67's owner test, and it stays OUT OF SCOPE, owed as its own vault-writer item (R104). **One line for the desk: YES, the deploy set can lawfully ship C4 with X3 open. L43 holds a branch only when it is not built, not checked, or turns the combined gate red. X3 is none of these for C4: it is `main`'s shared writer, already live for every Cobalt unit, and C4 reaches it only as one more caller.** `38` states this to the seats and asks any NO to say whether X3 alone decides it.

## RECORDS
- My own runs (read-only):
  - `uv run python -c` with `yaml.safe_load` on constructed lines → `{'a': 5.1, 'b': 631, 'c': '09:31', 'd': '2026-09-03 10:00', 'e': True, 'f': ['x', 'y'], 'g': datetime.date(2026, 9, 3), 'h': -120.5}`.
  - `git log --oneline c1dc476d..s3/exits-c4 -- src/cobalt/vaultwrite` → EMPTY (`git merge-base main s3/exits-c4` → `c1dc476d`).
  - `create_if_absent` seeds baselines only for marker sections (`writer.py:621-641`, called at `:611`). The frontmatter region therefore has no baseline at its first `upsert_region`, and `base = human` (`:946-948`). That is why U2 showed Cobalt's re-render winning at once.
- Callers of the merge (`git grep` at `01d0fbb9`): `aset/web.py:1047` (`/size`), `:1550` (the fill, `create_only`), `:1569` (a leg / the close), `cards/cli.py:149` (the retry), `prefill/trade_note.py:375`, `:436`. `37` pins each (K25 (2)).
- RULE STRINGS, checked 20:48 ET:
  - `37` line 5 equals the line derived from `24` line 5 by substituting only the path and the name (`cmp` identical). `comm -3` of the sorted double-quoted tokens (28 each) prints only the two `Read '…'` paths.
  - `38`'s launch line (from `claude --bg` to the last `--add-dir`) equals the one derived from `25` line 1 (`cmp` identical). `comm -3` (18 tokens each) prints only the two `Read '…'` paths. The four R88 `cp` strings are unchanged.
- Placeholders:
  - `37`: `R_[_]` once (the launch-row line `:45`); the `FILL AT LAUNCH` literal at the two value slots `:14`, `:16` and the gate line `:43`.
  - `38`: `R_[_]` once (`:13`); the `FILL AT LAUNCH` literal at its three value slots `:4`, `:5`, `:6` (its gate is `21`'s block).
- Sizes: `37` 32,129 B; `38` 18,707 B.
- The L76 lock at 20:44: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`.

## OWNER ITEMS
NONE.

## FOR DEJAN
New rule strings: NONE. No A/B now. The prepared A/B for the case where round 3 ends NO on X3 alone is under `## ESCALATE` 1, for the desk.

## ESCALATE
1. **The last round's fallback (L39)** [20:49 ET]. If `38` ends `ready: NO` and every NO is `X3 alone`, nothing loops, and the item reaches him as ONE A/B:
   - **(A)** C4 ships in tonight's S3 exits deploy set. X3 stays owed as its own vault-writer item (R104), fixed for every Cobalt unit writer at once.
   - **(B)** C4 waits until the X3 item is designed, built and checked. C1–C3 still land (L43).
   - Recommendation: **A**. X3 is `main`'s live behavior today, and holding C4 does not remove it from his daily notes.

   This is the desk's draft, not an owner item now (L67).
2. **B1 changes two things besides his bytes. Both are inside the row.**
   - (a) A Cobalt-owned key absent from his block is appended just before the closing `---`, instead of at its `FIELD_ORDER` place.
   - (b) A block the line merge cannot map is refused loud with nothing written (B1-6). Today it is re-rendered.

   Safe default taken: both stay (L1: never guess at his shape). The desk may strike B1-6 before launch if it reads (b) as widening.
3. **U3 in the last round.** A `NO REFUSAL TEXT` result is an `ESCALATE U3` for the desk, never a defect of this round. `/fill`'s parse is C1's, and after round 3 nothing loops (L39).
4. **The frontmatter region and X3 (UNPROVEN, not run, L70).** The first `upsert_region` on a new note has no baseline (RECORDS). An edit he makes to one of Cobalt's five keys before the first merge is therefore overwritten with no override row, and after that it wins once. This is my reading of `writer.py`, for X3's own item, not a finding here. B1 does not touch Cobalt's five.
5. **RESTARTS.** `37` changes `src/cobalt/prefill/trade_note.py`, so its RESTARTS row is derived by the build and not predicted (L42). The deploy set carries whatever that row names.
6. **The DESK LINE.** Launch `37` only while `ls ~/cobalt-wt/*/.env` has no match and no with-DB run is in flight (L76), and with `## OWNER ITEMS` empty (it is). Fill `37`'s `<base>` and dev-vault listing, and `38`'s three values, at launch.
7. L74: recorded once under `## L74`.

## CONTINUE
next: none. The desk verifies (L35) and commits `37`, `38` and this report. It writes `37`'s launch row (`<base>`, the dev-vault listing, `no with-DB run in flight`) and launches it under the DESK LINE (ESCALATE 6).

S3 EXITS C4 FIX R2 DRAFTED · FIX: 1 · NOT REAL: 10 · UNPROVEN: 1 · OUT OF SCOPE: 1 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 7
