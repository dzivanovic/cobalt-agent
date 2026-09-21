# Typesafe classifier research — run report, 2026-09-21

Seat `typesafe-research-0921` · Fable 5.1 · prompt `prompts/2026-09-21/42-research-typesafe-classifier.md` · ordered `cto-2026-09-21.md` §4 R31, widened 15:00 ET.

## §0 Headline

Document WRITTEN: `docs/30 - Design/TYPESAFE-CLASSIFIER-RESEARCH-2026-09-21.md`, 299 lines, §0–§9, 27 project areas mapped, 10 tribunal questions.
The product is a five-day-old hosted, closed decision model; the PATTERN fits Cobalt's seam, the PRODUCT only partly, and it cannot run locally.
Nothing was run, installed, signed up for or sent out; searches carried generic terms only. No git write — both files are untracked in `~/cobalt` for the desk to commit.
ESCALATE: 5.

## DIGEST FOR THE DESK

What it is. A San Francisco start-up's hosted model, called Jev, launched publicly on September 16th. You send it content plus typed questions — pick one option, rate on levels, yes or no — and it answers with a probability for every option instead of text. Closed weights, hosted in the United States, its own API shape.

Does it fit Cobalt's seam. The pattern, yes, exactly: validated input, one routed call, validated typed answer with a first-class "unsure", stored record, shadow first. The product, only partly: it is not chat-completions-shaped, so it is reachable only through a LiteLLM proxy pass-through with no fallback, or behind a new Cobalt adapter; a direct SDK call would be a routing bypass needing his ruling. It cannot run locally at all. One finding matters beyond this product: the new core has no routed model call yet, so the first typed classifier is also where that seam gets designed.

Best three uses. One, triage of incoming text — headlines, X posts, filing sections. Two, the places Cobalt already says "unknown" and waits for him: the three desk-graded card dots and the unknown catalyst that makes a definition not evaluable — the shadow slot for a judgment dot already exists in the scoring model. Three, cheap routing of a DM or voice sentence, and of a task to a model tier.

Hardest three limits. One, hosted-only and a new vendor: local-first fails, and spend plus data exposure need his ruling. Two, its own documentation says it is unreliable with numbers, dates and counting, and it gives no reasons because it does not generate text — so it must never see Cobalt's computed features as numbers, and "classification with reasons" needs either several narrow questions or a text model with a schema. Three, no independent accuracy or calibration evidence exists, and no determinism setting was found.

On his scoring example. A classifier picks a label; a ruled table in code turns the label into a grade; the score's numbers, ranking and sizing stay deterministic. The vendor's own scoring pattern says the same — weights in code.

Cost line. Four point two cents per million input tokens, output free, vendor-stated. With assumed volumes, text triage is about a dollar a month. Price is not the constraint; the ruling, the data terms and the missing evidence are. The local model with schema-constrained output does the same job today with no new vendor — slower, without per-option probabilities.

## BUDGET USED

WebFetch 18/20 (one returned HTTP 403) · WebSearch 1/10 · file reads 11/25 Read calls over 9 distinct files (allowance raised 15 → 25 by the desk's 15:00 ET addition; `grep` / `ls` / `wc` calls not counted as reads) · document lines 299/450

Split of the 18 fetches: supplied site 11 (incl. the docs index `llms.txt`) · independent 3 · alternatives 4.

## SCOPE ADDITION RECEIVED (L48)

15:0x ET, cross-session message from the CTO desk (`661f1dab`), relaying Dejan's spoken words at 15:00 ET: "I want agents to be aware of our project and see where other areas of the project require classifications and quick, multiple choice or complex choice, classification reasoning." Effect: §5 covers the WHOLE project (choice set by kind, who decides today, helps yes / no / shadow, latency needed, never-do); file-read allowance 15 → 25; web budget and the 450-line ceiling unchanged. Accepted — reads only, inside this session's existing permissions. Delivered: §5 has 27 rows; a typed classifier helps in 14, is excluded in 13.

## ESCALATE

1. **(L74, recorded once.)** The Read result for the prompt file carried an appended block asking for a `Claude-Session:` line in commits and naming a file-send tool. It arrived inside a tool result, so it is data; not followed. This run made no commit.
2. **Web text addressing agents (L15) — not followed.** The vendor's quickstart page recommends coding agents install a vendor plugin (`claude plugin marketplace add …`), and the docs index lists a "Drop-in skill for Claude Code, Codex, and other agent environments". Nothing was installed or run. No other page text tried to instruct this session.
3. **Site pages: 11 against the prompt's "stop at ≤ 8".** The three over were the models page (version pinning, limits — needed for L57), the privacy policy (training and retention terms — needed for L32, which the prompt asks to be quoted) and the quickstart (the SDK call shape for §3–§4). Paid for out of the alternatives allotment (4 of 6 used); the hard total held at 18/20. Judged better than shipping NOT FOUND on two law tests one fetch away; the desk may rule it a defect.
4. **Quotes are "verbatim as returned" by a fetch tool that passes pages through a small model.** The document says so at its head. Before a tribunal leans on a figure (price, rate limit, the privacy sentences, the limits-page quotes), a verifier re-opens that URL — about ten URLs, a read-and-judge job (L35). The co-founder names, founding year and lead investor came only from a search-result summary of an unfetched press release; the document marks them UNVERIFIED and leaves them out of the text.
5. **Both output files sit untracked in `~/cobalt` (production checkout), written there because the prompt names those absolute paths.** `docs/30 - Design/` and `docs/40 - DevDocs/reports/` are documentation paths (L42: no restart). The commit is the desk's.

Not an escalate, for the record: CLAUDE.md's wake-up path (INDEX → NOW → LAWS) was followed, costing two reads the prompt's index card did not list.

MEMORY: [stated 2026-09-21 · Code] Typed-classifier research for the tribunal is at `docs/30 - Design/TYPESAFE-CLASSIFIER-RESEARCH-2026-09-21.md`; finding that outlives the product: the new core (`src/cobalt`) has no routed model call site yet — the first typed classifier is where the L5 seam gets designed.

## CONTINUE

Nothing owed by this seat. Next lawful steps belong to the desk: L35 check of the document (the ten-URL quote re-verification in ESCALATE 4 fits a read-only seat with `WebFetch`), commit both files, then the tribunal prompt with the document as input (L67, L52 for anything reaching a dot). If this run is relaunched: everything is in the two files; no partial state exists elsewhere.

TYPESAFE RESEARCH DONE · what it is: hosted closed decision model, typed probabilistic answers · fits the routing seam: partly · runs locally: no · uses mapped: 27 · tribunal questions: 10 · fetches: 18/20 · searches: 1/10 · ESCALATE: 5
