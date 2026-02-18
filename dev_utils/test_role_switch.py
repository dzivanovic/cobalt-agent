"""
Test script for role switching (Two-Brain Hot Swap)
Project Cobalt: Verifies Qwen 80B -> DeepSeek 70B transition

This script tests the role switch capability:
1. Initialize the Agent with default role
2. Print current model (Should be Qwen 80B)
3. Execute role switch: agent.llm.switch_role("strategist")
4. Print new model (Should be DeepSeek 70B)

This triggers a "Hot Swap" - unloading Qwen (48GB) and loading DeepSeek (42GB).
Watch RAM usage - this tests our 'MAX_LOADED_MODELS=1' safety valve.
"""

import sys
import os

# Add the project root to the path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cobalt_agent.llm import LLM
from cobalt_agent.config import load_config


def test_role_switch():
    """Test the role switching functionality."""
    print("=" * 80)
    print("TWO-BRAIN ROLE SWITCH TEST")
    print("=" * 80)
    print()
    
    # Load config to display current settings
    config = load_config()
    
    print("Current Configuration:")
    print(f"  Strategist role: {config.active_profile.get('strategist', 'NOT FOUND')}")
    print(f"  Strategist model: {config.models.get('local_strategist_r1', {}).get('model_name', 'NOT FOUND')}")
    print()
    
    # Step 1: Initialize Agent with default role
    print("Step 1: Initialize Agent with 'default' role...")
    agent_llm = LLM(role="default")
    print(f"  Current model: {agent_llm.model_name}")
    print()
    
    # Verify initial model is Qwen 80B (local_bleeding_edge)
    expected_initial = "ollama/qwen3-coder-next"
    if agent_llm.model_name == expected_initial:
        print(f"  ✓ Initial model matches expected: {expected_initial}")
    else:
        print(f"  ⚠ Initial model differs from expected ({expected_initial})")
    print()
    
    # Step 2: Execute role switch to strategist
    print("Step 2: Execute role switch to 'strategist'...")
    agent_llm.switch_role("strategist")
    print(f"  New model: {agent_llm.model_name}")
    print()
    
    # Verify new model is DeepSeek 70B (local_strategist_r1)
    expected_strategist = "ollama/deepseek-r1:70b"
    if agent_llm.model_name == expected_strategist:
        print(f"  ✓ Strategist model matches expected: {expected_strategist}")
    else:
        print(f"  ⚠ Strategist model differs from expected ({expected_strategist})")
    print()
    
    # Summary
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"  Initial model (default):    {agent_llm.model_name}")
    print(f"  After switch to strategist: {agent_llm.model_name}")
    print()
    
    # Hot swap note
    print("HOT SWAP NOTES:")
    print("  - This test triggers model unloading/reloading")
    print("  - Expected: Qwen 80B (48GB) -> DeepSeek 70B (42GB)")
    print("  - Monitor RAM usage to verify MAX_LOADED_MODELS=1 safety valve")
    print("=" * 80)


if __name__ == "__main__":
    test_role_switch()