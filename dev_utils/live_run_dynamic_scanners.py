"""
Live Run Dynamic Scanners - YAML Test Runner

Tests the Universal Abstract Screener by loading scanner configurations
from configs/scanners.yaml and executing them via FinvizApiClient.

Displays:
- Scanner name
- Compiled filter string
- Total tickers found
- Total columns extracted (should be 151)

Usage:
    uv run dev_utils/live_run_dynamic_scanners.py
"""

import asyncio
import os
import sys
from pathlib import Path

import yaml

# Add src to path for imports (standard pattern matching live_run_finviz.py)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cobalt_agent.skills.research.finviz_api import FinvizApiClient


async def main():
    """Load scanners from YAML and execute dynamic screeners."""
    # Load configuration
    config_path = Path("configs/scanners.yaml")

    if not config_path.exists():
        print(f"❌ Configuration file not found: {config_path}")
        return

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    scanners = config.get("scanners", {})

    # Find all active scanners
    active_scanners = {
        name: data for name, data in scanners.items()
        if data.get("active", False)
    }

    if not active_scanners:
        print("⚠️  No active scanners found in configuration")
        return

    print("=" * 60)
    print("🔬 Universal Abstract Screener - YAML Test Runner")
    print("=" * 60)

    # Instantiate client once for all scanners
    client = FinvizApiClient()

    for scanner_name, scanner_config in active_scanners.items():
        print(f"\n📊 Scanner: {scanner_name}")
        print("-" * 40)

        # Get description if available
        description = scanner_config.get("description", "No description")
        print(f"   Description: {description}")

        # Get filters
        filters = scanner_config.get("filters", {})

        if not filters:
            print("   ⚠️  No filters defined")
            continue

        # Compile filter string using the client's method
        compiled_filters = client.compile_filters(filters)
        print(f"   Compiled Filters: {compiled_filters}")

        # Execute dynamic screener
        try:
            results = await client.execute_dynamic_screener(filters)

            # Get metrics
            total_tickers = len(results)
            total_columns = len(results[0].keys()) if results else 0

            print(f"   Total Tickers Found: {total_tickers}")
            print(f"   Total Columns Extracted: {total_columns}")

            if total_columns == 151:
                print("   ✅ All 151 columns successfully extracted")
            else:
                print(f"   ⚠️  Expected 151 columns, got {total_columns}")

        except Exception as e:
            print(f"   ❌ Error executing screener: {e}")

    print("\n" + "=" * 60)
    print("✅ Test run complete")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())