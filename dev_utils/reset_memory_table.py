"""
Reset Memory Table
Drops and recreates memory_logs table for clean testing.
Uses centralized config from cobalt_agent.config.
"""
import sys
import os

# Ensure we can import cobalt_agent
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from cobalt_agent.config import load_config

def reset_table():
    """
    Connect to database using centralized config and reset memory_logs table.
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
    with psycopg.connect(conn_str) as conn:
        print(f"🔁 Resetting table in database: {db_config.db}")
        
        table_name = 'memory_logs'
        
        # Drop table if exists
        conn.execute(f"DROP TABLE IF EXISTS {table_name};")
        print(f"✅ Dropped table: {table_name}")
        
        # Recreate table
        create_table_query = f"""
        CREATE TABLE {table_name} (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            source VARCHAR(255),
            content TEXT,
            embedding vector(768)
        );
        """
        conn.execute(create_table_query)
        print(f"✅ Created table: {table_name}")

if __name__ == "__main__":
    reset_table()