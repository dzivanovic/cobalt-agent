---
status: Done
priority: P0
module: Brain
complexity: S
---
- _Goal:_ Create `base.py` abstract class to standardize memory storage.
    
- _Why:_ Decouples logic from storage, allowing us to swap JSON for Postgres later without breaking code.