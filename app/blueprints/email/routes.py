from flask import Blueprint, request, jsonify
from .service import EmailService

email_bp = Blueprint("email", __name__, url_prefix="/api/email")
service = EmailService()

@email_bp.route("/send", methods=["POST"])
def send_email():
    data = request.get_json() or {}
    to = data.get("to")
    subject = data.get("subject")
    body = data.get("body")

    if not to or not subject or not body:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        service.send_email(to, subject, body)
        return jsonify({"status": "sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
