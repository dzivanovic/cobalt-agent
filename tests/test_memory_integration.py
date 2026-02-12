"""
Memory Integration Tests
Verifies that the Docker Database is reachable and properly configured.
"""
import os
import pytest
import psycopg  # We assume psycopg 3 (modern standard)

# Load environment variables (normally loaded by python-dotenv in app)
# For tests, we can just grab them from os if they are set, or define defaults
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_NAME = os.getenv("POSTGRES_DB", "cobalt_memory")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "cobalt_password")

def get_connection_string():
    return f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"

@pytest.mark.integration
def test_database_connection():
    """Can we actually knock on the door?"""
    try:
        conn_str = get_connection_string()
        with psycopg.connect(conn_str) as conn:
            # Execute a simple query
            res = conn.execute("SELECT 1").fetchone()
            assert res[0] == 1
    except Exception as e:
        pytest.fail(f"Could not connect to Docker DB: {e}")

@pytest.mark.integration
def test_vector_extension_enabled():
    """
    CRITICAL: Is the 'pgvector' extension turned on?
    Without this, the AI cannot have Long-Term Memory.
    """
    conn_str = get_connection_string()
    with psycopg.connect(conn_str) as conn:
        # Check the pg_extension table
        res = conn.execute("SELECT extname FROM pg_extension WHERE extname = 'vector'").fetchone()
        
        if not res:
            pytest.fail("The 'vector' extension is missing! Memory retrieval will fail.")
        
        assert res[0] == "vector"

@pytest.mark.integration
def test_create_and_read_memory():
    """Can we write a fake memory and read it back?"""
    conn_str = get_connection_string()
    table_name = "test_memory_check"
    
    with psycopg.connect(conn_str) as conn:
        # 1. Create a dummy table
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                content TEXT
            );
        """)
        
        # 2. Insert data
        test_phrase = "Cobalt Integration Test"
        conn.execute(f"INSERT INTO {table_name} (content) VALUES (%s)", (test_phrase,))
        
        # 3. Read it back
        res = conn.execute(f"SELECT content FROM {table_name} ORDER BY id DESC LIMIT 1").fetchone()
        assert res[0] == test_phrase
        
        # 4. Cleanup (Drop table)
        conn.execute(f"DROP TABLE {table_name}")