"""The formation registries (FINAL §2.2–2.5; setups one build STEP-2).

Formation is data-driven, keyed by the definition's own data — never by a
trade name (L31/L32, `anatomy/registry.py`):

    TRIGGERS         trigger.type            -> TriggerResolver   (triggers.py)
    STOPS            stop.placement.type     -> StopResolver      (stops.py)
    STRUCTURAL_REFS  StructuralRef           -> ref resolver      (stops.py)
    ATOMS            atom text               -> AtomResolver      (atoms.py)
    RELATIONS        relation word           -> RelationResolver  (atoms.py)

`registry.evaluability` reads these same tables (L3, §2.5). A future brick is
one resolver plus one row here; the stage, the registry and the card are
untouched.
"""
