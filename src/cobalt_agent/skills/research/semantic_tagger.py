"""
Semantic Tagging Drip Engine - Step 3 (Recursive Architecture Update)

This module implements a batch-processing semantic tagging system that:
1. Queries the 'themes' table for ACTIVE names to establish a controlled vocabulary
2. Pulls untagged instruments from the 'instruments' table (limit: 20)
3. Sends an ultra-lean JSON prompt to the local LLM
4. Formats and updates results back into the 'instruments.active_themes' JSONB column

Usage:
    python -m src.cobalt_agent.skills.research.semantic_tagger
"""

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import psycopg2
from loguru import logger
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel, Field

# Resolve project root and add to path for imports
sys_path_root = Path(__file__).resolve().parents[4]
import sys
sys.path.insert(0, str(sys_path_root))

from cobalt_agent.config import get_config
from cobalt_agent.llm import LLM

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ============================================================================
# Pydantic Models for Strict Schema Validation
# ============================================================================

class ThemeAssignment(BaseModel):
    """Schema for a single theme assignment from LLM response."""
    ticker: str = Field(..., description="Stock ticker symbol")
    themes: list[str] = Field(default_factory=list, description="List of matching theme names")


class ThemeAssignmentResponse(BaseModel):
    """Schema for the complete LLM response."""
    assignments: list[ThemeAssignment] = Field(
        default_factory=list,
        description="List of ticker-to-theme mappings"
    )


class InstrumentThemeState(BaseModel):
    """Schema for stateful theme objects stored in instruments.active_themes."""
    theme: str = Field(..., description="Theme name from controlled vocabulary")
    status: str = Field(default="HOT", description="Theme status: HOT, WARM, COLD")
    added_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        description="ISO date when theme was added"
    )


# ============================================================================
# Database Connection Helper (CLEANED - NO HARDCODING)
# ============================================================================

def get_db_connection():
    """Create a Postgres connection using the central config engine."""
    from cobalt_agent.config import get_config
    
    config = get_config()
    return psycopg2.connect(
        host=config.postgres.host,
        port=config.postgres.port,
        database=config.postgres.db,
        user=config.postgres.user,
        password=config.postgres.password,
    )


# ============================================================================
# SemanticTagger Class - Batch Processing Drip Engine
# ============================================================================

class SemanticTagger:
    def __init__(self, batch_size: int = 20):
        self.batch_size = batch_size
        self.conn = None
        self.config = get_config()

    def _get_db_connection(self):
        if self.conn is None:
            self.conn = get_db_connection()
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def _get_active_themes(self) -> list[str]:
        """Query the recursive themes table for active names."""
        conn = self._get_db_connection()
        with conn.cursor() as cur:
            cur.execute("""
                SELECT name
                FROM themes
                WHERE status ILIKE 'active'
                ORDER BY name ASC
            """)
            rows = cur.fetchall()
            return [row[0] for row in rows]

    def _get_untagged_batch(self, limit: int = 20) -> list[dict[str, Any]]:
        conn = self._get_db_connection()
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT
                    id,
                    symbol as ticker,
                    name as company_name,
                    metadata->>'sector' as sector,
                    metadata->>'industry' as industry
                FROM instruments
                WHERE active_themes IS NULL
                   OR active_themes = '[]'::jsonb
                   OR jsonb_array_length(active_themes) = 0
                ORDER BY created_at ASC
                LIMIT %s
            """, (limit,))
            return [dict(row) for row in cur.fetchall()]

    def _build_prompt(self, active_themes: list[str], instruments: list[dict]) -> str:
        instrument_data = [
            {
                "ticker": inst["ticker"],
                "company": inst["company_name"] or "",
                "sector": inst.get("sector") or "",
                "industry": inst.get("industry") or ""
            }
            for inst in instruments
        ]

        template = self.config.prompts.research.get("semantic_tagger") if self.config.prompts.research else None
        if not template:
            template = self._get_fallback_prompt_template()

        return template.format(
            themes=json.dumps(active_themes, indent=2),
            instruments=json.dumps(instrument_data, separators=(",", ":"))
        )

    def _get_fallback_prompt_template(self) -> str:
        return """You are a semantic tagging assistant. Assign market themes to stocks from the ALLOWED_LIST below.

ALLOWED THEMES (use ONLY these exact names):
{themes}

INSTRUMENTS TO TAG:
{instruments}

Return a JSON array with this exact schema:
{{"assignments": [{{"ticker": "NVDA", "themes": ["Nuclear Energy"]}}]}}

Rules:
1. Use ONLY themes from the ALLOWED THEMES list (exact match)
2. If no themes apply, return empty themes array: {{"themes": []}}
3. Return valid JSON only - no markdown, no explanations

Response:"""

    def _format_theme_state(self, theme_names: list[str]) -> list[dict]:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return [{"theme": name, "status": "HOT", "added_at": now} for name in theme_names]

    def _update_instruments(self, assignments: list[dict]) -> int:
        """Update the database with the LLM-assigned themes."""
        import json
        from datetime import datetime
        
        conn = self._get_db_connection()
        cur = conn.cursor()
        updated_count = 0
        now = datetime.now().isoformat()
        
        try:
            for item in assignments:
                ticker = item.get("ticker")
                if not ticker: 
                    continue
                
                themes = item.get("themes", [])
                
                # THE FIX: Strictly enforce the fallback JSON structure
                if not themes:
                    theme_state = [{"theme": "Not Tagged Yet", "status": "NONE", "added_at": now}]
                else:
                    theme_state = [{"theme": t, "status": "ACTIVE", "added_at": now} for t in themes]
                    
                cur.execute("""
                    UPDATE instruments 
                    SET active_themes = %s::jsonb, updated_at = CURRENT_TIMESTAMP 
                    WHERE symbol = %s
                """, (json.dumps(theme_state), ticker))
                
                updated_count += cur.rowcount
                
            conn.commit()
            
        except Exception as e:
            logger.error(f"Failed to update database: {e}")
            conn.rollback()
        finally:
            cur.close()
            conn.close()
            
        return updated_count

    def run_batch(self) -> dict[str, Any]:
        """Process a single batch of untagged instruments."""
        instruments = self._get_untagged_batch()
        
        # Action 3: Fast-fail if queue is empty. Never wakes the LLM.
        if not instruments:
            logger.info("✅ Database queue is clean. No untagged instruments found. Sleeping.")
            return {
                "status": "complete",
                "instruments_processed": 0,
                "instruments_updated": 0,
                "duration_seconds": 0.0
            }
            
        logger.info(f"Processing batch of {len(instruments)} instruments...")
        
        prompt = self._build_prompt(self._get_active_themes(), instruments)
        start_time = datetime.now()
        
        try:
            # Temperature locked at 0.0 for deterministic JSON
            self.llm = LLM(role='strategist')
            response = self.llm.ask(system_message=prompt, temperature=0.0, max_tokens=24000)
            clean_text = self._extract_json(response)
            
            parsed_dict = json.loads(clean_text)
            assignments = parsed_dict.get("assignments", [])
            
            # Action 2: The Ghost Ticker Reconciliation
            # If the LLM completely omitted a ticker, force it into the assignments
            # list so the _update_instruments fallback catches it.
            returned_tickers = {a.get("ticker") for a in assignments}
            for inst in instruments:
                ticker = inst["ticker"]
                if ticker not in returned_tickers:
                    logger.warning(f"LLM omitted {ticker}. Forcing fallback state.")
                    assignments.append({"ticker": ticker, "themes": []})
            
            updated_count = self._update_instruments(assignments)
            
            duration = (datetime.now() - start_time).total_seconds()
            logger.info(f"Processed batch of {len(instruments)}. Updated {updated_count} instruments in {duration:.1f} seconds.")
            
            return {
                "status": "complete",
                "instruments_processed": len(instruments),
                "instruments_updated": updated_count,
                "duration_seconds": duration
            }
            
        except Exception as e:
            logger.error(f"Batch failed: {e}")
            return {"status": "failed", "error": str(e)}
        finally:
            self.close()

    def _extract_json(self, response: str) -> str:
        """Extract JSON from LLM response by stripping markdown and reasoning tags."""
        # Strip reasoning tags
        if "</think>" in response:
            final_output = response.split("</think>")[-1]
        else:
            final_output = response

        # Clean markdown to isolate JSON
        clean_text = final_output.replace("```json", "").replace("```", "").strip()
        start_idx = clean_text.find('{')
        end_idx = clean_text.rfind('}')
        if start_idx != -1 and end_idx != -1:
            clean_text = clean_text[start_idx:end_idx+1]

        return clean_text

def process_entire_queue(batch_size: int = 50) -> dict[str, Any]:
    logger.info(f"Initiating full semantic tagging pipeline. Batch size: {batch_size}")
    total_tagged = 0
    batches_processed = 0
    
    while True:
        tagger = SemanticTagger(batch_size=batch_size)
        result = tagger.run_batch()
        
        if result.get("status") == "failed":
            logger.error("Batch failed. Pausing 15 seconds before retry.")
            time.sleep(15)
            continue
            
        processed = result.get("instruments_processed", 0)
        updated = result.get("instruments_updated", 0)
        total_tagged += updated
        batches_processed += 1
        
        if processed == 0: 
            logger.info(f"Queue is empty. Total instruments tagged this session: {total_tagged}")
            break
            
        logger.info(f"Batch {batches_processed} complete. Cooling down KV cache for 3 seconds...")
        time.sleep(3)
        
    return {"status": "complete", "total_batches": batches_processed, "total_tagged": total_tagged}

if __name__ == "__main__":
    result = process_entire_queue(batch_size=50)
    print(json.dumps(result, indent=2))
