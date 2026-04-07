-- ============================================================================
-- Cobalt Agent: 5-Pillar Relational Schema (14 Tables)
-- ============================================================================

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS vector;

-- ============================================================================
-- PILLAR 1: ENTITIES (Foundation)
-- ============================================================================

-- instruments: Master registry of all tradeable assets
CREATE TABLE IF NOT EXISTS instruments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    symbol VARCHAR(20) UNIQUE NOT NULL,
    asset_class VARCHAR(20) DEFAULT 'EQUITY',  -- EQUITY, OPTION, ETF, CRYPTO
    name VARCHAR(255),
    metadata JSONB DEFAULT '{}'::jsonb,  -- Dynamic attributes (sector, exchange, etc.)
    active_themes JSONB DEFAULT '[]'::jsonb,  -- Array of active theme tags
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- themes: Taxonomy of market themes/motifs (hierarchical & AI Ready)
CREATE TABLE IF NOT EXISTS themes (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) NOT NULL,
    parent_id UUID REFERENCES themes(id) ON DELETE CASCADE,  -- Hierarchical structure
    status VARCHAR(50) DEFAULT 'active',
    example_tickers TEXT,
    ai_metadata JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT themes_name_parent_unique UNIQUE (name, parent_id)
);

-- key_levels: Support/resistance zones per instrument
CREATE TABLE IF NOT EXISTS key_levels (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    instrument_id UUID NOT NULL REFERENCES instruments(id) ON DELETE CASCADE,
    level_type VARCHAR(20) NOT NULL, -- Removed strict constraint for day-trading flexibility (VWAP, PM_HIGH, etc.)
    price DECIMAL(12, 4) NOT NULL,
    source VARCHAR(100),  
    confidence DECIMAL(3, 2) CHECK (confidence >= 0 AND confidence <= 1),
    notes TEXT,
    ai_metadata JSONB DEFAULT '{}'::jsonb, -- AI intelligence drop-zone
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- daily_in_play: Daily "in-play" ticker snapshot
CREATE TABLE IF NOT EXISTS daily_in_play (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    date DATE NOT NULL,
    instrument_id UUID NOT NULL REFERENCES instruments(id) ON DELETE CASCADE,
    rank INTEGER DEFAULT 1,
    catalyst TEXT,
    rvol_multiplier DECIMAL(5, 2),  
    notes TEXT,
    UNIQUE(date, instrument_id)
);

-- ============================================================================
-- PILLAR 2: PHYSICS (Market Data)
-- ============================================================================

-- market_snapshots: Real-time price/volume state
CREATE TABLE IF NOT EXISTS market_snapshots (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    instrument_id UUID NOT NULL REFERENCES instruments(id) ON DELETE CASCADE,
    timestamp TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    price DECIMAL(12, 4),
    volume BIGINT,
    vwap DECIMAL(12, 4),  
    spread DECIMAL(12, 4),  
    raw_data JSONB DEFAULT '{}'::jsonb,  
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- news_events: Aggregated news with embeddings for semantic deduplication
CREATE TABLE IF NOT EXISTS news_events (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_hash VARCHAR(64) UNIQUE,  
    title TEXT NOT NULL,
    summary TEXT,
    embedding VECTOR(1536),  
    taxonomy_hash VARCHAR(64),  
    sources JSONB DEFAULT '[]'::jsonb,  
    published_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- news_mentions: Link news events to instruments and timeframes
CREATE TABLE IF NOT EXISTS news_mentions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_id UUID NOT NULL REFERENCES news_events(id) ON DELETE CASCADE,
    instrument_id UUID REFERENCES instruments(id) ON DELETE SET NULL,
    mention_context TEXT,  
    sentiment_score DECIMAL(3, 2) CHECK (sentiment_score >= -1 AND sentiment_score <= 1),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- PILLAR 3: CATALYSTS (Alerting & Signals)
-- ============================================================================

-- system_alerts: MFE/MAE performance tracking and alerting
CREATE TABLE IF NOT EXISTS system_alerts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    alert_type VARCHAR(50) NOT NULL,  
    instrument_id UUID REFERENCES instruments(id) ON DELETE CASCADE,
    threshold DECIMAL(12, 4),
    trigger_value DECIMAL(12, 4),
    mfe DECIMAL(12, 4),  
    mae DECIMAL(12, 4),  
    success_grade VARCHAR(5),  
    criteria_matrix JSONB DEFAULT '{}'::jsonb,  
    r_multiple DECIMAL(6, 2),  
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    triggered_at TIMESTAMPTZ
);

-- strategy_signals: Cobalt's autonomous pattern recognition output
CREATE TABLE IF NOT EXISTS strategy_signals (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    instrument_id UUID NOT NULL REFERENCES instruments(id) ON DELETE CASCADE,
    strategy_name VARCHAR(100) NOT NULL,
    signal_direction VARCHAR(10) CHECK (signal_direction IN ('LONG', 'SHORT', 'NEUTRAL')),
    confidence_score DECIMAL(3, 2) CHECK (confidence_score >= 0 AND confidence_score <= 1),
    ai_logic_payload JSONB DEFAULT '{}'::jsonb, -- Exact EV math and indicator variables
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- PILLAR 4: ENGINE (Orchestration)
-- ============================================================================

-- trading_accounts: Account/portfolio state tracking
CREATE TABLE IF NOT EXISTS trading_accounts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    account_id VARCHAR(50) UNIQUE NOT NULL,  
    balance DECIMAL(15, 2),
    equity DECIMAL(15, 2),
    day_trades_remaining INTEGER DEFAULT 3,  
    margin_used DECIMAL(15, 2),
    buying_power DECIMAL(15, 2),
    metadata JSONB DEFAULT '{}'::jsonb,  
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- PILLAR 5: EXECUTION (Trade Lifecycle & HITL)
-- ============================================================================

-- hitl_proposals: Human-in-the-Loop authorization gate
CREATE TABLE IF NOT EXISTS hitl_proposals (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    instrument_id UUID NOT NULL REFERENCES instruments(id) ON DELETE CASCADE,
    proposal_type VARCHAR(50) NOT NULL, -- e.g., 'TRADE_EXECUTION', 'PORTFOLIO_REBALANCE'
    status VARCHAR(20) DEFAULT 'PENDING' CHECK (status IN ('PENDING', 'APPROVED', 'REJECTED', 'EXPIRED')),
    execution_payload JSONB DEFAULT '{}'::jsonb, -- The exact trade parameters Cobalt wants to execute
    mattermost_post_id VARCHAR(100), -- Link back to the chat approval message
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMPTZ
);

-- trades: Trade lifecycle with psychological metrics
CREATE TABLE IF NOT EXISTS trades (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    instrument_id UUID NOT NULL REFERENCES instruments(id) ON DELETE CASCADE,
    account_id UUID REFERENCES trading_accounts(id) ON DELETE SET NULL,
    direction VARCHAR(10) NOT NULL CHECK (direction IN ('LONG', 'SHORT')),
    entry_price DECIMAL(12, 4) NOT NULL,
    exit_price DECIMAL(12, 4),
    quantity INTEGER NOT NULL,
    entry_timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    exit_timestamp TIMESTAMPTZ,
    realized_pnl DECIMAL(15, 2),
    r_multiple DECIMAL(6, 2),  
    emotional_state JSONB DEFAULT '{}'::jsonb,  
    mistake_tags JSONB DEFAULT '[]'::jsonb,  
    tilt_score DECIMAL(3, 2),  
    trader_note TEXT,
    trader_note_embedding VECTOR(1536),  
    status VARCHAR(20) DEFAULT 'OPEN' CHECK (status IN ('OPEN', 'CLOSED', 'CANCELLED')),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- order_fills: Granular fill history for partial fills
CREATE TABLE IF NOT EXISTS order_fills (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    trade_id UUID NOT NULL REFERENCES trades(id) ON DELETE CASCADE,
    fill_price DECIMAL(12, 4) NOT NULL,
    quantity INTEGER NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    commission DECIMAL(10, 2) DEFAULT 0,
    side VARCHAR(10) CHECK (side IN ('BUY', 'SELL')),
    notes TEXT
);

-- ============================================================================
-- INDEXES FOR PERFORMANCE
-- ============================================================================

-- Instrument & Theme indexes
CREATE INDEX idx_instruments_symbol ON instruments(symbol);
CREATE INDEX idx_instruments_asset_class ON instruments(asset_class);
CREATE INDEX idx_instruments_active_themes ON instruments USING GIN(active_themes);
CREATE INDEX idx_themes_parent_id ON themes(parent_id);

-- News indexes
CREATE INDEX idx_news_events_hash ON news_events(event_hash);
CREATE INDEX idx_news_mentions_event ON news_mentions(event_id);
CREATE INDEX idx_news_mentions_instrument ON news_mentions(instrument_id);

-- Execution indexes
CREATE INDEX idx_trades_instrument ON trades(instrument_id);
CREATE INDEX idx_trades_status ON trades(status);
CREATE INDEX idx_trades_mistake_tags ON trades USING GIN(mistake_tags);
CREATE INDEX idx_hitl_proposals_status ON hitl_proposals(status);
CREATE INDEX idx_strategy_signals_instrument ON strategy_signals(instrument_id);

-- ============================================================================
-- END OF SCHEMA
-- ============================================================================
