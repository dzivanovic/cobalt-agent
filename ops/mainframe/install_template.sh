#!/bin/bash
# install_template.sh — put the Cobalt-owned chat template into the model dir.
#
# 2026-09-09, PROMPT 5 phase A1.
#
# WHY THIS EXISTS. LM Studio 1.11.0 forwards neither `enable_thinking` nor
# `reasoning_effort` from the API into the model's Jinja chat template (proven
# 2026-09-07 and 2026-09-08), so thinking is unconditionally on and there is no
# API-side way to turn it off. The only lever left is the template itself, which
# lives in the model directory — outside the repo, outside git, outside review.
# ops/mainframe/chat_template.jinja is therefore the repo-owned source of truth
# and this function copies it into place on every mainframe start.
#
# WHY IT IS ITS OWN FILE. It has to run in two different processes: the main
# start path, and the heartbeat's self-heal `reload()`, which lives inside a
# separate single-quoted `bash -c '…'`. Inlining the body in both places would
# be two implementations of one thing (one-path rule), so both `source` this.
#
# SAFETY. The upstream template is backed up once to <target>.orig before the
# first install, and the function REFUSES to overwrite a template whose sha
# matches neither upstream nor ours — an unrecognised template means either a
# model update or a hand-edit, and clobbering it silently is exactly the kind of
# invisible drift this file was written to end. Rollback is a one-liner:
#     cp chat_template.jinja.orig chat_template.jinja
#
# Requires from the caller: OPS_DIR, MODEL_PATH, and a `log` function.

# shellcheck shell=bash

# Upstream mlx-community/Qwen3.8-27B-8bit chat_template.jinja, verified
# 2026-09-09. If a model update changes this, install_template refuses and says
# so rather than overwriting the new template.
UPSTREAM_SHA="c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041"

sha_of() { shasum -a 256 "$1" 2>/dev/null | awk '{print $1}'; }

install_template() {
    local template_src model_dir target src_sha target_sha
    template_src="$OPS_DIR/mainframe/chat_template.jinja"
    model_dir="/Users/cobalt/.lmstudio/models/$MODEL_PATH"
    target="$model_dir/chat_template.jinja"

    if [ ! -f "$template_src" ]; then
        log "FATAL: template source missing: $template_src"
        log "FATAL: refusing to start without the repo-owned chat template."
        exit 1
    fi
    src_sha="$(sha_of "$template_src")"

    if [ ! -f "$target" ]; then
        log "FATAL: no chat template in model dir ($target) — refusing"
        exit 1
    fi
    target_sha="$(sha_of "$target")"

    # One-time backup of the pristine upstream template.
    if [ ! -f "$target.orig" ]; then
        if [ "$target_sha" = "$UPSTREAM_SHA" ]; then
            cp "$target" "$target.orig"
            log "template: backed up upstream template to $target.orig"
        elif [ "$target_sha" = "$src_sha" ]; then
            # Ours is already installed but the .orig was lost (model re-download,
            # manual cleanup). Not fatal — the repo copy still carries the upstream
            # sha in its header, so the original is recoverable from the model repo.
            log "WARN: template already ours but $target.orig is missing — no backup to make"
        else
            log "FATAL: unknown template in model dir, refusing"
            log "FATAL:   $target sha $target_sha"
            log "FATAL:   expected upstream $UPSTREAM_SHA or ours $src_sha"
            exit 1
        fi
    fi

    if [ "$target_sha" != "$src_sha" ]; then
        cp "$template_src" "$target"
        log "template installed: $src_sha"
    else
        log "template current: $target_sha"
    fi
}
