#!/usr/bin/env bash
#
# S1 SMOKE — Charter §8 sprint acceptance, run against cobalt_dev + the
# dev vault. Repeatable: every run cleans up the cards it creates.
#
# SPRINT ACCEPTANCE IS A SMOKE OF *ALL* DELIVERED FUNCTIONALITY, not of
# the newest feature (Charter §8 / NN#16). So this walks F1, F6, F7, F16,
# F17, F18 and F19 in one pass, and a red anywhere is a red sprint.
#
#   scripts/smoke_s1.sh
#
# ENVIRONMENT. Hard-pinned to dev, deliberately and unconditionally: the
# script CREATES CARDS and MOVES STATE, and L28 says the live vault and
# the live database are never a test target. It refuses to run with
# COBALT_ENV=production even if the caller sets it.
set -uo pipefail
cd "$(dirname "$0")/.."

export COBALT_ENV=dev
unset COBALT_VAULT_PATH          # dev vault from configs/dev/vault.yaml

PASS=0; FAIL=0
step() { printf '\n\033[1m── %s\033[0m\n' "$*"; }
ok()   { PASS=$((PASS+1)); printf '  \033[32mPASS\033[0m %s\n' "$*"; }
bad()  { FAIL=$((FAIL+1)); printf '  \033[31mFAIL\033[0m %s\n' "$*"; }
# check <description> <expectation: "contains"|"lacks"> <needle> -- cmd...
check() {
  local desc="$1" mode="$2" needle="$3"; shift 4
  local out; out="$("$@" 2>&1)"
  case "$mode" in
    contains) if grep -qF -- "$needle" <<<"$out"; then ok "$desc"; else
                bad "$desc"; printf '       expected to find: %s\n' "$needle"
                sed 's/^/       | /' <<<"$out" | tail -12; fi ;;
    lacks)    if grep -qF -- "$needle" <<<"$out"; then
                bad "$desc"; printf '       expected NOT to find: %s\n' "$needle"
                sed 's/^/       | /' <<<"$out" | tail -12
              else ok "$desc"; fi ;;
  esac
}

printf '\033[1mS1 SMOKE — Charter §8 sprint acceptance\033[0m\n'
printf 'database: cobalt_dev · vault: %s · %s\n' "$(uv run python -c 'from cobalt.vault import resolve_vault_path; print(resolve_vault_path())' 2>/dev/null)" "$(date '+%Y-%m-%d %H:%M:%S %Z')"

# ---------------------------------------------------------------------
step "F16 — every config family validates"
check "cobalt validate passes" contains "registry <-> plists: schedules and COBALT_ENV agree" -- \
  uv run cobalt validate

# ---------------------------------------------------------------------
step "F17 — every job is a row, and every plist is loaded"
uv run cobalt jobs register >/dev/null 2>&1
check "all 10 jobs registered"      contains "registered 10 job(s)" -- uv run cobalt jobs register
check "no job is a zombie"          lacks    "zombie"               -- uv run cobalt jobs list
check "every ops plist is loaded"   lacks    "not loaded"           -- uv run cobalt jobs check

# ---------------------------------------------------------------------
step "F17d — the kill phrase stops one-shots, and resume releases them"
uv run cobalt stop --by smoke >/dev/null 2>&1
check "a one-shot refuses to start while stopped" contains "NOT RUN" -- \
  uv run cobalt cards expire
uv run cobalt resume --by smoke >/dev/null 2>&1
check "the same job runs after resume" contains "database" -- uv run cobalt cards expire
check "the switch reads clear"         contains "kill switch CLEAR" -- uv run cobalt jobs list

# ---------------------------------------------------------------------
step "F19 — the redactor strips a token from a DM payload"
check "a token in a DM is redacted before send" lacks "0000aaaa1111bbbb2222" -- \
  uv run python -c "
from cobalt.redact import redact
print(redact('DM: https://elite.finviz.com/export.ashx?v=111&auth=0000aaaa1111bbbb2222',
             channel='smoke').text)"
check "and the redaction names the kind" contains "REDACTED:url_query_secret" -- \
  uv run python -c "
from cobalt.redact import redact
print(redact('DM: https://elite.finviz.com/export.ashx?v=111&auth=0000aaaa1111bbbb2222',
             channel='smoke').text)"

# ---------------------------------------------------------------------
step "F6 — the day mode gates the keys and the sheet"
check "A is accepted on today's rung"  contains "A ACCEPTED"  -- uv run python -c "
from cobalt.daymode import assert_grade_allowed, load_daymode_config, SheetMismatch
cfg = load_daymode_config(); mode = cfg.lowest_enabled
for g in ('A', 'A+', 'B'):
    try:
        assert_grade_allowed(g, mode, cfg=cfg); print(f'{g} ACCEPTED')
    except SheetMismatch: print(f'{g} REFUSED')"
check "A+ is refused on today's rung"  contains "A+ REFUSED"  -- uv run python -c "
from cobalt.daymode import assert_grade_allowed, load_daymode_config, SheetMismatch
cfg = load_daymode_config(); mode = cfg.lowest_enabled
for g in ('A', 'A+', 'B'):
    try:
        assert_grade_allowed(g, mode, cfg=cfg); print(f'{g} ACCEPTED')
    except SheetMismatch: print(f'{g} REFUSED')"
check "B is accepted on today's rung"  contains "B ACCEPTED"  -- uv run python -c "
from cobalt.daymode import assert_grade_allowed, load_daymode_config, SheetMismatch
cfg = load_daymode_config(); mode = cfg.lowest_enabled
for g in ('A', 'A+', 'B'):
    try:
        assert_grade_allowed(g, mode, cfg=cfg); print(f'{g} ACCEPTED')
    except SheetMismatch: print(f'{g} REFUSED')"
check "the full sheet on a reduced day refuses a card" contains "reload half.htk" -- \
  uv run python -c "
from cobalt.daymode import assert_sheet_matches, load_daymode_config, SheetMismatch
cfg = load_daymode_config()
try:
    assert_sheet_matches({'attested_sheet': 'full.htk'}, cfg.lowest_enabled, cfg=cfg)
    print('NOT REFUSED')
except SheetMismatch as e: print(e)"
check "the selector lists only declared sheets"  lacks "reduced_day.htk" -- \
  uv run python -c "
from cobalt.daymode import load_daymode_config
print(load_daymode_config().hotkey_file_names)"

# ---------------------------------------------------------------------
step "F1 + F7 — the full card walk, the one-click fill, and the 20:30 block"
# One python block rather than five `check` calls: these steps share
# cards, and a card created by one and asserted by another has to be the
# same row. It prints its own PASS/FAIL lines and its exit code folds
# into the tally below.
if uv run python scripts/_smoke_cards.py; then
  ok "card walk, one-click fill, radar refusal and the 20:30 block (see above)"
else
  bad "the card block failed (see above)"
fi

# ---------------------------------------------------------------------
step "F18 — the heartbeat probes, writes and reports"
check "a dev beat completes and reports a headline" contains "HEARTBEAT" -- \
  uv run cobalt heartbeat beat --dry-run
check "every plist's loaded state + last exit code is probed" contains "launchd: loaded" -- \
  uv run cobalt jobs check
# THE CHARTER'S OWN ACCEPTANCE TEST, through the real code path. The
# smoke does NOT `launchctl bootout` a live job — a repeatable script
# must not leave the host's scheduler in a state that depends on it
# finishing. It substitutes launchd's answer for one label and asserts
# the verdict, which is the half that was broken: before S1-P3 an
# unloaded ONE-SHOT stayed green, because between runs it looks the same
# either way. The real bootout/bootstrap cycle was run by hand against
# production and is in the S1-P3 report.
check "an unloaded plist turns the heartbeat RED" contains "SMOKE-RED" -- \
  uv run python -c "
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path('.env'))
from cobalt.jobs import watchdog
from cobalt.jobs.config import load_job_registry
from cobalt.jobs.store import JobStore
label = 'com.cobalt.cards-expire'
real = watchdog.launchctl_status
watchdog.launchctl_status = lambda l, **kw: (
    watchdog.LaunchdStatus(l, False, None, None, 'NOT LOADED (smoke substitution)')
    if l == label else real(l, **kw))
try:
    found = {f.label: f for f in watchdog.sweep()}[label]
    print('SMOKE-RED' if not found.ok else 'STILL GREEN', found.state, '|', found.detail)
finally:
    watchdog.launchctl_status = real"

# ---------------------------------------------------------------------
step "The new-core test suite"
if uv run pytest tests/cobalt tests/taxonomy -q >/tmp/smoke_pytest.$$ 2>&1; then
  ok "$(tail -1 /tmp/smoke_pytest.$$)"
else
  bad "pytest FAILED"; tail -15 /tmp/smoke_pytest.$$ | sed 's/^/       | /'
fi
rm -f /tmp/smoke_pytest.$$

# ---------------------------------------------------------------------
printf '\n\033[1m════ S1 SMOKE: %d passed, %d failed ════\033[0m\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ] || { printf '\033[31mRED SMOKE TEST = SPRINT NOT DONE (Charter §8).\033[0m\n'; exit 1; }
printf '\033[32mS1 smoke GREEN.\033[0m\n'
