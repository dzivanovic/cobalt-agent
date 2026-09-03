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
