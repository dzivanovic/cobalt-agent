"""HIS DRC template — the one template of the DRC note (DRC D3-1, v2 §6
`[F-20]`, R65 d, R98).

    template_path(vault_root)       <vault>/<prefill.yaml drc_template>
    read_template(vault_root)       his file's text, or TemplateError
    render_template(text, day)      ONLY `{{date:YYYY-MM-DD}}` replaced
    note_path(vault_root, day)      <vault>/<review_dir>/<drc_filename_pattern>

THE ONE SUBSTITUTION. The literal `{{date:YYYY-MM-DD}}` becomes the ISO
date; ANY other `{{` fails the build naming its line (L1): his template is
his, and a token Cobalt does not know is never guessed at. No Jinja, no
Templater. His example trade blocks and example If/Then copy into every
DRC as they are (R98): nothing is stripped.

THE PATHS come from `configs/cobalt/prefill.yaml` through
`load_prefill_paths()` — the same `review_dir` + `drc_filename_pattern`
the 21:10 miss line (`replay.line.drc_note_path`), the 09:00 reader and the
smoke read. Never a hard-coded path (L3).
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from cobalt.prefill.config import load_prefill_paths

#: The ONE token his template carries (X-T: two lines, both this token).
DATE_TOKEN = "{{date:YYYY-MM-DD}}"


class TemplateError(ValueError):
    """His template is missing, unconfigured, or carries a token Cobalt does
    not replace — the build FAILS naming it (L1)."""


def template_path(vault_root: Path) -> Path:
    rel = load_prefill_paths().drc_template
    if not rel:
        raise TemplateError(
            "configs/cobalt/prefill.yaml names no drc_template — the DRC build reads his template "
            "and nothing else (L1)"
        )
    return Path(vault_root) / rel


def read_template(vault_root: Path) -> str:
    path = template_path(vault_root)
    if not path.is_file():
        raise TemplateError(f"his DRC template is not at {path} — nothing built (L1)")
    return path.read_text(encoding="utf-8")


def render_template(text: str, day: date) -> str:
    """`text` with every `{{date:YYYY-MM-DD}}` replaced by `day`; any other
    `{{` raises `TemplateError` naming the line (1-based)."""
    out: list[str] = []
    for n, line in enumerate(text.split("\n"), start=1):
        rendered = line.replace(DATE_TOKEN, day.isoformat())
        if "{{" in rendered:
            raise TemplateError(
                f"his DRC template, line {n}: a token other than {DATE_TOKEN} — only the date is "
                "replaced; nothing built (L1)"
            )
        out.append(rendered)
    return "\n".join(out)


def note_path(vault_root: Path, day: date) -> Path:
    paths = load_prefill_paths()
    return Path(vault_root) / paths.review_dir / day.strftime(paths.drc_filename_pattern)


__all__ = ["DATE_TOKEN", "TemplateError", "note_path", "read_template", "render_template", "template_path"]
