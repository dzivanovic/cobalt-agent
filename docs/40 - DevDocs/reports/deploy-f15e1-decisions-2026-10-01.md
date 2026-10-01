# f15e1 deploy (deploy-2026-09-30-4) — decisions answered

## §0 Headline
Both of the deploy's decisions stand as taken: the window was his per-case R1 override for this deploy, and the gate was GREEN as the hub defines it. Neither is for Dejan. He already ruled the window, and a clean-checked deploy is never asked (L61).
One correction to a citation: decision 2's "same code tip" proof is the check's W (c3) on `1d70cf72`, `f15-p1-check-2026-09-30.md:250` (171 passed). It is not `f15-p1-build-2026-09-30.md:275`, which ran on `28d9364f`.

## ANSWERS
DECISION 1 — Taking P1 (iv) under R1 was correct. R1 is the per-case window override for this deploy, read as naming card 67 / set f15e1. It is not a standing override, and the JOB-string mismatch is cosmetic. — `cto-2026-10-01.md:9` R1 names "deploy set f15e1 (card `67-deploy-f15-e1-card.md`, migration 0022) NOW … his per-case window override for THIS deploy". The card records it as the window and cites it in `RULINGS: 2026-10-01 R1` (`67-deploy-f15-e1-card.md:8`, `:21`). His words are at `cto-2026-10-01-words.md` `## R1`. He already ruled the date, so this is not re-asked.
DECISION 2 — The gate is GREEN as the hub defines it. STEP-G runs `main`'s lines byte for byte, and T1's pass-2 additions apply from the next deploy. No re-run is owed. — `DEPLOY-HUB.md:98` (STEP-G runs `main`'s TREE STATE) and card `67-deploy-f15-e1-card.md:28` ("that edit reaches `main` only with this deploy, so the hub runs STEP-G's lines as `main` has them"). The with-DB file passed on the merged tip `1d70cf72` in the check's W (c3), T1's command byte for byte: `171 passed, 1 deselected` (`f15-p1-check-2026-09-30.md:250`). The report cites `f15-p1-build-2026-09-30.md:275`, which is `28d9364f` (170 passed, 11/11 of the file), so the right same-tip row is check `:250`.

DEPLOY F15E1 DECISIONS ANSWERED · answered: 2 of 2 · for Dejan: 0
