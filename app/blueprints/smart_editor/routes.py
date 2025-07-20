from flask import Blueprint, request, jsonify
from .service import SmartEditorService

smart_editor_bp = Blueprint("smart_editor", __name__, url_prefix="/api/smart-editor")
service = SmartEditorService()

@smart_editor_bp.route("/generate-section", methods=["POST"])
def generate_section():
    data = request.get_json() or {}
    instruction = data.get("instruction")

    if not instruction:
        return jsonify({"error": "Missing instruction"}), 400

    try:
        html_code = service.generate_html_section(instruction)
        return jsonify({"html": html_code}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
