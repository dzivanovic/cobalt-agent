# `src/cobalt/daymode/__init__.py`

## What it does
F6 — the two-stage day mode and the `.htk` match check (Charter §3 F6,
moment M4).

## The two stages
| Stage | When | What decides |
|---|---|---|
| 1 | before 09:00 ET | the **lowest enabled** mode, by system rule. No input asked, no row written. |
| 2 | 09:00 ET | Cobalt **proposes** with a reason; he approves or overrules **with a reason**. Until he answers, stage 1 stays in force. |

Stage 1 is market mechanics, not a personal gate: no stop can rest
premarket, so the floor is not a judgement anyone needs to make at
05:15.

## `reduced` is a ROLE, not a sheet (ruled 2026-09-04)
The **sheets** are an ordered config list in `configs/cobalt/aset.yaml`
(`sheet_modes.order`, today `[half, full]`). **`reduced` is the name of
the bottom rung's role**, and `daymode.reduced_sheet` is the pointer
saying which sheet plays it — today `half`.

> The code says `reduced`; the config says which sheet that is.

When a quarter sheet exists it becomes a row in `aset.yaml` plus a line
in `hotkey_files`, `reduced_sheet` is repointed, and **nothing in
`src/` changes**. Nothing in the tree names `half` or `full` as a
literal, and nothing counts the sheets. `tests/cobalt/test_daymode.py`
proves this by building a mocked `quarter` ladder and asserting the
floor and the refusal messages follow the pointer.

Charter §8 collision #2 ("no quarter sheet exists today; half is the
premarket floor until then") is unchanged — it is exactly what
`reduced_sheet: half` encodes.

## The four modules
`config.py` (the derived ladder + the pointer) · `propose.py` (stage 1
rule, stage 2 proposal, the reason) · `match.py` (the attested `.htk`) ·
`store.py` (`day_modes`, one row per trading day).
