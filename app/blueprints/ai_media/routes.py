from flask import Blueprint, request, jsonify
from .utils import generate_instagram_caption_from_image, generate_ad_copy_from_image

ai_media_bp = Blueprint('ai_media', __name__)


@ai_media_bp.route('/generate/caption', methods=['POST'])
def generate_caption():
    data = request.get_json() or {}
    image_url = data.get("image_url")

    if not image_url:
        return jsonify({"error": "Image URL is required"}), 400

    try:
        caption = generate_instagram_caption_from_image(image_url)
        return jsonify({"caption": caption}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@ai_media_bp.route('/generate/ad-copy', methods=['POST'])
def generate_ad_copy():
    data = request.get_json() or {}
    image_url = data.get("image_url")

    if not image_url:
        return jsonify({"error": "Image URL is required"}), 400

    try:
        ad_copy = generate_ad_copy_from_image(image_url)
        return jsonify({"ad_copy": ad_copy}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
