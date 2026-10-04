#!/bin/sh
# desk-list.sh — read-only. LIST for the desk: live sessions only (rows with a pid),
# one line each: id · name · cwd · status · state. Stale ended rows are omitted.
# Tracked here beside desk-context.sh, whose --guard reads this copy (card 2026-10-03/03
# adoption-scripts L4). A live row without an `id` is skipped and counted on stderr
# (`skipped <n> live row(s) without an id`), never a traceback.
export LC_ALL=C
claude agents --json 2>/dev/null | python3 -c "
import json,sys
skipped = 0
for a in json.load(sys.stdin):
    if a.get('pid'):
        if 'id' not in a:
            skipped += 1
            continue
        print(a['id'], a.get('name','?'), a.get('cwd','?').replace('/Users/cobalt','~'), a.get('status','?'), a.get('state','?'), sep=' · ')
if skipped:
    print('skipped %d live row(s) without an id' % skipped, file=sys.stderr)
"
