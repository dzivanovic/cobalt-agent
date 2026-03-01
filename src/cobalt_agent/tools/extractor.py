"""
Universal Extractor Module - Graph Data Parser

This module provides LLM-powered extraction of graph entities (nodes and edges)
from raw text content (either Markdown from Fast-Path or AOM from Fallback).

Features:
- LLM-powered entity extraction
- Strict Pydantic schemas matching database structure
- Delta engine for computing new edges against existing graph state
- Integration with PostgresMemory for graph operations

Pydantic Schemas:
- GraphNode: entity_type (str), name (str), properties (dict)
- GraphEdge: source_name (str), target_name (str), relationship (str), properties (dict)
"""
import os
import json
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field, ValidationError
from loguru import logger
from litellm import completion

from ..config import get_config
from ..memory.postgres import PostgresMemory


class GraphNode(BaseModel):
    """
    Pydantic model representing a graph node.
    
    Attributes:
        entity_type: The type of entity (e.g., 'Ticker', 'Material', 'Strategy')
        name: The unique name of the entity (e.g., 'TSLA', 'Cellulose')
        properties: Additional JSON properties of the entity
    """
    entity_type: str = Field(..., description="The type of entity")
    name: str = Field(..., description="The unique name of the entity")
    properties: Dict[str, Any] = Field(default_factory=dict, description="Additional properties")


class GraphEdge(BaseModel):
    """
    Pydantic model representing a graph edge.
    
    Attributes:
        source_name: The name of the source node
        target_name: The name of the target node
        relationship: The type of relationship between nodes
        properties: Additional JSON properties of the edge
    """
    source_name: str = Field(..., description="The name of the source node")
    target_name: str = Field(..., description="The name of the target node")
    relationship: str = Field(..., description="The type of relationship")
    properties: Dict[str, Any] = Field(default_factory=dict, description="Additional properties")


class DeltaResult(BaseModel):
    """
    Pydantic model for delta computation results.
    
    Attributes:
        new_nodes: List of nodes that don't exist in DB
        new_edges: List of edges that don't exist in DB
        existing_count: Number of edges already in DB
    """
    new_nodes: List[Dict[str, Any]] = Field(default_factory=list, description="New nodes")
    new_edges: List[Dict[str, Any]] = Field(default_factory=list, description="New edges")
    existing_count: int = Field(default=0, description="Count of existing edges")


class GraphExtractionOutput(BaseModel):
    """
    Pydantic model for LLM extraction output.
    
    Attributes:
        nodes: List of extracted graph nodes
        edges: List of extracted graph edges
    """
    nodes: List[GraphNode] = Field(default_factory=list, description="Extracted graph nodes")
    edges: List[GraphEdge] = Field(default_factory=list, description="Extracted graph edges")


class UniversalExtractor:
    """
    LLM-powered graph entity extractor.
    
    Extracts nodes and edges from raw text content using an LLM,
    and validates/transforms them into structured Pydantic models.
    """
    
    def __init__(self):
        """Initialize the UniversalExtractor with config and LLM client."""
        self.config = get_config()
        self.llm_model = self.config.llm.model_name
        self._postgres_memory: Optional[PostgresMemory] = None
        
        # Try to initialize PostgresMemory if available
        try:
            self._postgres_memory = PostgresMemory()
            logger.info("✅ PostgresMemory initialized for delta computation")
        except Exception as e:
            logger.warning(f"⚠️ PostgresMemory initialization skipped: {e}")
            self._postgres_memory = None
    
    def _build_extraction_prompt(self, raw_text: str) -> str:
        """
        Build the LLM extraction prompt.
        
        Args:
            raw_text: The raw text content to extract from
            
        Returns:
            Formatted prompt string
        """
        system_prompt = """
You are a graph extraction agent. Your task is to parse the input text and extract 
graph entities (nodes) and relationships (edges).

OUTPUT FORMAT:
Return a JSON object with two arrays: "nodes" and "edges".

NODE SCHEMA:
Each node must have:
- entity_type: A high-level category like 'Ticker', 'Material', 'Strategy', 'Company', 'Person', 'Event', 'Metric'
- name: A unique identifier for the entity (e.g., 'TSLA', 'Morning Gapper Strategy')
- properties: An object with additional attributes (e.g., {'price': 175.50, 'sector': 'Auto'})

EDGE SCHEMA:
Each edge must have:
- source_name: The name of the source node
- target_name: The name of the target node  
- relationship: A descriptive relationship type (e.g., 'TRIGGERED_STRATEGY', 'IS_USED_IN', 'HAS_METRIC')
- properties: An object with edge attributes (e.g., {'confidence': 0.95})

EXTRACTION RULES:
1. Extract ALL entities mentioned in the text
2. For stocks/tickers, use entity_type='Ticker'
3. For strategies, use entity_type='Strategy'
4. For materials/products, use entity_type='Material'
5. For companies, use entity_type='Company'
6. Relationships should capture causal or associative links
7. If no entities found, return empty arrays

EXAMPLE OUTPUT:
{
  "nodes": [
    {"entity_type": "Ticker", "name": "TSLA", "properties": {"price": 175.50, "sector": "Auto"}},
    {"entity_type": "Strategy", "name": "Morning Gapper", "properties": {"score_threshold": 80}}
  ],
  "edges": [
    {"source_name": "TSLA", "target_name": "Morning Gapper", "relationship": "TRIGGERED_STRATEGY", "properties": {"confidence": 0.95}}
  ]
}
"""
        
        user_prompt = f"""
Please extract graph entities from the following content:

=== START CONTENT ===
{raw_text[:15000]}  # Limit context size
=== END CONTENT ===

Return ONLY the JSON object, no other text.
"""
        
        return f"{system_prompt}\n\n{user_prompt}"
    
    def extract(self, raw_text: str) -> GraphExtractionOutput:
        """
        Extract graph entities from raw text using LLM.
        
        Args:
            raw_text: The raw text content to extract from
            
        Returns:
            GraphExtractionOutput with nodes and edges
        """
        prompt = self._build_extraction_prompt(raw_text)
        
        try:
            response = completion(
                model=self.llm_model,
                messages=[
                    {"role": "system", "content": "You are a graph extraction agent. Return only valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            
            # Extract content from response
            content = response.choices[0].message.content
            
            # Parse JSON
            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                # Try to extract JSON from response if wrapped in markdown or text
                import re
                json_match = re.search(r'\{[\s\S]*\}', content)
                if json_match:
                    data = json.loads(json_match.group())
                else:
                    raise ValueError(f"Could not parse JSON from response: {content}")
            
            # Validate against Pydantic model
            return GraphExtractionOutput(**data)
            
        except ValidationError as e:
            logger.error(f"Validation error in extraction: {e}")
            # Return empty result on validation error
            return GraphExtractionOutput(nodes=[], edges=[])
        except Exception as e:
            logger.error(f"Extraction failed: {e}")
            return GraphExtractionOutput(nodes=[], edges=[])


def compute_delta(
    extracted_nodes: List[GraphNode],
    extracted_edges: List[GraphEdge],
    postgres_memory: Optional[PostgresMemory] = None
) -> Dict[str, List[Dict[str, Any]]]:
    """
    Compute the delta between extracted graph entities and existing database state.
    
    This function checks if the extracted edges already exist in the PostgresMemory
    database and returns only the new/updated edges as a delta payload.
    
    Args:
        extracted_nodes: List of extracted graph nodes
        extracted_edges: List of extracted graph edges
        postgres_memory: Optional PostgresMemory instance for database queries
        
    Returns:
        Dictionary with:
        - 'new_nodes': List of nodes that don't exist in DB
        - 'new_edges': List of edges that don't exist in DB
        - 'existing_count': Number of edges already in DB
    """
    delta_payload = {
        "new_nodes": [],
        "new_edges": [],
        "existing_count": 0
    }
    
    # Return empty delta if no postgres memory available
    if not postgres_memory:
        logger.warning("PostgresMemory not available, returning all edges as new")
        delta_payload["new_nodes"] = [n.model_dump() for n in extracted_nodes]
        delta_payload["new_edges"] = [e.model_dump() for e in extracted_edges]
        return delta_payload
    
    try:
        # Upsert all nodes first (get their IDs)
        node_ids = {}  # name -> id mapping
        for node in extracted_nodes:
            node_id = postgres_memory.upsert_node(
                entity_type=node.entity_type,
                name=node.name,
                properties=node.properties
            )
            node_ids[node.name] = node_id
        
        # Check each edge for existence and add new ones to delta
        for edge in extracted_edges:
            # Get source and target IDs
            source_id = node_ids.get(edge.source_name)
            target_id = node_ids.get(edge.target_name)
            
            if not source_id or not target_id:
                logger.warning(f"Could not find node IDs for edge: {edge.source_name} -> {edge.target_name}")
                continue
            
            # Check if edge already exists
            existing_edges = postgres_memory.get_edges(source_id, direction='out')
            
            edge_exists = False
            for existing_edge in existing_edges:
                if (existing_edge.get('target_id') == target_id and 
                    existing_edge.get('relationship') == edge.relationship):
                    edge_exists = True
                    delta_payload["existing_count"] += 1
                    break
            
            # If new edge, add to delta payload
            if not edge_exists:
                # Create edge in database
                postgres_memory.upsert_edge(
                    source_id=source_id,
                    target_id=target_id,
                    relationship=edge.relationship,
                    properties=edge.properties
                )
                delta_payload["new_edges"].append(edge.model_dump())
        
        # Add all nodes to new_nodes (upserted but tracked for completeness)
        delta_payload["new_nodes"] = [n.model_dump() for n in extracted_nodes]
        
        logger.info(f"Delta computed: {len(delta_payload['new_edges'])} new edges, {delta_payload['existing_count']} existing")
        
    except Exception as e:
        logger.error(f"Failed to compute delta: {e}")
        # Fallback: return all edges as new
        delta_payload["new_edges"] = [e.model_dump() for e in extracted_edges]
        delta_payload["new_nodes"] = [n.model_dump() for n in extracted_nodes]
    
    return delta_payload


def extract_with_delta(raw_text: str, postgres_memory: Optional[PostgresMemory] = None) -> Dict[str, Any]:
    """
    Convenience function that performs extraction and computes delta in one call.
    
    Args:
        raw_text: The raw text content to extract from
        postgres_memory: Optional PostgresMemory instance
        
    Returns:
        Dictionary with:
        - 'nodes': All extracted nodes
        - 'edges': All extracted edges  
        - 'delta': The delta payload with new edges only
    """
    extractor = UniversalExtractor()
    
    # Extract entities
    result = extractor.extract(raw_text)
    
    # Compute delta
    delta = compute_delta(result.nodes, result.edges, postgres_memory)
    
    return {
        "nodes": [n.model_dump() for n in result.nodes],
        "edges": [e.model_dump() for e in result.edges],
        "delta": delta
    }