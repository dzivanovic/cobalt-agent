#!/usr/bin/env python3
"""
Test script to verify Pydantic Settings configuration override from .env file.

This script tests that:
1. YAML config is loaded correctly
2. Environment variables override YAML values
3. Nested values like network.nodes.cortex.ip are properly overridden
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from cobalt_agent.config import load_config, get_config


def test_config_override():
    """Test that config overrides work correctly."""
    print("=" * 60)
    print("Testing Pydantic Settings Config Override")
    print("=" * 60)
    
    # Get configuration instance
    config = get_config()
    
    # Test 1: Check cortex IP (should be 'localhost' from .env)
    # Pydantic env_nested_delimiter="_" maps: NETWORK_NODES_CORTEX_IP -> network.nodes.cortex.ip
    print("\n[Test 1] Cortex IP Override")
    print("-" * 40)
    expected_yaml_ip = "10.200.2.196"
    expected_env_ip = "localhost"
    
    cortex_ip = config.network.nodes["cortex"].ip
    
    print(f"  Expected (from .env): {expected_env_ip}")
    print(f"  Expected (from yaml): {expected_yaml_ip}")
    print(f"  Actual: {cortex_ip}")
    
    if cortex_ip == expected_env_ip:
        print("  [PASS] Environment variable override works!")
    else:
        print(f"  [FAIL] Expected '{expected_env_ip}' but got '{cortex_ip}'")
        print("  NOTE: Use NETWORK_NODES_CORTEX_IP in .env for Pydantic env_nested_delimiter")
    
    # Test 2: Check Obsidian Vault Path (should be from .env)
    print("\n[Test 2] Obsidian Vault Path Override")
    print("-" * 40)
    expected_vault_path = "/Users/cobalt/cobalt/docs/Cobalt"
    
    vault_path = config.system.obsidian_vault_path
    
    print(f"  Expected: {expected_vault_path}")
    print(f"  Actual: {vault_path}")
    
    if vault_path == expected_vault_path:
        print("  [PASS] Obsidian vault path loaded correctly!")
    else:
        print(f"  [FAIL] Expected '{expected_vault_path}' but got '{vault_path}'")
    
    # Test 3: Print full cortex node configuration
    print("\n[Test 3] Full Cortex Node Configuration")
    print("-" * 40)
    cortex_node = config.network.nodes["cortex"]
    print(f"  Role: {cortex_node.role}")
    print(f"  IP: {cortex_node.ip}")
    print(f"  Port: {cortex_node.port}")
    print(f"  Protocol: {cortex_node.protocol}")
    
    # Test 4: Print system configuration
    print("\n[Test 4] System Configuration")
    print("-" * 40)
    print(f"  Debug Mode: {config.system.debug_mode}")
    print(f"  Version: {config.system.version}")
    print(f"  Obsidian Vault Path: {config.system.obsidian_vault_path}")
    
    print("\n" + "=" * 60)
    print("Config Override Test Complete")
    print("=" * 60)
    
    return cortex_ip == expected_env_ip


if __name__ == "__main__":
    success = test_config_override()
    sys.exit(0 if success else 1)