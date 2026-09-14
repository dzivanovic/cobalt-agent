# ingest_knowledge.py

## Overview

The `ingest_knowledge.py` script is a data ingestion utility that loads external knowledge files into Cobalt's memory system. It enables the agent to incorporate research documents, market analysis, and other contextual information into its persistent memory store for retrieval during operations.

## Purpose

This script serves the following functions:
- Ingests knowledge files (text, markdown, or structured data) into the memory system
- Processes and indexes content for semantic search capabilities
- Enables knowledge persistence across agent sessions
- Supports batch processing of multiple knowledge sources

## Location

```
dev_utils/ingest_knowledge.py
```

## Dependencies

- Cobalt Agent memory system (`src/cobalt_agent/memory/`)
- Standard Python libraries for file handling and text processing

## How It Works

The ingestion process follows these steps:

1. **File Loading**: Reads the specified knowledge file(s) from disk
2. **Content Parsing**: Extracts and normalizes text content
3. **Chunking**: Splits content into manageable segments for vector embedding
4. **Indexing**: Generates embeddings and stores in the memory database
5. **Metadata Tagging**: Associates metadata for filtering and retrieval

## Usage

### Prerequisites

1. Ensure the memory system is properly configured (see [PostgreSQL Memory](postgres.md))
2. Prepare knowledge files in supported formats (.txt, .md, .csv)

### Running the Script

From the project root:

```bash
uv run dev_utils/ingest_knowledge.py --file <path_to_knowledge_file>
```

For batch ingestion:

```bash
uv run dev_utils/ingest_knowledge.py --directory <path_to_knowledge_directory>
```

### Command-Line Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--file` | Path to single knowledge file | No (use with --directory) |
| `--directory` | Path to directory containing knowledge files | No (use with --file) |
| `--collection` | Target collection name in memory store | No (default: 'knowledge') |

## Expected Output

On successful execution, the script will display:
- Number of documents processed
- Total chunks created and indexed
- Collection name where data was stored

On failure, it will provide:
- Specific error messages for troubleshooting
- File path or content parsing issues

## Troubleshooting

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| File Not Found | Incorrect file path | Verify the file exists at specified location |
| Memory Connection Error | PostgreSQL not running | Start the memory service per postgres.md |
| Empty Content | File contains no parseable text | Check file encoding and content format |

## Related Documentation

- [Knowledge Tool](knowledge.md) - Runtime knowledge retrieval
- [PostgreSQL Memory](postgres.md) - Memory system configuration
- [Cortex](cortex.md) - Knowledge integration with agent brain

## Maintenance Notes

This script should be used:
- When adding new research materials to the agent's knowledge base
- Before major analysis sessions requiring specific domain knowledge
- As part of onboarding new market verticals or strategies