# `src/cobalt/jobs/restarts.py`

Derives resident restarts from changed plists, declared runtime reads, and a static Python import graph. Missing import declarations, unresolved dynamic imports, and unclassified paths are conservative and loud; worktree-ending ranges include untracked files.

