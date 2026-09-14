---
title: "ADR-005 Agentic RAG"
status: Active 
priority: P0
module: [Architecture]
phase: 1
complexity: M
tags: [cobalt, architecture, documentation, adr]
created: 2026-02-23
---

# ADR-005: Agentic RAG - Memory as a Tool

## Status: ACCEPTED

## Decision

We implement an **Agentic RAG (Retrieval-Augmented Generation)** system using **Memory as a Tool** rather than passive context injection.

### Architecture
```
                    ┌──────────────┐
                    │   User Query │
                    └───┬───────┬──┘
                        │       │
              ┌─────────▼───┐   │
              │   Query     │   │
              │   Encoder   │   │
              └───┬─┬─┬─────┘   │
                  │ │ │
        ┌─────────┘ │ └──────┐
        │           │        │
┌───────▼────┐ ┌───▼──┐ ┌───▼───┐
│  Postgres  │ │Vector│ │  Agentic│
│   pgvector │ │Search│ │  RAG    │
│  (Storage) │ │Engine│ │  Tool   │
└────────────┘ └──────┘ └───────┘
        │           │        │
        └───────────┴────────┘
                    │
        ┌───────────▼────────┐
        │   Generated        │
        │   Response         │
        └────────────────────┘
```

### Components

#### 1. Postgres/pgvector Database
- Stores all conversation logs with vector embeddings
- Uses cosine similarity for search
- Indexes on timestamp and source

#### 2. Vector Search Engine
- Converts query to embedding
- Retrieves similar memories by semantic similarity
- Applies temporal and relevance filters

#### 3. Agentic RAG Tool
- Memory retrieval as a callable tool
- Context-aware query routing
- Dynamic memory injection into prompts

### Memory Rules
| Rule Type | Behavior |
|-----------|----------|
| **PREFERENCE** | Keep forever (e.g., "I like TSLA") |
| **MARKET CONTEXT** | Expire after 24 hours |
| **SESSION** | Expire after conversation ends |

## Implementation Details

### Database Schema
```sql
CREATE TABLE memory_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source VARCHAR(255),
    message TEXT,
    data JSONB,
    embedding VECTOR(768)
);

CREATE INDEX idx_memory_embedding ON memory_logs 
USING ivfflat (embedding vector_cosine_ops);
```

### Python Interface
```python
class AgenticRAG:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.session = Session()
    
    def store_memory(self, message: str, source: str, data: dict):
        embedding = self._generate_embedding(message)
        self.session.add(MemoryLog(
            message=message,
            source=source,
            data=data,
            embedding=embedding
        ))
        self.session.commit()
    
    def search_memories(self, query: str, limit: int = 10) -> List[Dict]:
        query_embedding = self._generate_embedding(query)
        results = self.session.execute(
            """
            SELECT message, source, data, 
                   1 - (embedding <=> :query_embedding) as similarity
            FROM memory_logs
            WHERE timestamp > NOW() - INTERVAL '24 hours'
            ORDER BY similarity DESC
            LIMIT :limit
            """,
            {"query_embedding": query_embedding, "limit": limit}
        )
        return results.fetchall()
```

### Memory Filter Rules
```python
def filter_memories(memories: List[Dict], context: Dict) -> List[Dict]:
    # Remove stale memories
    filtered = [m for m in memories 
                if not _is_stale(m, context)]
    
    # Apply relevance threshold
    return [m for m in filtered if m['similarity'] > 0.5]
```

## Trade-offs

| Option | Pros | Cons |
|--------|------|------|
| Keyword Search | Fast | Poor semantic understanding |
| Full RAG (Chosen) | High quality retrieval | Requires vector storage |

## Next Steps

1. Set up Postgres with pgvector extension
2. Implement embedding generation
3. Create memory filter rules engine
4. Integrate RAG into PromptEngine

## References

- [pgvector Documentation](https://github.com/pgvector/pgvector)
- [Retrieval-Augmented Generation Paper](https://arxiv.org/abs/2005.11401)