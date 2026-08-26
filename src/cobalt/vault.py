"""ONE vault-path resolver for the new core.

TRIAGE 2.6 ruling: `obsidian_vault_path` resolution is KEEP-CONCEPT /
REBUILD — "ONE resolver; closes CLAUDE.md's OPEN ITEM." This is that
resolver, for `src/cobalt/*` only.

Single source: `configs/dev/vault.yaml`'s `obsidian_vault_path`,
overridable by the `COBALT_VAULT_PATH` env var. Fail-loud: unset (no
config file and no env override) or a path that doesn't exist on disk
both crash with `VaultConfigError` — never a guess, never a silent
fallback.

Deliberately NOT touching the old tree's four-way ambiguity (.env
`OBSIDIAN_VAULT_PATH` vs `configs/config.yaml` vs `config.py:69`'s
hardcoded default vs `scribe.py`'s own env/~/Documents fallback) — that
stays exactly as it is; the old tree's scribe keeps pointing wherever it
already points. `COBALT_VAULT_PATH` is a deliberately distinct env var
name from `OBSIDIAN_VAULT_PATH` so setting it can never bleed into old-
tree behavior.
"""

import os
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "configs" / "dev" / "vault.yaml"
ENV_OVERRIDE = "COBALT_VAULT_PATH"


class VaultConfigError(RuntimeError):
    """Vault path unset, misconfigured, or missing on disk — crash loudly."""


class VaultConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    obsidian_vault_path: str = Field(min_length=1)


def resolve_vault_path() -> Path:
    """Return the new core's single vault root, or raise VaultConfigError."""
    env_val = os.getenv(ENV_OVERRIDE)
    if env_val:
        raw, source = env_val, f"env:{ENV_OVERRIDE}"
    else:
        if not CONFIG_PATH.exists():
            raise VaultConfigError(
                f"Vault path unset: {CONFIG_PATH} not found and "
                f"{ENV_OVERRIDE} not set. Create the config or set the env var."
            )
        data = yaml.safe_load(CONFIG_PATH.read_text())
        if not isinstance(data, dict):
            raise VaultConfigError(
                f"{CONFIG_PATH}: expected a YAML mapping, got {type(data).__name__}"
            )
        try:
            cfg = VaultConfig(**data)
        except ValidationError as e:
            raise VaultConfigError(f"{CONFIG_PATH}: invalid vault config:\n{e}") from e
        raw, source = cfg.obsidian_vault_path, str(CONFIG_PATH)

    path = Path(raw).expanduser()
    if not path.is_dir():
        raise VaultConfigError(
            f"Vault path from {source} does not exist or is not a directory: {path}"
        )
    return path.resolve()
