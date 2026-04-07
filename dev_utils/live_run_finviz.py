"""
Live Finviz API Runner - The Macro Engine

This script performs a live, unmocked API call to Finviz Elite via HTTP
to verify the new async CSV-based client works correctly.

Usage:
    uv run dev_utils/live_run_finviz.py

Requirements:
    - COBALT_MASTER_KEY environment variable set
    - Vault unlocked with Finviz API token (finviz.com::api_token)
"""

import asyncio
import json
import os
import sys
import time

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from cobalt_agent.skills.research.finviz_api import FinvizApiClient


async def main():
    """Main entry point for live Finviz API execution."""
    print("=" * 70)
    print("🚀 COBALT FINVIZ MACRO ENGINE - LIVE API EXECUTION RUNNER")
    print("=" * 70)

    # Step 1: Load COBALT_MASTER_KEY from environment
    print("\n📋 Step 1: Loading COBALT_MASTER_KEY from environment...")
    master_key = os.getenv("COBALT_MASTER_KEY")

    if not master_key:
        print("❌ ERROR: COBALT_MASTER_KEY environment variable not set!")
        print("   Please export it before running this script:")
        print('   $ export COBALT_MASTER_KEY="your-master-key-here"')
        sys.exit(1)

    print(f"✅ Master key loaded (length: {len(master_key)})")

    # Step 2: Initialize FinvizApiClient
    print("\n🔐 Step 2: Instantiating FinvizApiClient...")
    vault_path = "data/.cobalt_vault"

    try:
        client = FinvizApiClient(vault_path=vault_path)
        print("✅ Client initialized successfully")
    except Exception as e:
        print(f"❌ ERROR: Failed to initialize client: {e}")
        sys.exit(1)

    # Step 3: Execute screener request with timing
    print("\n🎯 Step 3: Executing 'Morning Up Gapper' screener request...")
    print("   This will:")
    print("   - Resolve API token from Vault (finviz.com::api_token)")
    print("   - Perform async HTTP GET to elite.finviz.com/export.ashx")
    print("   - Parse CSV response into list of dictionaries")
    print()

    start_time = time.time()

    try:
        result = await client.get_screener("Morning Up Gapper")
    except Exception as e:
        print(f"❌ Screener request failed with exception: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    end_time = time.time()
    execution_time = end_time - start_time

    # Step 4: Display results with timing
    print("\n" + "=" * 70)
    print("📈 API EXECUTION RESULTS")
    print("=" * 70)

    if not result:
        print("❌ ERROR: No data returned from API")
        sys.exit(1)

    # Extract metadata (dynamic typing)
    screener_name = "Morning Up Gapper"
    total_results = len(result)

    print(f"\n✅ Screener: {screener_name}")
    print(f"📊 Total Results: {total_results}")
    print(f"⏱️  Execution Time (Latency): {execution_time:.3f} seconds")

    # Verify Volume sort by checking first 5 stocks
    if result:
        print("\n🔽 First 5 Stocks (sorted by Volume DESC):")
        print("-" * 70)

        for i, stock in enumerate(result[:5], 1):
            # Dynamic access to dictionary keys (no Pydantic model)
            ticker = stock.get("Ticker", stock.get("ticker", "N/A"))
            volume = stock.get("Volume", stock.get("volume", "N/A"))
            price = stock.get("Price", stock.get("price", "N/A"))

            # Format volume for display
            if isinstance(volume, (int, float)):
                vol_text = f"{volume:,}"
            else:
                vol_text = str(volume) if volume != "N/A" else "N/A"

            # Format price for display
            if isinstance(price, (int, float)):
                price_text = f"${price:.2f}"
            else:
                price_text = str(price) if price != "N/A" else "N/A"

            print(f"   {i}. {str(ticker):8s} | Volume: {vol_text:>12s} | Price: ${price_text:>8}")

        # Verify descending order (extract numeric volumes)
        volumes = []
        for stock in result[:10]:
            vol = stock.get("Volume", stock.get("volume"))
            if isinstance(vol, (int, float)):
                volumes.append(float(vol))
            elif isinstance(vol, str) and vol.replace(".", "").replace(",", "").isdigit():
                volumes.append(float(vol.replace(",", "")))

        if len(volumes) >= 2:
            is_descending = all(volumes[i] >= volumes[i + 1] for i in range(len(volumes) - 1))
            sort_status = "✅ CORRECT (descending)" if is_descending else "❌ INCORRECT (not descending)"
            print(f"\n📉 Volume Sort Verification: {sort_status}")

    # Pretty-print first 5 stocks as JSON (dynamic typing)
    print("\n" + "-" * 70)
    print("📋 First 5 Stocks (Pretty-Printed JSON):")
    print("-" * 70)

    first_5 = result[:5]
    print(json.dumps(first_5, indent=2))

    print("\n" + "=" * 70)
    print("✅ LIVE API EXECUTION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())