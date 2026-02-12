import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def reset_table():
    host = os.getenv("POSTGRES_HOST", "localhost")
    db = os.getenv("POSTGRES_DB", "cobalt_memory")
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "cobalt_password")
    
    conn_str = f"postgresql://{user}:{password}@{host}:5432/{db}"
    
    try:
        with psycopg.connect(conn_str, autocommit=True) as conn:
            print(f"🔌 Connecting to {db}...")
            # Drop the table that has the wrong schema
            conn.execute("DROP TABLE IF EXISTS memory_logs;")
            print("💥 Table 'memory_logs' destroyed successfully.")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    reset_table()