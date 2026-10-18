"""F23: the Sunday playbook decks — one `.pptx` per setup family, plus `unfiled`.

`cobalt playbook render` (`cli.py`) reads the strategy notes through the one
vault loader and the radar cards through one SELECT (`data.py`), builds the
decks with python-pptx (`deck.py`) and swaps them into
`data/playbook/<date>/`. It writes no vault note.

Nothing is imported here: `cobalt.cli` mounts `cobalt.playbook.cli`, and
python-pptx must stay out of that import graph (FINAL [F-17]).
"""
