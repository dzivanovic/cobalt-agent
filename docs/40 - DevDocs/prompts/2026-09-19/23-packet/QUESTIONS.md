You are an independent reviewer from another house, one of three reading this packet
separately. Read ONLY the files in this folder; you cannot run commands — everything you need is
already here as a file. `p2-dark-settings.yaml` is the file currently loaded in production
(`radar.cards_enabled: false`, sha256 `945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca`).
`p2-live-settings.yaml` is the desk's DRAFT go-live file (never applied to any database —
this check is of the artifact only). `golive.diff` is the unified diff between them.
`src-settings-card.py` is the full Pydantic settings module that parses and validates this exact
file format (`CardSettings`, `load_card_file`, `cmd_load_card`). `src-radar-evaluate-desk_shadow.py`,
`src-session-guard-assert_writable.py`, `src-session-clock-windows_for.py`,
`src-cards-shadow_report-excerpt.py`, `src-settings-store.py` are supporting excerpts.
`plan-s2-p2-excerpt-step5-10.md` is the design-of-record section covering these settings.
`facts.md` is the desk's own pre-computed reading, with file:line — treat every claim in it as a
CLAIM to verify against the source files, never as settled fact, exactly like a builder's report.

This artifact would (if approved and applied) flip a live production trading-support system's
radar cards from dark to visible/advisory for Monday premarket. For every finding give SEVERITY
(BLOCKER = the file does something other than what facts.md says, or contradicts a LAW: L1
fail-loud, L7 shadow-mode promotion, L28 vault/HITL, L32 user-side data, L52 nothing here may
touch scoring/ranking without tribunal / MAJOR / MINOR), FILE + LINE, the EVIDENCE you read (quote
it), and the FAILING SCENARIO. Say "none found" rather than inventing.

(Q1) Is `p2-live-settings.yaml` VALID against `CardSettings` as written in `src-settings-card.py`?
Trace it yourself: `radar.cards_enabled: true` with only `card.shadow_promotion_bar` set, no
`card.proposed_key`, no `card.curves`. Does `_enabled_needs_bands_and_curves`
(`src-settings-card.py`, look for that method) accept or refuse this? `facts.md` §0 claims it is
REFUSED with a specific error string — confirm or contradict that from the code alone, and say
whether `card.alignment_default`/`card.shadow_promotion_bar` are anywhere required by that same
validator (facts.md claims they are NOT — only `card.proposed_key`/`card.curves` are).

(Q2) Does enabling (if the file were valid) do ONLY what facts.md §5 says — a `/radar` panel
becoming visible with hollow, tappable dots and no card_score until tapped — or does anything in
`src-settings-card.py`/`src-radar-evaluate-desk_shadow.py` suggest a sizing change, a new alert, a
Mattermost/heartbeat notification, or a vault write beyond the pre-existing `save_card` key-tap
path? Is there anything here that would let an engine-computed value (e.g. `card.alignment_default`
or a shadow dot grade) replace Dejan's own hand input on a card face rather than merely being
mirrored into a reason string (L7 — no engine-fed value silently promotes)?

(Q3) `card.alignment_default` is ABSENT from `p2-live-settings.yaml`. `facts.md` §2 claims this
is inert either way, because `src-radar-evaluate-desk_shadow.py`'s `desk_shadow()` hardcodes
`DEFAULT_UNRULED` for both alignment dots regardless of any setting, and separately claims the
plan's own record (`plan-s2-p2-excerpt-step5-10.md`, Astra R2-6) rejects the only numeric mapping
ever proposed (10/6/4) and directs "ship N/A" through S2. Verify both halves from the files given:
does `desk_shadow()` read `card.alignment_default` anywhere, and does the plan excerpt say what
facts.md says it says?

(Q4) `card.shadow_promotion_bar` is set to `{sessions: 10, pairs: 30, median_max: 1,
within2_min: 0.90}`. Does `plan-s2-p2-excerpt-step5-10.md` actually cite these exact four numbers
as the "09-14 group-2 ruling," and does `src-cards-shadow_report-excerpt.py` read this setting the
way facts.md describes (refuses loud if unset, never defaults, never itself flips anything)?

(Q5) Is the rollback real? `p2-dark-settings.yaml` in this packet — does its sha256 match
`945e42f86997559267b2e7c20783f2d023b9135ae4bb437ca25a4999ca7cd3ca` exactly (recompute it if your
sandbox allows a hash of a pasted/read file; otherwise say UNVERIFIABLE FROM READS)? Does
`golive.diff` show ONLY the two changes `facts.md` claims (cards_enabled false→true,
`shadow_promotion_bar` added) with nothing else touched?

(Q6) Restart / market-reset: does `src-session-guard-assert_writable.py` gate this write on
anything besides the `MARKET_RESET` session, and does `src-session-clock-windows_for.py` support
facts.md's claim that a non-trading day (`is_trading_day` false) never produces `MARKET_RESET`
(falls through to `OVERNIGHT` instead)? Does anything in `src-settings-store.py`/
`src-settings-card.py` suggest a resident process needs restarting for this change to take effect,
or does `CardSettingsReader.current()` genuinely re-read on every call?

(Q7) Anything that behaves differently at 04:00 ET premarket specifically vs regular trading
hours — a different code path, a different gate, a different default — for THIS settings load or
for the radar's first evaluate cycle after it? Say "none found in these files" if so, and name
what you could not check from reads alone (e.g., the scan scheduler itself is not in this
packet).

(Q8) Cross-cutting: any secret, credential, path, or connection string visible in any file? Does
`p2-live-settings.yaml` or the diff touch any key outside the five named in
`src-settings-card.py`'s `CARD_SETTING_KEYS`? Does anything here look like a second
implementation of a rule that already exists elsewhere (L3)?

End with exactly one line:
`VERDICT: FILE VALID-AS-DRAFTED / FILE INVALID (name why) / UNSAFE TO APPLY (name why)`
