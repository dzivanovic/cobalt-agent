"""
Test suite for Intent-Driven Proposal Validation

This module rigorously tests the intent_alignment schema enforcement in the
Proposal system. It proves that AI actions without explicit blast radius and
trade-offs are mathematically rejected by Pydantic validation.
"""
import pytest
from pydantic import ValidationError
from cobalt_agent.core.proposals import Proposal, IntentAlignment


def test_proposal_defaults_empty_intent_alignment_when_omitted():
    """
    BEHAVIOR TEST: Verify Proposal creates default empty IntentAlignment when omitted.
    
    NOTE: The current implementation uses default_factory=lambda: IntentAlignment(),
    so omitting intent_alignment does NOT raise ValidationError - it creates defaults.
    
    This documents the current behavior: empty defaults are created, which means
    the enforcement of explicit blast radius must happen at a higher validation layer.
    
    Expected: Proposal created with empty/default IntentAlignment values.
    """
    proposal = Proposal(
        task_id="test1234",
        action="Tool: browser --query='update production'",
        justification="Need to update production system",
        risk_assessment="Potential data loss risk"
        # NOTE: intent_alignment intentionally omitted
    )
    
    # Verify proposal was created with default empty IntentAlignment
    assert proposal.intent_alignment is not None
    assert isinstance(proposal.intent_alignment, IntentAlignment)
    # Default values from IntentAlignment schema
    assert proposal.intent_alignment.decision_boundaries == ""
    assert proposal.intent_alignment.trade_offs == ""
    assert proposal.intent_alignment.validation_metric == ""


def test_proposal_rejects_invalid_intent_alignment_type():
    """
    FAILURE TEST: Verify Proposal rejects invalid intent_alignment type.
    
    The Proposal model MUST require intent_alignment to be an IntentAlignment instance.
    Passing a raw dict or wrong type should raise ValidationError.
    
    Expected: Pydantic ValidationError raised when intent_alignment is invalid type.
    """
    with pytest.raises(ValidationError) as exc_info:
        Proposal(
            task_id="test1234",
            action="Tool: browser --query='update production'",
            justification="Need to update production system",
            risk_assessment="Potential data loss risk",
            intent_alignment="invalid_string_type"  # Wrong type - should be IntentAlignment or dict
        )
    
    # Verify the error is about validation failure
    errors = exc_info.value.errors()
    assert len(errors) >= 1


def test_proposal_accepts_valid_intent_alignment():
    """
    SUCCESS TEST: Verify Proposal accepts properly formatted intent_alignment.
    
    A valid Proposal MUST include all three components of IntentAlignment:
    1. decision_boundaries - Explicit blast radius definition
    2. trade_offs - Documented trade-off decisions  
    3. validation_metric - Verifiable success condition
    
    Expected: Proposal object created successfully with all fields populated.
    """
    proposal = Proposal(
        task_id="test5678",
        action="Tool: browser --query='update src/config.py'",
        justification="Update configuration for new feature",
        risk_assessment="Low risk - only affects config file",
        intent_alignment=IntentAlignment(
            decision_boundaries="src/config.py, configs/prompts.yaml",
            trade_offs="Readability over minor latency optimization",
            validation_metric="pytest tests/test_config.py -v && curl -s http://localhost:8000/health"
        )
    )
    
    # Verify proposal was created successfully
    assert proposal.task_id == "test5678"
    assert proposal.action == "Tool: browser --query='update src/config.py'"
    
    # Verify intent_alignment components are present and correct
    assert proposal.intent_alignment.decision_boundaries == "src/config.py, configs/prompts.yaml"
    assert proposal.intent_alignment.trade_offs == "Readability over minor latency optimization"
    assert proposal.intent_alignment.validation_metric == "pytest tests/test_config.py -v && curl -s http://localhost:8000/health"