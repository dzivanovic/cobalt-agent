"""
Knowledge Ingestion Engine
Sweeps the codebase, config files, and docs, chunks them, and embeds them into the Postgres Vector DB.
"""
import os
import sys
from pathlib import Path
from loguru import logger

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from cobalt_agent.memory.postgres import PostgresMemory

def chunk_text(text: str, max_chars: int = 1500, overlap: int = 200) -> list[str]:
    """Splits text into overlapping chunks."""
    chunks = []
    start = 0
    text_len = len(text)
    
    while start < text_len:
        end = start + max_chars
        chunks.append(text[start:end])
        start += max_chars - overlap
    return chunks

def ingest_directory(db: PostgresMemory, base_dir: Path, extensions: list[str], source_type: str):
    logger.info(f"Scanning {base_dir} for {extensions}...")
    
    if not base_dir.exists():
        logger.warning(f"Directory {base_dir} does not exist. Skipping.")
        return

    files_processed = 0
    chunks_embedded = 0

    for ext in extensions:
        for file_path in base_dir.rglob(f"*{ext}"):
            # Skip hidden dirs and env
            if any(part.startswith('.') for part in file_path.parts) or 'venv' in file_path.parts:
                continue
                
            try:
                content = file_path.read_text(encoding='utf-8')
                if not content.strip():
                    continue
                    
                chunks = chunk_text(content)
                
                for chunk in chunks:
                    metadata = {
                        "filepath": str(file_path.relative_to(base_dir.parent)),
                        "type": source_type
                    }
                    # Add to vector DB
                    db.add_log(
                        message=chunk,
                        source=source_type,
                        data=metadata
                    )
                    chunks_embedded += 1
                files_processed += 1
                
            except Exception as e:
                logger.error(f"Failed to read {file_path}: {e}")

    logger.info(f"✅ Finished {source_type}: Processed {files_processed} files into {chunks_embedded} vector chunks.")

def main():
    logger.info("🚀 Starting Knowledge Ingestion Pipeline...")
    db = None
    try:
        with PostgresMemory() as db:
            project_root = Path(__file__).parent.parent

            # 1. Ingest Codebase
            ingest_directory(db, project_root / "src", [".py"], "python_code")
            
            # 2. Ingest Playbooks
            ingest_directory(db, project_root / "configs", [".yaml", ".yml"], "configuration")
            
            # 3. Ingest Obsidian Sandbox
            ingest_directory(db, project_root / "docs", [".md"], "obsidian_note")
            
            logger.info("🎉 Ingestion Complete. The Vector Librarian is ready.")
    except Exception as e:
        logger.exception(f"Database operation failed: {e}")
        return

if __name__ == "__main__":
    main()
