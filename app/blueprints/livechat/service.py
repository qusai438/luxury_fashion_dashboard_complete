import uuid
from flask import current_app

class LiveChatService:
    def __init__(self):
        self.sessions = {}
        self.agents = {}

    def start_chat(self, user_id):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {
            'user_id': user_id,
            'messages': [],
            'status': 'waiting'
        }
        current_app.logger.info(f"Chat session started: {session_id} for user {user_id}")
        return session_id

    def register_agent(self, agent_id):
        self.agents[agent_id] = {'active': True}
        current_app.logger.info(f"Agent {agent_id} registered for live chat.")
