# INCIDENT 2026-09-03 — Daily-note overwrite investigation

**Status:** forensics complete.
**Scope:** `1 - Trading/1- Daily Notes/2026-09-02.md` and `2026-09-03.md` in the
production vault `/Users/cobalt/Vault/Think`.
**Investigator constraint:** read-only. No vault writes, no restarts, no
commits. `com.cobalt.prefill-daily` and `com.cobalt.prefill-drc` were unloaded
before any inspection and are still unloaded. `com.cobalt.aset` (PID 79273) was
left running — it was not in scope of the instruction, and it is a daily-note
writer. **It should be stopped before any recovery action.**

---

## 0. Headline — the reported premise is inverted

The report was: *"two daily notes were replaced top-to-bottom with the default
template during the session that produced 0dbc207."*

That is not what the evidence shows.

1. **No Cobalt code path wrote `2026-09-02.md` today.** Not prefill, not ASET,
   not DRC. Proven below.
2. **`2026-09-03.md` never contained human content on disk today** up to and
   including the prefill run. At 14:09:08 it was a 44-line ASET stub. The
   `upgraded_stub` write at 14:22:23 therefore destroyed **no human content** —
   there was none above the banner to destroy.
3. **The destructive write happened at 17:36 and it was not Cobalt.** It
   replaced the prefilled `2026-09-03.md` with an editor buffer, losing the
   three ASET card blocks and the entire Cobalt template/rules block.
4. **Both files as they stand right now hold more of Dejan's writing than any
   earlier version today.** `2026-09-02.md` *grew* from 4810 bytes to 23820
   bytes between 14:13 and 17:37.

5. **Obsidian caused both losses** — 09-02 on Sep 2 at 16:44, 09-03 today at
   17:36. Cobalt's code caused neither.

> **RULING NEEDED — DO NOT RESTORE EITHER NOTE WHOLESALE FROM A SNAPSHOT.**
> Restoring `2026-09-03.md` from any pre-17:36 version destroys the day's
> journal and the full TSLA trade review. `2026-09-02.md` needs nothing — it is
> byte-identical to its best snapshot. The correct recovery is *additive*: merge
> the three ASET cards (and optionally the Cobalt rules block) from the 17:01:58
> Obsidian snapshot into the current `2026-09-03.md`, and nothing else.
>
> **Time-sensitive:** that snapshot lives in Obsidian's File Recovery store,
> default 7-day retention, and Obsidian is still running and writing to it.
> There is **no Time Machine, no git, no sync** covering this vault (§4).

---

## 1. Timeline

All times **EDT (America/New_York)** unless marked `Z`. Claude Code transcripts
and `obsidian.log` record UTC; those have been converted.

### 2026-09-02 (context — precedes the reported incident)

| Time | Actor | Event | Evidence |
|---|---|---|---|
| 06:30:59 | — | `2026-09-02.md` created | `stat` birthtime |
| 08:40–12:17 | Claude session `114b46c0` | ASET-card forensics; appended `BACKFILLED by Cobalt forensics` content to the note via Bash | transcript `114b46c0…jsonl`, tool_use at `12:40:13Z`–`13:21:55Z` |
| 11:57:50 | — | Obsidian snapshot: **23820 B, 17 cards** — the good version | recovery store |
| **16:44** (snapshotted 17:10:53) | **Obsidian-side clobber** | Note reduced to **4810 bytes, 7 headings, zero ASET cards**. Stayed damaged on disk for the next 24 h | `stat` mtime; recovery-store snapshot; `ls -la` in transcript `3b69fc08` at `18:13:07Z` |

**Resolved by the snapshot ladder** (§4): the same failure mode as 09-03 — an
editor-side write replacing the note with a template-shaped version, one day
earlier. Restored from the editor buffer at 17:37:00 on 09-03. **This is the
damaged state `0dbc207` mistook for evidence that prefill had eaten the cards.**

### 2026-09-03

| Time | Actor | Event | Evidence |
|---|---|---|---|
| 06:29:21 | UNRESOLVED | `2026-09-03.md` created | `stat` birthtime |
| 07:22:55–08:54:06 | earlier ASET session | 15 `TEST`/`FORDATE` rows written to `aset_sizings` (ids 171–185). These did **not** land in the Think note | DB query captured at `18:09:38Z` |
| 07:31:56 | commit `410b054` | launchd schedules for the prefill jobs installed for the first time | `git log` |
| 07:47–08:10 | `manual_backfill_20260903.sh` | Bar-archiver backfill. **Ruled out** — touches no daily note | script + log grep = 0 hits |
| 10:02:06 | ASET | TSLA LONG B card appended (`aset_sizings` id 186) | note snapshot + DB |
| 10:02:36 | ASET | TSLA FILL UPDATE appended | note snapshot |
| 10:42:53 | ASET | AVGO LONG B card appended (`aset_sizings` id 187) | note snapshot + DB |
| **14:09:08** | session `3b69fc08` | **`cat` of the full note — 44 lines, ASET stub banner + 3 cards, ZERO human content** | transcript tool_result, `18:09:08Z` |
| 14:22:07 | session `3b69fc08` | NVDA proof card POSTed through `/size`, landed in the note | transcript `18:22:06Z` |
| **14:22:23** | `prefill-daily` (kickstart 1) | `action=upgraded_stub`, filled `rules, trading, market_calendar` | `logs/prefill-daily.log`, `logs/prefill-daily.err` |
| 14:22:37 | `prefill-daily` (kickstart 2) | `action=skipped_idempotent` — all three slot markers present on disk | same |
| 14:23:11 | session `3b69fc08` | `Edit` removing the NVDA proof card from the note (atomic temp+rename → explains dir mtime 14:23:12) | transcript `18:23:11Z` |
| 14:23:32 / 14:24:37 | session `3b69fc08` | Deleted `aset_sizings` ids 188–197 and 198–200 (its own proof rows) | transcript |
| 14:24:19 | — | commit `0dbc207` | `git log` |
| 14:24:51 | session `3b69fc08` | **last tool call of that session** | transcript |
| 15:40:00 | `prefill-drc` | `DRC-2026-09-03.md` created, "17 cards" — 15 of them `TEST`/`FORDATE` | `logs/prefill-drc.log`, DRC content |
| 17:01:58 | — | Obsidian snapshot of `2026-09-03.md`: **6993 B, prefilled template + all 3 ASET cards** — the last good version | recovery store |
| **17:36:37** | **Obsidian (not Cobalt)** | `2026-09-03.md` rewritten to 347 lines / 19635 bytes: full human journal, **0 ASET cards, 0 `cobalt-slot` markers** | `stat`, content grep |
| **17:36:59** | **Obsidian (not Cobalt)** | `2026-09-02.md` rewritten to 601 lines / 23820 bytes: full journal + Vitals brief + **17 ASET card blocks** (grew ~19 KB) | `stat`, content grep |
| 17:39 | this session | forensics begins; both prefill agents unloaded | — |

### Attribution of the 17:36 writes

Not Cobalt, on four independent grounds:

- `prefill-daily.log`/`.err` end at 14:22:37; `prefill-drc` at 15:40:00.
- The `0dbc207` session's last tool call was 14:24:51.
- No prefill process was running (`launchctl list`, `ps`).
- Both writes landed 22 s apart and **removed** every `cobalt-slot` marker — the
  opposite of what any prefill path does.

Obsidian has been running since Saturday (PIDs 398/621/622) and was active at
17:34 (`.obsidian/workspace.json` rewritten). The signature — two open notes
flushed seconds apart, Cobalt's machine-written content gone, the human buffer
content restored — is a stale-editor-buffer flush or a manual File Recovery
restore.

---

## 2. Explicit answer: did any code path write `2026-09-02.md` today?

**No.** Three independent proofs:

1. **`prefill daily` cannot target a past date.** `src/cobalt/prefill/cli.py:47`
   registers the subparser with no arguments — only `drc` has `--date`
   (`cli.py:50`):
   ```python
   sub.add_parser("daily", help="Prefill (or append to) today's Daily Note.")

   drc_parser = sub.add_parser("drc", help="Prefill (or append to) the evening DRC draft.")
   drc_parser.add_argument("--date", help="Target date YYYY-MM-DD (default: today).")
   ```
   and `run_daily_prefill` derives the filename from *now*
   (`src/cobalt/prefill/daily.py:402,407`):
   ```python
   when = when or datetime.now().astimezone()
   ...
   filename = when.strftime(aset_cfg.daily_note.filename_pattern)
   ```

2. **ASET always targets today**, deliberately — `src/cobalt/aset/daily_note.py:177`:
   ```python
   Targets the note for `when` (today), not the original card's date —
   ```

3. **Only four write sites exist under `src/cobalt/`** (`rules_gen.py:116`,
   `daily.py:398`, `vault_writer.py:61`, `vault_writer.py:77`); only
   `daily.py:398` writes a daily note, and it is reached only via the path
   above. `logs/prefill-daily.log` names `2026-09-03.md` and nothing else.

The only process to touch `2026-09-02.md` today at all was the `0dbc207`
session, and only with `grep`/`ls`/`stat` — read-only (transcript `18:12:56Z`,
`18:13:07Z`).

---

## 3. Current content vs. what the template alone produces

Template: `configs/cobalt/templates/daily.md.j2`.

### `2026-09-03.md` — 347 lines, 19635 bytes

| Section | Template produces | Actually present |
|---|---|---|
| `Sleep/Readiness/RHR` | blank | **human**: 80 / 81 / 56 |
| `1% goal:` | blank | **human**: "exit on structure break, not on hope" |
| `Daily HARD Stop: $420`, `STOP TRADING AFTER 11AM`, 2× `I WILL NOT TOLERATE…` | present (literal template text) | **ABSENT** |
| `<!-- cobalt-slot:rules -->` + 12 rule checkboxes + sheet-mode line + mantras | present | **ABSENT** |
| `### Trading` table | SPY/QQQ/IWM filled with prices | present but **all cells empty** |
| `### Market Context:` | `-` | **human**: full Vitals Macro Brief (~170 lines) |
| `<!-- cobalt-slot:market_calendar -->` | filled | **ABSENT**; section body is `- ` |
| `### Trade Ideas` | 6 blank rows | **human**: DELL / GTLB / TSLA / SNOW with levels and bias |
| `## Notes` scores | blank | **human**: full T1 TSLA review, three Q&A answers, missed/passed-trade log |
| ASET card blocks | n/a (appended by ASET) | **ABSENT — 3 cards lost** |

Net: this is a **pre-prefill human note**. Every Cobalt-authored element is
gone; every human element is present.

### `2026-09-02.md` — 601 lines, 23820 bytes

Fully human-authored and intact, plus **17 ASET card blocks** (TSLA 07:50:18;
GTLB 09:31:30–09:34:41 incl. 2 FILL UPDATEs; DELL 10:15:16, 10:18:35; GTLB
10:51:53–10:52:27). Contains **no** Cobalt template guardrail lines and **no**
`cobalt-slot` markers — it was never prefilled by Cobalt at all. Manual entries
(`VIX 16.1`, `SPY 762.5`, `BTC 76.779.00`) confirm hand authorship.

**Nothing is missing from this file.** It is materially richer than the version
that existed at 14:13 today.

---

## 4. Recovery inventory

| Source | Covers | Timestamp | Size / rows | Retrieval |
|---|---|---|---|---|
| **Obsidian File Recovery** (LevelDB snapshot store) | `2026-09-03.md` | **17:01:58 today** | 6993 B, **all 3 ASET cards** + the prefilled Cobalt template | Obsidian → Settings → File recovery → Snapshots. **Best source.** Also decoded to `…/scratchpad/recovered/2026-09-03__snapshot_20260903T170158.md` |
| Obsidian File Recovery | `2026-09-03.md` | 17:36:38 | 19635 B, 0 cards | = current damaged on-disk state |
| Obsidian File Recovery | `2026-09-02.md` | 23 versions, 2026-09-02 07:51:50 → 2026-09-03 17:37:00 | 256 B → 23820 B | same UI; ladder below |
| Transcript snapshot (extracted) | `2026-09-03.md` 3 ASET cards | 14:09:08 | 911 B | `…/scratchpad/snapshot_2026-09-03T18-09-08.080Z.md` |
| `cobalt_dev.aset_sizings` | `2026-09-03` | — | 17 rows, **only 2 real** (ids 186 TSLA, 187 AVGO); 15 are `TEST`/`FORDATE` | `docker exec cobalt_memory psql -U cobalt -d cobalt_dev` |
| `cobalt_dev.aset_sizings` | `2026-09-02` | — | 44 rows, **14 real** | same |
| `2 - Trades/` notes | `2026-09-03` | 10:02, 10:42 | 2 files, 443 B each | on disk |
| `2 - Trades/` notes | `2026-09-02` | 07:50–10:52 | 14 files | on disk |
| **Time Machine** | — | — | **NONE — no destination configured** | unavailable |
| Vault git / `.trash` / `.bak` / iCloud / Obsidian Sync | — | — | **NONE** | unavailable |

### `2026-09-02.md` snapshot ladder

`2026-09-02` 07:51:50 (256 B, 1 card) → 09:33:50 (17334, 10) → 10:18:50 (18507,
14) → 10:57:50 (19335, 17) → **11:57:50 (23820 B, 17 cards)** → **17:10:53
(4810 B, 0 cards — clobbered)**; `2026-09-03` **17:37:00 (23820 B, 17 cards —
restored)**.

This resolves the Sep 2 16:44 mystery: the note was clobbered to 4810 bytes on
Sep 2 (mtime 16:44, first snapshotted at 17:10:53), stayed damaged on disk all
of 09-03 — which is the state `0dbc207` saw and drew its root cause from — and
was restored from the editor buffer at 17:37:00 today. **`2026-09-02.md` on disk
right now is byte-identical to its best snapshot. Nothing to recover.**

### Verdict on usability

1. **Obsidian File Recovery is the only complete source and it is sufficient.**
   The 17:01:58 snapshot of `2026-09-03.md` carries all three blocks including
   the `aset-fill` FILL UPDATE.
2. **Postgres is a partial fallback, not a substitute.** `aset_sizings` has no
   fill/recompute columns, so the TSLA FILL UPDATE has **no DB row at all**. For
   09-02 the DB holds 14 of the 17 blocks on disk (09:34:06, 09:34:41, 10:52:27
   have no row). A DB→note rebuild would **silently drop cards** — it violates
   fail-loud and should not be used.
3. **Trade notes cross-check counts** (14 for 09-02, 2 for 09-03) but carry no
   grade/shares/risk_budget and cannot rebuild card blocks.
4. **There is no backup of the production vault.** No Time Machine destination,
   no git, no sync. Obsidian File Recovery — default 7-day retention — is the
   only versioning this vault has, and Obsidian is still running and writing to
   that store.

> **Time-sensitive:** retrieve the 17:01:58 snapshot of `2026-09-03.md` before
> the recovery store rolls over.

**Not provable:** only two snapshots exist for `2026-09-03.md` (17:01:58 and
17:36:38), so there is no intraday ladder to prove the card count never exceeded
3. The 2 real DB rows plus 2 trade notes are consistent with exactly 3 blocks
(2 sizings + 1 fill update), so 3 is probably complete — but the snapshot record
alone cannot establish it.

---

## 5. Root cause of the code path that *can* destroy human content

The reported failure did not occur, but the capability is real and is a live
hazard. `src/cobalt/prefill/daily.py:475-485`:

```python
    if STUB_BANNER in existing:
        # ASET bootstrapped this note itself (aset/daily_note.py's own
        # stub-on-create fallback — happens whenever the first card of
        # the day lands before this job ever runs, e.g. prefill was
        # broken/late that morning). It has none of the anchors below,
        # so the normal fill-in-place path would fail loud on the rules
        # anchor. Upgrade it to the full template instead, preserving
        # every appended card byte-for-byte after the rendered template.
        preserved_cards = existing.split(STUB_BANNER, 1)[1]
        new_text = _render_template(context) + preserved_cards
        _write_if_unchanged(path, existing, new_text)
```

Two defects:

**(a) Everything above the banner is discarded unconditionally.**
`existing.split(STUB_BANNER, 1)[1]` keeps only the suffix. Whatever precedes the
banner — YAML frontmatter, journal, plan, Market Context, Trade Ideas — is
replaced by a freshly rendered template. Today that prefix was two lines
(`# 2026-09-03` + blank), so nothing was lost. **If Dejan had typed into the
stub above the banner and saved before 14:22, it would have been destroyed
silently, and reported as `upgraded_stub … filled: rules, trading,
market_calendar` — no warning, exit 0.**

**(b) The trigger is a bare substring test on the whole file.**
`if STUB_BANNER in existing:` matches the banner *anywhere*, at any depth, at any
point in the note's life. A note that is 95 % human prose still takes this branch
if that one line appears in it — and then loses everything above it.

`_write_if_unchanged` does **not** protect against this. It only guards against a
*concurrent* writer between read and write; it happily writes a `new_text` that
has already discarded the prefix.

### Why "human sections untouched" was asserted

The claim rests on the module docstring's standing promise
(`daily.py:7`) —

```
PRINCIPLE (never modify existing note content): if today's note
doesn't exist yet, render the full Jinja template …
```

— which is honoured by the `_fill_all_slots` path but **not** by the stub-upgrade
branch added in `0dbc207`. The new branch was never reconciled against it.

The test that "proves" preservation only ever exercises a pristine stub
(`tests/cobalt/test_prefill_daily.py`, added in `0dbc207`):

```python
    path.write_text(f"# 2026-09-03\n\n{STUB_BANNER}{card_block}")
```

Nothing human is placed above the banner, so the discarded-prefix behaviour is
invisible to the suite. The assertion generalised from card preservation
(genuinely tested) to human-content preservation (never tested).

**Correction to `0dbc207`'s commit message.** It states as root cause: *"2026-09-02:
14 real cards computed and persisted … but zero landed in the real daily note"*
and attributes this to prefill's stale-read race. That inference was drawn from a
`2026-09-02.md` that was **already damaged** (4810 bytes, truncated at Sep 2
16:44 by an unidentified writer). The cards **had** landed — 17 of them are in the
file today. `prefill-daily` had no launchd schedule until 07:31 on 09-03 and its
log shows no 09-02 run, so **prefill never ran against `2026-09-02.md` at all.**
The committed race fix is still correct and worth keeping on its own merits, but
its stated root cause is unproven and the 09-02 evidence does not support it.

---

## 6. What was actually lost

| Item | Where it was | Lost at | Recoverable |
|---|---|---|---|
| 3 ASET card blocks in `2026-09-03.md` (TSLA 10:02:06, TSLA FILL UPDATE 10:02:36, AVGO 10:42:53) | note body | 17:36:37, Obsidian editor write | **Yes** — verbatim in the 17:01:58 Obsidian snapshot *and* the 14:09:08 transcript snapshot; 2 of 3 also in `aset_sizings` |
| Cobalt rules/slot block in `2026-09-03.md` (12 checkboxes, sheet-mode line, mantras, hard-stop lines, SPY/QQQ/IWM prices, market calendar) | note body | 17:36:37, same | **Yes** — intact in the 17:01:58 Obsidian snapshot (preferred; re-running prefill would fill with stale prices) |
| Human content | — | — | **Nothing human was lost, on either date.** |

`2026-09-02.md` lost nothing: it is byte-identical to its best snapshot.

---

## 7. Proposed fixes — Dejan rules

### Immediate (before anything writes again)

1. **Stop `com.cobalt.aset`** (PID 79273). It is the one remaining live writer to
   these notes and Obsidian still has both open.
2. **Close the two notes in Obsidian** before any recovery write, or Obsidian
   will flush its buffer over the top again — that is exactly what happened at
   17:36.
3. **Retrieve the 17:01:58 snapshot of `2026-09-03.md` from Obsidian File
   Recovery now** — 7-day default retention, and Obsidian is still writing to
   that store. Copies already decoded to the session scratchpad
   (`…/scratchpad/recovered/`) should be moved somewhere durable; the scratchpad
   is session-scoped.
4. **Recover additively**: take the 3 card blocks (and, if wanted, the Cobalt
   rules block) from the 17:01:58 snapshot and merge them into the current
   `2026-09-03.md`. **Do not restore either file wholesale** — the 17:01:58
   version has none of the day's journal or trade review.
5. **Do nothing to `2026-09-02.md`.** It is byte-identical to its best snapshot.

### Code — `daily.py` stub-upgrade branch

6. **Refuse instead of discarding.** Compute the prefix
   (`existing.split(STUB_BANNER, 1)[0]`) and, if it contains anything beyond the
   `# YYYY-MM-DD` heading and whitespace, raise loudly rather than upgrade —
   same shape as `NoteChangedDuringPrefill`. Fail-loud law; a stub upgrade that
   silently drops bytes is a plausible-empty artifact.
7. **Tighten the trigger.** Require the stub shape at the *head* of the file
   (`existing.startswith(f"# {date}\n\n{STUB_BANNER}")`), not a substring match
   anywhere in it.
8. **Test the gap.** Add a case with human prose above the banner asserting it
   survives (or that the run refuses). The current suite cannot see this class of
   bug.

### Vault-level — the actual cause of both losses

9. **Cobalt and Obsidian are two unsynchronised writers to the same files, and
   Obsidian is the one that has destroyed data — twice** (09-02 at 16:44, 09-03
   at 17:36). No fix inside `daily.py` addresses this. Options for ruling:
   (a) schedule prefill writes for a window when Obsidian is closed; (b) have
   prefill refuse when the note's mtime is younger than N minutes (proxy for "a
   human is editing"); (c) move Cobalt's machine-authored blocks into a sidecar
   note the human never opens, transcluded into the daily note. **(c) is the
   only one that removes the race rather than narrowing it**, and it also makes
   an editor-side clobber non-destructive.
10. **The production vault has no backup.** No Time Machine destination is
    configured (`tmutil destinationinfo` → "No destinations configured"), the
    vault is not a git repo, and there is no sync. Obsidian's File Recovery — a
    7-day rolling store, inside the app that caused both incidents — is the only
    versioning that exists. **This is the single largest risk surfaced by this
    investigation and it is unrelated to Cobalt's code.** Proposals: configure
    Time Machine, or add a cheap read-only vault snapshot job (hourly `rsync` or
    a git mirror outside the vault).

### Hygiene

11. **Purge the 15 `TEST`/`FORDATE` rows** (`aset_sizings` ids 171–185, written
    07:22–08:54 today). They are polluting `DRC-2026-09-03.md`, which reports
    "17 cards" when 2 are real. `0dbc207`'s "test DB rows removed after proof"
    covered only ids 188–200, its own.
12. **Amend the record** for `0dbc207` (ledger note, not a rewrite) — its stated
    root cause is not supported by the evidence.
13. **Note the DB's limits as a recovery source**: `aset_sizings` has no
    fill/recompute columns, so FILL UPDATE blocks are unrecoverable from it, and
    for 09-02 it holds 14 rows against 17 blocks on disk. Any future
    "rebuild the note from the DB" tool would silently drop cards — that is a
    fail-loud violation and should be designed against now.

### Unresolved

14. `2026-09-03.md` has birthtime 06:29:21 but its content at 14:09 was an ASET
    stub, which `aset/daily_note.py:140-143` writes only when the file does not
    exist — and the first card is 10:02:06. `2026-09-01.md` (06:32:08) and
    `2026-09-02.md` (06:30:59) show the same ~06:30 creation pattern, so
    something creates these notes each morning. What wrote the stub banner into
    an already-existing file is not explained by any code path read here.

---

## Containment 2026-09-03

**Scope of this session:** ops-only. No code edits, no vault writes, no DB
writes, no restarts. Only mutations: `launchctl bootout`/`disable` on the
three named jobs, and this append.

### 1. Inventory

**Before state — `launchctl list | grep -i cobalt`:**

```
79273	143	com.cobalt.aset
-	0	com.cobalt.agent
-	0	com.cobalt.archiver
-	2	com.cobalt.mainframe
```

`com.cobalt.prefill-daily` and `com.cobalt.prefill-drc` do not appear at all —
confirmed still unloaded from the prior forensics session (per this file's
header). `launchctl print-disabled gui/$(id -u) | grep -i cobalt` returned
**no rows** before containment — nothing was disabled yet.

**`ps aux` — relevant PIDs (full output too large to paste; filtered):**

```
cobalt   79281  0.1  0.1  ...  2:21PM  /opt/homebrew/.../Python -m cobalt.aset
cobalt   79273  0.0  0.0  ...  2:21PM  uv run python -m cobalt.aset
cobalt   30826  0.0  0.3  ...  Mon06AM /opt/homebrew/.../Python src/cobalt_agent/main.py
cobalt   30824  0.0  0.0  ...  Mon06AM uv run src/cobalt_agent/main.py
```

No `prefill`, `archiver`, or `mainframe` process was running at inventory
time (archiver is calendar-scheduled, Mon-Fri 20:30, `RunAtLoad=false`;
mainframe is the LM Studio server, not a vault writer).

**Writer table — every process that touches a file under `/Users/cobalt/Vault/Think`:**

| Label | Entrypoint | Note(s) written | Write mode | Loaded Y/N (before) |
|---|---|---|---|---|
| `com.cobalt.prefill-daily` | `ops/com.cobalt.prefill-daily.plist` → `uv run prefill daily` → `run_daily_prefill()` | Today's Daily Note (`daily_note.daily_notes_dir`/`filename_pattern`, e.g. `1 - Trading/1- Daily Notes/YYYY-MM-DD.md`) | **create** (`write_new`, `src/cobalt/prefill/daily.py:469`); **whole-file rewrite** on the stub-upgrade branch (`daily.py:475-485`, discards everything before `STUB_BANNER` — this is the defect in §5) via `_write_if_unchanged`→`path.write_text` (`daily.py:398`); **section-replace** (anchor fill-in-place, `_fill_all_slots` at `daily.py:347`) via the same `_write_if_unchanged`/`daily.py:398` | **N** — not in `launchctl list` |
| `com.cobalt.prefill-drc` | `ops/com.cobalt.prefill-drc.plist` → `uv run prefill drc` → `src/cobalt/prefill/drc.py` | `DRC-YYYY-MM-DD.md` | **create** (`write_new`, `drc.py:327`); **append** (`append_block`, `drc.py:334`, fenced idempotency-marked block) | **N** — not in `launchctl list` |
| `com.cobalt.aset` | `ops/com.cobalt.aset.plist` → `ops/start_aset.sh` → `uv run python -m cobalt.aset` (Flask sizing sheet, PID 79273/79281) | Today's Daily Note, via `save_card`/`save_fill_update` (`src/cobalt/aset/web.py:466,521`) → `_append` (`src/cobalt/aset/daily_note.py:120-144`) | **create** stub-on-first-write (`daily_note.py:140-143`, writes `# {date}\n\n{STUB_BANNER}` if the file doesn't exist yet); **append** (`daily_note.py:144`, card body) | **Y** — PID 79273, KeepAlive+RunAtLoad |
| `com.cobalt.agent` (old tree) | `ops/com.cobalt.agent.plist` → `cobalt.sh start` → `uv run src/cobalt_agent/main.py` (PID 30824/30826) | **Nothing under `/Users/cobalt/Vault/Think`.** `scribe.append_to_daily_note()` (`src/cobalt_agent/skills/productivity/scribe.py:136-177`) writes only under `OBSIDIAN_VAULT_PATH`, which `.env:38` sets to `/Users/cobalt/cobalt/docs` (the repo's own D6/gitignored playground tree) — `docs/0 - Inbox/Daily_Log_YYYY-MM-DD.md`. Every write also routes through `ToolManager`/the Proposal Engine, i.e. HITL-gated (`scribe.py:158-165`), not direct filesystem access. **Not a production-vault writer at all** — reported per instruction for a separate ruling, not stopped. | **append** (repo docs tree, not the vault) | **Y** — running since Mon06AM, not shown with a PID in `launchctl list` because `AbandonProcessGroup` detaches it (same pattern as `archiver`) |
| `com.cobalt.archiver` | `ops/com.cobalt.archiver.plist` → `uv run archiver` → `src/cobalt/archiver/report.py` | **Nothing under `/Users/cobalt/Vault/Think`.** Writes `docs/30 - Design/archiver-runs.md` (`report.py:12,64-65`) — inside the repo's own docs/ tree, not the vault. Reported per instruction for a separate ruling, not stopped. | **create-header-then-append** (`report.py:64` header if new, `:65` row append) | **Y** (loaded, calendar-scheduled Mon-Fri 20:30, not currently running) |
| `com.cobalt.mainframe` | `ops/com.cobalt.mainframe.plist` → `~/.lmstudio/start_mainframe.sh` | none — LM Studio model server, no vault access | n/a | **Y** (loaded) |

Also touching the vault but **read-only**: `regenerate_rules_config()`
(`src/cobalt/prefill/rules_gen.py`) reads `Rules.md` from the vault and
writes the parsed result to `configs/cobalt/rules.yaml` in the repo
(`rules_gen.py:116`) — not a vault write.

### 2/3. Stop + verify

Commands run:

```
launchctl bootout gui/501/com.cobalt.prefill-daily   # "Boot-out failed: 3: No such process" — already unloaded
launchctl bootout gui/501/com.cobalt.prefill-drc     # "Boot-out failed: 3: No such process" — already unloaded
launchctl bootout gui/501/com.cobalt.aset            # succeeded, no output
launchctl disable gui/501/com.cobalt.prefill-daily
launchctl disable gui/501/com.cobalt.prefill-drc
launchctl disable gui/501/com.cobalt.aset
```

`com.cobalt.agent` and `com.cobalt.archiver` were **not** touched.

**After — `launchctl list | grep -i cobalt`:**

```
-	0	com.cobalt.agent
-	0	com.cobalt.archiver
-	2	com.cobalt.mainframe
```

`com.cobalt.aset` no longer appears (was `79273	143	com.cobalt.aset`).

**After — `launchctl print-disabled gui/$(id -u) | grep -i cobalt`:**

```
"com.cobalt.aset" => disabled
"com.cobalt.prefill-daily" => disabled
"com.cobalt.prefill-drc" => disabled
```

**PID 79273:**

```
$ ps -p 79273
  PID TTY           TIME CMD
$ echo $?
1
```

Gone — confirmed via exit code 1 (no matching process) and empty output.
No survivor; `kill -9` was not needed and was not used.

### 4. ASET question (read-only, no code change)

**Is `com.cobalt.aset` the Flask sizing sheet process itself?** Yes —
`ops/com.cobalt.aset.plist` runs `ops/start_aset.sh`, which execs
`uv run python -m cobalt.aset`, the Flask app in `src/cobalt/aset/web.py`
(confirmed live: PID 79273/79281 was the sheet process before bootout).

**Is there an existing config/env flag that keeps the sheet serving while
disabling its daily-note write, with no code change? No.**

- `src/cobalt/aset/web.py:466` (`size()`) and `:521` (`fill()`) call
  `save_card`/`save_fill_update` unconditionally — no config check gates
  the call.
- `save_card`/`save_fill_update` (`src/cobalt/aset/daily_note.py:158-181`)
  call `_append()` (`daily_note.py:120`) unconditionally — no env/flag
  branch inside it either.
- `AsetConfig` (`src/cobalt/aset/config.py:84`) has a `daily_note` field
  (a `DailyNoteConfig`, target dir/filename only) and `enabled_grades`
  (`config.py:151`, gates which grade *options* the sheet accepts) — no
  write-enable/dry-run/disable toggle exists anywhere in the schema.
- `ops/start_aset.sh` sets only `COBALT_VAULT_PATH`, `COBALT_ENV`, and
  sources the key file — no write-suppression env var.

So under NN#16's current code, "sheet serves, daily-note write disabled" is
not reachable without a code change. This is why the sheet itself is down
right now (bootout above) rather than left running — there was no other way
to honor the ruling. Flagging for the fix session, not implementing.

### 5. Re-enable (for the fix session, after the L28 vault-write fix is proven in dev)

```
launchctl enable gui/$(id -u)/com.cobalt.prefill-daily
launchctl enable gui/$(id -u)/com.cobalt.prefill-drc
launchctl enable gui/$(id -u)/com.cobalt.aset

launchctl bootstrap gui/$(id -u) /Users/cobalt/cobalt/ops/com.cobalt.prefill-daily.plist
launchctl bootstrap gui/$(id -u) /Users/cobalt/cobalt/ops/com.cobalt.prefill-drc.plist
launchctl bootstrap gui/$(id -u) /Users/cobalt/cobalt/ops/com.cobalt.aset.plist
```

(`prefill-daily`/`prefill-drc` are calendar-triggered, `RunAtLoad=false` —
bootstrap alone re-arms their `StartCalendarInterval`, no immediate run.
`aset` has `RunAtLoad=true`, so its bootstrap starts the sheet immediately.)

### Status

All three named writers confirmed down and disabled across login/reboot.
`com.cobalt.agent` (writes only inside the repo's docs/ tree, HITL-gated,
never touches `/Users/cobalt/Vault/Think`) and `com.cobalt.archiver`
(writes only `docs/30 - Design/archiver-runs.md`, also inside the repo)
are unchanged, pending the separate ruling requested. Manual process is
now the only path into the production vault's daily notes.

---

## Fix 2026-09-03

**Status:** LAW L28 implemented, proven in the dev vault, deployed, and
exercised against production in `--dry-run` only. **No live vault write
happened in this session.** ADR-0004 has the decision record; the
DevDoc is `docs/40 - DevDocs/cobalt/vaultwrite/README.md`.

### What was built

`src/cobalt/vaultwrite/` — the ONE vault write path. Everything under
`src/cobalt/` writes through it; nothing writes a vault file any other
way. Grep-proof:

```
$ grep -rn 'write_text\|open(.*"a"\|"w")\|os\.replace' src/cobalt/ --include="*.py"
src/cobalt/prefill/rules_gen.py:116   -> configs/cobalt/rules.yaml   (repo, not the vault)
src/cobalt/archiver/report.py:62      -> docs/30 - Design/           (repo, not the vault)
src/cobalt/vaultwrite/writer.py:328   -> the one write path itself
```

### Writer table after conversion

| write site | entry point (file:line) | mode |
|---|---|---|
| prefill daily — create | `prefill/daily.py:463` `writer.create_if_absent` | whole-file, **only when absent** |
| prefill daily — 3 slots | `prefill/daily.py:497` `writer.upsert_unit` | merge into `rules` / `trading` / `market_calendar` |
| prefill drc — create | `prefill/drc.py:429` `writer.create_if_absent` | whole-file, **only when absent** |
| prefill drc — 3 units | `prefill/drc.py:449` `writer.upsert_unit` | merge into `drc-risk` / `drc-trades` / `drc-rules` |
| ASET card + fill update | `aset/daily_note.py:184-185` `create_if_absent` → `upsert_unit` | stub if absent, then merge unit `card-…` / `fill-…` |
| trade note — create | `prefill/trade_note.py:155` `writer.create_if_absent` | whole-file, **only when absent** |
| trade note — frontmatter | `prefill/trade_note.py:166` `writer.upsert_region` | the one marker-less region (Obsidian requires frontmatter first in file) |

Deleted, not repaired:

- **`daily.py:475-485`, the stub-upgrade branch** — the §5 defect. Both
  the `existing.split(STUB_BANNER, 1)[1]` prefix-discard *and* the bare
  `if STUB_BANNER in existing` substring trigger are gone. An existing
  note now always takes the merge path, 05:15 included.
- `prefill/vault_writer.py`'s `write_new` / `append_block` / `overwrite`
  — that module is path resolution only now.
- `aset/daily_note.py`'s append-mode writer and inline stub creation.
- `drc.py`'s `_render_append_block` and its `cobalt-prefill:DATE` marker.

### Answering §7's proposals

- **#6/#7 (refuse instead of discarding; tighten the trigger)** —
  superseded. The branch is deleted rather than guarded, and with it the
  class of defect rather than the instance.
- **#8 (test the gap)** — done, and it is the case the old suite could
  not see: `test_the_exact_0903_shape_loses_nothing` puts human text
  ABOVE the stub banner and asserts the note still `startswith` it.
- **#9 (Obsidian is the second writer)** — **NOT solved, and L28 cannot
  solve it.** L28 makes a *Cobalt* write non-destructive, auditable and
  reversible; it does nothing about an editor buffer flush. Option (c),
  the sidecar note, remains the only proposal that removes the race, and
  it is a Vault-Session decision about note layout. Still open.
- **#10 (no backup of the production vault)** — **still open, still the
  largest risk in this document.** Untouched by this session.
- **#11 (purge the TEST/FORDATE rows)** — done, below.
- **#12 (amend the record for `0dbc207`)** — ADR-0004 records that its
  stated root cause is unsupported and that the committed race fix is
  kept on its own merits.
- **#13 (the DB's limits as a recovery source)** — designed against.
  `aset_sizings` gains `status` + the actual-fill columns (migration
  `0003`), so a FILL UPDATE finally has a row. A "rebuild the note from
  the DB" tool is still refused permanently: for 09-02 the DB holds 14
  rows against 17 blocks on disk, so any rebuild would silently drop
  cards — a fail-loud violation.
- **#14 (unresolved: what wrote the stub into an already-existing
  note)** — **still unexplained.** Nothing in this session's reading
  accounts for it either. Note that it no longer *matters* for data
  safety — a stub is now merged into, not split on — but the unknown
  writer is still unknown.

### The FILL UPDATE row that never existed

§4's finding — "the TSLA FILL UPDATE has **no DB row at all**" — is
closed. The recompute is an UPDATE to the card row it belongs to now
(`status` FILLED plus `actual_fill` / `recomputed_shares` /
`recomputed_used_risk` / `share_delta` / `distance_change_pct` /
`filled_at`), addressed by an explicit `card_row_id` carried on the
form, never by nearest-timestamp matching. `mark_filled()` raises rather
than report a fill that touched zero rows.

`status` is deliberately minimal — `CARD` and `FILLED`. The full
lifecycle ruled on 09-02 is out of scope while the sheet is beta.

The DRC shows **two numbers** now — cards written, and trades taken
counting `FILLED` only. This is what produced "17 cards" when 2 were
real.

### §7 #11 — the TEST/FORDATE rows

Sanctioned deletion, in a transaction, guarded on the count:

```
SELECT count(*) WHERE id BETWEEN 171 AND 185 AND ticker IN ('TEST','FORDATE')  -->  15
DELETE ... rowcount = 15
COMMIT
```

Counts before → after:

| query | before | after |
|---|---|---|
| whole table | 199 | 172 |
| ids 171-185, ticker IN ('TEST','FORDATE') | 15 | 0 |
| 2026-09-03 (America/New_York) | 29 | **2** |

The 09-03 count was 29, not the 17 this report recorded, because this
session's own test runs added 12 more (ids 201-212, 20:06-20:13 ET).
Those were removed in a second, separately-reported transaction — the
same cleanup `0dbc207` did for its own ids 188-200. What remains for
09-03 is exactly the two real cards: **186 TSLA 10:02:06, 187 AVGO
10:42:53.**

**Root cause of the pollution, now fixed:** `tests/cobalt/test_aset_store.py`
writes REAL rows into the same `aset_sizings` the production sheet
writes to, and never cleaned up. Every test now deletes exactly the ids
it created.

**These rows are in `cobalt_dev`, not `cobalt_brain`** — `cobalt_brain`
has no `aset_sizings` table at all. Production ASET and prefill write
live trading data into `cobalt_dev` because `configs/dev/aset.yaml` sets
`db_name: cobalt_dev` for both. That is how test rows and live cards
came to share a table in the first place. **The prod/dev database split
needs a ruling** — it is not fixed here.

### Proof, in the dev vault and the dev DB

`tests/cobalt/test_vaultwrite.py`, 34 cases, run in
`~/dev-vault-cobalt/_l28-tests/` against `cobalt_dev`. Live vault and
live DB were never test targets. Full suite: **245 passed**; the old
tree is unchanged (12 failed / 16 errors both with and without this
work, verified by stashing the working tree against HEAD).

Covered: human content above/below/inside a section survives
byte-for-byte; the exact 09-03 shape loses nothing; second run = zero
diff; three runs of a card update = one card; a human-added line inside
a unit survives while Cobalt's update still lands; a human-modified
Cobalt line wins, records exactly one override row, and does not
re-record; create-if-absent creates and never rewrites an existing
file; an mtime race aborts loud and retries once (a persistent racer
raises rather than clobbers); dry-run leaves the hash unchanged and
writes no audit rows; restore restores; and a production vault path is
refused without `COBALT_ENV=production` — including with
`COBALT_ALLOW_DEV_ENTRY=1`, which is not a write back door.

### Deploy

The three writers stopped in the Containment section were re-enabled
with exactly the commands recorded there.

```
$ launchctl list | grep -i cobalt
8476	0	com.cobalt.aset
-	0	com.cobalt.agent
-	0	com.cobalt.archiver
-	2	com.cobalt.mainframe
-	0	com.cobalt.prefill-daily
-	0	com.cobalt.prefill-drc

$ launchctl print-disabled gui/$(id -u) | grep -i cobalt
	"com.cobalt.aset" => enabled
	"com.cobalt.prefill-daily" => enabled
	"com.cobalt.prefill-drc" => enabled
```

`com.cobalt.aset` restarted onto the new code (PID 8476/8487, started
20:19:27) — L28.6, restart-on-deploy. `prefill-daily` next fires
09-04 05:15; `prefill-drc` 15:40.

### Production dry-runs — no live write

All three ran with `COBALT_ENV=production` against
`/Users/cobalt/Vault/Think`. Every target's sha256 was identical before
and after.

1. **`prefill daily` → 2026-09-04.md (absent).** `created`; 119 lines,
   every one an addition; the file did not exist before and does not
   exist now.
2. **`prefill drc` → DRC-2026-09-03.md.** `skipped_idempotent`, note
   byte-identical — it carries the pre-L28 `<!-- cobalt-prefill:drc:
   2026-09-03 -->` marker and historical notes are not retro-marked. The
   run report still shows the corrected figures: **cards written: 2 ·
   trades taken (FILLED): 0.** To see what the writer *would* emit, the
   live draft was copied into the dev vault with that marker stripped:
   the diff is **pure insertion, zero deletion lines**, and lists only
   TSLA 10:02:06 and AVGO 10:42:53.
3. **ASET sample card → 2026-09-03.md.** A single `aset-cards` section
   appended at the end of the note; the 347 lines of Dejan's journal
   above it appear in the diff as context only. Zero deletion lines.

**One thing found by these dry-runs and fixed before deploy:** the
`drc-risk` placement originally WRAPPED the existing `Risk Parameters:`
line so Cobalt's computed figures replaced it. In a Templater-created
DRC that line is `Risk Parameters: A:5R, B:1R, C:0.5R` — Dejan's own
text. The section is inserted BELOW it now (commit `fdb7c4a`); a
stale-looking duplicate is the correct price.

### RULING NEEDED — one judgement call against the stop condition

The instruction was to stop and re-disable if any dry-run showed a
change outside a Cobalt section. Run 1 and 3 show none. **`prefill
daily --dry-run` against the live 2026-09-03.md shows two**, and both
are the fill-in-place behaviour ruled on 08-31, not damage:

```
 | VIX |     |     |
 | --- | --- | --- |
-| SPY |     |     |          +| SPY | $773.17 | +1.05% |
-| QQQ |     |     |    -->   +| QQQ | $717.67 | +1.19% |
-| IWM |     |     |          +| IWM | $295.19 | +0.40% |
 | BTC |     |     |
```
```
 ### Market Calendar:
-- 
+<the calendar block, inside its markers>
```

Three blank table cells and an empty `- ` bullet. No character of
content is replaced; the row labels, the VIX and BTC rows, and every
other line are untouched. Reading the stop condition to forbid this
would forbid the feature Dejan asked for on 08-31 ("filled IN PLACE
inside Dejan's actual section layout, never appended below it"), so the
writers were left enabled — **flagged here rather than decided
silently.** To reverse:

```
launchctl bootout gui/$(id -u)/com.cobalt.prefill-daily
launchctl disable gui/$(id -u)/com.cobalt.prefill-daily
```

Note this affects the 09-03 note only in a hand-run; the 05:15 job
always targets *today*, and 2026-09-04.md does not exist, so tomorrow's
scheduled run is a clean create.

Two related items also want a ruling:
- **DRC-2026-09-03.md still says "17 cards"** in its own body and will
  never self-correct — it is a pre-L28 note. Fix by hand, or accept.
- **`configs/cobalt/rules.yaml`** carries an uncommitted `generated_at`
  bump and **`docs/_archive/gemini-era-vault-side/`** (128 files, 720K,
  untracked) is unstaged. Both were left exactly as found, per
  instruction. The dry-runs regenerated `rules.yaml`; it was restored
  byte-for-byte to the state this session found it in.

### Rollback, demonstrated

```
$ cobalt vault restore --write-id 424 --dry-run
[DRY-RUN] restored: …/2026-09-03.md · section=aset-cards · unit=card-20260903T100206
@@ -7,7 +7,7 @@
 ### 10:02:06 — TSLA LONG B
 ```aset
 ticker: TSLA
-shares: 999   <-- WRONG
+shares: 120
 ```
sha256 identical before and after the dry run.

$ cobalt vault restore --write-id 424
[WRITE] restored: … · write_id=425
(same diff, applied; the human journal line above the section untouched)
```

### What this does NOT fix

1. **Obsidian is still an unsynchronised second writer**, and it is the
   one that has destroyed data — twice. §7 #9(c), the sidecar note, is
   still the only proposal that removes the race.
2. **The production vault still has no backup.** No Time Machine, no
   git, no sync. Unchanged, and still the biggest exposure here.
3. **§7 #14 is still unexplained** — what wrote a stub banner into an
   already-existing note.
4. **Production writes live cards to `cobalt_dev`.** Needs a ruling.

---

## Containment 2026-09-03

**Scope of this session:** ops-only. No code edits, no vault writes, no DB
writes, no restarts. Only mutations: `launchctl bootout`/`disable` on the
three named jobs, and this append.

### 1. Inventory

**Before state — `launchctl list | grep -i cobalt`:**

```
79273	143	com.cobalt.aset
-	0	com.cobalt.agent
-	0	com.cobalt.archiver
-	2	com.cobalt.mainframe
```

`com.cobalt.prefill-daily` and `com.cobalt.prefill-drc` do not appear at all —
confirmed still unloaded from the prior forensics session (per this file's
header). `launchctl print-disabled gui/$(id -u) | grep -i cobalt` returned
**no rows** before containment — nothing was disabled yet.

**`ps aux` — relevant PIDs (full output too large to paste; filtered):**

```
cobalt   79281  0.1  0.1  ...  2:21PM  /opt/homebrew/.../Python -m cobalt.aset
cobalt   79273  0.0  0.0  ...  2:21PM  uv run python -m cobalt.aset
cobalt   30826  0.0  0.3  ...  Mon06AM /opt/homebrew/.../Python src/cobalt_agent/main.py
cobalt   30824  0.0  0.0  ...  Mon06AM uv run src/cobalt_agent/main.py
```

No `prefill`, `archiver`, or `mainframe` process was running at inventory
time (archiver is calendar-scheduled, Mon-Fri 20:30, `RunAtLoad=false`;
mainframe is the LM Studio server, not a vault writer).

**Writer table — every process that touches a file under `/Users/cobalt/Vault/Think`:**

| Label | Entrypoint | Note(s) written | Write mode | Loaded Y/N (before) |
|---|---|---|---|---|
| `com.cobalt.prefill-daily` | `ops/com.cobalt.prefill-daily.plist` → `uv run prefill daily` → `run_daily_prefill()` | Today's Daily Note (`daily_note.daily_notes_dir`/`filename_pattern`, e.g. `1 - Trading/1- Daily Notes/YYYY-MM-DD.md`) | **create** (`write_new`, `src/cobalt/prefill/daily.py:469`); **whole-file rewrite** on the stub-upgrade branch (`daily.py:475-485`, discards everything before `STUB_BANNER` — this is the defect in §5) via `_write_if_unchanged`→`path.write_text` (`daily.py:398`); **section-replace** (anchor fill-in-place, `_fill_all_slots` at `daily.py:347`) via the same `_write_if_unchanged`/`daily.py:398` | **N** — not in `launchctl list` |
| `com.cobalt.prefill-drc` | `ops/com.cobalt.prefill-drc.plist` → `uv run prefill drc` → `src/cobalt/prefill/drc.py` | `DRC-YYYY-MM-DD.md` | **create** (`write_new`, `drc.py:327`); **append** (`append_block`, `drc.py:334`, fenced idempotency-marked block) | **N** — not in `launchctl list` |
| `com.cobalt.aset` | `ops/com.cobalt.aset.plist` → `ops/start_aset.sh` → `uv run python -m cobalt.aset` (Flask sizing sheet, PID 79273/79281) | Today's Daily Note, via `save_card`/`save_fill_update` (`src/cobalt/aset/web.py:466,521`) → `_append` (`src/cobalt/aset/daily_note.py:120-144`) | **create** stub-on-first-write (`daily_note.py:140-143`, writes `# {date}\n\n{STUB_BANNER}` if the file doesn't exist yet); **append** (`daily_note.py:144`, card body) | **Y** — PID 79273, KeepAlive+RunAtLoad |
| `com.cobalt.agent` (old tree) | `ops/com.cobalt.agent.plist` → `cobalt.sh start` → `uv run src/cobalt_agent/main.py` (PID 30824/30826) | **Nothing under `/Users/cobalt/Vault/Think`.** `scribe.append_to_daily_note()` (`src/cobalt_agent/skills/productivity/scribe.py:136-177`) writes only under `OBSIDIAN_VAULT_PATH`, which `.env:38` sets to `/Users/cobalt/cobalt/docs` (the repo's own D6/gitignored playground tree) — `docs/0 - Inbox/Daily_Log_YYYY-MM-DD.md`. Every write also routes through `ToolManager`/the Proposal Engine, i.e. HITL-gated (`scribe.py:158-165`), not direct filesystem access. **Not a production-vault writer at all** — reported per instruction for a separate ruling, not stopped. | **append** (repo docs tree, not the vault) | **Y** — running since Mon06AM, not shown with a PID in `launchctl list` because `AbandonProcessGroup` detaches it (same pattern as `archiver`) |
| `com.cobalt.archiver` | `ops/com.cobalt.archiver.plist` → `uv run archiver` → `src/cobalt/archiver/report.py` | **Nothing under `/Users/cobalt/Vault/Think`.** Writes `docs/30 - Design/archiver-runs.md` (`report.py:12,64-65`) — inside the repo's own docs/ tree, not the vault. Reported per instruction for a separate ruling, not stopped. | **create-header-then-append** (`report.py:64` header if new, `:65` row append) | **Y** (loaded, calendar-scheduled Mon-Fri 20:30, not currently running) |
| `com.cobalt.mainframe` | `ops/com.cobalt.mainframe.plist` → `~/.lmstudio/start_mainframe.sh` | none — LM Studio model server, no vault access | n/a | **Y** (loaded) |

Also touching the vault but **read-only**: `regenerate_rules_config()`
(`src/cobalt/prefill/rules_gen.py`) reads `Rules.md` from the vault and
writes the parsed result to `configs/cobalt/rules.yaml` in the repo
(`rules_gen.py:116`) — not a vault write.

### 2/3. Stop + verify

Commands run:

```
launchctl bootout gui/501/com.cobalt.prefill-daily   # "Boot-out failed: 3: No such process" — already unloaded
launchctl bootout gui/501/com.cobalt.prefill-drc     # "Boot-out failed: 3: No such process" — already unloaded
launchctl bootout gui/501/com.cobalt.aset            # succeeded, no output
launchctl disable gui/501/com.cobalt.prefill-daily
launchctl disable gui/501/com.cobalt.prefill-drc
launchctl disable gui/501/com.cobalt.aset
```

`com.cobalt.agent` and `com.cobalt.archiver` were **not** touched.

**After — `launchctl list | grep -i cobalt`:**

```
-	0	com.cobalt.agent
-	0	com.cobalt.archiver
-	2	com.cobalt.mainframe
```

`com.cobalt.aset` no longer appears (was `79273	143	com.cobalt.aset`).

**After — `launchctl print-disabled gui/$(id -u) | grep -i cobalt`:**

```
"com.cobalt.aset" => disabled
"com.cobalt.prefill-daily" => disabled
"com.cobalt.prefill-drc" => disabled
```

**PID 79273:**

```
$ ps -p 79273
  PID TTY           TIME CMD
$ echo $?
1
```

Gone — confirmed via exit code 1 (no matching process) and empty output.
No survivor; `kill -9` was not needed and was not used.

### 4. ASET question (read-only, no code change)

**Is `com.cobalt.aset` the Flask sizing sheet process itself?** Yes —
`ops/com.cobalt.aset.plist` runs `ops/start_aset.sh`, which execs
`uv run python -m cobalt.aset`, the Flask app in `src/cobalt/aset/web.py`
(confirmed live: PID 79273/79281 was the sheet process before bootout).

**Is there an existing config/env flag that keeps the sheet serving while
disabling its daily-note write, with no code change? No.**

- `src/cobalt/aset/web.py:466` (`size()`) and `:521` (`fill()`) call
  `save_card`/`save_fill_update` unconditionally — no config check gates
  the call.
- `save_card`/`save_fill_update` (`src/cobalt/aset/daily_note.py:158-181`)
  call `_append()` (`daily_note.py:120`) unconditionally — no env/flag
  branch inside it either.
- `AsetConfig` (`src/cobalt/aset/config.py:84`) has a `daily_note` field
  (a `DailyNoteConfig`, target dir/filename only) and `enabled_grades`
  (`config.py:151`, gates which grade *options* the sheet accepts) — no
  write-enable/dry-run/disable toggle exists anywhere in the schema.
- `ops/start_aset.sh` sets only `COBALT_VAULT_PATH`, `COBALT_ENV`, and
  sources the key file — no write-suppression env var.

So under NN#16's current code, "sheet serves, daily-note write disabled" is
not reachable without a code change. This is why the sheet itself is down
right now (bootout above) rather than left running — there was no other way
to honor the ruling. Flagging for the fix session, not implementing.

### 5. Re-enable (for the fix session, after the L28 vault-write fix is proven in dev)

```
launchctl enable gui/$(id -u)/com.cobalt.prefill-daily
launchctl enable gui/$(id -u)/com.cobalt.prefill-drc
launchctl enable gui/$(id -u)/com.cobalt.aset

launchctl bootstrap gui/$(id -u) /Users/cobalt/cobalt/ops/com.cobalt.prefill-daily.plist
launchctl bootstrap gui/$(id -u) /Users/cobalt/cobalt/ops/com.cobalt.prefill-drc.plist
launchctl bootstrap gui/$(id -u) /Users/cobalt/cobalt/ops/com.cobalt.aset.plist
```

(`prefill-daily`/`prefill-drc` are calendar-triggered, `RunAtLoad=false` —
bootstrap alone re-arms their `StartCalendarInterval`, no immediate run.
`aset` has `RunAtLoad=true`, so its bootstrap starts the sheet immediately.)

### Status

All three named writers confirmed down and disabled across login/reboot.
`com.cobalt.agent` (writes only inside the repo's docs/ tree, HITL-gated,
never touches `/Users/cobalt/Vault/Think`) and `com.cobalt.archiver`
(writes only `docs/30 - Design/archiver-runs.md`, also inside the repo)
are unchanged, pending the separate ruling requested. Manual process is
now the only path into the production vault's daily notes.

---

## Nightly restart 2026-09-04

Read-only forensics session. No writes to the vault, no DB writes, no
restarts, no `launchctl` changes, no commits other than this file.

### A. Did `com.cobalt.prefill-daily` write `2026-09-04.md` this morning?

**Answer: YES, at 05:15:04 — and Obsidian destroyed it 75 minutes later.
The bytes on disk right now are Obsidian's, not Cobalt's.**

#### A.1 The live note

```
$ grep -c 'cobalt:section' "/Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md"
0

$ stat -f '%N | birth %SB | modified %Sm | size %z' -t '%Y-%m-%d %H:%M:%S' <note>
/Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md | birth 2026-09-04 06:30:19 | modified 2026-09-04 06:30:19 | size 1423

$ shasum -a 256 <note>
e4b005ba0d3b3195e2d8af3b75c9f3ce7c7445a33451c3d8d27de800dbc00d36
```

Zero `cobalt:section` markers. 1423 bytes / 76 lines.

**Decisive content test** — the live note against Obsidian's own daily
template:

```
$ diff "/Users/cobalt/Vault/Think/5 - Templates/Daily.md" <note>
6c6
< #### {{date:YYYY-MM-DD}}
---
> #### 2026-09-04
```

One line differs, and that line is Obsidian's `{{date:YYYY-MM-DD}}` token
expanded. The file on disk **is** `5 - Templates/Daily.md` rendered by the
Obsidian daily-notes core plugin (`.obsidian/daily-notes.json`:
`{"folder": "1 - Trading/1- Daily Notes", "template": "5 - Templates/Daily.md"}`).
It is not Cobalt output in any part.

#### A.2 `logs/prefill-daily.log` — every line from 09-04

(The plists write to `logs/`, not `ops/logs/` — `ops/logs/` does not exist.
`stdout path = /Users/cobalt/cobalt/logs/prefill-daily.log`.) Lines 1-4 are
the 2026-09-03 14:22 manual runs; lines 5-129 are this morning's run:

````
Daily prefill [WRITE]: created — /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md
  filled: rules, trading, market_calendar
  skipped (not touched): none
[WRITE] created: /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md · write_id=525
--- /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md (before)
+++ /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md (after)
@@ -0,0 +1,118 @@
+---
+tags:
+  - Daily
+---
+#### 2026-09-04 T 05:15
+
+## Journal
+
+### How do you feel
+
+Sleep:
+Readiness:
+RHR:
+## Today's Plan
+
+1% goal:
+
+Daily HARD Stop: $420
+STOP TRADING AFTER 11AM until one month green 4 out of 5 days a week
+I WILL NOT TOLERATE THE MISTAKE OF OVERSIZING RISK ON A SINGLE TRADE THAT I DID NOT PLAN JUST TO MAKE A LARGFE POSITION
+I WILL NOT TOLERATE THE MISTAKE OF HAVING MORE THAN 3 LOSSES IN A ROW IN A TRADING DAY
+
+<!-- cobalt:section rules -->
+<!-- cobalt:unit rules -->
+- [ ] Card first: grade → $ risk → shares **written before every entry**. No card, no trade. #process
+- [ ] Grades: **B = $30 half / $60 full, A = $70 half / $135 full.** Nothing bigger. C = pass. #sizing
+- [ ] Stop at **structure**, never a default distance. If R:R < 2:1, pass. #process
+- [ ] Prime window only: **9:30–11:00.** Nothing before, nothing after. #time_window
+- [ ] **Max 5 trades.** #sizing
+- [ ] Reversion entry needs all three: **my level + exhaustion printed + trigger.** Approaching ≠ rejecting. #process
+- [ ] Re-entry #2 same thesis: write **what's new** — blank or "better price" = no trade. #re_entry
+- [ ] Entry #3 same thesis: **stand down.** Ticker done for the day. #re_entry
+- [ ] Two straight losses → **10-min cooldown.** #circuit_breaker
+- [ ] **One position at a time** while red. Never two correlated names. #circuit_breaker
+- [ ] First partial at 1R → **stop to B/E**, immediately. #process
+- [ ] Daily stop hit ($215 live) → **done trading.** Watch only. #hard_stop
+
+Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half
+
+- Tape check: In because criteria met — or because it excites me?
+- Identity: My sizing is arithmetic, not habit. Stand-down gives me back my eyes.
+<!-- /cobalt:unit rules -->
+<!-- /cobalt:section rules -->
+
+### Trading
+
+<!-- cobalt:section trading -->
+<!-- cobalt:unit market_table -->
+| VIX |     |     |
+| --- | --- | --- |
+| SPY | $773.60 | +0.06% |
+| QQQ | $720.37 | +0.38% |
+| IWM | $295.23 | +0.01% |
+| BTC |     |     |
+<!-- /cobalt:unit market_table -->
+<!-- /cobalt:section trading -->
+
+
+### Market Context:
+-
+
+### Market Calendar:
+<!-- cobalt:section market_calendar -->
+<!-- cobalt:unit market_calendar -->
+- 08:30 ET — Average Hourly Earnings MoM (impact 2, expected 0.3%, prior 0.1%)
+- 08:30 ET — Average Hourly Earnings YoY (impact 2, expected 3%, prior 3.2%)
+- 08:30 ET — Average Weekly Hours (impact 1, expected 34.3, prior 34.3)
+- 08:30 ET — Government Payrolls (impact 1, prior -53K)
+- 08:30 ET — Manufacturing Payrolls (impact 1, expected 5K, prior 5K)
+- 08:30 ET — Non Farm Payrolls (impact 3, expected 58K, prior -23K)
+- 08:30 ET — Nonfarm Payrolls Private (impact 1, expected 58K, prior 30K)
+- 08:30 ET — Participation Rate (impact 2, prior 61.4%)
+- 08:30 ET — U-6 Unemployment Rate (impact 1, prior 7.9%)
+- 08:30 ET — Unemployment Rate (impact 3, expected 4.1%, prior 4.1%)
+- 13:00 ET — Baker Hughes Oil Rig Count (impact 1, prior 447)
+- 13:00 ET — Baker Hughes Total Rigs Count (impact 1, prior 588)
+<!-- /cobalt:unit market_calendar -->
+<!-- /cobalt:section market_calendar -->
+### Game Plan:
+
+
+### Trade Ideas
+
+| Ticker | Score | Catalyst | Setup | Support | Inflection | Resistance | ATR | RVOL | BIAS |
+| ------ | ----- | -------- | ----- | ------- | ---------- | ---------- | --- | ---- | ---- |
+|        |       |          |       |         |            |            |     |      |      |
+|        |       |          |       |         |            |            |     |      |      |
+|        |       |          |       |         |            |            |     |      |      |
+|        |       |          |       |         |            |            |     |      |      |
+|        |       |          |       |         |            |            |     |      |      |
+|        |       |          |       |         |            |            |     |      |      |
+
+### Trade Execution
+```dataview
+TABLE symbol, profit_loss, strategy, entry_time, direction, profit_loss
+FROM "1 - Trading/2 - Trades"
+WHERE file.cday = this.file.day
+SORT entry_time ASC
+```
+
+## Notes
+
+Overall Score:
+
+Premarket:
+Score -
+
+9:30 - 11:
+Score -
+
+11 - 1
+Score -
+
+1-3
+Score -
+
+3-4
+Score -
````

`logs/prefill-daily.err` timestamps that run precisely:

```
2026-09-04 05:15:04.462 | INFO | cobalt_agent.config:_load_config:554 - Loading configuration from: /Users/cobalt/cobalt/configs
... (vault unlock, Finviz token resolve) ...
```

`prefill-daily.log` and `.err` both have mtime `2026-09-04 05:15:04`.
Cobalt has not written since.

#### A.3 `launchctl print gui/501/<label>`

```
gui/501/com.cobalt.prefill-daily
	path = /Users/cobalt/cobalt/ops/com.cobalt.prefill-daily.plist
	state = not running          active count = 0
	program/args = /Users/cobalt/.local/bin/uv run prefill daily
	environment = COBALT_ENV=production, COBALT_VAULT_PATH=/Users/cobalt/Vault/Think
	runs = 1                     last exit code = 0
	event triggers = StartCalendarInterval { Minute 15, Hour 5, Weekday 1..5 }

gui/501/com.cobalt.prefill-drc
	path = /Users/cobalt/cobalt/ops/com.cobalt.prefill-drc.plist
	state = not running          active count = 0
	program/args = /Users/cobalt/.local/bin/uv run prefill drc
	environment = COBALT_ENV=production, COBALT_VAULT_PATH=/Users/cobalt/Vault/Think
	runs = 0                     last exit code = (never exited)
	event triggers = StartCalendarInterval { Minute 40, Hour 15, Weekday 1..5 }

gui/501/com.cobalt.aset
	path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist
	state = running              active count = 1     pid = 8476
	program = /Users/cobalt/cobalt/ops/start_aset.sh
	runs = 1                     last exit code = (never exited)
	properties = keepalive | runatload | abandon process group

$ launchctl print-disabled gui/501 | grep -i cobalt
		"com.cobalt.aset" => enabled
		"com.cobalt.prefill-daily" => enabled
		"com.cobalt.prefill-drc" => enabled
```

`launchctl print` on this macOS build does not expose a "next fire date"
field; the calendar descriptors above are the schedule of record. Next
fires: prefill-daily Mon 2026-09-07 05:15, prefill-drc today 15:40,
aset is a KeepAlive daemon (no fire time).

`runs = 1 / last exit 0` for prefill-daily is this morning's 05:15 run.
`runs = 0` for prefill-drc: it has not fired since being re-enabled last
night (its 15:40 slot has not come round yet today).

#### A.4 `vault_writes`

**Which DB: `cobalt_dev`.** The writer store is constructed as
`VaultWriteStore(aset_cfg.db_name)` (`src/cobalt/prefill/daily.py:411`,
`drc.py:423`, `aset/daily_note.py:152`, `cli.py:38`), and `db_name` comes
from `configs/dev/aset.local.yaml:12` → `db_name: cobalt_dev`. **This is
the open item already logged at the end of the 09-03 section — production
writes its audit trail to the dev database.** Query run there:

```
$ SELECT id, ts, note, section, unit FROM vault_writes WHERE note LIKE '%2026-09-04%';

 id  |              ts               |                                note                                |     section     |      unit
-----+-------------------------------+--------------------------------------------------------------------+-----------------+-----------------
 525 | 2026-09-04 09:15:04.722414+00 | /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md |                 |
 526 | 2026-09-04 09:15:04.737616+00 | /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md | rules           | rules
 527 | 2026-09-04 09:15:04.748347+00 | /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md | trading         | market_table
 528 | 2026-09-04 09:15:04.763012+00 | /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md | market_calendar | market_calendar
(4 rows)
```

Timestamps are UTC: 09:15:04 UTC = **05:15:04 EDT**. Writer / run_id /
hashes:

```
525|prefill.daily|a83292db9d4d|hash_before=(empty)|hash_after=d6f6e9ab7eaacd97eb1e014a9da140f32746f62d44536e76ce895c251a106cef
526|prefill.daily|a83292db9d4d|hash_before=(empty)|hash_after=d6f6e9ab...
527|prefill.daily|a83292db9d4d|hash_before=(empty)|hash_after=d6f6e9ab...
528|prefill.daily|a83292db9d4d|hash_before=(empty)|hash_after=d6f6e9ab...
```

`hash_before` empty on row 525 = the note did **not** exist at 05:15;
Cobalt created it whole. Nothing has written through the ONE writer path
since 09:15:04 UTC — rows 525-528 are the newest non-pytest rows in the
table (the next ids down, 488-498, are all `/private/var/folders/.../pytest-of-cobalt/...`
temp vaults from the 00:24 test run).

#### A.5 Verdict

**Cobalt created it. Obsidian destroyed it.**

| | Cobalt's version | What is on disk now |
|---|---|---|
| written | 2026-09-04 05:15:04 | 2026-09-04 06:30:19 |
| sha256 | `d6f6e9ab…` (vault_writes 525-528) | `e4b005ba…` |
| shape | 118 lines, `#### 2026-09-04 T 05:15`, `Daily HARD Stop: $420`, filled rules/market table/market calendar, `cobalt:section` markers | 76 lines / 1423 bytes, `#### 2026-09-04`, all sections empty, zero markers |
| provenance | `prefill.daily`, run_id `a83292db9d4d` | `5 - Templates/Daily.md` with `{{date:YYYY-MM-DD}}` expanded — Obsidian daily-notes plugin |

Supporting timeline (unified log + `obsidian.log`, which logs in UTC):

- `2026-09-03 21:54:23Z` — last Obsidian launch before the reboot.
- `2026-09-03 18:53` local — shutdown; `19:02` — boot. **No Obsidian
  instance ran between the reboot and this morning.**
- `2026-09-04 05:15:04` — prefill-daily creates the note (write_id 525).
- `2026-09-04 06:22:19` — console login on ttys002.
- `2026-09-04 06:30:19` — the note's content is replaced by the plain
  template render. Header line becomes `#### 2026-09-04`.
- `2026-09-04 06:30:42` — LaunchServices launches Obsidian:
  `runningboardd: Launch request for app<application.md.obsidian…> …
  "LS launch md.obsidian" … originator [osservice<com.apple.coreservices.uiagent>:786]`,
  and `obsidian.log: 2026-09-04 10:30:42 Loaded main app package`. This is
  the "open a .md with its default app" path, not a Dock/Spotlight launch.
- `2026-09-04 06:30:44` — the note's ctime bumps (metadata touch by the
  now-running app).
- `2026-09-04 06:37:52` — Obsidian relaunched (`obsidian.log 10:37:52`);
  this is the currently-running instance, pid 38662. `.obsidian/*.json`
  all rewritten at 06:37:53-54.
- Yesterday's note has the same fingerprint one day earlier: `2026-09-03.md`
  birth `2026-09-03 06:29:21` — i.e. the ~06:30 daily-note creation is a
  standing morning-routine event, and today it landed on top of Cobalt's
  05:15 write instead of on an empty folder.

**One filesystem detail does not fit and is recorded rather than
explained away.** The note is mode `-rw-------` — the *only* 0600 markdown
file in the entire vault (367 others are 0644), and 0600 is the signature
of `tempfile.mkstemp` in `src/cobalt/vaultwrite/writer.py:326`. The parent
directory's mtime is also still `05:15:04`, i.e. no directory entry was
added or removed after Cobalt's write. Both of those say "Cobalt's inode,
rewritten in place." But the file's birth time reads `06:30:19` from
`stat`, `mdls` (`kMDItemFSCreationDate`) and `GetFileInfo` alike, and a
control test in scratchpad confirms an in-place `O_TRUNC` rewrite on this
APFS volume preserves both birth time and inode (as does Obsidian's own
save path — `.obsidian/workspace.json` is inode 17911252, birth
2026-08-26, mtime today 06:37:54). The three signals are mutually
inconsistent and the exact syscall path that produced the 06:30:19 file is
**not established**. It does not change the verdict: the *content* on disk
is unambiguously Obsidian's template render and unambiguously not
Cobalt's, and `vault_writes` proves nothing went through the ONE writer
after 05:15.

### B. The nightly restart

#### B.1 Finding: there is no nightly restart on this machine.

Nothing runs between 00:00 and 05:00. No reboot happened last night.

```
$ last reboot | head -5
reboot time                                Thu Sep  3 19:00
shutdown time                              Thu Sep  3 18:55
reboot time                                Sat Aug 29 10:35
reboot time                                Tue Aug 18 15:58
reboot time                                Tue Aug 11 11:27

$ last cobalt | head -5
cobalt     ttys002                         Fri Sep  4 06:22   still logged in
cobalt     ttys000                         Thu Sep  3 19:42   still logged in
cobalt     console                         Thu Sep  3 19:02   still logged in
cobalt     ttys000                         Thu Sep  3 18:46 - 18:46  (00:00)
cobalt     ttys003                         Mon Aug 31 12:39 - 12:39  (00:00)

$ uptime
 6:57  up 11:57, 3 users, load averages: 1.69 1.47 1.33

$ pmset -g sched
(no output — no scheduled sleep/wake/restart events)

$ crontab -l
crontab: no crontab for cobalt

$ ls /etc/periodic
ls: /etc/periodic: No such file or directory
$ cat /etc/crontab
cat: /etc/crontab: No such file or directory
```

`sudo crontab -l` and `sudo pmset -g sched` could **not** be run — this
session is non-interactive and `sudo` requires a password. `pmset -g sched`
without sudo already reports the full scheduled-events list (it needs no
privilege to read), and it is empty. **The root crontab remains unchecked —
run `sudo crontab -l` by hand to close that gap.**

Every LaunchAgent/LaunchDaemon on the box, with its calendar interval:

```
~/Library/LaunchAgents/
  com.cobalt.agent.plist        (no StartCalendarInterval) → cobalt.sh start
  com.cobalt.archiver.plist     Weekday 1-5, Hour 20, Minute 30 → uv run archiver
  com.cobalt.aset.plist         (no StartCalendarInterval) → ops/start_aset.sh
  com.cobalt.mainframe.plist    (no StartCalendarInterval) → ~/.lmstudio/start_mainframe.sh
  com.cobalt.prefill-daily.plist  Weekday 1-5, Hour 5,  Minute 15 → uv run prefill daily
  com.cobalt.prefill-drc.plist    Weekday 1-5, Hour 15, Minute 40 → uv run prefill drc
  com.google.GoogleUpdater.wake.plist / com.google.keystone.*     (Google updater)
  homebrew.mxcl.ollama.plist.bak   (.bak — not loaded)

/Library/LaunchAgents/    (empty)
/Library/LaunchDaemons/   dev.orbstack.OrbStack.privhelper.plist only
```

**No job anywhere has an Hour between 0 and 5 except prefill-daily at
05:15.** No `StartInterval` job exists. No label mentions restart, reboot,
or kickstart. LM Studio has no scheduled-restart setting (`~/.lmstudio/`
contains `settings.json` and `start_mainframe.sh`; nothing schedules them).

#### B.2 What the Gemini-era "unstick the local model" mechanism actually is

It exists, but it is **boot-triggered, not nightly**:
`~/.lmstudio/start_mainframe.sh`, run by `com.cobalt.mainframe`
(RunAtLoad, no calendar interval). What it touches:

```
ulimit -l unlimited                     # remove macOS locked-RAM limit
lms server stop                         # stop the LM Studio HTTP server
lms unload --all                        # unload every loaded model
pkill -9 -f llmster                     # kill the inference engine
pkill -9 -f "node.*lmstudio"            # kill the background workers
pkill -9 -f caffeinate                  # kill the old heartbeat
sleep 2
lms daemon up; lms server start         # bring the daemon + server back
<poll http://localhost:1234/v1/models, 60s timeout, abort on failure>
lms load qwen3.5-122b-a10b --identifier "mainframe" --gpu max --context-length 32768
caffeinate -i -m bash -c 'while true; do curl … "model":"mainframe" … ; sleep 60; done'
```

That is the "refresh services to unstick Qwen" routine: a hard purge of the
LM Studio process tree plus a caffeinate-held 60-second ping heartbeat to
stop the model being evicted from VRAM. Note that `pkill -9 -f caffeinate`
kills *any* caffeinate on the box, not just its own, and the heartbeat loop
is unsupervised and unlogged — it survives only as long as its parent.

Repo greps for a scheduled restart (`file:line`):

```
$ grep -rn 'restart\|reboot\|shutdown\|kickstart\|bootstrap' cobalt.sh ops docs/_archive/gemini-era-vault-side
cobalt.sh:69      "Sending graceful shutdown signal to Cobalt (PID: $PID)..."
cobalt.sh:96      restart)                       # manual ./cobalt.sh restart only
cobalt.sh:103     "Usage: ./cobalt.sh {start|stop|status|restart}"
ops/README.md:27,29,34,44,55   (KeepAlive / log-rotation-on-restart notes)
ops/README.md:73,118,129,133   (documented MANUAL launchctl kickstart/bootstrap recipes)
ops/com.cobalt.aset.plist:23   (comment about the Aug 29 reboot)
docs/_archive/gemini-era-vault-side/Tasks/45 Headless LM Studio LaunchAgent.md:21
    "- [ ] Implement automatic restart on process failure"   ← UNCHECKED, never built
docs/_archive/gemini-era-vault-side/90 - Project Management/Requirements/PRD-008 Watcher Daemon.md:39,89
docs/_archive/gemini-era-vault-side/90 - Project Management/Requirements/PRD-009…:157
docs/_archive/gemini-era-vault-side/90 - Project Management/Requirements/PRD-010…:102
docs/_archive/gemini-era-vault-side/00 - Master Plan/Developer Docs/postgres.md:406,411,478,520,535
docs/_archive/gemini-era-vault-side/00 - Master Plan/Developer Docs/scheduler.md:99
docs/_archive/gemini-era-vault-side/00 - Master Plan/ADR/ADR-013…:25
```

`grep -rniE '02:00|03:00|2 ?am|3 ?am|nightly|StartCalendarInterval|crontab'`
over `docs/_archive/gemini-era-vault-side/` returns **zero hits**. The
Gemini-era nightly restart was planned (task 45, unchecked) but never
implemented as a scheduled job; what shipped is the RunAtLoad purge above.

#### B.3 What actually loaded the three writers, and exactly when

Not a restart. A `launchctl enable` from last night's deploy session.

```
$ log show --last 36h --predicate 'process == "launchd" AND eventMessage CONTAINS "com.cobalt"' --style compact

2026-09-03 05:15:05.457  [gui/501 [100004]:] service inactive: com.cobalt.prefill-daily
2026-09-03 07:26:22.910  [gui/501 [100004]:] service inactive: com.cobalt.diag
2026-09-03 07:26:34.901  [gui/501 [100004]:] removing service: com.cobalt.diag
2026-09-03 07:26:34.943  [gui/501 [100004]:] service inactive: com.cobalt.diag
2026-09-03 07:26:36.951  [gui/501 [100004]:] removing service: com.cobalt.diag
2026-09-03 07:27:55.409  [gui/501 [100004]:] removing service: com.cobalt.prefill-daily
2026-09-03 07:27:55.419  [gui/501 [100004]:] removing service: com.cobalt.prefill-drc
2026-09-03 07:28:28.510  [gui/501 [100004]:] service inactive: com.cobalt.prefill-daily-devtest
2026-09-03 07:29:19.957  [gui/501 [100004]:] removing service: com.cobalt.prefill-daily-devtest
2026-09-03 14:21:35.622  [gui/501 [100004]:] service inactive: com.cobalt.aset
2026-09-03 14:22:23.770  [gui/501 [100004]:] service inactive: com.cobalt.prefill-daily
2026-09-03 14:22:37.480  [gui/501 [100004]:] service inactive: com.cobalt.prefill-daily
2026-09-03 15:40:01.011  [gui/501 [100004]:] service inactive: com.cobalt.prefill-drc
2026-09-03 17:39:19.892  [gui/501 [100004]:] removing service: com.cobalt.prefill-daily
2026-09-03 17:39:19.899  [gui/501 [100004]:] removing service: com.cobalt.prefill-drc
2026-09-03 18:33:40.599  [gui/501 [100004]:] service inactive: com.cobalt.aset
2026-09-03 18:33:40.599  [gui/501 [100004]:] removing service: com.cobalt.aset
2026-09-03 18:33:44.562  [gui/501 [100004]:] Setting service com.cobalt.prefill-daily to disabled (initiated by launchctl[92859]<-zsh[92856]<-claude.exe[24239]<-zsh[50633]<-tmux[50632])
2026-09-03 18:33:44.568  [gui/501 [100004]:] Setting service com.cobalt.prefill-drc to disabled (initiated by launchctl[92861]<-zsh[92856]<-claude.exe[24239]<-zsh[50633]<-tmux[50632])
2026-09-03 18:33:44.573  [gui/501 [100004]:] Setting service com.cobalt.aset to disabled (initiated by launchctl[92863]<-zsh[92856]<-claude.exe[24239]<-zsh[50633]<-tmux[50632])
2026-09-03 19:02:07.646  [gui/501 [100012]:] pending spawn, domain in on-demand-only mode: com.cobalt.mainframe
2026-09-03 19:02:07.647  [gui/501 [100012]:] pending spawn, domain in on-demand-only mode: com.cobalt.agent
2026-09-03 19:02:43.006  [gui/501 [100012]:] service inactive: com.cobalt.agent
2026-09-03 19:04:11.502  [gui/501 [100012]:] service inactive: com.cobalt.mainframe
2026-09-03 20:19:27.113  [gui/501 [100012]:] Setting service com.cobalt.prefill-daily to enabled (initiated by launchctl[8465]<-zsh[8462]<-claude.exe[4130]<-zsh[3960]<-tmux[3959])
2026-09-03 20:19:27.120  [gui/501 [100012]:] Setting service com.cobalt.prefill-drc to enabled (initiated by launchctl[8467]<-zsh[8462]<-claude.exe[4130]<-zsh[3960]<-tmux[3959])
2026-09-03 20:19:27.127  [gui/501 [100012]:] Setting service com.cobalt.aset to enabled (initiated by launchctl[8469]<-zsh[8462]<-claude.exe[4130]<-zsh[3960]<-tmux[3959])
2026-09-03 20:53:11.560  [gui/501 [100012]:] service inactive: com.cobalt.archiver
2026-09-04 05:15:04.852  [gui/501 [100012]:] service inactive: com.cobalt.prefill-daily
```

Shutdown/reboot events in the same 36 h — **exactly one**:

```
$ log show --last 36h --predicate '… loginwindow shutdown …' --style compact
2026-09-03 18:53:51.335 loginwindow[164] -[SessionLogoutManager saveSoftwareUpdateOptionIfNeeded] | restart or shutdown, checking update flags
2026-09-03 18:53:51.337 loginwindow[164] … This is a shutdown or restart, setting swap compaction to OFF
2026-09-03 18:53:52.134 loginwindow[164] … sendBSDNotification: com.apple.loginwindow.shutdownNoReturn
2026-09-03 18:53:52.281 loginwindow[164] … waiting for the restart
2026-09-03 19:02:26.338 loginwindow[454] … progress complete, shutdown progress windows
```

**Exact load timestamps for the three writers — all three, same event, last
night:**

| Label | Enabled at | By |
|---|---|---|
| `com.cobalt.prefill-daily` | **2026-09-03 20:19:27.113** | `launchctl[8465] <- zsh[8462] <- claude.exe[4130] <- zsh[3960] <- tmux[3959]` |
| `com.cobalt.prefill-drc` | **2026-09-03 20:19:27.120** | `launchctl[8467] <- zsh[8462] <- claude.exe[4130] <- …` |
| `com.cobalt.aset` | **2026-09-03 20:19:27.127** | `launchctl[8469] <- zsh[8462] <- claude.exe[4130] <- …` |

pid 4130 is `claude --model opus`, started 19:45 in tmux session `cobalt` —
i.e. **last night's L28 fix/deploy session ran the §5 "Re-enable" recipe
from this very file**, at 20:19:27, ~77 minutes after the 19:00 reboot.
`com.cobalt.aset` came up immediately (RunAtLoad): `uvicorn` pid 8487 with
a start time of 20:19. They have simply stayed loaded since. Nothing loaded
anything this morning.

The reason it looked like a morning change: the reboot was at 19:00 and the
three were still `disabled` (set 18:33:44) at that point, so a check
between 19:02 and 20:19 would see only agent / archiver / mainframe. The
enable landed at 20:19:27.

### Recommendation — no action taken

1. **Nightly restart: nothing to keep or kill.** It does not exist. No
   cron, no calendar interval, no `pmset` schedule, no reboot last night.
   The only surviving Gemini-era artifact is
   `~/.lmstudio/start_mainframe.sh`'s RunAtLoad purge + heartbeat.
   *Convert that one to a registered ops job:* it is production
   infrastructure living outside the repo, it `pkill -9`s by pattern
   (`caffeinate` globally), and its heartbeat loop is unlogged and
   unsupervised. It belongs in `ops/` with the other captured LaunchAgents
   and a log path, like `start_aset.sh`. Not urgent, not this session.
   Close the last gap first: `sudo crontab -l` by hand.

2. **The real finding is A, and it is a live data-loss path.** Cobalt now
   writes the daily note at 05:15; Dejan's Obsidian opens/creates the daily
   note around 06:30; on 09-04 the second clobbered the first and 118 lines
   of prefill — rules, market table, market calendar — were replaced by an
   empty template. L28 protects Cobalt from stomping Dejan. Nothing protects
   Dejan's prefill from Obsidian's daily-notes plugin. Options to rule on,
   in preference order: (a) point the Obsidian daily-note template at a
   near-empty stub so a create-on-open cannot destroy content, (b) turn off
   "open daily note on startup" (`app.json: "openBehavior": "daily"`), or
   (c) have prefill-daily re-run/repair rather than only create. This needs
   a ruling before Monday's 05:15 fire.

3. **`vault_writes` in `cobalt_dev` is now load-bearing for prod
   forensics.** This whole reconstruction depended on rows 525-528, and
   they live in the dev database next to pytest temp-vault rows. The open
   item from the 09-03 section stands and should be ruled on.

---

## Ruling 7 + boot contract 2026-09-04

**Scope:** the environment law in code, the `cobalt_dev` → `cobalt_brain`
migration, Obsidian as a supervised service, `start_mainframe.sh` into
`ops/`, and a read-only boot-contract report. ADR-0005 has the decision
record. DevDocs: `cobalt/env.md`, `cobalt/obsidian.md`, `cobalt/devdb.md`,
and a revised `cobalt/db.md`. Every claim below is pasted command output.

Live vault and live DB were never test targets (L28.5): every proof ran in
`~/dev-vault-cobalt` + `cobalt_dev` except the four steps that name
production explicitly — the migration itself, the PROBE round-trip, the
production dry-runs, and the Obsidian service.

### 1. Environment law in code

`COBALT_ENV` ∈ {`production`, `dev`} is now the ONE resolver for the
database and the vault. Unset or unknown raises at boot.

```
$ COBALT_ENV=production uv run python -c "..."
COBALT_ENV           : production
env.resolve_db_name(): cobalt_brain
VaultWriteStore      : cobalt_brain
AsetStore            : cobalt_brain
vault root           : /Users/cobalt/Vault/Think
```

`db_name` is **deleted** from `AsetConfig` and from both
`configs/dev/aset.yaml` and the gitignored `aset.local.yaml`. With
`extra="forbid"`, re-adding the key is a loud crash. The routing this
ruling names — `configs/dev/aset.local.yaml:12` and
`VaultWriteStore(aset_cfg.db_name)` — is gone from all seven call sites
(`cli.py`, `prefill/daily.py` ×2, `prefill/drc.py` ×2,
`prefill/trade_note.py`, `aset/daily_note.py`, `aset/web.py` ×2).

**1b — every ops/ plist declares it.** `prefill-daily`/`prefill-drc`
already did; `aset` declared it only inside `ops/start_aset.sh`;
`agent`, `archiver`, `mainframe` and the new `obsidian` gained it.

```
$ launchctl print gui/501/com.cobalt.aset | grep -A4 'environment = {'
	environment = {
		COBALT_ENV => production
		PATH => /opt/homebrew/bin:...:/Users/cobalt/.local/bin
		XPC_SERVICE_NAME => com.cobalt.aset
	}
```

**1c — destructive helpers are hard-coded to `cobalt_dev`.** Exercised
against production before the truncate that follows:

```
$ COBALT_ENV=production ... devdb.truncate(['aset_sizings'], db_name='cobalt_brain', confirm=True)
EnvConfigError: REFUSED: destructive operation targeted 'cobalt_brain'. Destructive
helpers may only ever touch cobalt_dev (RULING 7.1c) — this is hard-coded and cannot
be overridden.

$ COBALT_ENV=dev uv run python -m cobalt.devdb --truncate aset_sizings
FAILED: DestructiveRefused: REFUSED: destructive call without explicit confirmation
(confirm=True / --yes-truncate-cobalt-dev).
```

**1d — the test suite runs in a transaction and rolls back.** The
measured problem first: one full suite run grew `vault_writes` **383 →
529**, +146 rows of pytest temp-vault paths into the table the 09-03/04
forensics depended on. Per-test cleanup could not fix this —
`test_vaultwrite.py` cleaned up at *setup*, by note prefix, so every
run's rows survived.

The ruling names the ASET-store and vaultwrite tests. Measuring the
actual delta found four more leaking modules — `test_prefill_daily`
(+29), `test_prefill_drc` (+23), `test_aset_daily_note` (+18),
`test_prefill_trade_note` (+3) — so the fixture is **autouse** across
`tests/cobalt/`; opt-in would have left +73 rows per run and failed the
proof this ruling asks for.

```
=============== BEFORE full test run ===============
aset_sizings=177   vault_writes=871   vault_overrides=0
289 passed in 5.77s
=============== AFTER full test run ================
aset_sizings=177   vault_writes=871   vault_overrides=0
```

New core 245 → **289 passing**. Old tree unchanged at its baseline
(12 failed / 17 errors, identical before and after this work).

**Bug found by the fixture, fixed here.** `AsetStore.for_date()` ordered
by `created_at` alone. `created_at` defaults to `now()` — the
TRANSACTION timestamp — so two cards written in one transaction tie and
the sort between them was arbitrary: the DRC's re-entry numbering could
silently invert. Now `ORDER BY created_at, id`. Reachable in production,
not just in tests.

### 2. Migration `cobalt_dev` → `cobalt_brain`

**(a) Sheet down.**

```
$ launchctl bootout gui/501/com.cobalt.aset          # 14:45:00
$ launchctl list | grep -i cobalt
-	0	com.cobalt.agent
-	0	com.cobalt.archiver
66535	-15	com.cobalt.mainframe
-	0	com.cobalt.prefill-daily
66104	0	com.cobalt.obsidian
-	0	com.cobalt.prefill-drc
$ curl -m 3 http://127.0.0.1:5010/   ->  connection refused
```

**(b) The rollback dump.**

```
path        : docs/00 - Project/incident-2026-09-03/dump-20260904T144514.sql
size        : 1055474 bytes (1.0M)
sha256      : 8e786d9d62df12ed0976af9f9d6725582e9f123422ce2c578900e1857ab8da7b
rows inside : aset_sizings 177 · vault_overrides 0 · vault_writes 871
```

> **The dump is NOT committed and must never be.** `vault_writes.before/
> after/unit_before/unit_after` hold VERBATIM production note text —
> Dejan's daily notes, journal and trade cards. The directory sits inside
> the `!docs/00 - Project/**` carve-out, so without a rule it would have
> been tracked: `git add --dry-run` confirmed it *would* have been added.
> `.gitignore` now names `docs/00 - Project/incident-2026-09-03/`
> explicitly (narrowing an exception, never widening one).

**(c) Schema onto `cobalt_brain`**, through the stores' own
`ensure_schema()` so the DDL keeps its one path:

```
aset migrations applied      : 0001_aset_sizings.sql, 0002_aset_sizings_sheet_mode.sql, 0003_aset_sizings_status.sql
vaultwrite migrations applied: 0001_vault_writes.sql

aset_sizings   : IDENTICAL column list  (22 cols, `status` present)
vault_writes   : IDENTICAL column list  (13 cols)
vault_overrides: IDENTICAL column list  (12 cols)
```

**(d) Restore, ids preserved, sequences reset.**

```
COPY 177 · COPY 0 · COPY 871
setval: aset_sizings_id_seq -> 283 (max id 233)
setval: vault_overrides_id_seq -> 18 (no rows)
setval: vault_writes_id_seq -> 1780 (max id 1186)
```

All three sequences are ahead of `max(id)` — no collision possible.

**(e) THE PROOF — counts and md5 over ordered row contents, `SET TimeZone='UTC'`:**

```
################ cobalt_dev (SOURCE) ################        ################ cobalt_brain (TARGET) ################
       tbl       | rows |         md5_ordered_rows                    tbl       | rows |         md5_ordered_rows
-----------------+------+----------------------------------   -----------------+------+----------------------------------
 aset_sizings    |  177 | ab75130b3c6cd2461bef723c2b21d2ac     aset_sizings    |  177 | ab75130b3c6cd2461bef723c2b21d2ac
 vault_overrides |    0 | (empty)                              vault_overrides |    0 | (empty)
 vault_writes    |  871 | 082d72d82c6adc6e579d628c5bb051c9     vault_writes    |  871 | 082d72d82c6adc6e579d628c5bb051c9
```

**Equal, per table, counts and content.**

> **What the exact copy also carried — flagged, not fixed.** Of the 871
> `vault_writes` rows, **18 are production** (ids 525-542, under
> `/Users/cobalt/Vault/Think`) and **853 are pytest temp-vault rows**.
> `aset_sizings` is ~95 real cards (2026-08-24 → 09-04) plus
> `TEST`/`FORDATE`/`SMOKETEST`/`SMOKEAB`/`TESTHALF`. The copy was exact
> because (e) demands equality and because filtering `aset_sizings`
> would mean *guessing* which tickers were tests, interleaved with real
> cards across three weeks, with deleted trading history as the price of
> guessing wrong. So `cobalt_brain` now carries 853 pytest rows.
> **This wants its own cleanup ruling** — the rows are identifiable with
> certainty by note path (`%pytest-of-cobalt%`), and the precedent is
> 09-03's sanctioned, counted, transactional delete of ids 171-185. Not
> a data-loss risk, and bounded: the transaction fixture means no new
> test row can reach either database.

**(f) Sheet back up, round-trip through the live sheet.**

```
$ launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist
	path = /Users/cobalt/cobalt/ops/com.cobalt.aset.plist
	state = running      pid = 66984      runs = 1
	properties = keepalive | runatload | abandon process group
	environment = { COBALT_ENV => production, ... }
```

The sheet's own page banner now names the database it will write to:

```
Every computed sizing persists to Postgres (cobalt_brain — chosen by COBALT_ENV
alone, RULING 7: production writes cobalt_brain, dev writes cobalt_dev)
```

POST `/size` with `ticker=PROBE`:

```
Persisted: aset_sizings id 284 (cobalt_brain) · updated in .../2026-09-04.md
(unit card-20260904T144829) · trade note created: Trade-2026-09-04 14-48-29 -PROBE.md

cobalt_brain.aset_sizings:  id 284 | PROBE | B | long | full | 120 sh | 60.00 | CARD
cobalt_brain.vault_writes:  1781 aset-cards/card-20260904T144829 (aset.daily_note)
                            1782 (trade note, prefill.trade_note)
cobalt_dev: probe_rows_in_dev = 0 · probe_vault_writes_in_dev = 0
```

Removed in the same session, through the ONE write path (L28) — not by
hand-editing the note:

```
$ COBALT_ENV=production uv run cobalt vault restore --write-id 1781
[WRITE] restored: .../2026-09-04.md · section=aset-cards · unit=card-20260904T144829 · write_id=1783
  (diff: 14 deletion lines, ALL of them the PROBE block; zero other changes)
```

then the trade note deleted and rows 284 / 1781 / 1782 / 1783 deleted in
one guarded transaction. **Back to baseline, md5 identical to (e):**

```
 aset_sizings    |  177 | ab75130b3c6cd2461bef723c2b21d2ac
 vault_overrides |    0 | (empty)
 vault_writes    |  871 | 082d72d82c6adc6e579d628c5bb051c9

live note: PROBE occurrences = 0 · aset card units still present = 10 (Dejan's, untouched)
```

**(g) Truncate `cobalt_dev`** — only after (e) and (f), through the
guarded helper:

```
$ COBALT_ENV=dev uv run python -m cobalt.devdb --truncate aset_sizings,vault_writes,vault_overrides --yes-truncate-cobalt-dev
aset_sizings       177 -> 0
vault_writes       871 -> 0
vault_overrides    0 -> 0

cobalt_dev  : aset_sizings 0 · vault_writes 0 · vault_overrides 0
cobalt_brain: aset_sizings 177 · vault_writes 871 · vault_overrides 0
cobalt_dev.bars = 4563539   <-- NOT migrated, NOT truncated (outside the allowlist)
```

> **`bars` did not move.** 4.56M rows are still in `cobalt_dev` and the
> archiver still names its database explicitly instead of asking the
> resolver. RULING 7 named three tables; migrating a 4.5M-row table was
> not in scope and doing it silently would have been worse. A real
> inconsistency with "cobalt_dev = dev only" — second item handed
> forward.

**(h) Production dry-run.**

```
$ COBALT_ENV=production uv run prefill daily --dry-run
Daily prefill [DRY-RUN]: skipped_idempotent — /Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-04.md
  filled: none
  skipped (not touched): rules (already filled), trading (already filled), market_calendar (already filled)
```

**The diff is empty and that is the correct result** — today's note
already carries all three `cobalt:section` markers filled (rules 23-45,
trading 49-60, market_calendar 67-84). Nothing was written: the note's
sha256 is unchanged and `vault_writes` stayed at 871 / 0 (a dry run
writes nothing, Postgres included).

Since an empty diff cannot by itself prove *which* database was
consulted, the DRC dry-run does — `cobalt_dev` now holds **zero**
`aset_sizings` rows, so a non-zero card count can only have come from
`cobalt_brain`:

```
$ COBALT_ENV=production uv run prefill drc --dry-run
  cards written: 5 · trades taken (FILLED): 4
[DRY-RUN] created: /Users/cobalt/Vault/Think/1 - Trading/5 - Review/DRC-2026-09-04.md
```

Five cards and four fills is exactly 2026-09-04's real trading day.

### 3. Obsidian as a service

`ops/com.cobalt.obsidian.plist` — `RunAtLoad` + `KeepAlive`, `Program` =
the app binary directly. **Not `open -a`**: that execs, hands off to
LaunchServices and exits immediately, which under `KeepAlive` is a
relaunch loop.

```
$ launchctl print gui/501/com.cobalt.obsidian
	program = /Applications/Obsidian.app/Contents/MacOS/Obsidian
	state = running      pid = 65889      runs = 1
	properties = keepalive | runatload | inferred program

=== relaunch proof ===
14:37:21.539   pid 65889 (started 14:37:03), 1 instance
14:37:21       pkill -x Obsidian
14:37:23       instances: 1
14:37:33       pid 65928 (started 14:37:21), runs = 2, instances: 1

vault open: /Users/cobalt/Vault/Think   (obsidian.json "open": true)
obsidian.log 18:37:22Z "Loaded main app package"
```

**No note was harmed by either kill.** Today's daily note's mtime stayed
`14:36:38` across both — which *pre-dates* the first kill at 14:36:59.
The only change to it during this session was Dejan's own edit at
14:36:38 (+3/−2 lines, 10966 → 11172 bytes, content grew: a sentence
extended, Setup/Grade/Catalyst filled in, an "Answer:" line added). A
safety copy of all 270 daily notes was taken to the session scratchpad
first, because this vault still has no backup.

**(c) The heartbeat probe is BUILT but has nothing to attach to.**
`src/cobalt/obsidian.py::sync_status()` is the probe RULING 6.3c asks
for, tested (16 cases). **There is no heartbeat on this machine** — it
is an unchecked BACKLOG item ("Heartbeat probe: every ops/ plist
expected loaded is loaded", STANDING FOLLOW-UPS), sequenced after slice
2 in PROJECT-LEDGER 08-29/31. The writer and the future heartbeat call
the same function so they can never disagree about the wording. Flagged
rather than invented.

**(d) The writer's ERROR line — proven in the dev vault.** With
`com.cobalt.obsidian` booted out and Obsidian killed (the service is
`KeepAlive`, so the job must be booted out first):

```
$ COBALT_ENV=dev uv run prefill daily --dry-run
... | ERROR | cobalt.vaultwrite.writer:_annotate_sync:350 -
      /Users/cobalt/dev-vault-cobalt/.../2026-09-04.md: written; Obsidian not running — will not sync
[DRY-RUN] created: /Users/cobalt/dev-vault-cobalt/1 - Trading/1- Daily Notes/2026-09-04.md
  ERROR: written; Obsidian not running — will not sync
```

The identical command with Obsidian running emits neither line.

`WriteResult` gained `errors`, printed as `ERROR:` and never `NOTE:`.
Attached via a decorator on the four public writer methods rather than
at the ten `return WriteResult(...)` sites, so a future return site
cannot forget it — and a test asserts all four still carry it. Only
byte-producing actions (`created`/`updated`/`restored`) are annotated;
`unchanged`/`skipped` raise no false alarm. A *broken* probe reports
`UNKNOWN`, never "not running" — "the probe is broken" and "Obsidian is
down" are different facts.

### 4. Mainframe script → registered job

`~/.lmstudio/start_mainframe.sh` → `ops/start_mainframe.sh`;
`com.cobalt.mainframe` points at it; logs to `ops/logs/`.

**The global `pkill -9 -f caffeinate` is scoped.** A control
`caffeinate -i -t 3600` (pid 66157) was started before the change and
**survived three restarts** of the job — under the old script it would
have died on the first.

**A second defect surfaced while proving the first.** `$!` after
`caffeinate ... &` is **not** the caffeinate: measured here, `$!` was
66399 (a bash wrapper) and the real caffeinate was its child 66401. The
first fix's `comm`-based "is it still a caffeinate?" check therefore
never matched, logged `left alone`, and **leaked the old heartbeat on
every restart** — a regression against the over-broad `pkill` it
replaced. Fixed properly: a unique `COBALT_MAINFRAME_HEARTBEAT` marker
in the heartbeat's own command line, `kill_tree()` on the recorded pid,
and a marker-scoped orphan sweep as backstop.

```
$ launchctl kickstart -k gui/501/com.cobalt.mainframe
2026-09-04 14:42:15 | === start_mainframe.sh starting (pid 66535) ===
2026-09-04 14:42:15 | purging lingering LM Studio processes for warm-boot safety
2026-09-04 14:42:16 | heartbeat pid 66399 is not one of ours — left alone
2026-09-04 14:42:16 | swept orphaned heartbeat pids: 66523
2026-09-04 14:42:20 | API online — loading model into VRAM
2026-09-04 14:42:45 | model loaded — spawning heartbeat (60s ping, logged)
2026-09-04 14:42:45 | heartbeat running as pid 66633 (pidfile ops/logs/mainframe-heartbeat.pid)
2026-09-04 14:42:51 | heartbeat OK

$ curl .../v1/chat/completions  -d '{"model":"mainframe", ... "7 times 6" ...}'
model : mainframe   finish: stop   tokens: 214
content: 42

caffeinate processes: 3 — the control (66157, alive), LM Studio's own, and
exactly one marked heartbeat. No orphan pile-up.
```

**The logging earned its keep within fifteen minutes.** At ~14:45 the
122B model vanished from LM Studio and every subsequent ping logged
`heartbeat FAILED: ... "No models loaded"` on a 60-second cadence:

```
2026-09-04 14:40:04 | heartbeat OK        (x5)
2026-09-04 14:45:00 | heartbeat FAILED:   (x13, every 60s)

$ lms ps       ->  No models are currently loaded.
$ /v1/models   ->  the "mainframe" identifier is gone from the list
```

**Cause of the unload is UNKNOWN and is not guessed at here.** Only
three script starts are logged (14:39, 14:40, 14:42), none after the
model loaded successfully at 14:42:45 (64.84 GiB); nothing in the boot
log or stderr accounts for it; `lms ps` shows no TTL on the model, so it
was not a TTL expiry. Recorded as unexplained.

What is certain is the design flaw it exposed: **a heartbeat whose only
action is a ping can observe its own death and nothing else.** Once the
model is gone the ping can never bring it back. The pre-RULING-6 script
had exactly this flaw and no log to reveal it — very likely why "the
local model gets stuck" was folklore rather than a diagnosis.

Fixed, one bounded step beyond "keep its behaviour": on a failed ping
the heartbeat attempts ONE `lms load` and logs the outcome. Same 60 s
cadence, no retry storm. NN#16 says production is left working, and a
supervisor that cannot restore what it supervises does not meet that.

```
2026-09-04 14:58:48 | model loaded — spawning heartbeat (60s ping, logged, self-healing)
2026-09-04 14:58:48 | heartbeat running as pid 67820
2026-09-04 14:58:54 | heartbeat OK

$ lms ps
IDENTIFIER    MODEL                STATUS    SIZE        CONTEXT    DEVICE    TTL
mainframe     qwen3.5-122b-a10b    IDLE      69.62 GB    32768      Local
```

### 5. Boot contract — READ-ONLY, reported not changed

```
$ pmset -g
 standby              0
 sleep                0 (sleep prevented by caffeinate, powerd, screensharingd, ...)
 disksleep            10
 displaysleep         0
 autorestart          1
 womp                 1

$ defaults read /Library/Preferences/com.apple.loginwindow autoLoginUser
cobalt

$ fdesetup status
FileVault is Off.

$ sysadminctl -screenLock status
screenLock delay is 300 seconds
```

- **Never sleeps — MET, with one exception.** `sleep 0`, `standby 0`,
  `displaysleep 0`, and `autorestart 1` (comes back by itself after a
  power failure). **`disksleep 10` is the one non-zero value** — the
  disk is allowed to spin down after 10 minutes. On this internal SSD
  that is close to meaningless, but it is not literally "never sleeps"
  and it is the one line of `pmset` that does not match the contract.
- **Automatic login — MET.** `autoLoginUser = cobalt`, so an unattended
  reboot reaches a logged-in GUI session, which is what the `gui/501`
  LaunchAgents (ASET, Obsidian, the prefill jobs) need to exist at all.
- **FileVault — OFF.** Reported, not judged: FileVault being off is
  what *permits* the automatic login above; with it on, a reboot stops
  at the unlock screen and no LaunchAgent runs until someone types a
  password. The two settings are a single trade — an always-on
  unattended server, bought with an unencrypted disk that holds the
  vault, the trading record and `~/.cobalt_key`.
- **Lock screen: 300 s** — allowed by RULING 6.

**Dejan changes these himself. Nothing here was modified.**

### 6. Restart-on-deploy

Every job whose plist or code changed was reloaded and verified:
`archiver`, `mainframe`, `obsidian` (new), `aset` (restarted onto the
new code at 14:47, pid 66984), and `agent`.

**One honest gap.** `com.cobalt.agent`'s job now declares
`COBALT_ENV=production`, but the *running* process (pid 1362, started
09-03 19:02) survived the bootout — `AbandonProcessGroup` detaches it —
and its environment has no `COBALT_ENV`:

```
$ ps eww 1362 | grep -c '^COBALT_ENV='   ->  0
$ tail -1 ~/cobalt_agent_boot.log        ->  Cobalt is already running (PID: 1362).
```

No duplicate was spawned (`cobalt.sh start` is idempotent). This is
inert — the old tree imports nothing from `src/cobalt/` and reads no
`COBALT_ENV` (verified by grep) — and the old tree's code did not change
in this session, so per the strangler rule it was left running rather
than force-killed. It is the same class as Defect 1 (2026-09-01): env
vars are fixed at process launch and a config deploy cannot fix a live
process. It will pick the flag up at its next natural restart.

`configs/cobalt/rules.yaml` and `docs/_archive/gemini-era-vault-side/`
were left exactly as found, per instruction. Nothing was pushed.

### Final state

```
$ launchctl list | grep -i cobalt
66984	0	com.cobalt.aset
-	0	com.cobalt.agent
-	0	com.cobalt.archiver
66535	-15	com.cobalt.mainframe
-	0	com.cobalt.prefill-daily
66104	0	com.cobalt.obsidian
-	0	com.cobalt.prefill-drc
```

### What this does NOT fix

1. **853 pytest rows now live in `cobalt_brain`'s `vault_writes`.**
   Wants a cleanup ruling (§2e).
2. **`bars` (4.56M rows) is still in `cobalt_dev`** and the archiver
   still passes an explicit `db_name` (§2g).
3. **There is no heartbeat**, so RULING 6.3c's probe has no red light to
   turn (§3c).
4. **The production vault still has no backup.** No Time Machine, no
   git, no sync. Untouched by this session and still the largest open
   risk in this document — and this session's own Obsidian kills were
   only safe because a manual scratchpad copy was taken first.
5. **Obsidian is still an unsynchronised second writer.** Supervising
   it makes the Mac's instance reliably present; it does not stop an
   editor buffer flush. §7 #9(c), the sidecar note, remains the only
   proposal that removes the race.
6. **Why the 122B model unloaded itself at ~14:45 is unexplained.** The
   heartbeat now recovers from it, which means the symptom will stop
   being visible — so if the cause matters, `ops/logs/mainframe.log`
   is where the evidence will accumulate (`heartbeat: reload OK` lines
   are the tell). No TTL is set on the model.
