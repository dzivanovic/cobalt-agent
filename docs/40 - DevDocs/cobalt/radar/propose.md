# `src/cobalt/radar/propose.py`

Builds deterministic Screens/Lists proposal artifacts with provenance, target-note hashes, canonical JSON hashes, and exact final units. The bounded field parser accepts bare labels and both bold-colon forms, extracts annotated filter tokens without interpreting their glosses, reconciles pasted/export URLs locally, resolves inline or standalone columns, and recognizes explicit `after HH:MM` starts. A missing prose endpoint uses the configured scanning-session endpoint and is marked `# PROPOSED`. Relevant verbatim source lines remain adjacent to each generated field.

Lists proposal requires an explicit `--watchlists-yaml` input because the committed migration source was retired after the Lists note became authoritative. It carries the source YAML's complete leading derivation commentary into readable note prose. Tests materialize the fixed historical Git blob only under `tmp_path`.

`screens validate` shares the same derivation path, hashes current note bytes, validates the supplied pool and actual/prospective Lists, checks the ruled request budget, and compares prose-derived fields with installed YAML. It performs no network, DB, vault, or proposal write.

Apply uses only the recorded artifact units and performs no derivation or network access. Before constructing the audit store or writer, it verifies the artifact and target hashes, note absence/block state, non-empty HITL token, session, and environment-to-vault match. Only then does it write through `VaultWriter`.
