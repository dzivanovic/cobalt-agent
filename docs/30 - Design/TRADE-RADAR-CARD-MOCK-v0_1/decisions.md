# Decisions — Trade Radar Card v0.1

Format: decision · why · rejected alternative.

1. **Four live states + terminal, one card.** The same component renders WATCH → ARMED → TRIGGERED → IN-TRADE → TERMINAL. *Why:* the trader learns one layout; state changes are content changes, not screen changes. *Rejected:* separate widgets per state.

2. **Every field carries an owner badge (COBALT / YOU / N/A MANUAL).** *Why:* in the second before a trigger the trader must know whether a number is machine-read or their own; a missing structural stop is the single most dangerous silent failure, so it is solid red. *Rejected:* colour-only coding, tooltips.

3. **TRIGGERED shows exactly three numbers + hotkey.** Key · Shares · Stop at 34px. *Why:* it is the phone alert; anything else is noise at arm's length. *Rejected:* including distance, health, or why-line.

4. **Semaphore dots stay dots; grades live in the expander.** *Why:* a row of 8 coloured dots reads in < 1 s; eight numbers do not. *Rejected:* inline numeric grades.

5. **Judgment dots are hollow and scored by tap → 1–10 strip.** *Why:* precision without fumbling on a phone; hollow makes "you haven't weighed in" visible. *Rejected:* drag slider, tap-to-cycle, pre-filled neutral 5.

6. **Rank score is opaque (not a shown sum).** *Why:* per-dot weights (Catalyst 2.0, Spread 1.5…) are a likely next step; a visible sum would break when weights land. *Rejected:* "7 + 8 + 5 = 20" style breakdown on the card. The detail column does show conviction and proximity separately.

7. **ARMED / IN-TRADE always pin above WATCH regardless of score.** *Why:* live risk must never slide out of view because a fresh setup scored higher.

8. **Promote moves position, not rank.** Rank chip unchanged when a trader pulls a row to #2; a `promoted · release` button undoes it. *Why:* keeps "what Cobalt thinks" and "what you chose" both legible. *Rejected:* re-ranking on promote.

9. **Single ladder replaces the three-slot layout (v0.1 final).** #1 and #2 open by default; every row expands to card + detail column. *Why:* the radar must live beside DAS at one-card width (~750px) or widen to show detail — a fixed two-up grid cannot do both. *Rejected:* leader/adjacent/queue slots; a separate phone layout on desktop.

10. **Detail column is right of the card, drops below when narrow.** *Why:* extra data (rank breakdown, levels, notes/chart/news) is free real estate that grows with the window while the card keeps its width.

11. **Stop is editable in WATCH and IN-TRADE; key is frozen once armed.** *Why:* stops move with structure; the key is a risk commitment. Stop edits recompute shares/risk/targets/room live; override shows amber `YOURS` + delta + `↺` reset placed on the note line so the metrics grid never reflows. *Rejected:* ±1¢ only; reset inline with the input (overflowed the column).

12. **Stop input is a text field with a draft buffer, commit on Enter/blur.** *Why:* a `number` input re-rendered on each keystroke and its spinner hijacked digit keys. *Rejected:* controlled numeric input.

13. **Scale-out buttons are ½ off / ⅓ off / flat / reset, compounding off running shares.** *Why:* matches DAS hotkey behaviour exactly; typed count remains the precise control. *Rejected:* preset % ladders per grade (deferred, see open-questions).

14. **Day-mode floors to ¼ before 09:00, shown in amber.** *Why:* mirrors the hotkey file's premarket rule; the trader should see the floor, not wonder why sizes are small.

15. **Fill recompute warns at > 20 % distance drift.** *Why:* a bad fill can make a structural stop non-structural; the card says "re-read the level" rather than silently resizing.

16. **Typography: mono for every number and control, sans for prose.** *Why:* numbers align and scan; prose stays readable. Emoji avoided except the single 🔒 on the armed strip.
