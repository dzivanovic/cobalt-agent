"""
Cobalt Agent - JSON Serializers
Enterprise-grade JSON serialization utilities for RFC-compliant output.
"""

import json
import uuid
from datetime import datetime, date
from pydantic import BaseModel


class CobaltJSONEncoder(json.JSONEncoder):
    """
    Custom JSON encoder that handles Pydantic models, datetimes, UUIDs, and
    fallback string conversion for Playwright DOM handles and other unserializable objects.
    
    This encoder ensures RFC-compliant JSON output, preventing LLM parsing hallucinations
    by explicitly handling all edge cases that may arise during tool execution.
    """
    
    def default(self, obj):
        """
        Override the default JSON encoder to handle additional types.
        
        Args:
            obj: The object to serialize
            
        Returns:
            A JSON-serializable representation of the object
            
        Raises:
            TypeError: If the object cannot be serialized
        """
        # Handle datetime.datetime and datetime.date objects
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        
        # Handle UUID objects
        if isinstance(obj, uuid.UUID):
            return str(obj)
        
        # Handle Pydantic models (v2+)
        if isinstance(obj, BaseModel):
            return obj.model_dump()
        
        # Fallback: convert to string (handles Playwright DOM handles, etc.)
        return str(obj)


def serialize_to_json(obj) -> str:
    """
    Serialize an object to a JSON string using the CobaltJSONEncoder.
    
    Args:
        obj: The object to serialize
        
    Returns:
        A JSON-formatted string
        
    Raises:
        TypeError: If the object cannot be serialized
    """
    return json.dumps(obj, cls=CobaltJSONEncoder)