# `src/cobalt/smoke/config.py`

Loads a suite file. L10 requires that a bad file crash with its line number.

- `SUITES_DIR` = `configs/cobalt/smoke/`; `suite_path(name)` → `<name>.yaml`. The new-core config boundary holds: the file is under `configs/cobalt/`, outside the old loader's top-level glob.
- `SmokeConfigError(path, line, message)`: its text is `path:line: message`, and `.line` is 1-based, or None when the file is unreadable.
- `load_suite(path)`:
  - Reads the text once and parses it twice: `yaml.compose` keeps the node tree with its start marks, and `yaml.safe_load` feeds `SmokeSuite`.
  - A YAML syntax error reports the parser's `problem_mark` line.
  - A Pydantic error walks its location (`checks → 3 → sql → expect → 0 → op`) down the node tree:
    - The union tag (`sql`) is skipped, as is any key the file never wrote.
    - The line reported is that of the deepest node found. A missing required field therefore points at the check's own mapping.
  - The message names the first error and counts the rest.
  - A file that is not a mapping crashes at line 1.

Classification for `cobalt jobs restarts` (L42): a change under
`configs/cobalt/smoke/` derives no restart. The rule is `operator command (cobalt smoke); no job reads`, in `jobs/restarts.py`. The test keeps the claim true: no plist runs `cobalt smoke`, and only `smoke/cli.py` and this file open a suite.
