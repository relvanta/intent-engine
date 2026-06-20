import json
import logging
from events import RuntimeEvent, RuntimeEventType

# Configured for structured output
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("intent_runtime")

class TelemetryLogger:
    def __init__(self, session_id: str):
        self.session_id = session_id

    def _emit(self, event_type: RuntimeEventType, payload: dict, metadata: dict = None):
        event = RuntimeEvent(
            session_id=self.session_id,
            event_type=event_type,
            payload=payload,
            telemetry_metadata=metadata
        )
        # We output as JSON string for easy ingest by observability platforms later
        logger.info(json.dumps(event.model_dump(mode='json')))

    def log_input(self, raw_text: str):
        self._emit(RuntimeEventType.INPUT_RECEIVED, {"raw_text": raw_text})

    def log_extraction(self, facts: dict, reasoning: dict):
        self._emit(RuntimeEventType.FACTS_EXTRACTED, {"facts": facts}, metadata=reasoning)

    def log_transition(self, from_state: str, to_state: str, intent: str):
        self._emit(RuntimeEventType.STATE_TRANSITION, {
            "from_state": from_state,
            "to_state": to_state,
            "trigger_intent": intent
        })

