I could not save `/Users/cobalt/tmp/plan-radar-parser.md`: this session enforces read-only filesystem access. The complete plan follows.

# Radar parser recovery plan — 2026-09-12

## §0 Headline

Repair the parser against the real Screens note, preserving its prose. This is larger than a label fix: seven extraction defects, an over-budget pool, and an incomplete source-validation command need handling. Recommend GPT-5.6 Sol, high effort, for implementation; hub verification and commits. No deployed feature needs reverting. Monday scanning remains achievable, conditional on the gates below.

## §1 Authority and verified baseline

Dejan rules; Astra designs; Opus reviews and may object. This document proposes amendments explicitly where existing decisions cannot produce a working deployment.

Relevant authority:

- L29 implementation floor and Sol’s no-commit profile: `docs/00 - Project/PROJECT-LEDGER.md:1145`.
- L41 credential separation: ledger line 1147.
- L42 restart derivation: ledger line 1148.
- L43 one production deploy per evening: ledger line 1149.
- Local seat reads and judges, never composes: ledger line 1181.
- S2 dates remain September 10–23; Monday September 14 is the launch tripwire: ledger line 1140.
- The original plan’s **L13 NEXT SESSION** is distinct from ledger law **L13 Delegation contract**.

Source abbreviations used below:

| Reference | Absolute location |
|---|---|
| Screens | `/Users/cobalt/Vault/Think/1 - Trading/Radar Screens.md` |
| Lists | `/Users/cobalt/Vault/Think/1 - Trading/Radar Lists.md` |
| Repo | `/Users/cobalt/cobalt` |
| P1 plan | `/Users/cobalt/cobalt-wt/s2-p1-radar-pool/docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md` |
| P1 report | `/Users/cobalt/cobalt-wt/s2-p1-radar-pool/docs/40 - DevDocs/reports/s2-p1-2026-09-10.md` |

Observed baseline:

- Main is `92fe8a7`, the deployed stage-1 boundary.
- Screens contains 37 lines, four prose sections, no fenced YAML.
- Lists does not exist.
- `data/radar-pool-block.yaml` exists and contains D2’s cap-50 rule.
- The report records migration/registry completion and the ASET restart, then refusal at STEP 8 before artifact creation or vault writes: P1 report lines 610–658.
- Stage 2 remains separate; its recorded commit is `e3caf9a`.
- Existing unrelated working-tree changes must remain untouched.

The ledger’s September 11 appendix still says “NOTHING IS DEPLOYED” at line 1212. That historical statement is superseded by the later LIVE report and observed main checkout. Preserve its rulings; do not use its stale deployment status.

No production DB or live HTTP verification was performed during this design.

# Part A — Design and build plan

## §2 Complete Screens inventory

The parser’s field helper is at `src/cobalt/radar/propose.py:68`; extraction and comparisons occupy lines 74–109.

### Shared divergences across all four screens

| Field | Parser expects | Real note | Ruling |
|---|---|---|---|
| Field markup | Bare labels or bold closed **before** the colon | Bold encloses the colon: `**Sort:**` | Parse label and value separately. Support both conventional bold forms and bare labels. |
| Filters label | `Filters` immediately followed by colon | `Filters (`f=`):` | Accept the documented annotation; do not require note edits. |
| Filters value | Backticked codes matching export `f` | Individual codes followed by English glosses, separated by `·` | Extract codes from the field value; preserve glosses verbatim. |
| Export value | Everything after first colon, stripped of edge backticks | Bold closing marker remains after the colon | Extract the actual inline-code URL, excluding Markdown. |
| Sort value | Entire remainder after first colon is the sort | Sort code, optional English explanation, columns, preset commentary | Extract only the sort code from the Sort field. |
| Export sort check | Export URL must carry matching `o` | All four export URLs omit `o`; pasted URLs contain it | Derive from Sort; cross-check any explicit URL `o`. Missing export `o` is valid. |
| Columns | Independent capitalized Columns bullet | Inline lowercase `columns` field within Sort bullet | Accept inline or standalone field, with optional `c=` annotation. |
| Active window | Only `- Active: `HH:MM` to `HH:MM`` | Intent prose; Day Scan also has a time qualifier in heading | Preserve explicit Active support; derive recognized prose start times; mark absent endpoints PROPOSED. |
| Pasted URL | Ignored | Available in every section | Use as corroborating evidence, never as a network destination. |
| Intent | Ignored | Describes timing and purpose | Preserve verbatim; extract only narrowly defined, explicit timing statements. |
| Provenance | One source string per field | Some fields require multiple corroborating lines | Render adjacent verbatim source comments for each relevant line. |

The LIVE diagnosis understates the bold-markup problem. `**Sort:**` can match the current regex because its captured value begins with `**`; matching the line does not mean extracting the value correctly. The same contamination affects Export parsing.

### Screen-by-screen differences and expected result

All screens have this ordered columns list:

`0,1,4,5,129,6,7,25,26,28,30,84,93,49,83,61,63,64,67,65,66`

| Screen | Real evidence | Additional divergence | Required result |
|---|---|---|---|
| Up Gappers | Screens lines 11–16 | Export `c=<same columns>`; inline columns label includes `c=`; pasted filter/column commas percent-encoded | Key `up_gappers`; five filter tokens; sort `-volume`; resolve columns from inline field, corroborated by pasted URL. |
| Down Gappers | Lines 18–23 | Sort has `(RVOL desc)`; columns label has no annotation; commentary includes backticked `ar=60`; URL commas literal | Key `down_gappers`; five tokens, ending in the down-gap token; sort `-relativevolume`; ignore `ar=60` as UI commentary. |
| Day Scan | Lines 25–30 | Whole-title slug becomes `day_scan_after_10_00`; D2 override names `day_scan`; parser ignores explicit 10:00 start | Key `day_scan`; three tokens; sort `-volume`; `active_from: "10:00"`; preserve full original heading as insertion target. |
| Morning Low Float | Lines 32–37 | “morning” supplies no exact closing time | Key `morning_low_float`; three tokens; sort `-volume`; tunable scanning-span endpoints explicitly PROPOSED. |

Further field rulings:

- `v=150` in pasted screener URLs versus `v=152` in export URLs is intentional.
- Percent-encoded and literal commas must compare equally after one URL decode.
- `ft=4` occurs in pasted URLs for Up, Down, and Morning Low Float. Preserve it as evidence; retain D13’s comparison-based decision for generated `ft`.
- `preset`, `ar`, and pasted `v` are UI metadata, not runtime screen settings.
- Do not harvest arbitrary backticked text from the whole section: labels, presets, and annotations also contain backticks.
- No duplicate screen keys or duplicate required fields may pass silently.
- Runtime requests use the collector’s configured full export columns; screen columns record the trader’s selected layout. Preserve that existing distinction rather than changing collection behavior.

### Required note edits

**None for the current Screens note.**

“Premarket / open” and “morning” do not establish exact end times. Keep D13’s visible PROPOSED defaults and obtain approval through the existing card. Do not guess 09:30, 10:00, or noon.

For a future unsupported or contradictory timing expression, refuse with a field-specific explanation. A plain `Active` bullet is an available clarification, not a mandatory format imposed on all screens.

## §3 Extraction contract

Implement one deterministic extraction path, shared by proposal generation and validation.

1. Recognize screen headings and retain their exact text.
2. Recognize supported field labels, independent of bold-colon placement.
3. Extract field values within their own boundaries.
4. Parse URLs locally; never fetch a pasted URL.
5. Reconcile the evidence.
6. Construct existing `ScreenBlock` models.
7. Validate unique keys and pool references before network or artifact creation.

Specific precedence:

| Field | Authoritative evidence | Cross-check |
|---|---|---|
| `f` | Export URL | Ordered Filters token list; pasted URL if present |
| `sort` | Sort field | Explicit `o` in either URL |
| `columns` | Explicit inline/standalone field; otherwise numeric URL `c` | Every other explicit numeric declaration |
| Start time | Explicit Active range or recognized explicit prose start | Other explicit timing statements |
| Key | Heading name, removing a recognized timing suffix | Unique among all screens; pool references resolve |

For `<same columns>`, require an actual numeric declaration elsewhere in that section. It is a reference, not a default.

**Columns ruling: derived.** A separate Columns bullet is optional; resolvable columns data is required. Do not silently substitute `0-150`.

Strip only a recognized timing suffix such as `(after 10:00)` from the name used for slugging. Do not remove arbitrary parenthetical name text. Keep the original heading unchanged for VaultWriter placement.

Recognize Day Scan’s actual forms—heading “after HH:MM” and Intent “pool source only from HH:MM”—without hardcoding `day_scan`. Conflicting times refuse.

### Glosses

Extract token codes; do not structure or interpret English glosses for Monday.

Preserve:

- Original note bytes.
- Full Filters line in artifact inputs.
- Verbatim Filters evidence adjacent to the generated `f` field.
- Annotation-only edits without changing derived filters.

This avoids inventing a second filter semantics engine. An English correction remains the trader’s annotation; it cannot silently change a Finviz token.

## §4 Lists inventory and adjacent production hazards

### Lists migration

The real Lists artifact is absent, as expected before STEP 8. Its production precursor is `configs/cobalt/watchlists.yaml`.

Measured from that file:

| Field | Tier A | Tier B | Tier C |
|---|---:|---:|---:|
| Tickers | 185 | 25 | 55 |
| Archive intervals | i1, i2, i5, i15, i30 | i5, i30 | None |
| `radar` proposed | true | true | true |
| `backfill_default` proposed | true | false | false |
| `enabled` proposed | true | true | true |

`render_lists()` preserves tier descriptions, membership, interval ordering, and the intended flags: `propose.py:164–181`.

**Found divergence:** D13 requires the source YAML header’s derivation rules as prose. The renderer emits only “derived from the committed tier rules,” losing the substantive rules and judgment notes from `watchlists.yaml:1–53`.

Fix this now: carry the complete leading comment block into the proposed Lists note as readable prose, retaining its wording. Keep raw YAML in artifact inputs. Test against the actual committed source, not the synthetic 60-name Lists fixture.

Expected archive target count is **975**: `185 × 5 + 25 × 2`. Prove actual set equality and backfill equality; counts alone are insufficient.

### Pool: confirmed production blocker

Sources:

- Actual pool: `data/radar-pool-block.yaml:1`.
- Tunables: `configs/cobalt/taxonomy/tunables.yaml:392–424`.
- Budget algorithm: `src/cobalt/radar/notes.py:169–183`.
- List chunk size: `configs/cobalt/radar.yaml:23`.

Actual budget:

| Component | Requests/minute |
|---|---:|
| Cap 50, polling every 60 seconds | 50 |
| Four screens, scanning every 60 seconds | 4 |
| Lists: 4 + 1 + 2 chunks | 7 |
| **Total** | **61** |
| Configured ceiling | **30** |

Even after fixing the parser, the current pool must freeze as over-budget.

**Recommended D2 amendment for Dejan:** temporary cap **18**, keeping both cadences at 60 seconds. Budget becomes **29 rpm**, with one request/minute of nominal headroom. This sacrifices breadth explicitly and preserves one-minute bar polling.

Alternative: cap 50 with 180-second polling gives approximately **27.67 rpm**, but makes bar updates slower. I do not recommend changing freshness to preserve breadth before Monday.

Neither option is an already-approved ruling. Do not silently edit the pool or inflate the measured ceiling. The fixture must retain cap 50 as a refusal case.

### Source validation: confirmed false assurance

`radar sources` currently validates only Lists: `src/cobalt/radar/sources.py:79–100`.

`radar check` validates engine config and tunable types, not real notes or pool budget: `src/cobalt/radar/config.py:112`.

Consequently, original LIVE L7 cannot prove its promised Screens, Day Scan, pool, or budget assertions.

Fix `radar sources` to report and validate both notes and the pool using the existing shared loader. Exit nonzero on any invalid source, unresolved override, or over-budget pool. Also make an archiver diff mismatch exit nonzero; printed differences must not look successful to automation.

### Archiver source switch

The real stage-2 implementation reads Lists once and calls the shared archive/backfill functions before opening stores or resolving a token: worktree `src/cobalt/archiver/config.py:43–59`.

The installed-plan environment is compatible: archiver declares production; the current resolver supports that declaration. No new vault-path workaround is needed.

Critical integration detail: stage 2 also changes `propose.py`, `sources.py`, and `cli.py`, and introduces `lists propose --watchlists-yaml`. It overlaps this repair. Rebase/reconcile stage 2 after the fix, then retest the resulting tree. Do not merge the old stage-2 tip blindly.

Retain the pre-switch watchlists revision explicitly for equality checks after deletion.

### Account-mode attestation

Real daily note, September 11, lines 52–54: `.htk loaded` with `half.htk` checked, no account-mode field.

This is compatible with the actual implementation:

- Note readback passes only filename: `aset/web.py:456–476`.
- Store preserves existing mode with `COALESCE`: `daymode/store.py:146–167`.
- Web form sends `account_mode`: `aset/web.py:597–609`.
- POST validates live/sim: `aset/web.py:1086–1115`.
- Resolution is daily override, then standing setting, otherwise refusal: `aset/account_mode.py:23–40`.

No production note edit or account-mode source change is justified. Add a behavioral regression using the real checkbox shape and rendered form fields; the existing SQL-string assertion alone is weak evidence.

The LIVE report proves an ACCOUNT LIVE banner, not a successful SIM attestation round trip. That remains a hub dev-environment proof.

### Remaining real-data uncertainty

The configured ETF discriminator is expressly unverified in `radar.yaml:5–9`; actual tier lists contain ETFs. Exact matching in `radar/runner.py:135` can admit them if Finviz’s real label differs.

Before launch, the hub must probe a known equity and known ETF from the actual lists and verify classification. If the literal is wrong, update the configured value and add a captured-shape test. Do not infer the correct label from memory or silently drop Tier B: ETF-like entries also occur elsewhere.

Also harden `_ft_diff()` at `propose.py:203–220`: require a valid CSV with a Ticker header. HTML or malformed responses must not become two empty sets and a false “no difference” result. A valid header-only CSV remains permissible.

## §5 Fixture policy

**Recommendation: commit the real shape with real filter values, rather than the entire personal note verbatim.**

Create `tests/fixtures/radar/radar-screens.real-shape.md` containing:

- All four actual headings.
- Actual field markup, inline columns, gloss syntax, URLs’ relevant parameters, percent encoding, and literal commas.
- All real filter values and token ordering.
- Up Gappers’ `<same columns>` reference.
- Day Scan’s actual timing language.
- The structural frontmatter shape.
- No generated YAML; this is the pre-proposal input.

Remove only personal attribution/date metadata and saved-preset identifiers, replacing them with declared fixture metadata and synthetic preset values. Preserve the remaining field text and punctuation exactly. Document those substitutions.

Keep synthetic fixtures for isolated model and failure tests; they cease to be the sole product acceptance artifact.

**Trade-off for Dejan:** verbatim is simpler to audit and maximizes fidelity, but permanently places the complete screens, annotations, attribution, and preset identifiers in git history. The recommended fixture still permanently exposes the real filter strategies; that is explicitly allowed by this request. It avoids copying incidental personal metadata. If Dejan chooses verbatim, the same tests apply.

This is an explicit, narrow exception to the earlier vault-content prohibition and revokes P1 R2’s synthetic-only policy. Adjust `test_radar_notes.py:26` and the hub’s E5 check so approved fixtures are permitted. Do not weaken general credential protection or allow vault dumps elsewhere.

### Catching the next edit before production

Add:

```text
cobalt radar screens validate --pool-block <file>
```

It must:

- Read the current configured Screens note.
- Use the same derivation code as `propose`.
- Validate prospective Screens plus pool and actual/prospective Lists.
- Check budget.
- Print note hashes, derived keys/windows, and diagnostics.
- Make no network calls, DB writes, vault writes, or proposal files.

Before initial Lists creation, derive prospective Lists from the actual watchlists input in memory.

After installation, validation must also compare derived prose fields with installed screen blocks. Filters, sort, columns, or window drift must fail; annotation-only changes may pass. Compare only prose-derived fields—comparison-derived `ft` and approved PROPOSED values require their documented treatment.

Run this check:

1. Against current real input before every deploy.
2. Immediately before proposal creation.
3. After any screen edit, and in the hub’s pre-open checklist.

Record hashes so a gate against yesterday’s bytes is not presented as proof of today’s note. Existing apply-time target hashing remains the final race guard.

A committed fixture alone cannot catch later private edits. This live-input check closes that gap. Unattended continuous prose-drift monitoring and a general update-existing-block workflow are outside Monday’s scope; validation must flag their need rather than pretending prose edits automatically update YAML.

## §6 Numbered build sequence

1. **Pin the baseline and scope.**  
   Hub creates an isolated worktree from current stage 1, records full SHA and dirty-set exclusions. Sol receives this plan and approved fixture input, with no DB credentials or `.env`.

2. **Write failing real-input tests first.**  
   Assert all four keys, exact filters, sorts, columns, Day Scan start, provenance, unchanged note bytes, and cap-50 budget refusal. Demonstrate current failures before editing extraction.

3. **Implement bounded extraction.**  
   Change `propose.py`; retain current public models and apply semantics. Add narrow field parsing and evidence reconciliation, not a general Markdown/NLP framework.

4. **Add preflight and truthful source validation.**  
   Register `screens validate`; share derivation and existing budget logic. Extend sources output to both notes and pool, with nonzero failure status.

5. **Close nearby defects.**  
   Preserve Lists header rules; validate ft CSV; add actual-source Lists equality and account-form behavioral tests. Complete the ETF live classification check through the hub.

6. **Run offline acceptance.**  
   No real/dev vault writes, DB, credentials, or network. Use temporary test files and mocked HTTP. Run focused tests, then the full non-DB suite on the final tree.

7. **Reconcile stage 2 and repeat affected acceptance.**  
   Preserve new parser/preflight behavior and stage-2 migration compatibility. Test the complete proposed final tree. Keep the source-switch boundary distinct.

8. **Hub verification and review.**  
   Hub runs required DB-backed/dev-vault proofs under L41, removes credential material before commit, and verifies the actual fixture against the real note. Opus reviews decisions and implementation deltas; Dejan rules on scope-changing choices.

9. **Commit and prepare one reviewed LIVE dispatch.**  
   Hub commits. Pin actual deploy baseline, repair SHA, and reconciled stage-2 SHA. Derive restart output from each executing checkout. Carry explicit rollback commands and the current snapshot requirement.

### Offline acceptance gate

PASS requires all of the following:

- Four screens derive from the real-shape fixture.
- Keys are exactly `up_gappers`, `down_gappers`, `day_scan`, `morning_low_float`.
- Day Scan begins at 10:00; no invented morning close.
- Every filter/column order is preserved.
- Supported markup variants produce equal models.
- Genuine contradictory declarations refuse.
- All original note bytes survive proposal and apply simulation.
- Every generated field has correct verbatim evidence or a specific PROPOSED marker.
- Actual Lists membership and archive/backfill sets are unchanged; 975 archive targets.
- Current cap-50 configuration refuses at 61 rpm.
- Recommended cap-18 candidate passes at 29 rpm.
- Validation is side-effect-free and uses current input bytes.
- Installed YAML/prose drift is detected.
- Existing artifact hashing, HITL, environment, market-reset, and changed-target refusals remain green.
- Stage-2 reconciled tree passes relevant tests.
- Full offline suite passes; DB-backed tests are explicitly excluded and listed for the hub.

### Refusal matrix

| Real-shape mutation | Expected result |
|---|---|
| Bold colon inside/outside markup; annotated Filters label | Accept |
| Gloss edit; extra explanatory prose | Accept; preserve text |
| Literal versus encoded commas | Same derived values |
| Missing export `o`, valid Sort | Accept |
| Export/Pasted `o` contradicts Sort | Refuse before network/artifact |
| Export filter differs from Filters or pasted `f` | Refuse with screen and source fields |
| `<same columns>` plus valid inline columns | Accept |
| `<same columns>` without resolvable numeric columns | Refuse |
| Explicit columns disagree, duplicate, or exceed model range | Refuse |
| Day Scan heading and Intent both say 10:00 | Accept; key `day_scan` |
| Conflicting or invalid explicit timing | Refuse |
| Duplicate field, duplicate key, ambiguous URL parameter | Refuse |
| Unknown pool override | Refuse |
| Cap 50 under current budget | Refuse: 61 > 30 |
| Missing/invalid Lists after installation | Refuse |
| ft response HTML/missing Ticker/redirect | Refuse |
| Valid empty ft CSV on both sides | Accept; record zero counts |
| Note changed after proposal | Existing apply hash refusal |
| Installed prose contradicts installed screen YAML | Validation failure |
| Archiver target difference | Nonzero exit |

## §7 RESTARTS derivation

Read-only execution of the repository’s static import walk showed:

| Changed module | Resident reaching it |
|---|---|
| `cobalt.radar.propose` | `com.cobalt.radar` |
| `cobalt.radar.sources` | `com.cobalt.radar` |
| `cobalt.radar.cli` | `com.cobalt.radar` |

No unresolved dynamic imports were reported for those walks. Tests and report files require no resident restart.

**Provisional RESTARTS: `com.cobalt.radar`**

Radar is not yet launched, so its action is the original L10 bootstrap, not an early kickstart.

This is not the final deploy proof. Run:

```text
cobalt jobs restarts <actual-predeploy-sha>..<repair-sha>
```

Save the full derivation. Re-run against the reconciled stage-2 range and any rollback range. If ETF configuration changes enter the diff, derive their readers too.

Do not reuse `pre-s2-p1` as the restart baseline: the report’s lines 588–596 already establish why rollback anchor and actual deploy baseline differ. Unclassified paths remain an ESCALATE.

## §8 LIVE resumption

### Safe parked state

The recorded parked state is safe to hold:

- Stage-1 schema exists.
- ASET runs the stamped-card code.
- Archiver still reads committed watchlists.
- Radar is disabled and unlaunched.
- No incomplete note migration exists.

It provides **no radar scanning**. Hub must reconfirm those facts before resuming; historical report evidence is not a current process probe.

### Re-run versus retain

| Original work | Resume treatment |
|---|---|
| STEP 0 preconditions | Re-run against current state and new dispatch |
| STEP 1 backup | Obtain fresh snapshot for the new LIVE session |
| STEPS 2–4 rebase/test/pin | Repeat for repair and reconciled stage 2 |
| STEP 5 old stage-1 merge | Do not repeat; merge the repair |
| STEP 6 migration | Do not rerun completed migration as a repair step; verify status |
| STEP 6 validate/registry | Re-run validation; confirm disabled state |
| STEP 7 old ASET restart | Do not repeat unless new L42 derivation requires it |
| STEP 8 / L6 | Run fully afresh: both proposals, comparisons, card, token, both applies |
| L7 | Run repaired all-source validation |
| L8 | Run exact archive/backfill equality against pinned pre-switch YAML revision |
| L9 | Merge reconciled stage 2, then verify readers and restart derivation |
| L10–L12 | Bootstrap, enable/register, prove heartbeat |
| L13 | Execute Monday session evidence; do not mark complete on Sunday |

STEP 8 requires approval of the actual diffs, PROPOSED windows, and budget-compatible pool. Four screens mean **eight ft-comparison requests**, not the appendix’s estimated four to six.

No source changes during LIVE. Failure returns to the build lane.

### Deadline and acceptance

Target: deployment completed Sunday September 13, with Monday checks at:

- 04:00+: scanning and volume ranking.
- 09:30: RVOL switch.
- 10:00: Day Scan active and first among screens.
- 16:00: return to volume.
- 20:00–21:00: paused, no prohibited writes.
- 20:30: archiver succeeds with unchanged target set.

Weekend idle behavior cannot prove active-session ranking or bar freshness. L13 remains partially outstanding until those observations occur.

Respect L43 when scheduling the heartbeat regression. Prepare both changes offline; assign one coordinated production release window per evening. Do not revive September 11’s one-day window waiver.

Rollback must preserve unrelated later fixes. Revert the relevant repair/source-switch commits and use the six recorded vault restore IDs as needed; do not reset main to `pre-s2-p1` and erase subsequent heartbeat work.

## §9 Scope and cuts

This is **not confined to `propose.py` and its tests**.

Expected mandatory files:

| Files | Purpose |
|---|---|
| `src/cobalt/radar/propose.py` | Extraction, evidence, Lists prose, ft validation, preflight handler |
| `src/cobalt/radar/cli.py` | Validation command |
| `src/cobalt/radar/sources.py` | Complete source validation and failure status |
| `tests/cobalt/test_radar_propose.py` | Real-shape and refusal coverage |
| `tests/cobalt/test_radar_notes.py` | Fixture-policy update |
| Source/CLI tests | Budget and command contract |
| Account-mode/web tests | Actual attestation behavior |
| New real-shape fixture | Production-shaped input |
| Plan/build report | Gates, rulings, restart output |

Conditional: ETF config and corresponding collector/runner test, only if the hub probe demonstrates a mismatch.

Cut before compressing:

- Structured gloss semantics.
- General Markdown parsing.
- Arbitrary English scheduling.
- Screen editing UI and general regeneration workflow.
- Broader taxonomy, panel, ranking, or heartbeat redesign.
- Fresh throughput experiment to justify cap 50.

Do **not** cut real-input fixtures, budget validation, archive equality, or apply guards.

If these gates cannot finish Sunday, retain the safe parked deployment and report the Monday tripwire as missed. Remove downstream S2 scope; do not move dates or claim acceptance.

# Part B — Task size, builder, and meter

## §10 Concrete size

| Work | Estimate |
|---|---:|
| Production Python, added/changed | 220–350 lines |
| Tests, added/changed | 350–550 lines |
| Fixture | Approximately 40–60 lines |
| Total files including report and tests | Approximately 9–12 |
| Mechanical implementation after rulings | About 70% |
| Judgment/integration | About 30% |

Judgment concentrates in evidence precedence, timing ambiguity, approved defaults, budget trade-off, and stage-2 reconciliation.

The bounded implementation should fit **one uninterrupted Sol run**, approximately 90–150 minutes, followed by separate hub verification and review. That is an estimate, not a promise. Allow 45–90 minutes for hub gates and reconciliation. LIVE approval and Monday observations are separate.

Escalate rather than extending silently if implementation exceeds roughly 400 source lines, needs schema changes, or uncovers new collector/poller behavior.

## §11 Recommendation

**Builder: OpenAI, GPT-5.6 Sol at high effort.**

Reasons tied to this task:

- This is deterministic Python with explicit fixtures and refusal contracts.
- Most ambiguity has been resolved in the design.
- It touches proposal output destined for vault writes, so the L29 implementation floor applies.
- Sol can implement and prove the offline surface without credentials.
- Hub-only DB verification and commits already match L41 and the established workflow.
- It preserves scarce Anthropic architect capacity for review and the owed heartbeat work.

**Second choice: Anthropic Opus 5.**

Opus is appropriate if integration becomes a write-path redesign or if Sol’s handoff cannot leave enough time for the hub gates. Sonnet is suitable for the established bounded hub duties; it is not the authorized implementation substitute for this write-path repair under L29.

Qwen may perform a short fixed-command verification and return a bounded verdict. It must not author source, fixtures, or this plan.

Astra remains design/review only.

## §12 Strongest case against this recommendation

Sol’s lower marginal meter cost can be outweighed by another cross-house handoff. This repair overlaps an unmerged stage-2 migration and depends on hub-only proofs. A builder lacking the deployed-state context could lose the time supposedly saved.

**Opus becomes the better choice if:**

- The hub cannot promptly run credentialed gates.
- Real-data checks reveal account-mode, transaction, or collector changes.
- The patch grows beyond the bounded extraction/validation scope.
- Sunday time remaining cannot accommodate a Sol build plus integration review.

In those circumstances, one Opus session owning the permitted implementation and verification work may be cheaper in total elapsed time and retry cost. Cross-house diversity is useful; it is not itself a reason to route the build to OpenAI.

## §13 Meter estimate and weekend allocation

Actual remaining percentages are unavailable. `docs/40 - DevDocs/reports/seat-usage.md:7–18` explicitly says those harness percentages are human-entered; current cells are blank. API-equivalent accounting is not a subscription balance.

Planning estimate:

| Activity | Meter draw |
|---|---|
| Sol implementation | One substantial 5-hour allowance window; estimated 90–150 minutes of work |
| Sol generated output | Roughly 15k–30k tokens, excluding hidden reasoning; not convertible reliably to a percentage |
| Sonnet hub verification/commits | One short-to-medium hub session |
| Opus review | One focused review pass, preferably after the Sunday reset if schedule permits |
| Astra review | OpenAI allowance; scope to changed code and evidence |
| Qwen verification | Optional 5–10-minute fixed-command run; short verdict only |

No dollar or percentage estimate is defensible from the available meter data.

This routing leaves Anthropic’s scarce pre-reset architect allowance mostly available for necessary rulings and the heartbeat regression. The supplied Fable reset is Sunday **13:00 ET**; use post-reset capacity for final review if that still leaves deployment time.

Do not assume a 5-hour window replenishment restores the weekly allowance. Reserve a separate bounded Sol window for the heartbeat implementation if its plan is ready, and let the hub report actual harness usage before dispatching either build.

## §14 Decisions for Dejan and review limits

1. Approve real-shape fixture with real filters; verbatim is the explicit alternative.
2. Approve temporary cap 18, or choose slower polling for cap 50. Current cap 50/60-second combination cannot launch.
3. Approve the expanded validation scope and Sol-high builder recommendation.

Opus should object to unsupported parsing semantics, unsafe evidence precedence, underestimated integration, or a better deadline trade-off. No implementation should reinterpret these decisions silently.

DESIGN COMPLETE
