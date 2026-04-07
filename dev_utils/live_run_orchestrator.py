#!/usr/bin/env python3
"""
Live Run Orchestrator - Finviz Data Pipeline Stress Test

Purpose:
    Execute the full Finviz data pipeline to process a large batch of rows
    and verify the local LLM remains stable under concurrent load.

Operations:
    1. Establish PostgreSQL connection using psycopg2
    2. Initialize local LLM (role="coder")
    3. Initialize ScannerOrchestrator and run ingestion cycle for fresh data
    4. Initialize SemanticTagger with db_connection and llm
    5. Run tagging cycle to process backlog (batch_size=100)
    6. Commit and close database connection

Author: Cobalt SRE
"""

import asyncio
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import os
import psycopg2
from loguru import logger

# Project imports
from cobalt_agent.config import get_config
from cobalt_agent.llm import LLM
from cobalt_agent.security.vault import VaultManager
from cobalt_agent.skills.research.finviz_api import FinvizApiClient
from cobalt_agent.skills.research.scanner_orchestrator import ScannerOrchestrator
from cobalt_agent.skills.research.semantic_tagger import SemanticTagger


def get_db_connection():
    """
    Establish PostgreSQL connection using centralized configuration.

    Returns:
        psycopg2.connection: Database connection object

    Raises:
        ValueError: If required database configuration is missing
    """
    config = get_config()
    db_config = config.postgres

    # Validate all required credentials are present
    if not all([db_config.host, db_config.user, db_config.db]):
        raise ValueError("Missing required database configuration")

    logger.info("🔌 Establishing PostgreSQL connection...")
    return psycopg2.connect(
        host=db_config.host,
        port=db_config.port,
        database=db_config.db,
        user=db_config.user,
        password=db_config.password,
    )


async def main():
    """
    Main async function that orchestrates the full Finviz data pipeline.

    Workflow:
        1. Establish database connection
        2. Initialize local LLM with coder role
        3. Initialize FinvizApiClient and ScannerOrchestrator
        4. Run ingestion cycle to fetch fresh market data
        5. Initialize SemanticTagger with db and LLM
        6. Run tagging cycle to process backlog (batch_size=100)
        7. Commit and close database connection
    """
    conn = None

    try:
        print("=" * 70)
        print("COBALT FINVIZ DATA PIPELINE - STRESS TEST")
        print("=" * 70)

        # Step 1: Establish database connection
        logger.info("[STEP 1] Connecting to PostgreSQL...")
        conn = get_db_connection()
        logger.info("✓ Database connection established")

        # Step 2: Initialize local LLM with coder role
        logger.info("[STEP 2] Initializing local LLM (role='coder')...")
        llm = LLM(role="coder")
        logger.info(f"✓ LLM initialized with model: {llm.model_name}")

        # Step 3: Initialize FinvizApiClient and ScannerOrchestrator
        logger.info("[STEP 3] Initializing Finviz API Client...")
        vault_manager = VaultManager(vault_path="data/.cobalt_vault")
        config = get_config()

        # Unlock vault if master key is available for Finviz API token resolution
        if not vault_manager._is_unlocked:
            master_key = (
                config.system.debug_mode
                and hasattr(config, "vault")
                and getattr(config.vault, "master_key", None)
            )
            if not master_key:
                master_key = os.getenv("COBALT_MASTER_KEY")

            if master_key:
                logger.info("🔑 Unlocking vault for Finviz API token resolution")
                vault_manager.unlock(master_key)

        finviz_client = FinvizApiClient(vault_path="data/.cobalt_vault")
        logger.info("✓ Finviz API Client initialized")

        # Step 4: Initialize ScannerOrchestrator and run ingestion cycle
        logger.info("[STEP 4] Initializing ScannerOrchestrator...")
        scanner_orchestrator = ScannerOrchestrator(
            db_connection=conn,
            client=finviz_client,
        )

        logger.info("🔄 Running ingestion cycle to fetch fresh market data...")
        await scanner_orchestrator.run_ingestion_cycle()
        logger.info("✓ Ingestion cycle completed")

        # Step 5: Initialize SemanticTagger with db_connection and llm
        logger.info("[STEP 5] Initializing SemanticTagger...")
        semantic_tagger = SemanticTagger(db_connection=conn, llm=llm)
        logger.info("✓ SemanticTagger initialized")

        # Step 6: Run tagging cycle to process backlog
        logger.info("[STEP 6] Running tagging cycle (batch_size=100)...")
        await semantic_tagger.run_tagging_cycle(batch_size=100)
        logger.info("✓ Tagging cycle completed")

        # Step 7: Commit changes and close connection
        logger.info("[STEP 7] Committing changes and closing connection...")
        conn.commit()
        logger.info("✓ Changes committed successfully")

        print("\n" + "=" * 70)
        print("PIPELINE STRESS TEST COMPLETED SUCCESSFULLY")
        print("=" * 70)
        logger.info("✓ All pipeline stages executed without errors")

    except ValueError as e:
        logger.error(f"✗ CONFIGURATION ERROR: {e}")
        if conn:
            conn.rollback()
        raise

    except Exception as e:
        logger.error(f"✗ PIPELINE ERROR: {type(e).__name__}: {e}")
        if conn:
            conn.rollback()
        raise

    finally:
        # Always close the database connection
        if conn:
            conn.close()
            logger.info("[CLEANUP] Database connection closed")


if __name__ == "__main__":
    asyncio.run(main())