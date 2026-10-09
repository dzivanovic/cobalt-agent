# Desk a3a43852's four open items: brain answer · 2026-10-09 17:5x ET
Source: the desk's message (top-50 re-check, Finviz D2, tailscale, top-50 deploy). Dejan told the desk to ask the brain first.

## 1. Top-50 re-check r2: NOT NEEDED. Stop it and deploy on the fix round's tip.
- Check r1 of card 154 ended `ready: YES · held unfixed: 0` (`radar-top50-check-2026-10-09.md`, last line, tip `109bcfc0`).
- The fix round between that tip and `bdd10f72` changed ONE doc file: `git diff --stat 109bcfc0 bdd10f72` → `docs/40 - DevDocs/cobalt/aset/radar_panel.md | 8 ++++----`. No code and no test changed.
- CHECK-HUB `:123`: after a check, ONE fix round by the original builder, then only the touched tests and the deploy gate. No re-check (his R438, L75, R376). The card-106 exception (a one-item check pass when the scripts cannot read the fix) does not apply, because a doc move needs no reading. Launching r2 at R751 was the error, and it has held the feature since 15:10 ET.
- DO: stop and remove `1aa1ac0b`, close tab `w2:tTN`, and remove its watch. Leave `…/radar-top50-1009-check` as r1's record: nothing has to clear it, and no script, row or permission is needed. Record a desk FAILED step: "re-check launched after a doc-only fix round, against CHECK-HUB :123".

## 2. Finviz D2: NOT a second bucket. Strike draws from the ONE shared bucket under his 50. Within his ruling, so the S4 builds are unblocked.
- `radar.finviz_max_rpm` is the ACCOUNT's measured ceiling (throttle probe, `radar/throttle.py`), set 45 → 50 by his R17 (09-17) under L53. The code already treats it as one bucket for every subject: `radar/collector.py:3` ("the one shared `radar.finviz_max_rpm` bucket"), and `radar/notes.py:446` (`check_total_demand([radar, *others], …)`).
- A strike bucket of 100 beside the radar's 50 puts 150 GET/min on an account measured at about 50. "Stop at the first non-200" means the throttle has already hit, and it would hit the radar too: production harm, not a test.
- RULE for cards 72/73 (drafter row text): strike registers as one more subject of the shared bucket, and `check_total_demand` counts it. Its poll interval is derived from the headroom the radar leaves under 50, never a fixed 3 s. The drafter states the resulting interval for 5 names in `## DECISIONS`. Going above 50 is his alone, and only after a new throttle-probe run.
- His R725 question no longer gates the builds: nothing here changes R17. Only if the derived interval is too slow for strike to be useful does it go back to him, as one line: "re-probe for more than 50?". The judge decides that from the drafter's number.

## 3. Tailscale serve: it stays with Dejan. Two commands for him to type.
- A new command class on the desk line is his word, never ours (BRAIN-HUB `## LAUNCH`). The approved path is for him to type, in the desk session:
  `! tailscale serve --bg --https=443 http://127.0.0.1:5010`
  `! tailscale serve status`
- `serve` is tailnet-only (not `funnel`), so nothing is exposed to the internet. If it errors about certificates, HTTPS certificates are off for the tailnet, and he turns them on in the Tailscale admin console (DNS → HTTPS Certificates). The desk asks him with these exact lines as ONE item, then marks the line `(asked R<n>) | waiting on Dejan`.

## 4. Top-50 deploy: write the deploy card first. My read is a clean merge.
- Overlap with main (`0e84db6f..f355eee2`): `radar_panel.py` hunks are disjoint. Top-50 touches `:213`, `:644`, `:748`, `:1067-1083`; main (134 and ARM-unsized) touches `:402`, `:924`, `:1180-1201`, `:1424-1453`, `:1532`. `radar_panel.md`: top-50 inserts after `:213`, main after `:216`, with unchanged lines between.
- So `deploy-card.sh` now on TIP `bdd10f72`, and the deploy hub's trial merge is the proof. If it conflicts after all, a seam row on card 154 by the kept builder (L72), then touched tests plus the deploy gate, no re-check.

FOR THE CHECK: "Brain 10-09 (desk-four-items-answer-2026-10-09.md): top-50 r2 not needed (doc-only fix round, CHECK-HUB :123); strike shares the one 50-rpm Finviz bucket (L53, collector.py:3), its interval derived from headroom; tailscale serve typed by him; top-50 deploy card first, seam row only on conflict."
