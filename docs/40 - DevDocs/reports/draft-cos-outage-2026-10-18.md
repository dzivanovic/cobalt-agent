# Draft — K5 card cos-outage-1018 (prompt 783)

## §0 Headline
- Card written: `prompts/2026-10-18/784-cos-outage-card.md`, BASE `0bdb7089`, BAND LOW, RULINGS 2026-10-18 R1863, uncommitted.
- K1: `deploy-outage.sh` accepts `com.cobalt.cos` and bootstraps it from `$REPO/ops/com.cobalt.cos.plist`, as aset. K2: `deploy-step0.sh` census lists it after the agent. 9 tests, RED-first, controls included.
- BLOCKER for F20 (DECISION 1): cos ships `BOOTSTRAP: deferred`, so it is not loaded at the F20 deploy. K1 refuses it at rule E if the hub puts it in `<restart set>`, and `DEPLOY-HUB.md:93` refuses it at STEP-R first. This card alone does not unblock the F20 deploy.

## DECISIONS
1. ASK DESK: a deferred resident in `<restart set>` [16:31]. Card 730 ships `BOOTSTRAP: deferred com.cobalt.cos`: the plist merges and is not loaded. `cobalt jobs restarts` puts cos in RESTARTS (`plist in diff`, card 730 R1). `DEPLOY-HUB.md:93` refuses any set outside agent/aset/radar, and the hub forbids `launchctl` on any other label (`:3`). With the sibling copy, `deploy-outage.sh` rule E refuses a cos that is not loaded (`not running before the outage (gone)`, pinned by K1 CONTROL 2). Default: the card copies aset's handling as ruled and edits no hub text. The desk decides how F20's deploy treats a deferred resident, for example a DEPLOY-HUB change that drops a `BOOTSTRAP: deferred` label from `<restart set>` and adds it to the STEP-R set. That is a separate K5 item.
2. ASK DESK: which sibling [16:31]. Card 730 C4a models the cos plist's content on radar, but the plist lives at `ops/com.cobalt.cos.plist` in the repo, which is aset's root (`deploy-outage.sh:107`). `DEPLOY-HUB.md:144` also bootstraps `/Users/cobalt/cobalt/ops/com.cobalt.<label>.plist`. Default: aset's path. Aset's orphan-clean belongs to the hub (`DEPLOY-HUB.md:139`), not to the script, and does not apply to cos.
3. ASK DESK: census order [16:31]. Default: cos goes after `com.cobalt.agent` in `RESIDENTS`, so the other rows keep their positions and bytes.

## RECORDS
- 16:27 `date`; `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `0bdb7089`.
- 16:27 read `prompts/CARD.md`, `prompts/2026-10-18/721-deploy-card-fixes-card.md` whole.
- 16:28 `git show main:ops/desk/deploy-outage.sh` whole; `git show main:ops/desk/deploy-step0.sh` whole (`:73`, `:875-886`, header `:1-61`).
- 16:28 `grep` of `reports/f20-fix-preflight-2026-10-18.md`: row 22 and ISSUES 5 (a), (e) `BOOTSTRAP: deferred com.cobalt.cos`.
- 16:29 `grep` of `prompts/2026-10-18/730-f20-card.md`: `:13-14` RESTARTS / BOOTSTRAP, C4a, D8, `:50`.
- 16:29 `grep` of `prompts/DEPLOY-HUB.md`: `:3`, `:11`, `:89`, `:93`, `:139`, `:143-145`.
- 16:29 `git show fae30bbd:ops/com.cobalt.cos.plist`: Label `com.cobalt.cos`, "BUILT, NOT LOADED".
- 16:30 read `tests/ops/test_deploy_outage.py` `:1-215`, `:276-293`; `tests/ops/test_deploy_step0.py` `:20-63`, `:210-236`, `:366-400`. No existing test pins the residents list or the dry-run count; `:221-222` checks with `in`.
- 16:30 `grep` of `reports/cto-2026-10-18.md`: R1863, R1919, R1922, R1923.
- 16:30 `git -C /Users/cobalt/cobalt diff --stat main -- ops/desk tests/ops` printed nothing. The line numbers are main's.
- 16:31 read `Memory/topics/writing-rules.md`.
- Nothing committed, no test run, no `launchctl`.

DRAFTED · decisions: 3
