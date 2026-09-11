# `src/cobalt/radar/propose.py`

Builds deterministic Screens/Lists proposal artifacts with provenance, target-note hashes, canonical JSON hashes, and exact final units. Each prose-derived YAML field has an adjacent verbatim `# from:` comment; a missing prose window uses the configured scanning-session span and is marked `# PROPOSED`. Propose output includes the blocks, an insertion-only unified diff, and the canonical artifact SHA-256 while leaving the target unchanged.

Lists proposal requires an explicit `--watchlists-yaml` input because the committed migration source was retired after the Lists note became authoritative. Tests materialize the fixed historical Git blob only under `tmp_path`.

Apply uses only the recorded artifact units and performs no derivation or network access. Before constructing the audit store or writer, it verifies the artifact and target hashes, note absence/block state, non-empty HITL token, session, and environment-to-vault match. Only then does it write through `VaultWriter`.
