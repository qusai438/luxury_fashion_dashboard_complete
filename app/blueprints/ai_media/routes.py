from flask import Blueprint, request, jsonify
from app.utils.openai_tools import generate_caption_from_image, generate_ad_copy_from_image

ai_media_bp = Blueprint("ai_media", __name__)

@ai_media_bp.route("/generate-caption-from-image", methods=["POST"])
def caption_from_image():
    data = request.get_json() or {}
    image_url = data.get("image_url")
    if not image_url:
        return jsonify({"error": "Missing image_url"}), 400
    try:
        caption = generate_caption_from_image(image_url)
        return jsonify({"caption": caption}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@ai_media_bp.route("/generate-ad-copy-from-image", methods=["POST"])
def ad_copy_from_image():
    data = request.get_json() or {}
    image_url = data.get("image_url")
    if not image_url:
        return jsonify({"error": "Missing image_url"}), 400
    try:
        ad_copy = generate_ad_copy_from_image(image_url)
        return jsonify({"ad_copy": ad_copy}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
