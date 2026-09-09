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
# CONTRACT. install_template RETURNS non-zero on every refusal; it never
# calls `exit`. The caller decides what a refusal means, because the two
# callers need opposite things: the main start path turns it into `exit 1`
# (fail-loud, before anything is loaded), while the heartbeat's self-heal
# reload() logs it and skips the reload, so a bad template can never take
# the heartbeat itself down (NN#16).
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
        return 1
    fi
    src_sha="$(sha_of "$template_src")"

    if [ ! -f "$target" ]; then
        log "FATAL: no chat template in model dir ($target) — refusing"
        return 1
    fi
    target_sha="$(sha_of "$target")"

    # RECOGNITION GATE. The template in the model dir must be either the
    # upstream we pinned or the one we install. Anything else means a model
    # update shipped a new template, or somebody hand-edited the file, and in
    # both cases overwriting it silently is exactly the invisible drift this
    # file exists to end.
    #
    # This runs on EVERY call, not only when .orig is missing (tightened
    # 2026-09-09 on the architect's ESCALATE 4.1 ruling). It used to sit
    # inside the `.orig`-missing branch, which meant that once a backup
    # existed a genuine upstream change was overwritten without a word — the
    # one case the guard was written for. A model update is a deliberate
    # human action; refusing loudly there is NN#16-correct, because the fix
    # is a two-minute review of ops/mainframe/, not a silent regression that
    # surfaces days later as bad model output.
    if [ "$target_sha" != "$UPSTREAM_SHA" ] && [ "$target_sha" != "$src_sha" ]; then
        log "FATAL: model dir template is neither upstream nor ours — a model update shipped a new template; review ops/mainframe/ before serving"
        log "FATAL:   $target sha $target_sha"
        log "FATAL:   expected upstream $UPSTREAM_SHA or ours $src_sha"
        return 1
    fi

    # One-time backup of the pristine upstream template.
    if [ ! -f "$target.orig" ]; then
        if [ "$target_sha" = "$UPSTREAM_SHA" ]; then
            cp "$target" "$target.orig"
            log "template: backed up upstream template to $target.orig"
        else
            # Ours is already installed but the .orig was lost (model
            # re-download, manual cleanup). Not fatal — the repo copy carries
            # the upstream sha in its header, so the original is recoverable
            # from the model repo.
            log "WARN: template already ours but $target.orig is missing — no backup to make"
        fi
    fi

    if [ "$target_sha" != "$src_sha" ]; then
        cp "$template_src" "$target"
        log "template installed: $src_sha"
    else
        log "template current: $target_sha"
    fi
}
