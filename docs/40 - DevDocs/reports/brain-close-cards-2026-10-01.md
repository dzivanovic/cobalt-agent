## §0 Headline
1. Run LIST to see your open FILLED cards (read-only). It shows 498 and the other two ids. The desk could not read them: it has no database access.
2. Run CLOSE after you edit the three `(id, "exit price")` pairs. It writes ONE "flat" exit leg per card through `legs.record_exit`, the same writer as the sheet's flat button. That exit brings running to 0, and the writer moves FILLED → CLOSED itself (`legs.py:228-241`). This is the designed close and needs no raw `transition()` call.
3. Run CHECK. Each card must say `CLOSED`, `running: 0`, with one flat exit leg.
Why the hand-close died: the running ASET gets `POSTGRES_HOST`/`POSTGRES_PORT`/`COBALT_DB_USER`/`COBALT_DB_PASSWORD` from the repo `.env`. It loads that file through `python-dotenv`, as a side effect of an import: `load_dotenv()` in `src/cobalt_agent/config.py:21`, with cwd `/Users/cobalt/cobalt` set by the plist. `src/cobalt/cli.py:59` loads the same file on purpose. Neither the plist, `ops/start_aset.sh` nor `cobalt.sh` exports them. A bare `python -c` loads neither, so each command below starts with `load_dotenv("/Users/cobalt/cobalt/.env")`. No secret is typed or printed.

## COMMANDS
LIST: your open FILLED cards with ticker, direction, shares and mode. `entry_legs=0` means filled before C1 (like 498). The session is set read-only, so this cannot write.
```
cd /Users/cobalt/cobalt && COBALT_ENV=production uv run python - <<'PY'
from dotenv import load_dotenv; load_dotenv("/Users/cobalt/cobalt/.env")
from cobalt import db, env
c = db.connect(env.resolve_db_name(), side=db.Side.USER); c.execute("SET default_transaction_read_only = on")
print("id  ticker  dir  shares  recomputed  mode  filled_at  entry_legs")
for r in c.execute("SELECT s.id, s.ticker, s.direction, s.shares, s.recomputed_shares, s.account_mode, s.filled_at, (SELECT count(*) FROM legs_current_v l WHERE l.card_id = s.id AND l.kind = 'entry') FROM aset_sizings s WHERE s.state = 'FILLED' ORDER BY s.id"): print(*r, sep="  ")
c.close()
PY
```
CLOSE: writes one confirmed flat exit leg at the price you type and closes each card in the same transaction. Replace `ID2`/`ID3` and each `"PRICE"` (the price you actually got out at, > 0) before you run it. You run this yourself; the desk ran nothing.
```
cd /Users/cobalt/cobalt && COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run python - <<'PY'
from dotenv import load_dotenv; load_dotenv("/Users/cobalt/cobalt/.env")
from decimal import Decimal
from cobalt.cards import legs
from cobalt.session import clock
for card_id, price in [(498, "PRICE"), (ID2, "PRICE"), (ID3, "PRICE")]:
    run = legs.read_position(card_id).running.shares
    r = legs.record_exit(card_id, preset="flat", price=Decimal(price), price_source="typed", price_asof=None, flag="confirmed", source="sheet", running_before=run, now=clock.now_utc())
    print(f"card {card_id}: flat {r.shares} sh @ {price} · running {r.running_before} -> {r.running_after} · closed={r.closed} (transition {r.transition_id})")
PY
```
CHECK: proves each card is closed. It uses the `cobalt` CLI, which loads `.env` itself (`cli.py:59`). Use the same three ids.
```
cd /Users/cobalt/cobalt && for id in 498 ID2 ID3; do COBALT_ENV=production uv run cobalt cards state $id; COBALT_ENV=production uv run cobalt cards legs $id | tail -3; done
```

## RISKS
- Realized R stays "not computed — no entry leg" (`legs.py:691-692`) on any path for a card filled before C1. Nothing in the code adds realized R to a daily total, so no total goes wrong. `legs_current_v` stays consistent: CLOSED with a current exit leg, so the running count still reads 0 (`legs.py:313-315`). A raw `transition()` would leave CLOSED with no legs, and `cobalt cards legs`, the radar panel and the trade note would all refuse it with "holds no position".
- If one card refuses (`market_reset` session gate, `stale`, or "not FILLED"), cards earlier in the list are already closed and later ones are not run. Read the printed lines, fix the cause, and re-run with only the ones still open.
- The sheet also writes a trade-note unit after each exit; this script does not. If you want them afterwards, run `COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt cards trade-note <id>` for each card.
- The exit price is permanent once written: a wrong price can only be fixed with a correction leg (`record_correction`), never undone. Type the broker's real fill.
BRAIN DONE — report /Users/cobalt/cobalt/docs/40 - DevDocs/reports/brain-close-cards-2026-10-01.md
