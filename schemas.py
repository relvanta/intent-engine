from enum import Enum
from pydantic import BaseModel, Field
from typing import Dict, Any

class IntentCategory(str, Enum):
    SCHEDULE = "schedule"
    MODIFY = "modify"
    CANCEL = "cancel"
    INQUIRE = "inquire"
    INFORM = "inform"
    UNKNOWN = "unknown"

class ParsedIntent(BaseModel):
    category: IntentCategory
    intent_name: str = Field(..., description="The specific, standardized intent name (e.g., 'book_appointment').")
    entities: Dict[str, Any] = Field(default_factory=dict, description="Validated facts mapped to this intent.")
    confidence: float = Field(..., ge=0.0, le=1.0)
    requires_clarification: bool = Field(..., description="True if the intent is vague or conflicting.")

class ParserMetadata(BaseModel):
    """Internal reasoning logs; never used for routing logic."""
    extractor_reasoning: str
    interpreter_reasoning: str

