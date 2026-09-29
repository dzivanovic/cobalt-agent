# `src/cobalt/drc/template.py`

## What it does
HIS DRC template is the one template of the DRC note (DRC D3-1, v2 `[F-20]`, R65 d).

- `template_path(vault_root)` — `<vault>/<prefill.yaml drc_template>` (`5 - Templates/DRC.md`); an unset key is a `TemplateError`, never a default path.
- `read_template(vault_root)` — his file's text; absent → `TemplateError` naming the path.
- `render_template(text, day)` — replaces ONLY `{{date:YYYY-MM-DD}}`; any other `{{` raises `TemplateError` naming the 1-based line. No Jinja, no Templater. His example trade blocks and example If/Then copy through untouched (R98).
- `note_path(vault_root, day)` — `review_dir` + `drc_filename_pattern` from `load_prefill_paths()`: the same values the 21:10 miss line, the 09:00 reader and the S2 smoke use.

## The fixture
`tests/fixtures/drc/template_shape.md` is his template's SHAPE (L32 / L45): the 17 heading lines and the 2 token lines in order, every text line a neutral placeholder, the same 187 lines. X-T (the build report) counted both files; seven of his headings carry U+00A0, which the build seat's tools could not write — the fixture has U+0020 there (ESCALATE).
