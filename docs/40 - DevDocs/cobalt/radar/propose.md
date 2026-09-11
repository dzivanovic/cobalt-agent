# `src/cobalt/radar/propose.py`

Builds deterministic Screens/Lists proposal artifacts with provenance, target-note hashes, canonical JSON hashes, and exact final units. Apply verifies artifact and target hashes, performs no derivation or network access, and writes only through `VaultWriter` after HITL.

