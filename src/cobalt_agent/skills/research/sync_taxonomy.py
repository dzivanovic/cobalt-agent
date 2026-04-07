"""
Master Taxonomy Sync Script (Recursive Architecture Restored)
Parses the 4-column Master_Taxonomy.md file and syncs data
to the recursive Postgres 'public.themes' table.
"""

import logging
from pathlib import Path
import psycopg2

from cobalt_agent.config import get_config

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def get_db_connection(config):
    return psycopg2.connect(
        host=config.postgres.host,
        port=config.postgres.port,
        database=config.postgres.db,
        user=config.postgres.user,
        password=config.postgres.password,
    )

def parse_markdown_table(file_path: Path) -> list[dict]:
    if not file_path.exists():
        logger.error(f"Taxonomy file not found: {file_path}")
        return []

    content = file_path.read_text(encoding="utf-8")
    lines = content.strip().split("\n")

    themes = []
    in_table = False

    for line in lines:
        clean_line = line.strip()
        
        if "| Macro Theme |" in clean_line and "| Sub-Theme |" in clean_line:
            in_table = True
            continue
            
        if in_table and ("| :---" in clean_line or "|---" in clean_line):
            continue
            
        if in_table and clean_line.startswith("|"):
            parts = [p.strip() for p in clean_line.split("|")]
            # Format: | empty | Macro | Sub | Status | Tickers | empty |
            if len(parts) >= 5: 
                macro_theme = parts[1]
                sub_theme = parts[2]
                status = parts[3].upper()
                tickers = parts[4]
                
                if macro_theme:
                    themes.append({
                        "macro_theme": macro_theme,
                        "sub_theme": sub_theme if sub_theme else None,
                        "status": status,
                        "example_tickers": tickers
                    })
        
        if in_table and not clean_line:
            break

    return themes

def upsert_themes(conn, themes: list[dict]):
    with conn.cursor() as cur:
        for theme in themes:
            macro_name = theme["macro_theme"]
            sub_name = theme["sub_theme"]
            status = theme["status"]
            tickers = theme["example_tickers"]

            # 1. Upsert Macro Theme (Parent)
            cur.execute("SELECT id FROM public.themes WHERE name = %s AND parent_id IS NULL", (macro_name,))
            macro_row = cur.fetchone()
            
            if macro_row:
                macro_id = macro_row[0]
                # Update status of macro if there is no sub-theme
                if not sub_name:
                    cur.execute("""
                        UPDATE public.themes 
                        SET status = %s, example_tickers = %s, updated_at = CURRENT_TIMESTAMP
                        WHERE id = %s
                    """, (status, tickers, macro_id))
            else:
                # Insert new Macro
                if not sub_name:
                    cur.execute("""
                        INSERT INTO public.themes (name, parent_id, status, example_tickers) 
                        VALUES (%s, NULL, %s, %s) RETURNING id;
                    """, (macro_name, status, tickers))
                else:
                    cur.execute("""
                        INSERT INTO public.themes (name, parent_id) 
                        VALUES (%s, NULL) RETURNING id;
                    """, (macro_name,))
                macro_id = cur.fetchone()[0]

            # 2. Upsert Sub-Theme (Child)
            if sub_name:
                cur.execute("""
                    INSERT INTO public.themes (name, parent_id, status, example_tickers)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (name, parent_id) DO UPDATE SET
                        status = EXCLUDED.status,
                        example_tickers = EXCLUDED.example_tickers,
                        updated_at = CURRENT_TIMESTAMP;
                """, (sub_name, macro_id, status, tickers))

    conn.commit()

def sync_taxonomy():
    config = get_config()
    
    MASTER_TAXONOMY_PATH = Path(config.system.obsidian_vault_path) / "0 - Projects/Cobalt/00 - Master Plan/Master_Taxonomy.md"
    
    logger.info(f"Syncing taxonomy from: {MASTER_TAXONOMY_PATH}")
    
    themes = parse_markdown_table(MASTER_TAXONOMY_PATH)
    if not themes:
        logger.warning("No themes parsed. Check Markdown format.")
        return

    conn = get_db_connection(config)
    try:
        upsert_themes(conn, themes)
        logger.info(f"✅ Successfully synced {len(themes)} themes to public.themes table.")
    except Exception as e:
        logger.error(f"Sync failed: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    sync_taxonomy()