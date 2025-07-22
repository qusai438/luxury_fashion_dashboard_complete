import json
import os

EVENTS_FILE = os.path.join(os.path.dirname(__file__), "user_events.json")

def load_events():
    if not os.path.exists(EVENTS_FILE):
        return []

    try:
        with open(EVENTS_FILE, "r") as file:
            events = json.load(file)
        return events
    except Exception:
        return []

def save_event(event: dict):
    events = load_events()
    events.append(event)

    with open(EVENTS_FILE, "w") as file:
        json.dump(events, file, indent=4)
