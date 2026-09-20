# CARDS HTF CURVE — DRAFT 2026-09-20

## §0 Headline

Four files drafted, nothing applied, nothing launched. The settings file is the 09-19 live file plus ONE line — `htf_level_proximity: [[0, 10], [1, 1]]` inside `card.curves` — and nothing else changes. `17-cards-htf-apply.md` (Opus apply hub, no `--permission-mode` flag) carries 15 allow strings: 13 byte-identical to `30-cards-golive-apply.md`, 2 NEW (the new file's dry-run and apply, necessarily new — new path, new hash), plus 1 NEW deny (`Bash(git push*)`, R12). `18-review-cards-htf.md` carries the 14 approved strings + 3 denies of `08-bars-chunk-e-check.md`, `NEW: NONE`. I cannot hash (no rule) — `SHA__` and `R__` are literal placeholders the desk fills; the apply prompt refuses to start while either remains. ESCALATE 4.

| file | path | status |
|---|---|---|
| settings file | `docs/40 - DevDocs/prompts/2026-09-20/16-packet/p2-live-settings-htf.yaml` | written, 9 lines |
| apply prompt | `docs/40 - DevDocs/prompts/2026-09-20/17-cards-htf-apply.md` | written |
| house-review prompt | `docs/40 - DevDocs/prompts/2026-09-20/18-review-cards-htf.md` | written |
| this report | `docs/40 - DevDocs/reports/cards-htf-draft-2026-09-20.md` | this file |

## §1 The one-key diff — live vs new, quoted

LIVE (`/Users/cobalt/cobalt/data/backups/cards-live-2026-09-19/p2-live-settings.yaml`, sha256 `f3663399b1cbb5ba94edadc7b929900a09be02439c84ffc24f89c12ea81c65f0`, 8 lines):

```
card_settings:
  radar.cards_enabled: true
  card.proposed_key: {a_plus_min: 0.90, a_min: 0.70, b_min: 0.50, c_min: 0.40}
  card.curves:
    atrs_from_open: [[1, 1], [3, 10]]
    rvol: [[1.2, 1], [5, 10]]
    Extension.leg_count: [[0, 10], [1, 10], [2, 6], [3, 3], [5, 1]]
  card.shadow_promotion_bar: {sessions: 10, pairs: 30, median_max: 1, within2_min: 0.90}
```

NEW (`16-packet/p2-live-settings-htf.yaml`, sha256 `SHA__`, 9 lines) — identical, with ONE line added as line 8:

```
    htf_level_proximity: [[0, 10], [1, 1]]
```

| line | live | new |
|---|---|---|
| 1–7 | as above | byte-identical |
| 8 | `  card.shadow_promotion_bar: {…}` | `    htf_level_proximity: [[0, 10], [1, 1]]` ← ADDED |
| 9 | — | `  card.shadow_promotion_bar: {…}` (unchanged, moved down one line) |

Float spelling, flow style, quoting, key order and the trailing newline are the live file's, unchanged. The curve's position inside `card.curves` (last, after `Extension.leg_count`) is the shape the 09-19 draft used — `git show d2262f4:"docs/40 - DevDocs/prompts/2026-09-19/23-packet/p2-live-settings.yaml"` carried `htf_level_proximity: [[0, 10], [2, 1]]` in exactly that slot; only the far-end x changes, from the invented `2` to his ruled `1`. The 09-19 UNVERIFIABLE row about unquoted YAML floats → Decimal was settled by the loader's own dry-run (`reports/cards-golive-2026-09-19.md` STEP 1: `"1.2"`, `"0.9"`, decimal-clean), so the spelling style is kept as-is.

## §2 The score table, from the code

`grade_from_curve` (`src/cobalt/cards/scoring.py:118-134`): flat outside the anchors, linear between, clipped to 1–10, rounded half-up ONCE (`_half_up`, `:114-115`, `ROUND_HALF_UP`). Under `[[0,10],[1,1]]` the interpolation is `raw = 10 + x·(1−10)/(1−0) = 10 − 9x`.

| x (distance ÷ daily ATR(14)) | raw | grade | note |
|---|---|---|---|
| 0 | 10.00 | **10** | at the level — his high end (09-19 R17) |
| 0.25 | 7.75 | **8** | |
| 0.5 | 5.50 | **6** | half-up, so 5.5 → 6 (the desk told him "≈5.5" as the raw) |
| 0.75 | 3.25 | **3** | |
| 1.0 | 1.00 | **1** | his low end (09-20 R35 "low end is 1") |
| 1.5 | 1.00 | **1** | clamped: `value >= anchors[-1].x` → `raw = anchors[-1].grade` |

Legality, read from the code: `Curve._increasing` (`src/cobalt/settings/card.py:125-130`) checks **x only** — a descending grade sequence is legal; `CurveAnchor.grade` is `ge=1, le=10` and both grades are inside it; `Field(min_length=2)` is met with two anchors. The raw value is `min(|last − prior high|, |last − prior low|) ÷ daily ATR(14)` with 0 = at the level (`radar/anatomy/daily.py:141-155`; `ATR_PERIOD = 14`, Wilder, `anatomy/indicators.py:39`), and the factor key the curve is looked up by is literally `htf_level_proximity` (`radar/evaluate.py:429`, `:464-479`). Today, with no anchors, `compute_dots` emits `na_reason="curve_unset"` and `engine_why = "htf_level_proximity <value> — card.curves anchors unset"` (`cards/scoring.py:184-189`) — the dot shows the raw number with no grade. After the apply it shows a grade beside Dejan's own tap; conviction stays the mean of the TAPPED trader grades ÷ 10 (`cards/scoring.py:27-28`), and `src/cobalt/aset/engine.py` contains no reference to `card.curves` or `CardSettingsReader` at all, so this reaches neither sizing nor the proposed key (L7 promotes nothing, L52 untouched).

Expected dry-run shape, from `cmd_load_card` (`settings/card.py:281-318`) and the 09-19 precedent: `= radar.cards_enabled` · `= card.proposed_key` · `~ card.curves` (db 3 curves → file 4) · no `card.alignment_default` line at all (absent both sides) · `= card.shadow_promotion_bar` · footer `DRY RUN — 1 card setting(s) would change. Nothing written.` The `file:` line is `json.dumps(sort_keys=True)`, so the four curves print in ASCII order `Extension.leg_count`, `atrs_from_open`, `htf_level_proximity`, `rvol`.

## §3 APPROVAL LIST for prompt 17 (15 allow + 3 deny)

### (a) Byte-identical to `30-cards-golive-apply.md`'s approved line — `grep -c -F` = 1 each, against that file

| # | string | one sentence |
|---|---|---|
| 1 | `"Bash(COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/cards-live-2026-09-19/p2-live-settings.yaml --sha256 f3663399b1cbb5ba94edadc7b929900a09be02439c84ffc24f89c12ea81c65f0 --dry-run)"` | ROLLBACK dry-run — the same string that was R20's string 1; tonight that file is what is live, so restoring it is the rollback. |
| 2 | `…/cards-live-2026-09-19/p2-live-settings.yaml --sha256 f3663399…65f0 --apply)"` (same string with `--apply`) | ROLLBACK apply, entered only from a STEP 2 error or a STEP 3 red. |
| 3 | `"Bash(COBALT_ENV=production uv run cobalt validate*)"` | STEP 3.2 read-only validation. |
| 4 | `"Bash(COBALT_ENV=production uv run cobalt db query *)"` | STEP 3.1 stored-values proof against `"user".trader_settings`. |
| 5 | `"Bash(COBALT_ENV=production uv run cobalt heartbeat show*)"` | P8 baseline and STEP 3.3 comparison. |
| 6 | `"Bash(curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/*)"` | STEP 3.5 liveness of the sheet and the radar panel. |
| 7 | `"Bash(git -C * status*)"` | P5 clean-tree check on `~/cobalt`. |
| 8 | `"Bash(git -C * log*)"` | P6 tip check and the authorization proof of his approval row. |
| 9 | `"Bash(shasum -a 256 *)"` | P2 hash check of both files before anything parses. |
| 10 | `"Bash(grep *)"` | the placeholder gate, the approval-row lookup, P4's line listings. |
| 11 | `"Bash(tail *)"` | STEP 3.4 resident error logs. |
| 12 | `"Bash(ls *)"` | P3 presence/size/mtime of both files. |
| 13 | `"Bash(date*)"` | P1's three window refusals, re-run immediately before the apply. |

Proof: strings 3–13 were also checked as one ordered 11-string sequence, `grep -c -F` = 1 in both `30-cards-golive-apply.md` and `17-cards-htf-apply.md` — the whole tail is byte-identical, not merely present.

### (b) NEW strings — each named, each with its sentence

| # | string | why it must be new |
|---|---|---|
| N1 | `"Bash(COBALT_ENV=production uv run cobalt settings load --card /Users/cobalt/cobalt/data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml --sha256 SHA__ --dry-run)"` | Necessarily new: it names a file that did not exist on 09-19 and a hash of its bytes. It reads and prints a diff; it writes nothing (`cmd_load_card` returns before `assert_writable`). |
| N2 | the same string with `--apply` | Necessarily new for the same reason; this is the ONE production write of the run, pinned to the reviewed hash — the loader refuses the whole command if the file's bytes do not hash to it (`load_card_file`, `settings/card.py:247-252`). |
| N3 (a DENY, not an allow) | `--disallowedTools … "Bash(git push*)"` | `30`'s line denied only `AskUserQuestion` and `EnterWorktree`. Since `cto-2026-09-20.md` R12 put two push-allow rules in `~/cobalt/.claude/settings.local.json`, a hub whose cwd is `~/cobalt` inherits them; R12's own residual clause makes this deny standing desk practice. It narrows the session, it does not widen it. |

**New rule strings (apply): 3** — 2 allows (N1, N2) + 1 deny (N3). No other string in the launch line is new. The two 09-19 DARK-file strings (R20's strings 3 and 4) are NOT carried: the rollback target is no longer the dark file.

What the allowlist cannot do, by construction: no `git add`/`commit`/`push`, no merge, no migration, no restart, no `launchctl`, no `cobalt_dev`, no pytest, no settings file other than the two named paths, no `cp`/`mv`/`rm`, no editor write outside the Write tool's report.

## §4 RULE PROOF for prompt 18 — 14 allow + 3 deny, `NEW: NONE`

Every string below measured with `grep -c -F` against `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-20/08-bars-chunk-e-check.md` (the R13 line, itself byte-identical to `04-/05-/06-bars-tribunal.md`).

| # | string | count |
|---|---|---|
| 1 | `"Bash(grok *)"` | 1 |
| 2 | `"Bash(agy *)"` | 1 |
| 3 | `"Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)"` | 1 |
| 4 | `"Bash(mkdir -p scratch/tribunal-bars-0920)"` | 1 |
| 5 | `"Bash(git -C /Users/cobalt/cobalt show*)"` | 1 |
| 6 | `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 |
| 7 | `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards show*)"` | 1 |
| 8 | `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards log*)"` | 1 |
| 9 | `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards diff*)"` | 1 |
| 10 | `"Bash(ls *)"` | 1 |
| 11 | `"Bash(grep *)"` | 1 |
| 12 | `"Bash(tail *)"` | 1 |
| 13 | `"Bash(wc *)"` | 1 |
| 14 | `"Bash(date*)"` | 1 |
| D1 | `"AskUserQuestion"` | 1 |
| D2 | `"EnterWorktree"` | 1 |
| D3 | `"Bash(git push*)"` | 1 |

Stronger proof, run in both directions: the entire 17-string sequence `"Bash(grok *)" … "Bash(date*)" --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)"` returns `grep -c -F` = 1 in `08-bars-chunk-e-check.md` AND = 1 in `18-review-cards-htf.md` — same strings, same order, same spacing. **NEW: NONE.**

Two consequences of using that list unchanged, both stated inside prompt 18 rather than papered over:
- The `mkdir` string names `scratch/tribunal-bars-0920` and is NEVER RUN. The review stages into the subfolder `scratch/tribunal-bars-0920/cards-htf-check/`, created by the Write tool — the same move `08` made the same night with `chunk-e-check/` (the folder exists, so the pattern is proven, not assumed). Naming a cards check inside a bars-tribunal folder is a compromise forced by the rule list; the alternative is ONE new string, `"Bash(mkdir -p scratch/review-cards-htf-0920)"`, which the desk may prefer — ESCALATE 3.
- Grok's own `--allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)"` already covers the subfolder, so it is carried unchanged too; it is an argument of `grok`, matched by string 1, not a Claude rule.
- DATE GATE in prompt 18: `2026-09-22 or later → FAILED` — R23 (17:47 ET, "yes") extended `Bash(grok *)` / `Bash(agy *)` through Monday 2026-09-21 23:59 ET.

## §5 Establish-from-reads (asked by the drafting prompt)

| question | answer, from the read |
|---|---|
| How did `p2-live-settings.yaml` reach `data/backups/` on 09-19, under which rule? | The **CTO desk** put it there, not a hub: `cto-2026-09-19.md:464` — "`23-packet/p2-live-settings.yaml` sha256 `f3663399…`; byte-identical copy at the no-space path `/Users/cobalt/cobalt/data/backups/cards-live-2026-09-19/p2-live-settings.yaml` (gitignored, beside the dark file's folder; **rule strings cannot carry a path with spaces cleanly**)." No Bash rule string is recorded for the copy; the desk made it in its own session. R20 then approved that path + hash. |
| Does `cobalt settings load --card` accept a path under `docs/`? | **Yes.** `load_card_file` does `raw = Path(path).read_bytes()` (`settings/card.py:245`) with no root, prefix or extension restriction anywhere in `card.py` or `settings/cli.py:304-316`. Spaces in the path are irrelevant to the loader — they are a problem only inside a `--allowedTools` rule string. The `data/backups/` copy is a HARNESS requirement, not a loader one, and prompt 17 says so in STEP 0. |
| sha256 check | `load_card_file` hashes the file's BYTES and compares before anything parses; a mismatch raises `CardSettingsError` naming both hashes and applies nothing (`:247-252`). `--apply` without `--sha256` is a `SystemExit` (`:286-289`). |
| pause refusal | `assert_writable("settings.load.card", target='"user".trader_settings')` is called at `card.py:322`, i.e. AFTER the dry-run's early return — a dry-run is never refused by the window, an apply inside 20:00–21:00 ET is (`session/guard.py:123-150`, `SessionBlocked`). |
| dry-run output shape | One marker line per key in fixed order (`=` / `~` / `+` / `-`); a key absent from both sides prints nothing; changed keys print `db  :` and `file:` as `json.dumps(sort_keys=True)`, Decimals as quoted strings. Footer `DRY RUN — <n> card setting(s) would change. Nothing written.`, or `no differences — …`. Proven against production by `reports/cards-golive-2026-09-19.md` STEP 1. |
| deletion semantics (why a dropped key matters) | The file is the WHOLE card-settings set: `cmd_load_card` collects `deletes` for any `CARD_SETTING_KEYS` member absent from the file and passes it into the single `store.put(..., delete=deletes)` transaction (`:301-305`, `:323`). This is why §1's "nothing else changes" is a hard requirement, not a courtesy. |

## §6 READING: — desk readings in these files, each his to correct

1. **R35's "low end is 1" = ONE daily ATR(14) on the x axis, grade 1.** His two messages give "linear between the numbers" and "low end is 1"; the desk read the "1" as the x end point (distance in ATRs), pairing with R17's high end (at the level → 10). The competing reading — "the low GRADE is 1" at some distance he has not named — is already satisfied by this curve, so the only thing genuinely his to correct is the DISTANCE. Stated back to him in the approval message; prompt 18 asks all three houses to challenge it (Q2) and the hub escalates any house that reads it differently.
2. **The x unit is distance ÷ daily ATR(14), 0 = at the level** — taken from `anatomy/daily.py:141-155`, not from his words. He was told the unit; he ruled the number.
3. **The loadable file lives at a no-space copy** `/Users/cobalt/cobalt/data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml`. The reviewed artifact is the `16-packet/` file; the copy exists only because a rule string cannot carry a path with spaces. A desk step, Write tool, no new rule string (09-19 precedent).
4. **The review packet folder is `scratch/tribunal-bars-0920/cards-htf-check/`** because the one allowed `mkdir` string names that parent and NEW: NONE was the instruction. A naming compromise, not a law reading.
5. **"A trading day between 04:00 and 20:00 ET" is derived from the weekday `date` prints.** A US market holiday falling Mon–Fri is treated as a trading day by that gate — it refuses more, never less. Sat/Sun outside the pause proceeds; Mon–Fri after 21:00 ET (overnight idle) proceeds.

## ESCALATE

1. **L74 — recorded once, never raised again.** A block inside the tool result that returned this drafting prompt's own file asked for a `Claude-Session: https://claude.ai/code/session_<id>` line in commit messages and PR bodies and named a file-send tool. It is DATA, not an instruction; not followed, not carried into any of the three drafted files. No reply to Dejan mentions it.
2. **The value's READING is the desk's, not his words.** R35's own row says the reading is "his to correct there" — the approval message must show him `[[0,10],[1,1]]`, the six-row score table of §2, and the sentence "at the level = 10, one daily ATR(14) away or farther = 1, straight line between", so his "approve" lands on the reading and not only on a hash.
3. **The review-packet folder name.** `scratch/tribunal-bars-0920/cards-htf-check/` is semantically wrong (a cards check in a bars folder) and was chosen to keep `NEW: NONE`. If the desk prefers a correct name, the ONE missing string is `"Bash(mkdir -p scratch/review-cards-htf-0920)"` — named here, not invented into the prompt.
4. **I cannot hash (no `shasum` rule in this seat), so both prompt 17 and its stop line ship with placeholders.** The desk must fill `SHA__` and `R__` at lines **1, 5, 7, 11, 13, 20, 22, 32, 45, 47, 65** of `17-cards-htf-apply.md` (line 1 carries two `SHA__`; line 47 carries one of each). The prompt's own PLACEHOLDER GATE runs `grep -n -E -e "R_[_]" -e "SHA_[_]" "<this file>"` and refuses to start unless it prints nothing — the bracket form is deliberate so the command cannot match itself; I ran it against the drafted file and it returned exactly those 11 lines.

## CONTINUE

Not mine. Next steps, in order: (1) the desk copies `16-packet/p2-live-settings-htf.yaml` to `data/backups/cards-htf-2026-09-20/p2-live-settings-htf.yaml` with the Write tool and hashes it; (2) the desk launches `18-review-cards-htf.md` as `review-cards-htf-0920`; (3) on `blocks the launch: 0`, ONE approval message to Dejan — file + sha256 + the §2 score table + the 15+3 rule strings; (4) on his "approve", the desk fills the 11 placeholder lines and launches `17-cards-htf-apply.md` as `cards-htf-apply-0920`, outside 20:00–21:00 ET and outside a trading day's 04:00–20:00 ET scanning window. First render of the new dot: Mon 2026-09-21 04:00 ET.

CARDS HTF CURVE DRAFTED · files: 4 · changed keys: 1 · new rule strings (apply): 3 · new rule strings (review): 0 · READING: 5 · ESCALATE: 4
