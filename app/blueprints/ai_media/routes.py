from flask import Blueprint, request, jsonify
from .service import upscale_image, enhance_image

ai_media_bp = Blueprint("ai_media", __name__, url_prefix="/api/ai-media")

@ai_media_bp.route("/upscale", methods=["POST"])
def upscale():
    data = request.get_json()
    image_url = data.get("image_url")

    if not image_url:
        return jsonify({"error": "Missing image_url"}), 400

    try:
        result_url = upscale_image(image_url)
        return jsonify({"enhanced_url": result_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@ai_media_bp.route("/enhance", methods=["POST"])
def enhance():
    data = request.get_json()
    image_url = data.get("image_url")

    if not image_url:
        return jsonify({"error": "Missing image_url"}), 400

    try:
        result_url = enhance_image(image_url)
        return jsonify({"enhanced_url": result_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
