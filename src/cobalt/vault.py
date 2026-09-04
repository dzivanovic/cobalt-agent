"""ONE vault-path resolver for the new core.

TRIAGE 2.6 ruling: `obsidian_vault_path` resolution is KEEP-CONCEPT /
REBUILD — "ONE resolver; closes CLAUDE.md's OPEN ITEM." This is that
resolver, for `src/cobalt/*` only.

RULING 7 (2026-09-04) — `COBALT_ENV` now gates this resolver the same
way it gates the database (`cobalt/env.py`). `resolve_env()` is called
FIRST: unset or unknown raises `EnvConfigError` before any path work
happens. There is no longer an implicit "no flag means dev" branch.
`production` resolves to `PROD_VAULT_PATH_REFERENCE` on its own; `dev`
resolves from `COBALT_VAULT_PATH` or `configs/dev/vault.yaml`. Every
sentence below that says "COBALT_ENV unset" describes the pre-RULING-7
behaviour and is kept for the history of the guards, not as current
behaviour — unset now simply raises.

Single source for the DEV root: `configs/dev/vault.yaml`'s
`obsidian_vault_path`, overridable by the `COBALT_VAULT_PATH` env var.
Fail-loud: unset (no config file and no env override) or a path that
doesn't exist on disk both crash with `VaultConfigError` — never a
guess, never a silent fallback.

NN#16 dev/prod vault split (formalized 2026-08-31): `configs/dev/
vault.yaml`'s committed value is the DEV default — `~/dev-vault-cobalt`
(`PROD_VAULT_PATH_REFERENCE` below), a skeleton copy (Templater
templates + Rules.md, no personal notes/trades) kept outside the repo,
same as the real vault. It is NOT auto-created or synced — see its own
DevDoc entry for how to reseed it. PRODUCTION reaches the real vault
(`/Users/cobalt/Vault/Think`) by setting `COBALT_VAULT_PATH` explicitly
in its own environment — `ops/start_aset.sh` (the ASET LaunchAgent's
wrapper) and the two `ops/com.cobalt.prefill-*.plist` files all do this
in their `EnvironmentVariables`. A bare interactive `uv run` with no
override therefore defaults to dev/safe — touching the real vault
always requires an explicit, visible opt-in, never the default.

Deliberately NOT touching the old tree's four-way ambiguity (.env
`OBSIDIAN_VAULT_PATH` vs `configs/config.yaml` vs `config.py:69`'s
hardcoded default vs `scribe.py`'s own env/~/Documents fallback) — that
stays exactly as it is; the old tree's scribe keeps pointing wherever it
already points. `COBALT_VAULT_PATH` is a deliberately distinct env var
name from `OBSIDIAN_VAULT_PATH` so setting it can never bleed into old-
tree behavior.

Defect 1 (2026-09-01): the ASET LaunchAgent kept running for 6+ hours
against `~/dev-vault-cobalt` after `ops/start_aset.sh` gained its
COBALT_VAULT_PATH override (79943f6) — that commit's own message
flagged the running process predated the fix and needed a manual
`launchctl kickstart`, which never happened. Env vars are fixed at
process launch; a code/config deploy alone can't fix a live process.
`COBALT_ENV=production` (set only by ops/start_aset.sh and both
ops/com.cobalt.prefill-*.plist) is the launchers' own explicit
declaration of intent — resolve_vault_path() refuses outright when that
flag is set but the resolved root isn't the real vault, so a stale
process fails loud on its very next resolve instead of silently
appending to the wrong vault all day. A dev run (COBALT_ENV unset)
never sets this flag, so the NN#16 dev-safe default is untouched.

Inverse guard (2026-09-02, "TSLA id 127" incident forensics): the
2026-09-01 fix above only refused a PRODUCTION-declared process that
resolved somewhere other than Think. It never refused the opposite —
a dev-declared process (COBALT_ENV unset/non-production) that somehow
resolves INTO Think (a manually-exported COBALT_VAULT_PATH, a hand-run
`uv run` with a stray env var, etc.). That investigation found no
process had actually done this — the incident's real cause was
elsewhere (see the daily-note append verification added in
aset/daily_note.py) — but the gap itself is real and symmetric with
the forward guard, so it's closed here too: a non-production run that
resolves under PROD_VAULT_PATH_REFERENCE now refuses the same way,
unless `COBALT_ALLOW_DEV_ENTRY=1` is set as an explicit, deliberate
override (e.g. a one-off manual test against the real vault).
"""

import os
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from cobalt import env

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "configs" / "dev" / "vault.yaml"
ENV_OVERRIDE = "COBALT_VAULT_PATH"
ENV_MODE = "COBALT_ENV"
PROD_ENV_VALUE = "production"
ALLOW_DEV_ENTRY_ENV = "COBALT_ALLOW_DEV_ENTRY"

# The production vault root. RULING 7 (2026-09-04) promoted this from a
# documentation-only constant to the value production actually resolves
# to: with COBALT_ENV=production and no COBALT_VAULT_PATH, this IS the
# answer. The plists still set COBALT_VAULT_PATH explicitly — belt and
# braces, and it keeps "what does prod point at" greppable in ops/ — but
# production no longer DEPENDS on that env var being present.
PROD_VAULT_PATH_REFERENCE = "/Users/cobalt/Vault/Think"


class VaultConfigError(RuntimeError):
    """Vault path unset, misconfigured, or missing on disk — crash loudly."""


class VaultWriteRefused(RuntimeError):
    """A resolved write target is unsafe — refuse, never guess."""


class VaultConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    obsidian_vault_path: str = Field(min_length=1)


def is_production() -> bool:
    """True in production. RULING 7: raises if COBALT_ENV is unset — the
    mode is never inferred from the absence of a flag any more."""
    return env.is_production()


def dev_entry_allowed() -> bool:
    return os.getenv(ALLOW_DEV_ENTRY_ENV) == "1"


def resolve_vault_path() -> Path:
    """Return the new core's single vault root, or raise.

    RULING 7: `COBALT_ENV` is resolved FIRST and unconditionally, so an
    unset mode fails here exactly as it fails for the database — there
    is no longer an implicit "no flag means dev" path. In production the
    root defaults to `PROD_VAULT_PATH_REFERENCE`; in dev it comes from
    `COBALT_VAULT_PATH` or `configs/dev/vault.yaml`.
    """
    mode = env.resolve_env()  # raises EnvConfigError when unset/unknown

    env_val = os.getenv(ENV_OVERRIDE)
    if env_val:
        raw, source = env_val, f"env:{ENV_OVERRIDE}"
    elif mode == env.PRODUCTION:
        raw, source = PROD_VAULT_PATH_REFERENCE, f"{ENV_MODE}={PROD_ENV_VALUE}"
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
    resolved = path.resolve()

    prod_root = Path(PROD_VAULT_PATH_REFERENCE).resolve()
    if mode == env.PRODUCTION:
        try:
            resolved.relative_to(prod_root)
        except ValueError:
            raise VaultConfigError(
                f"REFUSED: {ENV_MODE}={PROD_ENV_VALUE} but the resolved vault "
                f"root (from {source}) is {resolved}, not {prod_root} or a path "
                "under it. This process likely predates a vault-config fix and "
                "needs a restart — see PROD_VAULT_PATH_REFERENCE's DevDoc."
            )
    elif not dev_entry_allowed():
        try:
            resolved.relative_to(prod_root)
        except ValueError:
            pass  # dev run resolved outside prod — the expected, safe case
        else:
            raise VaultConfigError(
                f"REFUSED: a non-production run (no {ENV_MODE}={PROD_ENV_VALUE}) "
                f"resolved into the production vault ({resolved}, under "
                f"{prod_root}) from {source}. This looks like a stale tab or "
                "misconfigured dev process about to write live trading data "
                f"through a dev instance. Set {ALLOW_DEV_ENTRY_ENV}=1 if this is "
                "a deliberate one-off."
            )

    return resolved


def assert_within_vault(path: Path) -> None:
    """Refuse unless `path` resolves OUTSIDE the repo working tree.

    Shared safety gate (one-path rule) for every new-core module that
    writes into the vault (aset/daily_note.py, prefill/*). The vault
    lives outside the repo by design (see the module docstring's
    "outside the repo" property) — a target resolving INSIDE the repo
    means vault resolution went wrong somewhere upstream, so refuse
    rather than risk a write landing in git history.
    """
    resolved = path.resolve()
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError:
        return  # not inside the repo — safe
    raise VaultWriteRefused(
        f"REFUSED: resolved target {resolved} is INSIDE the repo working "
        f"tree ({REPO_ROOT}) — the vault must live outside the repo, never inside it."
    )
