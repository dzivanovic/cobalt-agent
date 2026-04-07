"""
Finviz Quote API Test Runner

Standalone test script to evaluate latency and payload structure of the
get_quote endpoint without modifying existing screener tests.

Usage:
    uv run dev_utils/live_run_finviz_quote.py
"""

import asyncio
import json
import time

from cobalt_agent.skills.research.finviz_api import FinvizApiClient


# ANSI color codes for UI formatting
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"


def print_header():
    """Print a clear UI header to the console."""
    print(f"{Colors.CYAN}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}Finviz Quote API Test Runner{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 60}{Colors.RESET}")


def print_latency(elapsed_seconds: float):
    """Print execution latency in milliseconds and seconds."""
    elapsed_ms = elapsed_seconds * 1000
    print(f"{Colors.GREEN}Latency:{Colors.RESET} {elapsed_ms:.2f} ms ({elapsed_seconds:.4f} s)")


def print_warning(message: str):
    """Print a warning message."""
    print(f"{Colors.YELLOW}⚠️  WARNING:{Colors.RESET} {message}")


def print_error(message: str):
    """Print an error message."""
    print(f"{Colors.RED}❌ ERROR:{Colors.RESET} {message}")


def print_success(message: str):
    """Print a success message."""
    print(f"{Colors.GREEN}✅ {Colors.BOLD}{message}{Colors.RESET}")


def format_json(data, indent=2):
    """Pretty-print JSON data."""
    return json.dumps(data, indent=indent, default=str)


async def run_quote_test(ticker: str):
    """
    Run the quote API test with high-precision timing.

    Args:
        ticker: Stock ticker symbol to query
    """
    print_header()
    print(f"Target Ticker: {Colors.BOLD}{ticker.upper()}{Colors.RESET}\n")

    # Instantiate the client
    client = FinvizApiClient()

    try:
        # Start high-precision timer
        start_time = time.perf_counter()

        # Await the quote fetch
        result = await client.get_quote(ticker)

        # Stop timer and calculate elapsed latency
        elapsed_time = time.perf_counter() - start_time

        # Print latency
        print_latency(elapsed_time)

        if result:
            print_success("Data retrieved successfully")
            print(f"\n{Colors.BOLD}Payload Structure (first dictionary):{Colors.RESET}")
            print(f"{Colors.CYAN}{'-' * 60}{Colors.RESET}")

            # Pretty-print the first dictionary in the returned list
            print(format_json(result[0]))

            print(f"\n{Colors.CYAN}{'-' * 60}{Colors.RESET}")
            print(f"{Colors.GREEN}Total rows returned:{Colors.RESET} {len(result)}")
        else:
            print_warning("No data returned from API")

    except Exception as e:
        print_error(f"Failed to fetch quote: {e}")


def main():
    """Main entry point."""
    # Target ticker as specified in requirements
    TARGET_TICKER = "NVDA"

    asyncio.run(run_quote_test(TARGET_TICKER))


if __name__ == "__main__":
    main()