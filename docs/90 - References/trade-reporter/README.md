# BigScalp Edge

Local trading review system based on SMB-style templates.

## Features

- Daily Report Card → 1-page PDF
- PlayBook → PPTX generated from the SMB template workflow
- Drag & drop, click upload, or paste screenshots
- Local-only: no API, no cloud upload

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python app.py --no-reload
```

Then open: http://127.0.0.1:5002

## Required project files

Keep your existing `utils/` folder with:

- `utils/drc_builder.py`
- `utils/playbook_builder.py`

and any SMB template files required by those builders.
