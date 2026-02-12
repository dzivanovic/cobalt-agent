"""
Wipe Memory Script (Smart Version)
Finds ANY table in the public schema and wipes it.
"""
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

# Load credentials from .env
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_NAME = os.getenv("POSTGRES_DB", "cobalt_memory")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "cobalt_password")

def wipe():
    print(f"🔌 Connecting to database: {DB_NAME}...")
    conn_str = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    
    try:
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
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    wipe()