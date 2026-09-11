# `tests/cobalt/test_radar_propose.py`

Tests the complete step-12 offline matrix with `tmp_path`, mocked HTTP, and recording writer/store doubles. Proposal cases cover prose/filter parity, invalid pool input, field-adjacent provenance, proposed session windows, conditional `ft`, verbatim inputs, insertion-only diffs, and stable artifact hashes. Apply cases cover every required refusal before writer construction plus artifact-only execution with no HTTP or re-derivation. Real audited writes remain outside this offline module's execution path.
