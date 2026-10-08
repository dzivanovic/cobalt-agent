"""The ONE model-fetch command (design VOICE-TTS FINAL [F-30], :317) — run by hand.

Fills the speech-to-text `model_dir` with the pinned snapshot of
`configs/cobalt/voice.yaml` (`stt_model` at `stt_revision`), so
`transcribe.model_present` is true and the widget's
`speech-to-text down (model missing)` banner clears (per request, no restart).

    sh ops/fetch-voice-models.sh [--from <dir>]

`--from <dir>`: a local cache holding the pinned snapshot (the dev
`model_dir`); its `models--Systran--faster-whisper-<model>` folder is copied
whole, links kept relative. Never a network call: a source without the
snapshot is FAILED. Without `--from`: the one download in Cobalt.

READS NO MODE: no `COBALT_ENV`, never `load_voice_config()` (that call
resolves the vault, which needs a mode). The four values are read from the
YAML; `COBALT_VOICE_MODEL_DIR` overrides `model_dir` as the loader does; the
loader's path refusals run, all but the resolved vault's
(`config.py:98`–`:99`; in production that vault is the production vault,
refused here too). Deletes nothing; overwrites nothing.

The last line is `voice model READY: <model> <revision> at <snapshot>`
(exit 0) or `FAILED: <step> — <ExceptionName>` (exit 1).
"""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

import yaml

from cobalt import vault as vault_mod
from cobalt.backup.config import load_backup_config
from cobalt.voice import config as vc
from cobalt.voice import transcribe


class Refused(RuntimeError):
    """A step that ends the run: `str()` is the FAILED line's text."""


class _Parser(argparse.ArgumentParser):
    """A usage error is a FAILED line like any other, never argparse's exit 2."""

    def error(self, message):
        raise argparse.ArgumentError(None, message)


def _snapshot(cfg: vc.VoiceConfig, cache_dir: Path) -> Path:
    """The pinned snapshot under `cache_dir`. Local lookup only."""
    from faster_whisper.utils import download_model

    return Path(download_model(cfg.stt_model, local_files_only=True, cache_dir=str(cache_dir),
                               revision=cfg.stt_revision))


def _download(cfg: vc.VoiceConfig) -> None:
    """The only network path in Cobalt (design :158)."""
    from faster_whisper.utils import download_model

    download_model(cfg.stt_model, cache_dir=str(cfg.model_dir), revision=cfg.stt_revision)


def _check_target(raw: Path, backup_sources: list[Path]) -> Path:
    """`config._check_path`'s refusals that need no mode, in its words."""
    name = "model_dir"
    if not raw.is_absolute():
        raise vc.VoiceConfigError(f"{name} {str(raw)!r} is relative — an absolute path outside repo, vault and backup is required")
    p = raw.expanduser().resolve()
    if vc._under(p, vc.REPO_ROOT / "docs"):
        raise vc.VoiceConfigError(f"{name} {p} sits under docs/ — refused (FINAL §5)")
    if vc._under(p, vc.REPO_ROOT):
        raise vc.VoiceConfigError(f"{name} {p} sits under the repo root {vc.REPO_ROOT} — audio never reaches git (FINAL §5)")
    if vc._under(p, Path(vault_mod.PROD_VAULT_PATH_REFERENCE)):
        raise vc.VoiceConfigError(f"{name} {p} sits under the production vault — refused (FINAL §5)")
    for src in backup_sources:
        if vc._under(p, src):
            raise vc.VoiceConfigError(f"{name} {p} sits under the backup source {src} — audio never reaches a backup (FINAL §5)")
    return p


def _config() -> vc.VoiceConfig:
    voice = yaml.safe_load(vc.CONFIG_PATH.read_text())["voice"]
    values = {key: voice[key] for key in ("model_dir", "stt_model", "stt_revision", "stt_compute_type")}
    override = os.environ.get(vc.MODEL_ENV)
    if override is not None:
        if not override.strip():
            raise vc.VoiceConfigError(f"{vc.MODEL_ENV} is set but empty — set a path, or unset it for the "
                                      "committed default; an empty override never falls back (L1)")
        values["model_dir"] = override
    values["model_dir"] = Path(values["model_dir"])
    return vc.VoiceConfig.model_construct(**values)


def _check_links(repo: Path) -> None:
    """Every link in the repo folder is relative and stays inside it, so the
    copy never links back into the source (X2). Reads only."""
    root = repo.resolve()
    for dirpath, dirnames, filenames in os.walk(repo):
        for name in dirnames + filenames:
            link = Path(dirpath) / name
            if not link.is_symlink():
                continue
            target = os.readlink(link)
            if os.path.isabs(target) or not (link.parent / target).resolve().is_relative_to(root):
                raise Refused(f"{link} links outside {repo.name} — nothing copied")


def _copy(cfg: vc.VoiceConfig, source: Path) -> None:
    try:
        snapshot = _snapshot(cfg, source)
    except Exception:  # noqa: BLE001 - absent is the answer
        raise Refused(f"the pinned {cfg.stt_model} {cfg.stt_revision} snapshot is not under {source}") from None
    if not (snapshot / "model.bin").exists():
        raise Refused(f"the pinned {cfg.stt_model} {cfg.stt_revision} snapshot is not under {source}")
    repo = snapshot.parents[1]
    _check_links(repo)
    dest = cfg.model_dir / repo.name
    if dest.exists() or dest.is_symlink():
        raise Refused(f"{dest} exists but does not hold the pinned snapshot — move it aside")
    cfg.model_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    shutil.copytree(repo, dest, symlinks=True)


def main(argv: list[str] | None = None) -> int:
    parser = _Parser(description="Fill the speech-to-text model_dir with the pinned snapshot.")
    parser.add_argument("--from", dest="source", type=Path, default=None,
                        help="a local cache holding the pinned snapshot; never a download")
    try:
        args = parser.parse_args(argv)
    except argparse.ArgumentError as e:
        print(f"FAILED: arguments — {type(e).__name__}")
        return 1
    step = "config"
    try:
        cfg = _config()
        step = "path"
        cfg.model_dir = _check_target(cfg.model_dir, [Path(p) for p in load_backup_config().sources])
        if transcribe.model_present(cfg):
            print(f"present: {cfg.stt_model} {cfg.stt_revision} under {cfg.model_dir} — nothing copied")
        elif args.source is not None:
            step = "copy"
            _copy(cfg, args.source)
        else:
            step = "download"
            _download(cfg)
        step = "verify"
        if not transcribe.model_present(cfg):
            print(f"verify: the pinned {cfg.stt_model} {cfg.stt_revision} is not present under {cfg.model_dir}")
            raise Refused(f"verify — {Refused.__name__}")
        transcribe._load_model(cfg)
        snapshot = _snapshot(cfg, cfg.model_dir)
    except Refused as e:
        print(f"FAILED: {e}")
        return 1
    except vc.VoiceConfigError as e:
        print(f"FAILED: {step} — VoiceConfigError: {e}")
        return 1
    except Exception as e:  # noqa: BLE001 - every failure is one named line
        print(f"FAILED: {step} — {type(e).__name__}")
        return 1
    print(f"voice model READY: {cfg.stt_model} {cfg.stt_revision} at {snapshot}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
