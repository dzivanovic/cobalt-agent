"""
Brain Scan v2 - Deep Diagnostic
Checks Schema, Content, and Embedding Health.
Uses centralized config from cobalt_agent.config.
"""
import sys
import os

# Ensure we can import cobalt_agent
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from cobalt_agent.config import load_config

def scan():
    """
    Connect to database using centralized config and scan memory logs.
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
        print(f"🔬 Scanning Database: {db_config.db}")
        
        # 1. GET TABLE INFO
        table_name = 'memory_logs'
        columns = conn.execute(f"""
            SELECT column_name, data_type 
            FROM information_schema.columns 
            WHERE table_name = '{table_name}';
        """).fetchall()
        
        print(f"\n📋 Schema for '{table_name}':")
        has_vector = False
        for col in columns:
            print(f"   - {col[0]} ({col[1]})")
            if 'vector' in col[1] or 'embedding' in col[0]:
                has_vector = True
        
        if not has_vector:
            print("\n❌ CRITICAL: No VECTOR column found! Semantic search is impossible.")
        
        # 2. CHECK CONTENT (Last 20 items)
        print(f"\n📜 Recent Memories (Last 20):")
        # We explicitly ask for embedding status
        query = f"""
            SELECT id, source, content, 
                   (embedding IS NOT NULL) as has_vector 
            FROM {table_name} 
            ORDER BY timestamp DESC LIMIT 20;
        """
        
        try:
            rows = conn.execute(query).fetchall()
        except Exception as e:
            # Fallback if 'embedding' column doesn't exist
            print(f"⚠️ Query failed (likely missing column): {e}")
            rows = conn.execute(f"SELECT id, source, content FROM {table_name} ORDER BY timestamp DESC LIMIT 20").fetchall()

        found_tsla = False
        for row in rows:
            id_val = row[0]
            source = row[1]
            content = row[2][:60].replace("\n", " ") # Truncate for display
            
            # Check vector status if we grabbed it
            vector_status = "✅" if (len(row) > 3 and row[3]) else "❌ NULL"
            
            print(f"   [{id_val}] {vector_status} | {source}: {content}...")
            
            if "TSLA" in content:
                found_tsla = True

        print("\n--- DIAGNOSIS ---")
        if not found_tsla:
            print("❌ 'TSLA' memory NOT FOUND in database. The Write failed.")
        else:
            print("✅ 'TSLA' memory FOUND.")

if __name__ == "__main__":
    scan()