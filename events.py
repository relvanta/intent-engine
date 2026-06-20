from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from typing import Dict, Any, Optional
import uuid

class RuntimeEventType(str, Enum):
    INPUT_RECEIVED = "input_received"
    FACTS_EXTRACTED = "facts_extracted"
    INTENT_PARSED = "intent_parsed"
    STATE_TRANSITION = "state_transition"
    ACTION_DISPATCHED = "action_dispatched"
    ACTION_COMPLETED = "action_completed"
    ACTION_FAILED = "action_failed"
    ANOMALY_DETECTED = "anomaly_detected"

class RuntimeEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    session_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    event_type: RuntimeEventType
    payload: Dict[str, Any]
    
    telemetry_metadata: Optional[Dict[str, Any]] = Field(
        default=None, 
        description="Internal LLM reasoning, token counts, and latency. Never used for routing."
    )
