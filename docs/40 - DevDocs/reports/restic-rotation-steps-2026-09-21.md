# Restic password rotation — your steps (2026-09-21)

For your own hand, in Local Terminal. Drafted by `ops-draft-0921` (Opus 5) for 09-20 R41/R42. **No password is in this file. You type or paste every secret.** Facts behind each step: `reports/ops-draft-2026-09-21.md`, FACTS table.

**Method: `restic key add` → prove → `restic key remove`.** Not `key passwd`. Add a second key with the new password, prove the new one opens the repository, then remove the old key. The old key keeps working until step 13. If you make a typo before then, nothing is locked.

**The repository:** one, `/Volumes/COBALT-BACKUP/restic` (the `ssd` leg; the B2 leg is off). restic 0.19.1.
**Where the nightly job reads the password:** Cobalt vault file `~/cobalt/data/.cobalt_vault`, key name **`RESTIC_PASSWORD`**. The new value goes there (step 11).

## When NOT to do it
- **Never 20:00–22:00 ET.** Deploys run 20:00–21:00. The backup fires at 21:40 and usually finishes in about 8 s, but its timeout is 60 min. After 21:40, if `~/cobalt/logs/backup.err` has no `com.cobalt.backup DONE` line for today, wait.
- Never while a deploy or a hub restore/backup is running. Ask the desk first.
- Best times: a weekend, or a weekday morning before 04:00 or after 22:00. The heartbeat runs every 15 min. Between steps 13 and 15 it can briefly show `backup` red if the vault still holds the old value.

## Steps
1. `date` — confirm you're outside 20:00–22:00 ET.
2. `echo "[${RESTIC_PASSWORD:+SET}${RESTIC_PASSWORD_FILE:+FILE}]"` — this must print `[]`. If it prints `SET` or `FILE`, open a new terminal window and start again. restic would silently use that variable instead of what you type.
3. `restic version` — expect `restic 0.19.1`. Anything else: stop and tell the desk.
4. `restic -r /Volumes/COBALT-BACKUP/restic key list` — paste the **OLD** password from LastPass. Expect **one** row, marked `*`. Write down its ID (first 8 characters) as the OLD-ID. If there's more than one row, stop and tell the desk.
5. In LastPass, generate the **NEW** password (32+ chars) and save it as a new entry, e.g. "restic COBALT-BACKUP 2026-09-21". Save it before using it. Keep the old entry for now.
6. `restic -r /Volumes/COBALT-BACKUP/restic key add` — restic asks for the current password (paste the OLD one), then the new one twice (paste the NEW one both times). Expect `saved new key with ID …`.
7. `restic -r /Volumes/COBALT-BACKUP/restic key list` — paste the **NEW** password. If it opens, you've proved the new password works. Expect **two** rows, with `*` on the NEW row (not the OLD-ID).
8. `cd ~/cobalt`
9. `source ~/.cobalt_key` — gives this shell the key that unlocks the Cobalt vault. It prints nothing.
10. `cp data/.cobalt_vault data/.cobalt_vault.pre-rotation-0921` — a safety copy. It stays encrypted, and the vault tool in step 11 rewrites the file non-atomically.
11. `uv run python dev_utils/manage_vault.py` → choose **3** → name `RESTIC_PASSWORD` → paste the **NEW** password (the input is hidden) → choose **5** to exit. **Never choose 2**, because it prints a secret on screen.
12. Repeat step 2. It must still print `[]`.
13. `restic -r /Volumes/COBALT-BACKUP/restic key remove <OLD-ID>` — paste the **NEW** password. Expect `removed key <OLD-ID>`. **From here the exposed password is dead.**
14. `restic -r /Volumes/COBALT-BACKUP/restic key list` — paste the **NEW** password. Expect **one** row, not the OLD-ID.
15. `COBALT_ENV=production uv run cobalt backup status` — the nightly job's own read, using the password from the vault. Expect the line `newest snapshot: … h old`, with no error. If you get a restic `wrong password` error, the vault holds the wrong value: repeat step 11 and then this step. You can't be locked out, because the NEW password in LastPass still opens the repository.
16. `COBALT_ENV=production uv run cobalt backup restore ssd latest --into ~/restic-proof-0921 --include "/Users/cobalt/Vault/Think/6 - Permanent/Memory/INDEX.md"` — expect `restored into /Users/cobalt/restic-proof-0921`.
17. `ls -la "$HOME/restic-proof-0921/Users/cobalt/Vault/Think/6 - Permanent/Memory/"` — expect `INDEX.md` with a size above 0.
18. `rm -rf ~/restic-proof-0921`
19. `rm data/.cobalt_vault.pre-rotation-0921` — only after step 15 passed.
20. **The old README on the backup disk**, `/Volumes/COBALT-BACKUP/RESTIC-PASSWORD-README.txt`, still holds the OLD password as a `RESTIC_PASSWORD=` line. After step 13 that password opens nothing. What to do with the file is **`[BLANK — YOUR RULING, owed since 09-11 (LEDGER:1225, :1229): update it to the new password, OR delete the password line and rely on the vault + LastPass]`**. The desk brings you this as an A/B; do nothing to the file until you've ruled.
21. In LastPass, mark the old entry "RETIRED 2026-09-21 (key removed)". Delete it after tonight's 21:40 backup is DONE (step 23).
22. `exit` — closes the shell, which drops the vault key from step 9.
23. Tell the desk: **"rotated <time>"**. After 21:40 tonight the desk checks that `~/cobalt/logs/backup.err` shows `com.cobalt.backup DONE`, and that the heartbeat `backup` probe is green.

## If a step fails
- **Steps 1–12:** the old password still opens the repository and the vault still has it (up to step 11). Stop, and send the desk the step number and the exact error line. Don't retry in a different way.
- **Step 13 or later:** only the NEW password opens the repository, and it's in LastPass. Stop and tell the desk. Your one fix is step 11 (vault value), and nothing else.
- **Never** paste a password into the desk chat, a report, or a command line. restic always asks for it.

## OWED WITH IT, BY A HUB (items of `prompts/2026-09-21/06-ops-0921.md`, item 6)
- **The Cobalt key store in restic's include set.** Today only `/Users/cobalt/Vault/Think` is backed up, plus a fresh `cobalt_brain` dump (`configs/cobalt/backup.yaml:37-46`). The vault file `~/cobalt/data/.cobalt_vault` is not in it (owed since 09-11, LEDGER:1174). Which files make up the "key store" (the vault file only, or also `~/.cobalt_key`) is an `ASK DESK`. The hub's default is the vault file only.
- **A fresh restore proof** of that key store from a snapshot taken after the change (BACKLOG.md:420-422, entry checklist item 1). The hub runs it only after the desk tells it you've rotated, and after the include-set change is deployed.
