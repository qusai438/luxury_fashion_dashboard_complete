from flask import Blueprint, request, jsonify
from .service import ChatbotService

chatbot_bp = Blueprint("chatbot", __name__, url_prefix="/api/chatbot")
service = ChatbotService()

@chatbot_bp.route("/ask", methods=["POST"])
def ask_bot():
    data = request.get_json()
    message = data.get("message")

    if not message:
        return jsonify({"error": "Missing message"}), 400

    try:
        reply = service.get_reply(message)
        return jsonify({"reply": reply}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
