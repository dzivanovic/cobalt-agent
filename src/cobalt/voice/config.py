"""`configs/cobalt/voice.yaml` — schema, loader, and the FINAL §5 path refusals.

L10: Pydantic, `extra="forbid"`, in git. L1: every key is REQUIRED — a
missing key crashes the load; nothing falls back to a default.

`scratch_dir` / `model_dir` follow the vault's pattern (`cobalt.vault`):
the committed value is the DEV path; production sets its own through an
explicit env override (`COBALT_VOICE_SCRATCH_DIR` / `COBALT_VOICE_MODEL_DIR`
in `ops/start_aset.sh`). Whatever the source, the path is REFUSED when it
is relative, or sits under the repo root, under `docs/`, under the
resolved vault (and always under the production vault), or — when the
caller passes them — under any `configs/cobalt/backup.yaml` source
(see `load_voice_config`) — audio must never reach git, the vault or a
backup (R18 (b)). `scratch_max_age_s ≤ stt_timeout_s` is
refused too (G2 / K5).
"""

from __future__ import annotations

import ipaddress
import os
from pathlib import Path
from typing import Literal, Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

from cobalt import vault as vault_mod

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "voice.yaml"
SCRATCH_ENV = "COBALT_VOICE_SCRATCH_DIR"
MODEL_ENV = "COBALT_VOICE_MODEL_DIR"


class VoiceConfigError(RuntimeError):
    """Missing / invalid / unsafe voice config — crash, never fall back."""


class VoiceConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    scratch_dir: Path
    model_dir: Path
    #: No cloud engine exists (W4, L23): the only value is the local one.
    stt_engine: Literal["faster-whisper"]
    stt_model: str = Field(min_length=1)
    stt_revision: str = Field(pattern=r"^[0-9a-f]{40}$")
    stt_compute_type: Literal["int8", "int8_float32", "float32"]
    max_clip_s: float = Field(gt=0)
    max_upload_bytes: int = Field(gt=0)
    stt_timeout_s: float = Field(gt=0)
    confirm_ttl_s: float = Field(gt=0)
    scratch_max_age_s: float = Field(gt=0)
    history_turns: int = Field(ge=0, le=20)
    #: A route NAME in `configs/cobalt/modelaccess.yaml`. The agent registry
    #: validates the route; `load_voice_config` refuses a `plan_route` that is
    #: not EXACTLY the registry's `route` (`_check_plan_route`).
    plan_route: str = Field(min_length=1)
    #: SOCKET-PEER addresses allowed on `/voice/*` (W11 [F-03]). IP
    #: literals only; a header is never the allow key.
    allowed_peers: list[str] = Field(min_length=1)

    @field_validator("allowed_peers")
    @classmethod
    def _ip_literals(cls, v: list[str]) -> list[str]:
        for p in v:
            try:
                ipaddress.ip_address(p)
            except ValueError:
                raise ValueError(f"allowed_peers holds {p!r}: an IP literal is required") from None
        return v


def _under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(Path(root).expanduser().resolve())
    except ValueError:
        return False
    return True


def _check_path(name: str, raw: Path, backup_sources: Optional[list[Path]]) -> Path:
    if not raw.is_absolute():
        raise VoiceConfigError(f"{name} {str(raw)!r} is relative — an absolute path outside repo, vault and backup is required")
    p = raw.expanduser().resolve()
    if _under(p, REPO_ROOT / "docs"):
        raise VoiceConfigError(f"{name} {p} sits under docs/ — refused (FINAL §5)")
    if _under(p, REPO_ROOT):
        raise VoiceConfigError(f"{name} {p} sits under the repo root {REPO_ROOT} — audio never reaches git (FINAL §5)")
    if _under(p, Path(vault_mod.PROD_VAULT_PATH_REFERENCE)):
        raise VoiceConfigError(f"{name} {p} sits under the production vault — refused (FINAL §5)")
    try:
        resolved_vault = vault_mod.resolve_vault_path()
    except vault_mod.VaultConfigError as e:
        raise VoiceConfigError(f"{name}: the vault path could not be resolved to check against ({e})") from None
    if _under(p, resolved_vault):
        raise VoiceConfigError(f"{name} {p} sits under the resolved vault {resolved_vault} — refused (FINAL §5)")
    for src in backup_sources or ():
        if _under(p, src):
            raise VoiceConfigError(f"{name} {p} sits under the backup source {src} — audio never reaches a backup (FINAL §5)")
    return p


def _check_plan_route(plan_route: str) -> None:
    """L3: the agent registry is the route's one home; `plan_route` must
    equal it EXACTLY, or the load crashes naming both (L1)."""
    from .registry import CONFIG_PATH as AGENT_PATH, AgentConfigError, load_agent

    try:
        route = load_agent().route
    except AgentConfigError as e:
        raise VoiceConfigError(f"plan_route: the agent registry could not be read to check against ({e})") from None
    if plan_route != route:
        raise VoiceConfigError(f"plan_route {plan_route!r} is not the agent registry's route {route!r} "
                               f"({AGENT_PATH}) — the two must be the same route name")


def load_voice_config(path: Path = CONFIG_PATH, *, backup_sources: Optional[list[Path]] = None) -> VoiceConfig:
    """The validated voice config, or a loud `VoiceConfigError`.

    `backup_sources`: when given, a path under any of them is refused too.
    The RESIDENT (com.cobalt.aset) does not pass them: reading
    `configs/cobalt/backup.yaml` from a resident would make that file a
    resident read, contradicting `configs/cobalt/jobs.yaml`'s declared
    no-resident-read and L42's derivation (`test_jobs_restarts.py`). The
    vault and repo refusals already cover both of today's sources; the
    suite checks the committed dev paths and `ops/start_aset.sh`'s
    production overrides against every `backup.yaml` source
    (`test_voice_config.py`). Build report ESCALATE carries the choice.
    """
    path = Path(path)
    if not path.exists():
        raise VoiceConfigError(f"voice config not found: {path}")
    try:
        raw = yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None)
        where = f" at line {mark.line + 1}" if mark else ""
        raise VoiceConfigError(f"{path}: YAML error{where}: {e}") from None
    if not isinstance(raw, dict) or not isinstance(raw.get("voice"), dict):
        raise VoiceConfigError(f"{path}: expected a 'voice' mapping")
    data = dict(raw["voice"])
    for var, key in ((SCRATCH_ENV, "scratch_dir"), (MODEL_ENV, "model_dir")):
        value = os.environ.get(var)
        if value is None:
            continue  # unset → the committed (dev) value
        if not value.strip():
            raise VoiceConfigError(f"{var} is set but empty — set a path, or unset it for the committed "
                                   "default; an empty override never falls back (L1)")
        data[key] = value
    try:
        cfg = VoiceConfig(**data)
    except ValidationError as e:
        raise VoiceConfigError(f"{path}: invalid voice config:\n{e}") from None
    _check_plan_route(cfg.plan_route)
    if cfg.scratch_max_age_s <= cfg.stt_timeout_s:
        raise VoiceConfigError(
            f"scratch_max_age_s ({cfg.scratch_max_age_s}) must exceed stt_timeout_s "
            f"({cfg.stt_timeout_s}) — a file younger than one transcribe is never 'old' (G2/K5)"
        )
    cfg.scratch_dir = _check_path("scratch_dir", cfg.scratch_dir, backup_sources)
    cfg.model_dir = _check_path("model_dir", cfg.model_dir, backup_sources)
    return cfg


__all__ = ["CONFIG_PATH", "MODEL_ENV", "SCRATCH_ENV", "VoiceConfig", "VoiceConfigError", "load_voice_config"]
