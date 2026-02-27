"""
Wipe Memory Script (Smart Version)
Finds ANY table in the public schema and wipes it.
Uses centralized config from cobalt_agent.config.
"""
import sys
import os

# Ensure we can import cobalt_agent
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from cobalt_agent.config import load_config

def wipe():
    """
    Connect to database using centralized config and wipe all memory tables.
    Raises ValueError if critical database credentials are missing.
    """
    # Load config and extract database credentials
    config = load_config()
    
    # Validate required database credentials
    db_config = config.postgres
    required_fields = ["host", "db", "user", "password"]
    missing = [f for f in required_fields if getattr(db_config, f, None) is None]
    
    if missing:
        raise ValueError("Missing critical database environment variable(s): {}. Check .env".format(", ".join(missing)))
    
    conn_str = f"postgresql://{db_config.user}:{db_config.password}@{db_config.host}:5432/{db_config.db}"
    
    import psycopg
    with psycopg.connect(conn_str, autocommit=True) as conn:
        # 1. Find the table name automatically
        res = conn.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public';
        """).fetchall()
        
        if not res:
            print("⚠️  No tables found in 'public' schema. Database is truly empty.")
            return

        # 2. Loop through and wipe them
        for row in res:
            table_name = row[0]
            print(f"🧹 Wiping table: {table_name}...")
            conn.execute(f"TRUNCATE TABLE {table_name};")
        
        print("✨ All memory tables wiped clean.")

if __name__ == "__main__":
    wipe()