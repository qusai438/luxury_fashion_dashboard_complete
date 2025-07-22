import logging
from datetime import datetime
from app.engine.user_behavior_tracker import track_event
from app.engine.ai_recommender import analyze_event, generate_recommendations

logger = logging.getLogger(__name__)

class LearningEngine:
    def __init__(self):
        self.events = []
        self.recommendations = []

    def record_event(self, event_type: str, payload: dict):
        timestamp = datetime.utcnow()
        event = {'type': event_type, 'payload': payload, 'timestamp': timestamp}
        self.events.append(event)
        track_event(event_type, payload, timestamp)
        try:
            recs = analyze_event(event)
            self.recommendations.extend(recs)
            logger.info(f"Generated {len(recs)} recommendations based on {event_type}")
        except Exception as e:
            logger.error(f"LearningEngine error on analyze_event: {e}")

    def get_recommendations(self):
        # Return and clear recommendations (one-time fetch)
        recs, self.recommendations = self.recommendations[:], []
        return recs
