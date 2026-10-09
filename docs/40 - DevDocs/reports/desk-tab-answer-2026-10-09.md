# The desk opens a new tab at every REFRESH: brain answer · 2026-10-09 19:0x ET
Source: his report with a screenshot. Tabs "CTO next", "CTO next 2" and "CTO next 3" piled up today. He renamed the tab twice, and each REFRESH made another one. A defect he reports: the desk fixes it without asking him (R685).

## §0 Cause: two steps that cannot both hold, and a lookup by label
- The REFRESH HOW step (5) in `topics/cto-desk-checklist.md` says "VIEW it in the 'CTO' tab". At that moment the OLD desk is still alive, and its own `claude attach <old id>` holds the CTO pane. It cannot run a second attach there, so it creates a new tab ("CTO next", R728; "CTO next 2", R747; "CTO next 3", R773).
- The successor then skips its wake-up step 4 (`CTO-DESK-WAKEUP.md:24`: "One herdr tab 'CTO' with a live VIEW of you; create or re-attach as needed; close any other desk tab"). It writes the NEW tab's id into §5 as "the CTO pane", and it leaves the old pane open because of `:22` ("A pane → leave it, name it in the plate as closable"). The next REFRESH starts from the new tab, and the count grows.
- The VIEW fallback (`:14`) finds the tab by its LABEL "CTO" (`herdr tab list`). Once he renames it, no "CTO" label exists, so the desk creates a tab and labels it itself. His name is never kept.

## FIX (the desk's: memory as its one writer; the wake-up text by a drafter on a small card)
1. ONE TAB, BY PANE ID, NEVER BY LABEL. §5 CURRENT keeps ONE desk pane id, the one he sees. No seat creates, renames or labels a desk tab while that pane exists. Whatever he names it stays.
2. REFRESH step (5) is dropped. The old desk does NOT view the successor. It writes the pane id into the handover line: `HANDOVER: predecessor <p> → successor <s> at <time> · pane <id>`.
3. The successor, right after `claude stop <p>` and `claude rm <p>` (`:22`), with the predecessor's attach now ended: `herdr pane run <that pane id> "claude attach <own id>"`. An exit box first takes `send-keys Enter` (H4). Alive = `pgrep -fl "claude attach <own id>"`. The `:22` sentence "A pane → leave it" is replaced, for the desk pane, by this re-attach.
4. A new tab only when that pane id no longer exists in `herdr pane list`. Then ONE tab with `--label "CTO"`, recorded in §5. Any other desk tab is closed the same turn (`herdr tab close`).
5. NOW, once: the live desk re-attaches itself in ONE tab (the one he has open, by its pane id), closes the stale desk tabs, and records the pane id in §5.
Red for the card (hub text): `grep -c 'VIEW it in the "CTO" tab'` → 1 on BASE, 0 after; the HANDOVER line shape carries `· pane `.

FOR THE CHECK: "Brain 10-09 (desk-tab-answer-2026-10-09.md): one desk pane by id, never by label; the successor re-attaches in the predecessor's pane after stop+rm; no REFRESH creates a tab while that pane exists."
