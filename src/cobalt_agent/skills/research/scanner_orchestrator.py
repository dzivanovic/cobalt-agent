import asyncio
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List
import yaml
from loguru import logger
import psycopg2
from psycopg2.extras import Json

class ScannerOrchestrator:
    """
    Orchestrates Finviz screener data ingestion into the 5-Pillar database.
    Deduplicates overlapping tickers and tags them with active scanners.
    """

    def __init__(self, db_connection: Any, client: Any, scanners_config_path: str = "configs/scanners.yaml"):
        self.db = db_connection
        self.client = client
        self.scanners_config_path = Path(scanners_config_path)

    async def run_ingestion_cycle(self):
        """Execute a complete asynchronous ingestion cycle."""
        logger.info(f"Loading scanners config from {self.scanners_config_path}")
        
        with open(self.scanners_config_path, "r") as f:
            config = yaml.safe_load(f)
        
        scanners = config.get("scanners", {})
        active_scanners = {k: v for k, v in scanners.items() if v.get("active", False)}
        
        if not active_scanners:
            logger.warning("No active scanners found in configuration.")
            return

        logger.info(f"Executing {len(active_scanners)} active scanner(s)...")

        # 1. Fetch data from all active scanners concurrently
        all_results = []
        for scanner_name, scanner_config in active_scanners.items():
            logger.info(f"Executing scanner: {scanner_name}")
            try:
                filters = scanner_config.get("filters", {})
                data = await self.client.execute_dynamic_screener(filters)
                all_results.append((scanner_name, data))
                logger.info(f"{scanner_name}: Fetched {len(data)} rows")
            except Exception as e:
                logger.error(f"Scanner {scanner_name} failed: {e}")

        # 2. Deduplicate and Tag
        deduped_tickers = {}
        for scanner_name, rows in all_results:
            for row in rows:
                # Catch the ticker whether Finviz returns "Ticker", "1_Ticker", or lowercase
                ticker = row.get("Ticker") or row.get("1_Ticker") or row.get("ticker") or ""
                ticker = str(ticker).strip().upper()
                
                if not ticker or ticker == "NONE":
                    continue
                
                if ticker not in deduped_tickers:
                    # First time seeing this ticker, initialize it
                    row["active_on_scanners"] = [scanner_name]
                    deduped_tickers[ticker] = row
                else:
                    # Ticker already exists, just append the scanner tag
                    if scanner_name not in deduped_tickers[ticker]["active_on_scanners"]:
                        deduped_tickers[ticker]["active_on_scanners"].append(scanner_name)

        logger.info(f"Total Unique Tickers after deduplication: {len(deduped_tickers)}")

        if not deduped_tickers:
            logger.warning("No unique tickers to process. Exiting cycle.")
            return

        # 3. Database Insertion (Pillars 1 and 2)
        logger.info(f"Processing {len(deduped_tickers)} unique instruments into cobalt_brain...")
        
        with self.db.cursor() as cursor:
            inserted_count = 0
            for ticker, raw_data in deduped_tickers.items():
                try:
                    # Step A: Upsert Instrument
                    cursor.execute(
                        """
                        INSERT INTO instruments (symbol, asset_class, metadata, active_themes)
                        VALUES (%s, 'EQUITY', '{}'::jsonb, '[]'::jsonb)
                        ON CONFLICT (symbol) DO UPDATE 
                        SET updated_at = CURRENT_TIMESTAMP
                        RETURNING id;
                        """,
                        (ticker,)
                    )
                    instrument_id = cursor.fetchone()[0]

                    # Step B: Insert Market Snapshot
                    cursor.execute(
                        """
                        INSERT INTO market_snapshots (instrument_id, timestamp, raw_data)
                        VALUES (%s, %s, %s)
                        """,
                        (instrument_id, datetime.now(timezone.utc), Json(raw_data))
                    )
                    inserted_count += 1
                except Exception as e:
                    logger.error(f"DB Insert failed for {ticker}: {e}")
            
            self.db.commit()
            logger.info(f"Successfully inserted {inserted_count} snapshots into cobalt_brain.")

        print("\n" + "="*60)
        print("INGESTION CYCLE SUMMARY")
        print("="*60)
        print(f"Active scanners executed: {len(active_scanners)}")
        print(f"Unique instruments processed: {len(deduped_tickers)}")
        print(f"Snapshots inserted:       {inserted_count}")
        print("="*60 + "\n")