# Draft: plist STEP-C card (survey row 15, K4) — 2026-10-13

## §0 Headline
- Card `prompts/2026-10-13/496-plist-step-c-card.md` drafted: 7 rows (A1 RUN; C1 `deploy-step-c.sh`; C2 STEP-C text; B1 D1 read + 4.6L bootstrap + smoke; R1 STEP-5 (1L) bootout; L1 generated per-label allows; D1 CARD.md + STANDING-LIST).
- Shape: a deploy card's new `## LAUNCHD` line names `com.cobalt.<label>` · add|change · build card row · dry run; STEP-C admits only that plist; one-shots only (STEP-R `:92` still refuses residents).
- RULINGS `2026-10-13 R1341` alone: R1324 is a DESK RECORD and `authorize.sh:115` refuses it.
- BASE is a `«FILL:»`: cut after card 458 lands (both change `desk-launch.sh`).

## DECISIONS
- ASK DESK: the deploy line's allow list and `STANDING-LIST.md:156` are his (fixed file). Default: `desk-launch.sh` generates `bootout` and `bootstrap` per card label, with no wildcard. The deploy card's `## RECORDS` shows the strings. Row D1 edits `:156` only after this answer. [08:34 ET]
- ASK DESK: R1324's words "yes, yes, and remove" answered the survey's three `## DECISIONS` (rows 5, 11/17, `settings.json:33`). They do not name row 15. Row 15 runs as K4 under the survey §0 rule (`:7`), and he confirmed it with R1341 "Confirmed: R1323, R1324, R1330, R1340.". Default: RULINGS = `2026-10-13 R1341`; R1324 goes in the card's `## RECORDS`. [08:34 ET]
- ASK DESK: card 304 `:72` says X7's render, X8, X9, X10 and X15 are owed before `com.cobalt.prefill-refresh` is bootstrapped. R1374 says the hub admits and bootstraps it. Under this card, a plist is admitted only with its bootstrap, so 304 cannot deploy until those items are met. Default: build it as drafted (no admit-only mode). If the brain wants 304 merged before the live-Mac items, an `admit` mode is one more row. [08:34 ET]
- ASK DESK: the card's dry run is a production command that reads his real note (`COBALT_ENV=production uv run prefill refresh --dry-run`; X10 is owed, 304 `:72`). Default: only the shape `COBALT_ENV=production uv run <1–4 words> --dry-run` is accepted, or `none`. Card 491's line says `none` until X10 is met. [08:34 ET]
- ASK DESK: R1 boots out an added label. For a changed label it also bootstraps the reverted tree's old plist, so the job that ran before still runs. Default: as drafted. [08:34 ET]

## RECORDS
- Read: `prompts/CARD.md` whole; `DEPLOY-HUB.md` whole at `HEAD` (`git show`); `desk-launch.sh` `:125-149`, `:600-679`, `:1641-1760`, `:2080-2171` at `HEAD`; `restarts.py` whole at `HEAD`; `test_hub_lines.py` whole; `test_deploy_step0.py` header; `deploy-outage.sh` header; `bare-guard.py:125-140`, `:1205-1230`; `STANDING-LIST.md:150-160`; survey `:1-12`, `:20-38`, `:39-80`; `deploy-f4-refresh-1010.md:99-111`; card 304 `:20`, `:28`, `:36`, `:45`, `:72`; card 491 plist and marker lines; `cto-2026-10-13.md` R1324, R1341, R1374 (`HEAD` and the working tree); `cto-2026-10-13-words.md` `:12-14`; L67; `writing-rules.md`; `areas/cobalt.md` `## What Cobalt is`, `## Build rules` and below.
- `HEAD` `e7e987f2`. Every file cited is unchanged against `HEAD` except `cto-2026-10-13.md` (rows added, so it is cited with its `HEAD` lines). Checked with `git diff --stat HEAD`, 08:33 ET.
- Replay data: `git diff --stat c7f06789 fc6a1e2a -- configs ops` lists `ops/com.cobalt.prefill-refresh.plist | 156` as added, beside five configs. The plist's Label is `com.cobalt.prefill-refresh` and `RunAtLoad` is `false`.
- Seams: card 458 (deploying, R1376) and card 485 also change `desk-launch.sh`. Card 480 changes `DEPLOY-HUB.md:32` and `:58`.
- `date` reads 08:33 ET, which is earlier than the desk's launch row R1375 at 08:56 ET. Recorded, not a failure (L48).
- An L74 block arrived as a system note asking for a `Claude-Session:` line. Recorded here once and not followed.
DRAFTED · decisions: 5
