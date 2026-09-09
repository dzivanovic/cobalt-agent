"""Offline tests for the Cobalt-owned mainframe chat template.

`ops/mainframe/chat_template.jinja` is the upstream mlx-community/Qwen3.8-27B-8bit
template plus ONE edit: the "Cobalt soft switch" block, which lets a request turn
thinking off (`/no_think`) or drop reasoning effort to low (`/think_low`) IN-BAND,
because LM Studio 1.11.0 forwards neither `enable_thinking` nor `reasoning_effort`
from the API into the template.

These tests never touch LM Studio, the network, or the model directory. They render
the REPO copy with jinja2 and assert on the generation prompt.

CAVEAT: LM Studio serves the template through minijinja, not jinja2. These tests
prove the template's logic under jinja2; the runtime proof is the `nothink probe`
in ops/start_mainframe.sh and the phase A2 side-instance run.
"""

from __future__ import annotations

import re
from pathlib import Path

import jinja2
import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = REPO_ROOT / "ops" / "mainframe" / "chat_template.jinja"
START_SCRIPT = REPO_ROOT / "ops" / "start_mainframe.sh"
INSTALL_SCRIPT = REPO_ROOT / "ops" / "mainframe" / "install_template.sh"

UPSTREAM_SHA = "c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041"
ANCHOR = "{%- if enable_thinking is undefined or enable_thinking is true %}"
MARKER = "{%- set cobalt_sw = namespace(no_think=false, low=false) %}"

# Verbatim from the upstream template (line 54 / line 52 of the original).
LOW_INSTRUCTION = (
    "Reasoning effort is set to low. Keep your thinking brief and focused, "
    "moving directly to the conclusion without unnecessary elaboration."
)
XHIGH_INSTRUCTION = "Reasoning effort is set to xhigh."

THINK_OPEN = "<|im_start|>assistant\n<think>\n"
THINK_SKIPPED = "<|im_start|>assistant\n<think>\n\n</think>\n\n"


def _raise_exception(message: str) -> None:
    """Stand-in for the `raise_exception` global HF injects into chat templates."""
    raise RuntimeError(message)


@pytest.fixture(scope="module")
def template_source() -> str:
    return TEMPLATE_PATH.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def template(template_source: str) -> jinja2.Template:
    # trim_blocks/lstrip_blocks match the environment HF uses for chat templates.
    # Default (non-strict) Undefined is required: the template evaluates a bare
    # `tools` for truthiness, which StrictUndefined would turn into an error.
    env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True)
    env.globals["raise_exception"] = _raise_exception
    return env.from_string(template_source)


def render(template: jinja2.Template, messages: list[dict]) -> str:
    return template.render(messages=messages, add_generation_prompt=True)


# --- a-d: the /no_think switch ----------------------------------------------


def test_no_marker_keeps_thinking_on(template: jinja2.Template) -> None:
    out = render(template, [{"role": "user", "content": "2+2?"}])
    assert out.endswith(THINK_OPEN), repr(out[-80:])


def test_no_think_in_system_message_disables_thinking(template: jinja2.Template) -> None:
    out = render(
        template,
        [
            {"role": "system", "content": "/no_think"},
            {"role": "user", "content": "2+2?"},
        ],
    )
    assert out.endswith(THINK_SKIPPED), repr(out[-80:])


def test_no_think_in_last_message_disables_thinking(template: jinja2.Template) -> None:
    out = render(
        template,
        [
            {"role": "user", "content": "hello"},
            {"role": "assistant", "content": "hi"},
            {"role": "user", "content": "2+2? /no_think"},
        ],
    )
    assert out.endswith(THINK_SKIPPED), repr(out[-80:])


def test_no_think_in_earlier_message_only_keeps_thinking_on(
    template: jinja2.Template,
) -> None:
    """A stale marker in an old turn must NOT silently disable thinking later."""
    out = render(
        template,
        [
            {"role": "user", "content": "2+2? /no_think"},
            {"role": "assistant", "content": "4"},
            {"role": "user", "content": "and 3+3?"},
        ],
    )
    assert out.endswith(THINK_OPEN), repr(out[-80:])


def test_multimodal_content_list_does_not_crash_the_switch(
    template: jinja2.Template,
) -> None:
    """`m.content is string` guards a list-shaped (multimodal) message content."""
    out = render(
        template,
        [{"role": "user", "content": [{"type": "text", "text": "2+2?"}]}],
    )
    assert out.endswith(THINK_OPEN), repr(out[-80:])


# --- e: the /think_low switch ------------------------------------------------


def test_think_low_selects_the_low_reasoning_instruction(
    template: jinja2.Template,
) -> None:
    out = render(
        template,
        [
            {"role": "system", "content": "/think_low"},
            {"role": "user", "content": "2+2?"},
        ],
    )
    assert LOW_INSTRUCTION in out
    assert XHIGH_INSTRUCTION not in out
    # /think_low must not also disable thinking.
    assert out.endswith(THINK_OPEN), repr(out[-80:])


def test_default_reasoning_effort_is_xhigh(template: jinja2.Template) -> None:
    out = render(template, [{"role": "user", "content": "2+2?"}])
    assert XHIGH_INSTRUCTION in out
    assert LOW_INSTRUCTION not in out


# --- f: structural provenance assertions -------------------------------------


def test_template_file_exists_and_is_the_repo_copy() -> None:
    assert TEMPLATE_PATH.is_file(), f"missing {TEMPLATE_PATH}"


def test_upstream_anchor_line_present_exactly_once(template_source: str) -> None:
    assert template_source.count(ANCHOR) == 1


def test_soft_switch_block_present_exactly_once(template_source: str) -> None:
    assert template_source.count(MARKER) == 1
    # ... and it sits immediately before the upstream anchor.
    assert re.search(
        re.escape(MARKER) + r".*?\n" + re.escape(ANCHOR),
        template_source,
        re.DOTALL,
    )


def test_start_script_sources_the_installer() -> None:
    script = START_SCRIPT.read_text(encoding="utf-8")
    assert "ops/mainframe/chat_template.jinja" in script
    assert "mainframe/install_template.sh" in script
    # Both the main path and the heartbeat's self-heal reload() must install
    # the template, or a reload brings the model up under a stale one.
    assert script.count("install_template") >= 2


def test_installer_owns_the_template_and_pins_the_upstream_sha() -> None:
    installer = INSTALL_SCRIPT.read_text(encoding="utf-8")
    assert "mainframe/chat_template.jinja" in installer
    assert UPSTREAM_SHA in installer
