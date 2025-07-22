import datetime
import json
import os

LOG_FILE = "user_behavior.log"

def track_event(user_id: str, event_type: str, metadata: dict):
    """
    Logs a user event with metadata to a local log file.
    """
    event = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "user_id": user_id,
        "event_type": event_type,
        "metadata": metadata
    }

    log_path = os.path.join("logs", LOG_FILE)
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


def load_events():
    """
    Loads all tracked events from the log file.
    """
    log_path = os.path.join("logs", LOG_FILE)
    if not os.path.exists(log_path):
        return []

    with open(log_path, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f.readlines()]
