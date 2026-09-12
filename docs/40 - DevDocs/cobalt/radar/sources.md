# `src/cobalt/radar/sources.py`

Derives archiver and backfill targets from validated Lists-note blocks. The CLI validates and reports both notes, the pool references, budget, hashes, and archive targets. An archiver comparison mismatch exits nonzero. The retired YAML schema lives here only for proposal/equality proofs; the archiver never loads it.
