#!/usr/bin/env python3
"""
Test Script: 5-Pillar Database Integration Test (Sprint 06 - Task 1.9)

Purpose:
    Verify that the PostgreSQL database correctly accepts and returns data,
    specifically focusing on JSONB columns and foreign key relationships.

Operations:
    1. Insert a dummy instrument (TEST_NVDA)
    2. Insert a market snapshot with JSONB payload
    3. Query using JSONB filter (raw_data->>'Price')
    4. Print retrieved payload to verify serialization/deserialization
    5. Teardown: Delete test data to leave database clean

Author: Cobalt SRE
"""

import sys
from pathlib import Path

# Add src to path for imports (standard project pathing)
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import psycopg2
from psycopg2.extras import RealDictCursor, Json
from psycopg2 import IntegrityError, Error

from cobalt_agent.config import get_config


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
    
    return psycopg2.connect(
        host=db_config.host,
        port=db_config.port,
        database=db_config.db,
        user=db_config.user,
        password=db_config.password,
    )


def insert_test_instrument(cursor, symbol: str = "TEST_NVDA", asset_class: str = "EQUITY"):
    """
    Insert a dummy instrument into the instruments table.
    
    Args:
        cursor: Database cursor
        symbol: Test instrument symbol (default: TEST_NVDA)
        asset_class: Asset class type (default: EQUITY)
    
    Returns:
        str: UUID of inserted instrument
    
    Raises:
        psycopg2.IntegrityError: If symbol already exists (unique constraint)
    """
    metadata = {"test": True, "created_by": "5_pillar_integration_test"}
    
    cursor.execute(
        """
        INSERT INTO instruments (symbol, asset_class, metadata)
        VALUES (%s, %s, %s)
        ON CONFLICT (symbol) DO UPDATE SET metadata = EXCLUDED.metadata
        RETURNING id;
        """,
        (symbol, asset_class, Json(metadata)),
    )
    
    result = cursor.fetchone()
    return str(result["id"])


def insert_test_snapshot(cursor, instrument_id: str, raw_data: dict):
    """
    Insert a market snapshot with JSONB payload.
    
    Args:
        cursor: Database cursor
        instrument_id: UUID of the linked instrument
        raw_data: Dictionary containing market data (stored as JSONB)
    
    Returns:
        str: UUID of inserted snapshot
    
    Raises:
        psycopg2.ForeignKeyViolation: If instrument_id doesn't exist
    """
    cursor.execute(
        """
        INSERT INTO market_snapshots (instrument_id, price, volume, raw_data)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        """,
        (instrument_id, raw_data.get("Price"), raw_data.get("Volume"), Json(raw_data)),
    )
    
    result = cursor.fetchone()
    return str(result["id"])


def query_snapshot_by_jsonb(cursor, price: float):
    """
    Query market_snapshots using JSONB filter.
    
    Args:
        cursor: Database cursor
        price: Price value to match (uses raw_data->>'Price')
    
    Returns:
        list: Matching snapshot records
    
    Raises:
        psycopg2.Error: If query fails
    """
    cursor.execute(
        """
        SELECT id, instrument_id, timestamp, price, volume, raw_data
        FROM market_snapshots
        WHERE raw_data->>'Price' = %s;
        """,
        (str(price),),
    )
    
    return cursor.fetchall()


def delete_snapshot(cursor, snapshot_id: str):
    """Delete a market snapshot by ID."""
    cursor.execute(
        "DELETE FROM market_snapshots WHERE id = %s;",
        (snapshot_id,),
    )


def delete_instrument(cursor, symbol: str = "TEST_NVDA"):
    """Delete a test instrument by symbol."""
    cursor.execute(
        "DELETE FROM instruments WHERE symbol = %s;",
        (symbol,),
    )


def run_integration_test():
    """
    Execute the full integration test workflow.
    
    Workflow:
        1. Connect to database
        2. Insert test instrument (TEST_NVDA)
        3. Insert market snapshot with JSONB payload
        4. Query using JSONB filter
        5. Print results to verify serialization
        6. Teardown: Delete test data
    
    Returns:
        bool: True if all tests pass, False otherwise
    """
    conn = None
    
    try:
        print("=" * 60)
        print("5-PILLAR DATABASE INTEGRATION TEST")
        print("=" * 60)
        
        # Step 1: Connect to database
        print("\n[STEP 1] Connecting to PostgreSQL...")
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        print("✓ Connection established")
        
        # Step 2: Insert test instrument
        print("\n[STEP 2] Inserting dummy instrument (TEST_NVDA)...")
        instrument_id = insert_test_instrument(cursor)
        print(f"✓ Instrument inserted with ID: {instrument_id}")
        
        # Step 3: Insert market snapshot with JSONB payload
        print("\n[STEP 3] Inserting market snapshot with JSONB payload...")
        test_raw_data = {
            "Price": 120.50,
            "Volume": 5000000,
            "ATR": 1.5,
        }
        snapshot_id = insert_test_snapshot(cursor, instrument_id, test_raw_data)
        print(f"✓ Snapshot inserted with ID: {snapshot_id}")
        conn.commit()
        
        # Step 4: Query using JSONB filter
        print("\n[STEP 4] Querying snapshot with JSONB filter (raw_data->>'Price' = '120.50')...")
        results = query_snapshot_by_jsonb(cursor, 120.50)
        
        if not results:
            print("✗ FAILED: No results returned from JSONB query")
            return False
        
        print(f"✓ Query returned {len(results)} result(s)")
        
        # Step 5: Print retrieved JSONB payload
        print("\n" + "=" * 60)
        print("RETRIEVED SNAPSHOT DATA")
        print("=" * 60)
        
        for record in results:
            print(f"\nSnapshot ID: {record['id']}")
            print(f"Instrument ID: {record['instrument_id']}")
            print(f"Timestamp: {record['timestamp']}")
            print(f"Price (from table): {record['price']}")
            print(f"Volume (from table): {record['volume']}")
            print("\nRaw JSONB Payload:")
            print("-" * 40)
            
            # The raw_data is already deserialized by psycopg2
            import json
            print(json.dumps(record["raw_data"], indent=4))
            
            # Verify the data matches what we inserted
            retrieved_price = record["raw_data"].get("Price")
            retrieved_volume = record["raw_data"].get("Volume")
            retrieved_atr = record["raw_data"].get("ATR")
            
            print("\n" + "-" * 40)
            print("VERIFICATION:")
            
            if retrieved_price == test_raw_data["Price"]:
                print(f"✓ Price matches: {retrieved_price}")
            else:
                print(f"✗ Price mismatch: expected {test_raw_data['Price']}, got {retrieved_price}")
                return False
            
            if retrieved_volume == test_raw_data["Volume"]:
                print(f"✓ Volume matches: {retrieved_volume}")
            else:
                print(f"✗ Volume mismatch: expected {test_raw_data['Volume']}, got {retrieved_volume}")
                return False
            
            if retrieved_atr == test_raw_data["ATR"]:
                print(f"✓ ATR matches: {retrieved_atr}")
            else:
                print(f"✗ ATR mismatch: expected {test_raw_data['ATR']}, got {retrieved_atr}")
                return False
        
        print("\n✓ JSONB serialization/deserialization verified successfully!")
        
        # Step 6: Teardown - Clean up test data
        print("\n" + "=" * 60)
        print("TEARDOWN: Cleaning up test data...")
        
        delete_snapshot(cursor, snapshot_id)
        print(f"✓ Deleted snapshot ID: {snapshot_id}")
        
        delete_instrument(cursor)
        print(f"✓ Deleted instrument: TEST_NVDA")
        
        conn.commit()
        
        print("\n" + "=" * 60)
        print("TEST RESULT: ALL CHECKS PASSED")
        print("=" * 60)
        print("\nThe 5-Pillar database schema is ready for Task 2 (Finviz Orchestrator).")
        
        return True
        
    except IntegrityError as e:
        print(f"\n✗ INTEGRITY ERROR (FK/Unique constraint): {e}")
        if conn:
            conn.rollback()
        return False
        
    except Error as e:
        print(f"\n✗ DATABASE ERROR: {e}")
        if conn:
            conn.rollback()
        return False
        
    except ValueError as e:
        print(f"\n✗ CONFIGURATION ERROR: {e}")
        return False
        
    except Exception as e:
        print(f"\n✗ UNEXPECTED ERROR: {type(e).__name__}: {e}")
        if conn:
            conn.rollback()
        return False
        
    finally:
        # Always close the connection
        if conn:
            conn.close()
            print("\n[CLEANUP] Database connection closed")


if __name__ == "__main__":
    success = run_integration_test()
    sys.exit(0 if success else 1)