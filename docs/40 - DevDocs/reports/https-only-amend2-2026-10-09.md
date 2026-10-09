## §0 Headline
- Card `156` amended for preflight r2: FAIL 13 and NOTEs 2–6 are fixed.
- Row A now lists `tests/cobalt/test_voice_config.py:105` (`== 14` → `== 15`) and the full `tests/cobalt` suite.
- NOTEs 7 and 8 were not in the DO list; the card is unchanged for them.

## CHANGES
- Row A files: add `tests/cobalt/test_voice_config.py` (`:105`, `len(checked) == 14` → `== 15`); the full `tests/cobalt` suite runs for row A too. (FAIL 13)
- M4: now only the commit check and the launch command; `HOST:` is already filled. (NOTE 2)
- M5: "the desk edits the yaml only" replaced by "HIS edits to `configs/dev/aset.local.yaml`". M5's owner moved from DESK to HIS. (NOTE 3, NOTE 5)
- M6: adds a RECORD for the hub's step: `STANDING-LIST.md:153` is the same `http://127.0.0.1:5010/*` curl allow entry as `DEPLOY-HUB.md:11`; the card edits no hub file. (NOTE 4)
- `## RECORDS` PEER GATE: "M3 proves this on the log line" removed; says M3 does not prove the `X-Forwarded-For` peer and that `127.0.0.1` is in `allowed_peers`, so the gate passes either way. (NOTE 6)
- `BASE`, `HOST`, `TIP`, `CHECK REPORT`, `HOUSE B`, `RULINGS` and the fence are untouched; no new command.

## DECISIONS
- NOTE 7 and NOTE 8 (double https line on a mic tap; `bind: lan` error text and the `__main__.py:1`–`:8` docstring; the "no allow-list changes" intro line) are outside the DO list. Default: left unchanged.

## RECORDS
- `git -C /Users/cobalt/cobalt grep -n "len(checked)" e4586978 -- tests/cobalt/test_voice_config.py` → `:105: assert checked == list(GOOD_VOICE["voice"]) and len(checked) == 14`.
- `git -C /Users/cobalt/cobalt show e4586978:configs/cobalt/voice.yaml`: 14 keys under `voice:` (scratch_dir … allowed_peers); `https_url` makes 15.
- `git -C /Users/cobalt/cobalt grep -n "127.0.0.1:5010" e4586978 -- STANDING-LIST.md DEPLOY-HUB.md`: `STANDING-LIST.md:153` and `DEPLOY-HUB.md:11`, `:123`, `:147` hold it.
- Read: card `156`, preflight r2 `## ISSUES`, `topics/writing-rules.md`.
- No `git write`, launch or production command ran.

HTTPS CARD AMENDED 2 · decisions: 1
