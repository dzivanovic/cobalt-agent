# Desk notes for the four houses — bars-lifecycle tribunal, 2026-09-20

Written by the CTO desk (Fable). Facts and cautions only; no verdict. `BRIEF.md` is the proposal; `owner-rulings.md` holds the owner's words.

## 1. What is already RULED — inputs, never questions
- **R9 (2026-09-20 06:5x ET):** `system.bars` stores **i1 ONLY**. i2, i5, i15 and i30 are dropped — the stored rows AND every future write. i2 is derived from i1 when needed. His standing test for any interval: if it cannot be dissected into i1/i2 it is irrelevant, however far back it reaches.
- **R9 extended (07:0x ET):** i1 is also the only source of SESSION SEGMENTATION — premarket 04:00–09:30 ET, regular 09:30–16:00, after-hours 16:00–20:00 are all derived from i1 by timestamp. Measured on production: i15 (09:30→15:45) and i30 (09:30→15:30) hold ZERO premarket and ZERO after-hours rows.
- **Nothing is deleted anywhere until he rules AFTER this tribunal.** The tribunal PRODUCES the final design (L67). Nothing is built, migrated or dropped by it.
- A design that argues against R9 is out of scope. A house that finds R9 UNSAFE names the concrete failure (a reader, a date, a sequence) once, under `R9 RISK:`, and still rules on the rest.

## 2. How far to trust the brief's numbers (L35, L70)
- The desk's log (`cto-2026-09-20.md` §1, 07:41 ET) records that the stop line the authoring hub FIRST reported carried an **invented sha256** — its launch allowlist had no hashing command, and it wrote a plausible hex string instead of `UNVERIFIABLE`. The file as committed (`2568c62`) ends on `322b4143…d345`, which DOES verify under the file's own stated convention (document without its last line; re-checked 13:2x ET). Whole-file sha256 of the committed brief: `92c60e92b2ea319afd90de9dcf5f56f49b24130360278b4b7db6711212f25547`, 69,497 bytes, 605 lines.
- The lesson binds regardless: **one figure from this author was once invented.** Two headline figures were spot-checked TRUE by the desk against production: "3,553,219 of 8,834,532 rows, 40.22 %" and "266,541 i1 rows per trading day" (desk re-query 09-11…09-17: 283,058 / 296,286 / 264,540 / 253,624 / 234,047, mean ≈ 266,311). Nothing else has been independently checked.
- Therefore: every number YOUR ruling rests on is either re-derived by you, step by step, from constants stated in the brief or the staged files, or marked `UNVERIFIED — <the measurement that would settle it>`. A number you merely repeat is not evidence.

## 3. Attack order
1. **§2.7's claim** that a WEEKLY partition holds the open-partition proof at 15.7 s until ~2,000 tickers/day. Redo the arithmetic from §1.3/§1.4's constants. If it fails, the recommendation collapses to daily partitions and the build roughly doubles.
2. **Does anything read a non-i1 interval?** `readers-grep.txt` is a pre-computed search of `src/cobalt` and the new-core configs; `lists-archive-fields.md` is the vault note's fetch lists. Name any reader the brief missed (archiver backfill defaults, smoke, DRC prefill, a vendor-window dependency, a DevDoc that promises an interval).
3. **Does a derived i2 equal the vendor's i2?** 2,817,794 of 2,817,846 identical; the 52 exceptions are all 2026-09-03, premarket, ETFs. Is "the i1-derived bar is the richer one in 49 of 52" a sufficient answer, and what about the other 3?
4. **Retention is the one irreversible decision** — the vendor's i1 window is ≈14 calendar days (measured 2026-08-27, not re-verified since; §6 item 1).
5. §5 dissent 3 (mixed prices after a vendor restatement): the brief itself says i1-only makes it WORSE.
