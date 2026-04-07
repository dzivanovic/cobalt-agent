"""
Metadata Enrichment Skill (Finviz API Bridge)
An importable, callable agent skill for injecting hard financial data into the database.

Usage (Programmatic):
    from cobalt_agent.skills.research.enrich_metadata import MetadataEnricher
    enricher = MetadataEnricher()
    stats = await enricher.enrich(tickers=["AAPL", "TSLA"])

Usage (CLI / Sweep):
    uv run src/cobalt_agent/skills/research/enrich_metadata.py
    (Defaults to finding all instruments missing sector/industry data and enriching them).
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

import psycopg2
from psycopg2.extras import RealDictCursor
from loguru import logger

from cobalt_agent.config import get_config

# Resolve project root and add to path for imports
sys_path_root = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(sys_path_root))

from cobalt_agent.skills.research.finviz_api import FinvizApiClient


def get_db_connection():
    """Create a Postgres connection using the central config engine."""
    from cobalt_agent.config import get_config
    import psycopg2
    
    config = get_config()
    return psycopg2.connect(
        host=config.postgres.host,
        port=config.postgres.port,
        database=config.postgres.db,
        user=config.postgres.user,
        password=config.postgres.password,
    )


class MetadataEnricher:
    """
    Production skill for enriching database instruments with Finviz metadata.
    Callable by other agents or scheduled orchestrators.
    """

    def __init__(self, batch_size: int = 100):
        self.client = FinvizApiClient()
        self.batch_size = batch_size

    def _get_starving_tickers(self) -> List[str]:
        """Fetch all tickers from the database missing core metadata."""
        conn = get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT symbol 
                FROM instruments 
                WHERE metadata IS NULL 
                   OR metadata = '{}'::jsonb 
                   OR metadata->>'sector' IS NULL;
            """)
            results = cur.fetchall()
        conn.close()
        return [row['symbol'] for row in results]

    async def enrich(
        self, 
        tickers: Optional[List[str]] = None, 
        enrich_starving: bool = False,
        force_update: bool = False
    ) -> Dict[str, Any]:
        """
        Execute metadata enrichment.

        Args:
            tickers: Specific list of tickers to enrich.
            enrich_starving: If True, automatically find and enrich tickers missing data.
            force_update: Future parameter for overwriting existing data.

        Returns:
            Dict containing execution statistics.
        """
        target_tickers = set(tickers or [])

        if enrich_starving:
            starving = self._get_starving_tickers()
            target_tickers.update(starving)

        ticker_list = list(target_tickers)

        if not ticker_list:
            logger.info("No tickers provided or found for enrichment.")
            return {"status": "complete", "tickers_targeted": 0, "instruments_updated": 0}

        logger.info(f"Initiating enrichment for {len(ticker_list)} tickers.")
        conn = get_db_connection()
        cur = conn.cursor()
        updated_count = 0

        try:
            for i in range(0, len(ticker_list), self.batch_size):
                chunk = ticker_list[i:i + self.batch_size]
                ticker_str = ",".join(chunk)

                # Pass tickers directly via the &t= parameter instead of the filter compiler
                query_string = f"v=152&c={self.client.MASTER_COLUMNS}&t={ticker_str}"
                results = await self.client._fetch_csv("export.ashx", query_string)

                for row in results:
                    ticker = row.get("Ticker")
                    if not ticker: continue

                    new_metadata = {
                        "sector": row.get("Sector", "").strip(),
                        "industry": row.get("Industry", "").strip(),
                        "market_cap": row.get("Market Cap.", "") or row.get("Market Cap", ""),
                        "shares_float": row.get("Shares Float", "").strip(),
                        "short_float": row.get("Short Float", "").strip(),
                        "average_volume": row.get("Average Volume", "").strip(),
                        "atr": row.get("Average True Range", "").strip()
                    }

                    clean_metadata = {k: v for k, v in new_metadata.items() if v and v != "-"}
                    if not clean_metadata: continue

                    cur.execute("""
                        UPDATE instruments 
                        SET metadata = %s, updated_at = CURRENT_TIMESTAMP 
                        WHERE symbol = %s
                    """, (json.dumps(clean_metadata), ticker))

                    updated_count += cur.rowcount

                conn.commit()

        except Exception as e:
            logger.error(f"Enrichment pipeline failed during execution: {e}")
            conn.rollback()
            return {"status": "error", "error": str(e)}
        finally:
            cur.close()
            conn.close()

        logger.info(f"Enrichment complete. Updated metadata for {updated_count} instruments.")
        return {
            "status": "complete",
            "tickers_targeted": len(ticker_list),
            "instruments_updated": updated_count
        }


# Allow direct execution for manual sweeps
if __name__ == "__main__":
    enricher = MetadataEnricher()
    result = asyncio.run(enricher.enrich(enrich_starving=True))
    print(json.dumps(result, indent=2))