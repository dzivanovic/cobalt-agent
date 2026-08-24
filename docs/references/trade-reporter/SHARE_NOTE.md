# Trade Reporter — Share Note

Small Flask app that generates two trading documents:

- **PlayBook** (`.pptx`) — fills the official SMB PlayBook template with your text and chart screenshots.
- **Daily Report Card** (`.pdf`) — generated from scratch with reportlab, no template file needed.

## What's in this archive

Source code only (~24 KB): Flask backend (`app.py`), builders (`utils/`), web UI (`static/`, `templates/`).

## What's NOT included (proprietary)

The **SMB PlayBook template** is proprietary and has been removed from this archive.
To use the PlayBook generator, you must supply your own licensed copy:

```
trade-reporter/
└── assets/
    └── SMB_PlayBook_Template_2024.pptx   ← place your copy here
```

Without it, the app still runs — the Daily Report Card works normally; the PlayBook
endpoint returns a clear "template missing" error.

## Setup

```bash
cd trade-reporter
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open the local URL printed in the console.

## PlayBook builder behavior (template-first)

The generator respects the SMB template rules:

- **Section order** follows the official SMB structure: Title → Big Picture → SPY → QQQ →
  Intraday Fundamentals → Technical Analysis → Trade Strategy → Trade Management →
  Risk Management → Reading the Tape → Technology → Trade Review → Score Card.
- **Unused slides are hidden** (PowerPoint "Hide Slide"), never deleted — the 17-slide
  template structure stays intact.
- **Section titles are enforced in Lato Bold CAPS**, per the template's own instructions.
- **Charts are fitted** into the template's picture zones (aspect ratio preserved, centered),
  so logos and disclosure areas are never covered.
- The Big Picture section auto-selects the best template layout depending on whether you
  provide zero, one, or two index charts (SPY/QQQ).

## Notes

- Disclaimer slide is always kept visible in the output.
- The Score Card table only fills grades whose labels match the template rows exactly
  (e.g. "Preparation", "Execution").
