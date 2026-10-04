# DEPLOY-HUB.md card 03d — Grok other-house read, 2026-10-04

Reader: Grok (`grok --sandbox cobalt-job --allow "Write(<agy-trial scratch>/**)" -p`, CHECK-HUB form), a house other than the author (Opus). Prompt `prompts/2026-10-03/37-03d-grok-read.md`. Files: `stage-copy.sh` copies of `DEPLOY-HUB.md` at `5ff16b1f` (card `03d` checked tip), at BASE `a8d8a848`, card `03d`, `gate.sh` at the tip. Source: `agy-trial/scratch/tribunal-bars-0920/deploy-hub-read-03d/house-a.md`, verbatim below. Runs 1 (stopped after its opening) and 2 (CLI refused the allow string) wrote nothing. No finding has a test or command run by a checker (K24); the brain judges them.

## Findings (verbatim)

The port keeps P7, STEP-T, and STEP-C, and the four ruled sentences are present; four changed lines still open a late restart, deploy past a disallowed skip, leave the lock directory, or stall on a hook block.

1. Line 93 (against base line 94)
Quote: "P1 (v) RE-READ: when P1 named `(v) provisional`, the derived `<restart set>` is read against it now: a non-empty set outside (i)–(iv) at P1's `date` → `cd /Users/cobalt/cobalt`, `FAILED: STEP-R — window (v) does not hold: <labels> · rollback: not used`; an empty set → record `window: (v) holds`."
Line 57 lets the worker name (v) at any hour before the set exists, including during (i) or (ii). This re-read stops only a non-empty set whose P1 clock was already outside (i)–(iv); a non-empty set with P1 inside (i)–(iv) matches neither arm, so the run falls through and the row stays `(v) provisional`. Unchanged D2.6 only re-checks "the window P1 named" and applies the 04:00 bound "under (i) or (ii)", so it never re-reads the set, and residents of that non-empty set can go down after 04:00.
grep -n "P1 (v) RE-READ" files/DEPLOY-HUB.md

2. Line 99 (against base line 99)
Quote: "When the clause holds: quote them from the check report with its path and skip (a)–(f)."
That skip drops (c), the only bullet that makes a skip outside the named set red, and it drops (a) and (e)'s `0 failed` checks. The gate call is not labeled (a)–(f), so `sh … gate.sh <WORKTREE> all --deploy` still runs. gate.sh prints `OUTSIDE the allowed set:` and does not change its exit, so a whole pass 1 can exit 0 with a disallowed skip. With (c) skipped, that line is not a stop, and line 111 still writes `GATE GREEN on <m1>` from the check's suite lines.
grep -n "skip (a)" files/DEPLOY-HUB.md

3. Line 108 (against base line 113)
Quote: "THE RELEASE: the gate releases the lock at its end and prints `.env: removed`; `ls -la <GATE>/.env` (No such file)."
The green path never requires the lock directory `/Users/cobalt/cobalt-wt/.cobalt_dev.lock` to be absent, and it never requires the release script to print `lock released` (base line 113 did). gate.sh `release()` notes the script's exit and then returns success whenever `<GATE>/.env` is already gone, so a script that removes `.env` and leaves the lock directory still exits 0. This hub then records the release and writes `GATE GREEN`.
grep -n "THE RELEASE: the gate releases" files/DEPLOY-HUB.md

4. Line 11 (against base line 11)
Quote: "A call the hook blocks is NOT A REFUSAL: resend it as single calls. Inside the outage (4.1–4.6) a blocked call is resent once as single calls; still blocked → STEP-5."
Outside the outage the flag has no "once" and no stop. Unchanged line 41 makes a listed command that is refused a FAILED run, but this sentence says a hook block is not a refusal, so that stop never starts. A listed call that stays blocked (the gate call among them) is resent with no terminal FAILED line, and the deploy stalls.
grep -n "NOT A REFUSAL" files/DEPLOY-HUB.md

READ DONE · findings: 4
