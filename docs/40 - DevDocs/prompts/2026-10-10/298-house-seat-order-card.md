JOB: house-seat-order-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R963
BRANCH: ops/house-seat-order-1010
WORKTREE: house-seat-order-1010
BASE: «FILL: 8-hex, the commit of main the branch is cut from (the desk, at the build launch)»
TIP:
REPORT: /Users/cobalt/cobalt-wt/house-seat-order-1010/docs/40 - DevDocs/reports/house-seat-order-build-2026-10-10.md
CHECK REPORT:
HOUSE B:
DB: none
RULINGS: 2026-10-10 R920 R921

## ROWS

WHY: his R921 (`reports/cto-2026-10-10.md:48`, L67 OVERRIDE) and R920 (`:49`) change who sits in a check, and brain R963 (`:7`) says ONE card carries it into the two files that still hold the old order: `CHECK-HUB.md` `SEAT ORDER` and `ops/desk/house-probe.sh`. A fixed file changes by a card row, never in place (G5, `ops/desk/bare-guard.py:71`, `:1122`). His words, as the rule the rows implement:
- R921: "checks Opus+Grok, Gemini only for mandatory-B or a Grok failure; tribunals Grok+Opus seat, Gemini only for money/sizing/vault or a load-bearing split; model tribunal unchanged."
- R920: "only the model tribunal uses OpenAI; no Codex probe elsewhere; a running holder finishes; OpenAI OUT after the tribunal until his word (houses per R921)."
- Brain R963 (the direction, not his ruling): "ONE card makes CHECK-HUB seat order and `house-probe.sh` Grok, Gemini (Sol only by header line, R920/R921)".
The three rows below carry them: S1 the order and house B, S2 the probe step and the Sol spelling, S3 the script and its tests. The rows prove R920 and R921 by their `reports/cto-2026-10-10.md` rows (each `HIS RULING · APPROVED`); the desk's `authorize.sh` reads the header `RULINGS: 2026-10-10 R920 R921`. No row adds a command: the probe stays `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh …` (CLASS (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`, `CHECK-HUB.md:12`), with one new flag `--card <path>` on the script itself. The red-first lines end with `uv run pytest -q tests/ops/test_house_probe.py tests/ops/test_hub_lines.py tests/ops/test_order_open.py tests/ops/test_bare_guard.py` → `0 failed`.

| row | what | red first | files |
|---|---|---|---|
| S1 | R921, R920, brain R963. `CHECK-HUB.md` `SEAT ORDER` (lines 23-27 at BASE, five lines) becomes TEXT S1 NEW, five lines, so the lines after 27 keep their numbers: Grok (xAI, grok-4.7) · Gemini (Google); OpenAI (Sol) only when the card header carries `HOUSE A: OpenAI — his <date> R<n>` (proved like a row of `RULINGS`); house A = the first house of the order that is UP; house B only when the card's `HOUSE B` begins `mandatory` (vault notes or sizing) or house A produced nothing (a Grok failure, `## 3`), else none (`house B: none (not needed)`; the stop line keeps its literal `none available`). Kept from the old text: the `mandatory` wait `FAILED PREFLIGHT: house B — mandatory and no second house is up (<each house and its line>)` with its `· overruled <date> R<n>` exception, `FAILED PREFLIGHT: no house A`, and "Gemini never sits ahead of a house that is up". The other four `OpenAI` lines of BASE are 24, 25, 26 (inside the block) and 90 (the Sol spelling, S2). Backed by `reports/cto-2026-10-10.md:48-49`, `:7` | `test_check_hub_seat_order_is_grok_gemini_and_openai_only_by_header` (new, in `tests/ops/test_house_probe.py`): exactly one hub line starts `SEAT ORDER: Grok (xAI, grok-4.7) · Gemini (Google). OpenAI (Sol) sits only when the card header carries "HOUSE A: OpenAI — his <date> R<n>"`; no hub line holds `OpenAI up → A = OpenAI` or `OpenAI (Sol, ` + backtick + `gpt-5.6-sol` + backtick + `) · Grok`. On `BASE`: fails on the first assertion (`:23` begins `SEAT ORDER, by the meter at launch`). `grep -c -F -e "OpenAI up" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` → 0 after, 1 on `BASE` (`:24`). `wc -l` of the file → 123 before and after | `docs/40 - DevDocs/prompts/CHECK-HUB.md` (lines 23-27 only), `tests/ops/test_house_probe.py` |
| S2 | R920. `CHECK-HUB.md` PREFLIGHT's probe step (line 65 at BASE) and the Sol spelling (line 90): two fragment edits, the rest of each line stands byte for byte. (a) Line 65: the call is `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (the card path typed, quoted); Grok and Gemini only; Sol only when the header carries the line, proved FIRST by the hub itself (`authorize.sh` reads only an `overruled` line, `ops/desk/authorize.sh:195-206`, so it does not): `grep -n "^| R<n> " "<reports/cto-<date>.md>"` → ONE row with `HIS RULING` and `APPROVED`, and `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R<n> |" -- "<that file>"` non-empty, else `FAILED: authorization mismatch — HOUSE A OpenAI`. TEXT S2a OLD → NEW. (b) Line 90: the `- **SOL:** ` label becomes `- **SOL, only with the header line "HOUSE A: OpenAI — his <date> R<n>" (his 2026-10-10 R920):** `, the codex spelling after it unchanged. TEXT S2b. Every other `codex` or Sol mention is a spelling or an allow string and stays: line 10 (`Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)`, the G9 string, `ops/desk/bare-guard.py:142`), line 12 ("the three house strings"), line 71 ("For SOL, (1) and (2) below as typed") | `test_check_hub_probe_step_calls_the_script_with_the_card` (new, same file): the one hub line holding `THE SOL PROBE` also holds `house-probe.sh --card "<card>"` and does not hold `(all three`; the `- **SOL` line holds `HOUSE A: OpenAI — his <date> R<n>`. On `BASE`: fails on `(all three` (`:65`). `grep -c -F -e 'house-probe.sh --card "<card>"'` on the hub → 1 after, 0 on `BASE`. `uv run pytest -q tests/ops/test_hub_lines.py` → `0 failed` (the GROK line test reads `- **GROK:** `, untouched). The existing `test_the_sol_stub_sees_the_hub_files_probe_exactly` still finds the `codex exec` spelling in the `THE SOL PROBE` line | `docs/40 - DevDocs/prompts/CHECK-HUB.md` (lines 65 and 90 only), `tests/ops/test_house_probe.py` |
| S3 | R920, R921. `ops/desk/house-probe.sh` probes Grok and Gemini only; Sol only when the card's header carries the line. Usage line 2 becomes `house-probe.sh [--card <card>] [grok] [gemini] [sol]`. SPEC: (1) with no house named, the set is `grok gemini`, and `sol grok gemini` (that order) when `--card` names a card whose header holds the line; the header is the lines before the first line starting `## `, the line is one whole line from column 0 matching `^HOUSE A: OpenAI — his 20[0-9][0-9]-[0-9][0-9]-[0-9][0-9] R[0-9][0-9]*$` (under `LC_ALL=C`; the dash is the bytes of the em dash as in the hub text); an indented line, one under `## ROWS`, `HOUSE A: OpenAI` alone, one with `overruled`, or one with a tail does not count. (2) `sol` named (with or without `--card`) and no such line → `REFUSED: house 'sol' is probed only when the card header carries "HOUSE A: OpenAI — his <date> R<n>" (his 2026-10-10 R920)` on stderr, exit 1, no `codex` call. (3) `--card` with no path, a path that is not a readable file, or `--card` twice → `REFUSED: <reason>`, exit 1; the existing refusals (unknown or repeated house, bad `HOUSE_PROBE_LIMIT`) stand. (4) The `codex` call, the `grok` and `agy` calls, the 180 s limit, the output lines and exit 0 are unchanged; the header comment's `sol` spelling note says "only with the header line". TESTS in `tests/ops/test_house_probe.py`, all with the stubs of its `houses` fixture and a card file in `tmp_path`: T1 `test_no_card_probes_grok_and_gemini_and_never_calls_codex` (replaces `test_all_three_by_default_up_out_and_timeout`): stdout is exactly the grok and gemini lines, `calls_of(calls, "codex") == []`. T2 `test_a_card_without_the_openai_line_makes_no_codex_call` (parametrized over: a plain card; `HOUSE A: none — overruled 2026-10-10 R1`; `HOUSE A: OpenAI`; the line indented; the line with `overruled` in place of `his`; the line with a tail; the line under `## ROWS`): `--card <card>` → rc 0, two lines, no codex call. T3 `test_a_card_with_the_line_probes_sol_first_with_the_hub_spelling`: stdout `sol: UP`, grok line, gemini line; ONE codex call whose argv equals the hub's `THE SOL PROBE` spelling (the shlex read of `test_the_sol_stub_sees_the_hub_files_probe_exactly`). T4 `test_naming_sol_without_the_line_is_refused`: `sol` alone and `--card <plain> sol` → rc 1, stderr starts `REFUSED: `, no call. T5 `test_naming_sol_with_the_line_probes_only_sol`. T6 `test_a_bad_card_call_is_refused` (`--card`; `--card <missing>`; `--card a --card b`). The two existing tests that call `probe(env, "sol")` (`test_the_sol_stub_sees_the_hub_files_probe_exactly`, `test_a_house_that_says_nothing_is_out`) pass `--card` with the line; `test_a_bad_call_is_refused` keeps its three rows | T1 on `BASE`: the stdout starts `sol: UP` and `calls_of(calls, "codex")` holds one call (`assert [] == [{…}]` fails on the codex assertion). T2, T3, T5, T6: on `BASE` rc is 1 and stderr is `REFUSED: house '--card' is none of sol, grok, gemini` (`ops/desk/house-probe.sh:44`). T4 on `BASE`: rc 0 and one codex call. `grep -c -F -e "--card" ops/desk/house-probe.sh` → ≥ 3 after, 0 on `BASE`. Mutation: the `sol` branch of the default set always on → T1 and T2 red; the refusal of a bare `sol` removed → T4 red | `ops/desk/house-probe.sh`, `tests/ops/test_house_probe.py` |

TEXT S1 OLD (`CHECK-HUB.md:23-27` at `BASE`, five whole lines):

```text
SEAT ORDER, by the meter at launch (PREFLIGHT): OpenAI (Sol, `gpt-5.6-sol`) · Grok (xAI) · Gemini (Google). House A = the first of the three that is UP; house B = the next one UP after it; both start at once.
- OpenAI up → A = OpenAI, B = Grok.
- OpenAI out → A = Grok, B = Gemini.
- OpenAI and Grok both out → A = Gemini, NO house B. A `mandatory` build then WAITS for a meter: `FAILED PREFLIGHT: house B — mandatory and no second house is up (<each house and its line>)`, unless the card's `HOUSE B` line ends `· overruled <date> R<n>` (his per-case ruling, proved like a row of `RULINGS`).
- Gemini never sits ahead of a house that is up. No outside house up → `FAILED PREFLIGHT: no house A`.
```

TEXT S1 NEW (five whole lines, in place of the five):

```text
SEAT ORDER: Grok (xAI, grok-4.7) · Gemini (Google). OpenAI (Sol) sits only when the card header carries "HOUSE A: OpenAI — his <date> R<n>" (proved like a row of RULINGS). By the meter at launch (PREFLIGHT) house A = the first house of the order that is UP (his 2026-10-10 R920, R921).
- HOUSE B is needed only when the card's `HOUSE B` line begins `mandatory` (vault notes or sizing) or house A produced nothing (a Grok failure, `## 3`); else NONE, and PREFLIGHT records `house B: none (not needed)`. When needed, house B = the next house UP after house A in the order, started at once with house A.
- No header line: Grok up → A = Grok, B = Gemini only when needed. Grok out → A = Gemini (the Grok failure), NO house B; a `mandatory` build then WAITS for a meter: `FAILED PREFLIGHT: house B — mandatory and no second house is up (<each house and its line>)`, unless the card's `HOUSE B` line ends `· overruled <date> R<n>` (his per-case ruling, proved like a row of `RULINGS`).
- Header line `HOUSE A: OpenAI — his <date> R<n>`: OpenAI up → A = OpenAI, B = Grok only when needed; OpenAI out → the line above applies as with no header line.
- Gemini never sits ahead of a house that is up. No outside house up → `FAILED PREFLIGHT: no house A`. OpenAI is never probed, started or seated without the header line (his R920).
```

TEXT S2a OLD (the fragment of `CHECK-HUB.md:65` at `BASE`, from "`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh`" through "(THE SOL PROBE it runs, never typed here:"):

```text
`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` (all three: Sol, Grok, Gemini, each asked for one word, in parallel, 180 s each) → quote its three lines WHOLE (THE SOL PROBE it runs, never typed here:
```

TEXT S2a NEW (replaces that fragment; the `codex exec …` spelling after it and the rest of the line stand):

```text
`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (Grok and Gemini, each asked for one word, in parallel, 180 s each; Sol too ONLY when the card header carries `HOUSE A: OpenAI — his <date> R<n>`, which you prove FIRST: `grep -n "^| R<n> " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-<date>.md"` → ONE row carrying `HIS RULING` and `APPROVED`, and `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R<n> |" -- "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-<date>.md"` non-empty, else `FAILED: authorization mismatch — HOUSE A OpenAI`) → quote its lines WHOLE (two; three with that header line) (THE SOL PROBE it runs ONLY then, never typed here:
```

TEXT S2b OLD → NEW (the label at the start of `CHECK-HUB.md:90`; the rest of the line stands):

```text
- **SOL:** 
```

```text
- **SOL, only with the header line "HOUSE A: OpenAI — his <date> R<n>" (his 2026-10-10 R920):** 
```

## NOT IN THIS JOB
- THE MERGE. BUILT and CHECK stop at this branch's tip; NO merge to `main`, no deploy card. The card's own check launches only after the model tribunal's OpenAI rounds end (brain R963); the desk then writes one line to him if Sol probes UP.
- `ops/desk/authorize.sh` and `ops/desk/desk-launch.sh` (they read only an `overruled` HOUSE line, `authorize.sh:195-206`, `desk-launch.sh:871-880`): proving the OpenAI line in them is a later card; the hub proves it by hand (S2).
- Every other line of `CHECK-HUB.md` and every other hub: line 3 and 16 ("TWO outside houses", "START HOUSE A AND HOUSE B AT ONCE"), 21, 28, 29, 87, 99-100, 117 and the stop line keep their words (`## DECISIONS` item of the report); the allow strings at lines 10 and 12; `BUILD-HUB.md`, `DEPLOY-HUB.md`, `STANDING-LIST.md`, the model tribunal's hub and its OpenAI rounds (R920: unchanged).
- `ops/desk/order-open.sh` (it calls `house-probe.sh` with no argument, `:133-134`, and so now reads Grok and Gemini only: the wanted effect) and `tests/ops/test_order_open.py` (its stub house lines are strings, not a probe).
- LAWS and `NOW` (applied by the desk at 14:18 and 14:21); the `bare-guard.py` G9 string (`:142`).
- A new command of any kind (R411, R412): a row that needs one is not built; the build stops with `decisions: 1`.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md` lines 7, 48, 49 (R963, R921, R920).
- `docs/40 - DevDocs/prompts/CHECK-HUB.md` lines 10-12, 21-29, 41, 65, 71, 90-92, 100, 117.
- `ops/desk/house-probe.sh` whole (109 lines); `tests/ops/test_house_probe.py` whole (156 lines).
- `ops/desk/authorize.sh` lines 188-207; `ops/desk/order-open.sh` lines 132-137.
- `docs/40 - DevDocs/prompts/CARD.md` header table (`HOUSE B`, `RULINGS`).
- Precedent: `prompts/2026-10-10/284-kill-hub-card.md` (hub text by TEXT blocks, `DB: none`), `prompts/2026-10-05/26-hub-text-card.md`.

## CHECK ASKS
- X1 Is the script's header test exactly the line S1 and S2 name, and can any card shape other than a column-0 header line `HOUSE A: OpenAI — his <date> R<n>` cause a `codex` call (a heading text, a quoted line, a `RULINGS` value, an `overruled` line)?
- X2 Does any caller reach `codex` without that line: `order-open.sh` (no argument), `preflight.sh`, the hubs, `tests/ops`?
- X3 The SEAT ORDER block: can a run end with house B started when the card is not `mandatory` and house A produced a list, or with OpenAI seated without the line? Trace "Grok out, mandatory" and "header line, OpenAI out".
- X4 Is the diff `<BASE>..<TIP>` only the five `SEAT ORDER` lines, the two fragments at lines 65 and 90, the script and its tests (`git diff --numstat`: `CHECK-HUB.md` unchanged in line count)?

## RECORDS
- Read by the drafter 2026-10-10 against `HEAD` `8ba5a819` (`git -C /Users/cobalt/cobalt log --oneline -1`): `git diff HEAD --stat` over the three files → nothing, so main's files equal `HEAD`. `CHECK-HUB.md` 123 lines, `house-probe.sh` 109, `test_house_probe.py` 156 (`wc -l`).
- At `BASE`: `OpenAI` stands on `CHECK-HUB.md` lines 23, 24, 25, 26 and 90; `(all three` on 65; `- **SOL`, `- **GROK`, `- **GEMINI` on 90, 91, 92; `house-probe.sh --card` and `HOUSE A: OpenAI` 0 times; `--card` and `OpenAI` 0 times in `house-probe.sh`. `house-probe.sh`: usage line 2, `refuse()` 32-35, house check 41-50 (`:44` the unknown-house refusal), default set `:51`, the `sol)` branch 58-61.
- `grep -rl house-probe tests/` → `tests/ops/test_order_open.py` (stub only), `tests/ops/test_house_probe.py`, `tests/ops/test_bare_guard.py` (`:1577` a comment). Other callers: `ops/desk/order-open.sh:133-134` (no argument), `ops/desk/preflight.sh:26-27` (a comment).
- R920 is `reports/cto-2026-10-10.md:49` and R921 `:48`, each `HIS RULING · APPROVED (via brain, L79)`; R963 `:7` is a DESK RECORD (the direction), not a ruling.
- `authorize.sh` `rulings` (`:125-146`) reads `2026-10-10 R920 R921` as one date and two rows.
- RESTARTS: `grep -n -E "ops/desk|tests/ops" configs/cobalt/jobs.yaml` → no match (no resident watches either path); every path is `docs/`, `ops/desk/` or `tests/ops/` (`DB: none`). RESTARTS none expected; `uv run cobalt jobs restarts <BASE>..HEAD` is UNPROVEN at drafting (no `uv` in the drafter's allow list), the build hub runs it.
- `BASE`, `TIP`, `CHECK REPORT` and `HOUSE B` are the desk's (`HOUSE B: as needed` at the check: the card writes no vault note and changes no sizing). With this card's own check the order is Grok alone, house B none.
