"""
Knowledge Ingestion Engine
Sweeps the codebase, config files, and docs, chunks them, and embeds them into the Postgres Vector DB.
"""
import os
import sys
import ast
from pathlib import Path
from loguru import logger

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from cobalt_agent.memory.postgres import PostgresMemory

def ingest_ast_graph(target_dir: str = "src/") -> tuple[int, int]:
    """Parse .py files via AST and map code dependencies to graph tables.
    
    Returns:
        Tuple of (nodes_created, edges_created) counts
    """
    import ast
    
    target_path = Path(target_dir)
    if not target_path.exists():
        logger.error(f"Target directory {target_path} does not exist")
        return 0, 0
    
    db = PostgresMemory()
    nodes_created, edges_created = 0, 0
    
    try:
        for py_file in target_path.rglob("*.py"):
            if any(p.startswith('.') or p == 'venv' for p in py_file.parts):
                continue
            
            try:
                content = py_file.read_text(encoding='utf-8')
                tree = ast.parse(content)
                rel_path = str(py_file.relative_to(target_path.parent))
                
                # Create File node
                file_node_id = db.upsert_node("File", rel_path, {"size_bytes": len(content)})
                nodes_created += 1
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        class_node_id = db.upsert_node("Class", f"{rel_path}:{node.name}", 
                            {"decorators": [ast.unparse(d) for d in node.decorator_list]})
                        nodes_created += 1
                        db.upsert_edge(file_node_id, class_node_id, "CONTAINS")
                        edges_created += 1
                        
                        for subnode in ast.walk(node):
                            if isinstance(subnode, ast.FunctionDef):
                                func_node_id = db.upsert_node("Method", f"{rel_path}:{node.name}.{subnode.name}",
                                    {"decorators": [ast.unparse(d) for d in subnode.decorator_list]})
                                nodes_created += 1
                                db.upsert_edge(class_node_id, func_node_id, "CONTAINS")
                                edges_created += 1
                    
                    elif isinstance(node, ast.FunctionDef):
                        func_node_id = db.upsert_node("Function", f"{rel_path}:{node.name}",
                            {"decorators": [ast.unparse(d) for d in node.decorator_list]})
                        nodes_created += 1
                        db.upsert_edge(file_node_id, func_node_id, "CONTAINS")
                        edges_created += 1
                    
                    elif isinstance(node, ast.Import):
                        for mod in node.names:
                            if mod.name.startswith('cobalt_agent'):
                                target_file = f"{mod.name.replace('.', '/')}.py"
                                if (target_path.parent / target_file).exists():
                                    db.upsert_edge(file_node_id, 
                                        db.upsert_node("File", target_file, {}), "IMPORTS")
                                    edges_created += 1
                    
                    elif isinstance(node, ast.ImportFrom):
                        if node.module and node.module.startswith('cobalt_agent'):
                            target_file = f"{node.module.replace('.', '/')}.py"
                            if (target_path.parent / target_file).exists():
                                db.upsert_edge(file_node_id,
                                    db.upsert_node("File", target_file, {}), "IMPORTS")
                                edges_created += 1
                
                logger.debug(f"✅ {rel_path}: {nodes_created} nodes, {edges_created} edges")
                
            except Exception as e:
                logger.error(f"Failed to parse {py_file}: {e}")
    
    finally:
        db.close()
    
    logger.info(f"🧠 AST Graph Ingestion Complete: {nodes_created} nodes, {edges_created} edges")
    return nodes_created, edges_created

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
