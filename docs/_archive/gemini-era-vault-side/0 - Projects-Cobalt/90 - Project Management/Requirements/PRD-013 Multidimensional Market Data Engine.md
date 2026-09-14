---
title: "PRD-013: Multidimensional Market Data Engine"
status: Approved
priority: P0
module: Core
phase: 5
complexity: H
tags: [cobalt, prd, requirements, data-engine]
created: 2026-03-25
---

# PRD-013: Multidimensional Market Data Engine

## 1. Executive Summary
**The Vision:** Build a relational market data engine that bridges raw market signals to human-readable Playbook generation.

**The Problem:** Current flat-table storage cannot support multi-asset trading, semantic news deduplication, or psychological performance tracking. The system lacks the relational integrity needed to connect instruments → themes → levels → trades → performance metrics.

**The Solution:** A 5-Pillar Relational Schema with PostgreSQL + pgvector that enables:
- Multi-asset support (Equities, Options, ETFs) in a unified model
- Semantic news clustering via vector embeddings
- MFE/MAE performance analytics with R-multiple tracking
- Psychological mistake tagging with tilt detection
- Automatic Obsidian Playbook generation via [[Ion Bridge]]

## 2. The 5-Pillar Architecture

### Pillar 1: Entities (Foundation)
**Purpose:** Master registry of all tradeable assets and their relationships.

**Functional Requirements:**
- `instruments` table must support asset_type enumeration (EQUITY, OPTION, ETF)
- `active_themes` JSONB field stores real-time theme associations (e.g., ["AI", "Earnings", "Breakout"])
- `themes` table provides hierarchical taxonomy with parent_id for motif grouping
- `key_levels` stores support/resistance with confidence scoring per instrument
- `daily_in_play` captures daily "in-play" ticker rankings with catalyst attribution

**Key Queries:**
```sql
-- Find all instruments in a theme
SELECT i.symbol FROM instruments i 
JOIN instrument_themes it ON i.id = it.instrument_id 
WHERE it.theme = 'AI';

-- Get key levels for a ticker
SELECT * FROM key_levels WHERE instrument_id = $1 ORDER BY price;
```

### Pillar 2: Physics (Market Data)
**Purpose:** Real-time market state capture with semantic news correlation.

**Functional Requirements:**
- `market_snapshots` captures price/volume/VWAP/spread at millisecond granularity
- `news_events` stores LLM-extracted summaries with vector embeddings for deduplication
- `news_mentions` links news to instruments with sentiment scoring
- Semantic similarity search via pgvector for clustering related news

**Key Queries:**
```sql
-- Find similar news events
SELECT * FROM news_events 
WHERE embedding <=> $1 < 0.7;

-- Get sentiment for instrument
SELECT n.summary, m.sentiment_score 
FROM news_mentions m 
JOIN news_events n ON m.event_id = n.id 
WHERE m.instrument_id = $1;
```

### Pillar 3: Catalysts (Alerting)
**Purpose:** Performance tracking and system alerting based on MFE/MAE thresholds.

**Functional Requirements:**
- `system_alerts` tracks MFE (Maximum Favorable Excursion) and MAE (Maximum Adverse Excursion)
- R-multiple calculation for each trade's performance
- Configurable threshold-based alerting (e.g., "Alert when MAE > 2R")

**Key Queries:**
```sql
-- Get MFE/MAE distribution by strategy
SELECT AVG(mfe), AVG(mae), COUNT(*) 
FROM system_alerts 
WHERE alert_type = 'trade_complete';
```

### Pillar 4: Engine (Orchestration)
**Purpose:** Account/portfolio state management and risk tracking.

**Functional Requirements:**
- `trading_accounts` tracks balance, equity, day trades remaining (Pattern Day Trader compliance)
- Real-time margin usage calculation
- Integration with [[Cobalt-Ion Tactical HUD]] for risk limits

**Key Queries:**
```sql
-- Check PDT compliance
SELECT day_trades_remaining FROM trading_accounts 
WHERE account_id = $1 AND date = CURRENT_DATE;
```

### Pillar 5: Execution (Trade Lifecycle)
**Purpose:** Complete trade lifecycle with psychological metadata.

**Functional Requirements:**
- `trades` table captures full lifecycle: entry → management → exit
- `mistake_tags` JSONB stores psychological errors (FOMO, Revenge, Overtrade)
- `tilt_score` quantifies emotional state during trade execution
- `order_fills` captures partial fills with granular timestamp data

**Key Queries:**
```sql
-- Get R-multiple distribution by mistake type
SELECT mistake_tags->>'type' as mistake, AVG(r_multiple) 
FROM trades 
GROUP BY mistake_tags->>'type';
```

## 3. Multi-Asset Abstraction Layer

The schema unifies all asset types through a single `instruments` table:

| Asset Type | asset_type Value | Special Handling |
|------------|------------------|------------------|
| Equities | `EQUITY` | Standard OHLCV + news |
| Options | `OPTION` | Links to underlying via `active_themes` |
| ETFs | `ETF` | Holdings analysis via themes |

**Unified Query Pattern:**
```sql
-- Works for ALL asset types
SELECT * FROM trades t 
JOIN instruments i ON t.instrument_id = i.id 
WHERE i.asset_type IN ('EQUITY', 'OPTION', 'ETF');
```

## 4. The 2x2 Performance Matrix

### System Edge (Quantitative)
- **MFE/MAE Analysis**: Measures how price moved after entry
- **R-Multiple Distribution**: Statistical analysis of win/loss ratios
- **Theme Performance**: Which market themes produce highest EV?

### Trader Edge (Qualitative)
- **Mistake Tagging**: Human errors classified and tracked
- **Tilt Detection**: Emotional state quantified per trade
- **Execution Quality**: Did the trader follow their playbook?

**Matrix Output:**
```
                    HIGH SYSTEM EDGE
                    ┌───────────────┐
    LOW TRADER EGE  │  FIX EXECUTION│
                    ├───────────────┤
    HIGH TRADER EDGE│  SCALE SIZE   │
                    └───────────────┘
                    LOW SYSTEM EDGE
```

## 5. Obsidian Bridge: Playbook Generation

### Data Flow
1. **Raw Trade** → PostgreSQL `trades` table
2. **Mistake Tags** → LLM analysis for pattern detection
3. **Theme Correlation** → Join with `themes` table
4. **Playbook Entry** → Auto-generated Markdown in Obsidian

### Generated Playbook Structure
```markdown
---
tags: [playbook, setup, gap-and-go]
instrument: [[NVDA]]
date: 2026-03-25
mfe: +2.5R
mae: -0.5R
mistakes: []
---

# NVDA Gap and Go Setup

## Performance Metrics
- **R-Multiple**: +2.5R
- **MFE**: +3.0R (price went higher)
- **MAE**: -0.5R (never stopped out)

## Key Observations
- Entry at $145.25 confirmed by RVOL > 2.0
- Exit at $152.00 aligned with pre-market resistance
- No psychological mistakes detected

## Related Plays
- [[AAPL Gap and Go]] - Similar setup on 2026-03-20
- [[AMD Extension Fade]] - Counter-example (failed setup)
```

### Bridge Components
1. **Daily Sync Job**: Runs post-market, generates daily setup summaries
2. **Theme Indexer**: Maintains [[Themes]] wiki with performance metrics
3. **Mistake Analyzer**: Aggregates psychological patterns weekly

## 6. Technical Constraints
- **Database**: PostgreSQL 15+ with pgvector extension
- **Vector Dimension**: 768-dimension embeddings (compatible with LLM models)
- **JSONB Indexing**: GIN indexes on all JSONB fields for query performance
- **Retention Policy**: Raw snapshots retained 30 days; aggregated metrics permanent

## 7. Integration Points
- [[PRD-001 Cobalt-Ion Tactical HUD]] - Real-time score calculations
- [[PRD-012 The Recon Scout]] - In-play ticker ingestion
- [[ADR-015 5-Pillar Relational Schema]] - Technical implementation details
- [[Sprint_06_Data_Engine]] - Implementation backlog

## 8. Success Metrics
- **Query Latency**: < 50ms for instrument lookups
- **News Deduplication**: > 80% reduction in duplicate news via semantic clustering
- **Playbook Coverage**: 100% of trades auto-generate Obsidian entries within 5 minutes
- **Mistake Detection**: > 90% accuracy in psychological error classification