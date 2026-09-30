#!/bin/sh
# wait-desk-idle.sh <predecessor-id> <desk-report> [max-seconds]
# Read-only. The successor desk's ONE wait at wake-up: silent until the predecessor's
# turn has ended, then prints how it ended and the desk report's last non-blank line.
# Turn ended = its transcript's last assistant entry is `end_turn` with text starting
# "REFRESHED" (watch shells keep LIST `state: working` after the turn ends, so state
# alone cannot decide — R117), or LIST state is no longer "working", or the row is gone.
# Exits 2 on timeout. Writes nothing.
id="$1"; f="$2"; max="${3:-600}"; waited=0
check() { claude agents --json 2>/dev/null | python3 -c "
import json,sys,os
a=next((a for a in json.load(sys.stdin) if a['id']=='$id'),None)
if a is None: print('absent'); sys.exit()
if a.get('state')!='working': print(a.get('state','?')); sys.exit()
p=os.path.expanduser('~/.claude/projects/'+a['cwd'].replace('/','-')+'/'+a['sessionId']+'.jsonl')
last=None
try:
    for l in open(p):
        try: d=json.loads(l)
        except Exception: continue
        if d.get('type') in ('user','assistant') and not d.get('isMeta'): last=d
except OSError: pass
m=(last or {}).get('message',{})
if last and last['type']=='assistant' and m.get('stop_reason')=='end_turn':
    t=' '.join(c.get('text','') for c in m.get('content',[]) if isinstance(c,dict))
    if t.strip().startswith('REFRESHED'): print('turn ended REFRESHED'); sys.exit()
print('working')
"; }
while [ "$waited" -lt "$max" ]; do
  s=$(check)
  if [ "$s" != "working" ]; then
    echo "$id: $s"
    grep -v '^[[:space:]]*$' "$f" | tail -1
    exit 0
  fi
  sleep 10
  waited=$((waited + 10))
done
echo "TIMEOUT after ${max}s — $id still working"
exit 2
