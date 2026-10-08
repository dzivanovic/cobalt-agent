## §0 Headline
Card `118` row C amended in place for preflight r2 FAIL 19.
`ctl` and `timer` are now declared before `try{`; `clearTimeout(timer)` in `finally` can no longer throw.
Test asserts declaration order and a mutation partner catches a declaration moved into the `try`.
Rows A, B, D, E, F and the header are unchanged. No other slip found.

## CHANGES
- `docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md`, row C (what and test columns) only.
- What: adds the scope rule; `const ctl=new AbortController(); let timer=null;` before `try{`, beside `let owned=false;`; `timer=setTimeout(()=>ctl.abort(),interval);` right after `owned=true;`, before the fetch; `signal:ctl.signal`; `clearTimeout(timer);` in `finally` before `if(owned){ladderInFlight=false;}`.
- Test: `const ctl`/`let timer` before `try{` and before the first guard `if(`; arm line after `try{` and before `fetch('/radar'`; `finally` holds both calls, `clearTimeout` first. New mutation partner `test_a_ctl_or_timer_declared_inside_the_try_is_caught` moves the declarations after `try{` and the test must raise.

## DECISIONS
1. `let timer=null` plus arming after `owned=true;`: the abort starts with the fetch, not at declaration. Default per the prompt.
2. `ctl` stays `const`, declared before `try{`: nothing reassigns it.
3. Scan of the rest of the card: every `finally` read and every guard-side declaration (`layer`, `focused`, `seen`, `termOpen`, `owned`, `ladderOkAt`) is either before `try{` for `finally` use or used only inside the `try`. Row B's `termOpen` is read and used inside the `try`. No other slip, nothing changed.

decisions: 3

## RECORDS
- Read: card `118`, preflight r2 report (check 19, `## ISSUES`), `topics/writing-rules.md`.
- Read `src/cobalt/aset/radar_panel.py:1586`–`:1636` on main: `:1589` `const interval` in scope of `tickLadder`; `:1605` `let ladderInFlight=false;`; `:1609` first guard; `:1611` `ladderInFlight=true;`; `:1612` `try{`; `:1613` fetch; `:1620` second guard; `:1624`–`:1629` catch; `:1630` `}finally{ladderInFlight=false;}`. Confirms the fetch is inside the `try` and `finally` is outside it.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `df50cb74`. `git diff --stat 50b0cd87 HEAD -- src tests configs/cobalt/jobs.yaml` → empty; BASE `50b0cd87` still carries the cited code.

RADAR DISPLAY CARD AMENDED · decisions: 3
