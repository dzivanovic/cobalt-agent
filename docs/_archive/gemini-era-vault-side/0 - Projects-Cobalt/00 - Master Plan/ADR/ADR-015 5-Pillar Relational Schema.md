# ADR-015: 5-Pillar Relational Schema

## Status
Active

## Context
The current market data storage uses flat tables that lack relational integrity and flexibility for multi-asset trading (Equities, Options, ETFs). As Cobalt scales to handle semantic news deduplication, MFE/MAE performance tracking, and psychological trader metrics (R-multiples, tiltmeter), the schema must evolve to support:

1. **Multi-Asset Support**: Single unified system for stocks, options chains, and ETFs
2. **Semantic News Deduplication**: Vector embeddings for news clustering and topic extraction
3. **Performance Analytics**: MFE (Maximum Favorable Excursion) / MAE (Maximum Adverse Excursion) tracking
4. **Psychological Metrics**: R-multiples, mistake tags, tilt detection via embeddings
5. **JSONB Flexibility**: Avoid column bloat while maintaining query performance

Additionally, historical candle data will be fetched on-demand via Finviz Quote API rather than stored locally, reducing storage overhead and ensuring data freshness.

## Decision

### 1. PostgreSQL with pgvector Extension
We will use PostgreSQL as the primary database with the `pgvector` extension enabled for:
- Semantic news similarity search (news_events.embedding)
- Journal entry vectorization for pattern detection
- Fast-path caching of computed embeddings

### 2. JSONB for Flexible Metadata
Instead of creating hundreds of columns for dynamic attributes, we will use PostgreSQL's JSONB type for:
- `instruments.active_themes`: Array of active theme tags with metadata
- `news_events.sources`: Multi-source attribution (RSS, Twitter, NewsAPI)
- `trades.mistake_tags`: Psychological error classification with embeddings

### 3. Finviz Quote API for Historical Candles
Historical OHLCV data will NOT be stored locally. Instead:
- Fetch on-demand via Finviz Quote API when needed for analysis
- Cache results temporarily in memory (not persistent storage)
- Reduces database bloat and ensures access to latest historical data

### 4. The 12 Bloat-Free Tables

#### Pillar 1: Entities (Foundation)
| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `instruments` | Master registry of all tradeable assets | symbol, asset_type, name, active_themes (JSONB), created_at |
| `themes` | Taxonomy of market themes/motifs | id, name, description, parent_id (hierarchical) |
| `key_levels` | Support/resistance zones per instrument | instrument_id, level_type, price, source, confidence |
| `daily_in_play` | Daily "in-play" ticker snapshot | date, instrument_id, rank, catalyst, rvol_multiplier |

#### Pillar 2: Physics (Market Data)
| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `market_snapshots` | Real-time price/volume state | instrument_id, timestamp, price, volume, vwap, spread |
| `news_events` | Aggregated news with embeddings | title, summary, embedding (vector), taxonomy_hash, sources (JSONB) |
| `news_mentions` | Link news to instruments/timeframes | event_id, instrument_id, mention_context, sentiment_score |

#### Pillar 3: Catalysts (Alerting)
| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `system_alerts` | MFE/MAE performance tracking | alert_type, threshold, trigger_value, mfe, mae, r_multiple |

#### Pillar 4: Engine (Orchestration)
| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `trading_accounts` | Account/portfolio state | account_id, balance, equity, day_trades_remaining, margin_used |

#### Pillar 5: Execution (Trade Lifecycle)
| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `trades` | Trade lifecycle with psychological tags | instrument_id, direction, entry_price, exit_price, r_multiple, mistake_tags (JSONB), tilt_score |
| `order_fills` | Granular fill history for partials | trade_id, fill_price, quantity, timestamp, commission |

## Consequences
- **Positive**: 12 tables provide complete coverage without column bloat
- **Positive**: JSONB enables flexible schema evolution without migrations
- **Positive**: pgvector enables semantic deduplication and pattern matching
- **Positive**: Finviz API eliminates storage costs for historical candles
- **Negative**: Requires pgvector extension installation and maintenance
- **Negative**: JSONB queries are slightly slower than typed columns (acceptable trade-off)

## References
- [[ADR-011 Vector Librarian]] - Previous vector strategy decision
- [[ADR-013 GraphRAG and Watcher Daemon]] - Entity relationship modeling
- [[PRD-013 Multidimensional Market Data Engine]] - Functional requirements for this schema