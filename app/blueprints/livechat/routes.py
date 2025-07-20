from flask import Blueprint, request, jsonify
from .service import LiveChatService

livechat_bp = Blueprint('livechat', __name__)
service = LiveChatService()

@livechat_bp.route('/start', methods=['POST'])
def start_chat():
    data = request.get_json() or {}
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400
    try:
        session = service.start_chat(user_id)
        return jsonify({'session': session}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@livechat_bp.route('/register-agent', methods=['POST'])
def register_agent():
    data = request.get_json() or {}
    agent_id = data.get('agent_id')
    if not agent_id:
        return jsonify({'error': 'agent_id is required'}), 400
    try:
        service.register_agent(agent_id)
        return jsonify({'message': 'Agent registered successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
