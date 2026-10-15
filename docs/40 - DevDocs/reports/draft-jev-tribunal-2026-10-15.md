# Draft JEV design tribunal — 2026-10-15 (seat `draft-jev-tribunal`, Opus 5.5, prompt 584)

## §0 Headline
- Drafted hub `prompts/2026-10-15/585-jev-design-tribunal.md` (29,288 B) and blind seat `586-jev-design-opus-seat.md` (8,811 B). The tribunal rules on eight items, §1–§8 of the design read with the decisions file. Each verdict is ADOPT, ADOPT WITH or REJECT, and each house also returns OWNER and ESCALATE blocks. The hub collates by lookup and gives no verdict of its own.
- Houses: Grok, counted on §1 and §3–§8, with its §2 ruling recorded apart; the blind Opus seat, counted on all eight; Gemini when `agy --version` is up (R921, money case). There is no OpenAI seat. The floor is Grok plus the Opus seat.
- Packet: 14 parts, every one ≤ 38,000 B (the largest is `14-collector.py.txt` at 27,766 B). The total is ≈ 150 KB, a bound from file sizes; the ceiling is 200,000 B, with a cut order.
- Blockers before launch: the routing answer's `## HIS RULING — 2026-10-15 (B)` and row R1552 are uncommitted, so the hub refuses until the desk commits them.

## DECISIONS
- ASK DESK: prompt 584 names the design as `reports/jev-shadow-design-2026-10-14.md`, but it lives at `docs/30 - Design/jev-shadow-design-2026-10-14.md` (committed `8b813ca7`). [09:47 EDT] Default: stage it from `docs/30 - Design/`.
- ASK DESK: these inputs are uncommitted: `routing-table-answer-2026-10-14.md` (its B section, +12 lines in `git diff`) and `cto-2026-10-15.md` rows R1548–R1552. The hub refuses an input or a row that is not committed. [09:47 EDT] Default: the desk commits both before it writes the launch row.
- ASK DESK: the launch row needs three literals: `Fable seat: yes` · `gemini: if up` · `openai: not seated (his 10-10)`. The last two are new. [09:47 EDT] Default: the desk writes all three into the row that names `585-jev-design-tribunal.md`.
- ASK DESK: "Grok's text on §2's band→model rules recorded apart" — should the apart record cover only those rules, or Grok's whole §2 verdict? [09:47 EDT] Default: the whole §2 verdict, as the sittings set whole cells apart.
- ASK DESK: if Grok is not up, should the tribunal run on Gemini and the Opus seat? [09:47 EDT] Default: launch nothing and the desk waits (532's floor rule).
- ASK DESK: Gemini "UP" means `agy --version` exits 0. No answer probe for Gemini is on a proven line (`STANDING-LIST.md:103`), so a meter that is out shows at launch. [09:47 EDT] Default: the version row decides; a launch failure is recorded `HARNESS` or `METER`.
- ASK DESK: on a Grok 429, L67 (R1471) says "recorded and retried, never a stop", while 532 says one attempt. [09:47 EDT] Default: rerun after a 429 per the law; every other stop gets one attempt.
- ASK DESK: the design text predates later rulings. It still says R1467 is unconfirmed, a four-house tribunal will sit, X1 is open, and decision 4 is "table-pending" (R1532 has since landed). [09:47 EDT] Default: stage the committed text unedited; `01-QUESTIONS` says those later rulings govern.

## RECORDS
Proven from the files:
- Hub launch line: the thirteen allow strings and three denies are `270-model-tribunal.md`'s line without the `codex exec` string. Proof: `grep -c -F` of the `grok`/`agy` head = 1 in 270; the eleven following strings, the denies and the add-dirs as one segment = 1 in 270 and 1 in 585; the 585 head = 1. The `cd .../agy-trial`, `--model claude-sonnet-5-5 --permission-mode auto` shape comes from 532 and 270.
- Seat launch line: 533's seven strings, three denies and add-dirs as one segment = 1 in 533 and 1 in 586.
- House spellings are from 270 `## 2`, which ran them on 10-10 (`model-tribunal-2026-10-10.md:29` `agy --version` 1.3.3, and its stop line shows Gemini and Grok ruling). Spellings: `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)" -p "<s>"` and `agy --model gemini-3.8-flash-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="<s>"`. Both are `grep -c -F` = 1 in 270 and in 585. The last tribunals where Gemini ruled are 270 and 278 (10-10); f20, f21 and f23 seated no Gemini.
- Desk lines: `sh /Users/cobalt/.claude/ops/desk-launch.sh prompt "<585|586 path>"`. `585-jev-design-tribunal.md` matches bare-guard G9 (`ops/desk/bare-guard.py:819`).
- Reused by reference ("as 532", through 427 and 270): the UNATTENDED, staging, PATTERN, RECOVERY and CLOCK rules, the REDACTION pointer (`73` §1), the packet reading order (`00`), Independence, L74, ASK DESK, the Opus-seat file-check and the seat's AUTHORIZATION, WRITE and RECOVERY. There is no derive step, as in 532; the brain folds.
- Packet parts (B, measured file sizes or a bound):
  - 10 design: 22,975
  - 11 decisions: 3,839
  - 12 routing answer: 3,869
  - 13 rulings: ≈ 7 KB (14 rows, 3 words blocks, the FOR THE CHECK line)
  - 14 `collector.py@f4e8de85` whole: 27,766
  - 15 trial code: ≈ 12 KB (ledger 5,210 + wrapper 954 + ranges)
  - 16 main code: ≈ 8 KB
  - 17 trial plan: 16,923
  - 18 trial reports: ≈ 8 KB
  - 19 MODEL-FINAL ranges: ≈ 4.5 KB
  - 27 laws: ≈ 16 KB
  - 00/01/02: ≈ 18 KB
- Stop lines:
  - Hub: `JEV DESIGN TRIBUNAL DONE · grok: … (apart: §2) · gemini: … · opus: … · floor · agreed: <n> of 8 · split · one house · claims that HOLD · owner items · ESCALATE`.
  - Seat: `JEV DESIGN TRIBUNAL OPUS DONE · <TRIBUNAL R1> · apart: none · withdrawn · ESCALATE`.
- Design citations proved against git:
  - Tip: `jev/trial-0923` = `f4e8de8596fb…`.
  - Trial-tip code, all HOLD: `collector.py` :55, :288, :444, :447, :461, :576, :583, :587, `_NoRedirect` :251; `config.py` :45; `ledger.py` :35, :39, :66, :83, :104; `trial.yaml` :24, :28, :31, :38, :41-42; wrapper :13, :23, :25; `cli.py` :63, :511; `trial.py` percentile :70; r3 build :9, :179, :419, :423.
  - Main, all HOLD: `secrets.py` :214, :237, :244; `cobalt_agent/config.py` :494-497; `configs/config.yaml` :38; `modelaccess/config.py` :43-44, :73-74; `test_modelaccess_config.py:102`.
  - Drift: the design cites `config.py@f4e8de85:125-132` for the URL refusal (actual :129-131) and `:136` for the `ruling:` check (actual :139).
  - Not cited by §7: `configs/config.yaml:57-63` (two `provider: "openrouter"` rows). It is staged in 16 and searched in 02.
- Where 585/586 differ from 532/533, and why:
  - Verdicts are ADOPT / ADOPT WITH / REJECT per section, with a `TRIBUNAL R1:` closing line (270's form), instead of grades. This is a design tribunal (brain R1552, L79).
  - The houses are Grok and Gemini-if-up, with no Astra and no `codex` string, because of R920/R921 and his 10-10 rule. The money case is recorded in §0.
  - Grok is apart on §2 only, not on every item: §2 is the only section that assigns models.
  - There is no Codex probe and no STAGGER row: no OpenAI seat sits, and R1471 removed the Grok cap. A Grok 429 is rerun.
  - The packet stages code from an unmerged branch at a fixed sha via `git show`; 270 and 532 staged committed docs only. A tip check refuses if the branch moved, and a secret-material check fails the packet (L41).
  - Collate is AGREED / SPLIT / ONE HOUSE by verdict word, with no per-band lines and no routing.
  - Each house adds an `ESCALATE:` block (brain), collated in `## House ESCALATE blocks`.
  - NO NEW RULE is proven against 270 for the hub and 533 for the seat: these are the lines that ran with these house strings.
  - Gemini capture carries 270's classifier lesson (`model-tribunal-2026-10-10.md:6`, :212).
- Files read:
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/584-draft-jev-tribunal.md`
  - `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `/Users/cobalt/Vault/Think/6 - Permanent/Memory/topics/writing-rules.md`; `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` (headings; L27, L29, L41, L67, L79)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/532-results-sitting-r2-tribunal.md`, `533-results-sitting-r2-opus-seat.md`, `531-draft-results-sitting-r2.md` (whole); `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/draft-results-sitting-r2-2026-10-14.md` (whole)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/428-results-sitting-opus-seat.md` (whole); `427-results-sitting-tribunal.md` (headings, :3, :13, :34, :50)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/270-model-tribunal.md` (line 1 segments, :7-11, :15-62)
  - `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/338-f23-tribunal.md:39`; `prompts/2026-10-10/278-f4-tribunal-r3.md:33`; `prompts/2026-09-29/17-f15-tribunal-r2.md:3`; `prompts/STANDING-LIST.md` (Gemini lines)
  - Reports: `model-tribunal-2026-10-10.md`, `f4-tribunal-r3-2026-10-10.md`, `f20/f21/f23-tribunal-2026-10-11.md` (Gemini lines and stop lines)
  - `/Users/cobalt/cobalt/docs/30 - Design/jev-shadow-design-2026-10-14.md` (whole); `reports/jev-design-decisions-2026-10-14.md`, `routing-table-answer-2026-10-14.md` (whole, plus `git diff`); `draft-jev-design-2026-10-14.md` (whole); `prompts/2026-10-14/534-draft-jev-design.md`
  - Desk files:
    - `cto-2026-10-15.md`: whole, plus `git diff`
    - `cto-2026-10-14.md`: R1467–R1471, R1495, R1496, R1505, OWED
    - `cto-2026-10-11.md`: R1069, R1112
    - `cto-2026-10-10.md`: R920, R921
    - `cto-2026-09-24.md`: R17, R19
    - `cto-2026-09-22.md`: R109
    - `cto-2026-09-23.md`: R42
    - `cto-2026-10-03.md`: R8
    - words files 10-14 and 10-15: R1467, R1532, R1535
  - `git log` of the design, decisions, routing answer, words file and rows R1467, R1532, R1535
  - Branch `jev/trial-0923`: `git rev-parse`, `git diff --stat main...`, `git ls-tree -l`; `git grep -n` on `collector.py`, `config.py`, `ledger.py`, `trial.py`, `cli.py`, `trial.yaml`, `jev-fix-r3-build-2026-09-23.md`; `git show` of `ops/run_classify_trial.sh`
  - Main: `src/cobalt/redact/secrets.py`, `src/cobalt_agent/config.py`, `configs/config.yaml`, `src/cobalt/modelaccess/config.py`, `tests/cobalt/test_modelaccess_config.py` (grep); `docs/30 - Design/JEV-TRIAL-PLAN-2026-09-23.md` (headings, size); `ops/desk/bare-guard.py` (grep)

DRAFTED · decisions: 8
