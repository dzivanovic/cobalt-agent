#!/usr/bin/env python3
"""
5-Pillar Schema Initialization Script for Cobalt Agent

This script performs a safe database migration:
1. Loads PostgreSQL credentials from cobalt_agent.config
2. Safely tears down legacy market data tables (tickers)
3. Explicitly preserves Cortex conversational memory tables
4. Creates the new 12-table 5-Pillar Relational Schema

CRITICAL: Cortex memory tables (e.g., 'memory') are NEVER dropped or altered.
"""

import sys
from pathlib import Path
from loguru import logger

# Configure logger for script output
logger.remove()
logger.add(sys.stdout, format="<green>{time:HH:mm:ss}</green> <bold>[INIT]</bold> {message}", level="INFO")


def get_db_connection_string():
    """Build PostgreSQL connection string from config."""
    from cobalt_agent.config import get_config
    
    config = get_config()
    postgres = config.postgres
    
    return {
        "host": postgres.host,
        "port": postgres.port,
        "user": postgres.user,
        "password": postgres.password,
        "database": postgres.db
    }


def execute_sql_file(cursor, sql_file_path: Path):
    """Execute all SQL statements from a file with auto-commit per statement."""
    logger.info(f"Reading SQL schema from: {sql_file_path}")
    
    with open(sql_file_path, "r") as f:
        sql_content = f.read()
    
    # Remove comments and split by semicolons more carefully
    lines = sql_content.split("\n")
    statements = []
    current_stmt = ""
    
    for line in lines:
        # Skip comment lines
        stripped = line.strip()
        if stripped.startswith("--"):
            continue
        
        current_stmt += line + "\n"
        
        # Check if line ends with semicolon (end of statement)
        if stripped.endswith(";"):
            stmt = current_stmt.strip()
            if stmt:
                statements.append(stmt)
            current_stmt = ""
    
    executed_count = 0
    skipped_count = 0
    
    for statement in statements:
        try:
            # Execute and immediately commit to avoid transaction blocking
            cursor.execute(statement)
            conn = cursor.connection
            conn.commit()
            executed_count += 1
            # Get table name from CREATE TABLE statement for logging
            if "CREATE TABLE" in statement.upper():
                import re
                match = re.search(r'CREATE TABLE IF NOT EXISTS (\w+)', statement, re.IGNORECASE)
                if match:
                    logger.info(f"Created table: {match.group(1)}")
                else:
                    logger.info(f"Executed: {statement[:60]}...")
            elif "CREATE EXTENSION" in statement.upper():
                logger.info(f"Created extension")
        except Exception as e:
            # Some statements may fail (e.g., extension already exists) - log but continue
            skipped_count += 1
            logger.warning(f"Statement failed: {e}")
    
    logger.info(f"Total executed: {executed_count}, skipped: {skipped_count}")
    return executed_count


def main():
    """Main initialization routine."""
    logger.info("=" * 60)
    logger.info("Cobalt Agent - 5-Pillar Schema Initialization")
    logger.info("=" * 60)
    
    # Step 1: Load credentials from config
    logger.info("Loading PostgreSQL credentials from cobalt_agent.config...")
    db_config = get_db_connection_string()
    
    logger.info(f"Connecting to PostgreSQL at {db_config['host']}:{db_config['port']}/{db_config['database']}")
    
    try:
        import psycopg2
    except ImportError:
        logger.error("psycopg2 not installed. Run: uv add psycopg2-binary")
        sys.exit(1)
    
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        logger.info("✓ Database connection established")
    except Exception as e:
        logger.error(f"Failed to connect to database: {e}")
        sys.exit(1)
    
    try:
        # Step 2: Safe teardown of legacy market tables ONLY
        logger.info("-" * 60)
        logger.info("Step 1: Safe teardown of legacy market data tables")
        
        # ONLY drop the old tickers table - NEVER touch Cortex memory tables
        legacy_drop_sql = """
        -- Drop legacy market data table (safe - only affects old tickers)
        DROP TABLE IF EXISTS tickers CASCADE;
        
        -- IMPORTANT: Cortex memory tables are EXPLICITLY PRESERVED
        -- The following tables are NOT touched:
        -- - memory (conversational memory)
        -- - conversation_metadata
        -- - graph_nodes, graph_edges (knowledge graph)
        """
        
        cursor.execute(legacy_drop_sql)
        conn.commit()
        logger.info("✓ Legacy 'tickers' table dropped (if existed)")
        logger.info("✓ Cortex memory tables PRESERVED (not touched)")
        
        # Step 3: Execute the new schema
        logger.info("-" * 60)
        logger.info("Step 2: Creating new 12-table 5-Pillar Schema")
        
        schema_path = Path(__file__).parent.parent / "src" / "cobalt_agent" / "db" / "schema.sql"
        
        if not schema_path.exists():
            logger.error(f"Schema file not found: {schema_path}")
            sys.exit(1)
        
        executed = execute_sql_file(cursor, schema_path)
        conn.commit()
        
        logger.info(f"✓ Executed {executed} SQL statements from schema.sql")
        
        # Step 4: Verify tables were created
        logger.info("-" * 60)
        logger.info("Step 3: Verifying schema creation")
        
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name
        """)
        
        tables = [row[0] for row in cursor.fetchall()]
        
        expected_tables = [
            "daily_in_play",
            "instruments",
            "key_levels",
            "market_snapshots",
            "news_events",
            "news_mentions",
            "order_fills",
            "system_alerts",
            "themes",
            "trading_accounts",
            "trades"
        ]
        
        logger.info("✓ Tables in database:")
        for table in tables:
            marker = "✓" if table in expected_tables else "~"
            logger.info(f"  {marker} {table}")
        
        # Verify all expected tables exist
        missing = set(expected_tables) - set(tables)
        if missing:
            logger.error(f"✗ Missing expected tables: {missing}")
            sys.exit(1)
        
        logger.info("-" * 60)
        logger.info("=" * 60)
        logger.info("SUCCESS: 5-Pillar Schema initialized successfully!")
        logger.info(f"Created {len(expected_tables)} tables for the 5-Pillar Relational Schema")
        logger.info("=" * 60)
        
    except Exception as e:
        conn.rollback()
        logger.error(f"Initialization failed: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
        logger.info("Database connection closed")


if __name__ == "__main__":
    main()