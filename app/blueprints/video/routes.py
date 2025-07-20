from flask import Blueprint, request, jsonify
from .service import generate_video_promo

video_bp = Blueprint('video', __name__, url_prefix="/api/video")

@video_bp.route('/generate', methods=["POST"])
def generate():
    data = request.get_json()
    if not data or "product_info" not in data:
        return jsonify({"error": "Missing product_info"}), 400

    try:
        video_url = generate_video_promo(data["product_info"])
        return jsonify({"video_url": video_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
