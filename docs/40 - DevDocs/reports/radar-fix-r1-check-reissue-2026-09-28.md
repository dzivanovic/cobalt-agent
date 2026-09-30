## §0 Headline
- `51` re-issued whole in place: seats Opus 5.5 · Sol · Grok (L67); the Astra seat is gone (`grep -c -i -F "astra"` = 0).
- Changed lines of `51`: 1, 20, 43, 48, 52, 53 (`diff` against `HEAD`); every other line is byte for byte. `50` untouched.
- Sol slug `gpt-5.6-sol` — the highest in `~/.codex/models_cache.json`; new rule strings: 0. ESCALATE: 1 (a note).
- Authorization verified: `cto-2026-09-28.md` line 152, row R143. Nothing committed.

## L74
No block asking for a `Claude-Session` line or naming a file-send tool arrived inside a tool result.

## CHANGES
| # | old line | new line | source |
|---|---|---|---|
| 1 | line 1 SEATS: `(as round 1; 09-23 R95 / R97): Opus 5.5 · Astra · Grok — NO Sol, NO Gemini` | `(L67 — a fix round is an "other check"; not round 1's seats, R142): Opus 5.5 · Sol · Grok; when the OpenAI meter is short, Opus + Grok — NO Gemini` | `43:1` (seats + meter-short rule) |
| 2 | line 1 FLOOR: `at least ONE of them is Astra or Grok` | `… is Sol or Grok` | spec |
| 3 | line 1 allow string: `Bash(codex exec … -m gpt-6-astra -s read-only *)` | `Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)` (same position, list stays 10 allow + 3 deny) | `43:1` |
| 4 | line 1 RULE STRINGS: `but this file's path and … ; comm against 47 → EMPTY` | adds the Sol string in place of `47`'s `codex exec` string, names `43` line 1 as its precedent; the comm check reads "EMPTY but the one `codex exec` pair, and the Sol string found by `grep -c -F` in `43` line 1" | `43:1` |
| 5 | line 20 probe: `ASTRA codex exec … -m gpt-6-astra -s read-only "Reply with only the word OK."` | `SOL codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | `43:47` |
| 6 | line 20 floor: `neither Astra nor Grok UP` | `neither Sol nor Grok UP` | spec |
| 7 | line 43 seat: `- **ASTRA:** codex exec … gpt-6-astra … "You are GPT-6 Astra (OpenAI), …"` | `- **SOL:** codex exec … gpt-5.6-sol … -c model_reasoning_effort="high" "You are SOL (OpenAI), …" < /dev/null`, `run_in_background`; the prompt body is unchanged | `43:76` |
| 8 | line 43 answer file: `S/astra-check.md` / `S/astra-check.partial.md` | `S/sol-check.md` / `S/sol-check.partial.md` | `43:1` (`sol-check.md`) |
| 9 | line 48: `Q · opus · astra · grok` | `Q · opus · sol · grok` | `43:81` shape |
| 10 | line 52 standing line: `Opus 5.5 (R109) · Astra · Grok (L67, R95)` | `Opus 5.5 (R109) · Sol · Grok (L67)` | `43:89` |
| 11 | line 53 stop line: `astra: <…>` | `sol: <…>` (order stays opus · sol · grok) | `43:92` |

## PROOF
- `grep -c -i -F "astra"` on the new `51`: **0** (old `51`: 6 lines).
- `diff` of `git show HEAD:<51>` against the new `51`: changed lines 1, 20, 43, 48, 52, 53 only. Launch-row placeholders and `FILL AT LAUNCH` values were not touched.
- Each of the 13 quoted tokens of the new launch line, `grep -c -F` in `43` / old `51`:

| token | `43` | old `51` |
|---|---|---|
| `Bash(grok *)` | 1 | 1 |
| `Bash(codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only *)` | 1 | 0 (replaced `-m gpt-6-astra`) |
| `Bash(claude -p --model claude-opus-5-5 *)` | 1 | 1 |
| `Bash(git -C /Users/cobalt/cobalt show*)` / `log*` | 1 / 1 | 1 / 1 |
| `Bash(ls *)` `grep *` `tail *` `wc *` `date*` | 1 each | 1 each |
| `AskUserQuestion` / `EnterWorktree` | 2 / 2 | 3 / 3 |
| `Bash(git push*)` | 1 | 1 |

  The allowlist is 13 tokens before and after. The one new-to-`51` string is `43`'s Sol string, so the new rule strings count is 0.
- Sol slug: `gpt-5.6-sol` (slugs in the cache: `gpt-6-astra`, `gpt-reserve`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.5`). Nothing newer than `gpt-5.6-sol`.
- Classification report `## ESCALATE` 1 read: the same L67 miss this re-issue fixes.

## ESCALATE
1. Note, no question: `51`'s AUTHORIZATION "THE SEATS" gate still greps `cto-2026-09-23.md` R95 (the Astra row) and R109. It has no Astra text, so per "every other line stays byte for byte" it was left. The desk may drop R95 from that gate at launch.

## CONTINUE
done: authorization, reads, `51` re-issued, proof, report. Nothing left to run.

RADAR FIX R1 CHECK REISSUED · seats: opus sol grok · astra lines: 0 · sol slug: gpt-5.6-sol · new rule strings: 0 · ESCALATE: 1
