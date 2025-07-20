from flask import Blueprint, request, jsonify
from .service import AIContentService

ai_content_bp = Blueprint('ai_content', __name__)
service = AIContentService()

@ai_content_bp.route('/generate-description', methods=['POST'])
def generate_description():
    data = request.get_json() or {}
    title = data.get('title')
    if not title:
        return jsonify({'error': 'title is required'}), 400
    try:
        description = service.generate_product_description(title)
        return jsonify({'description': description}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ai_content_bp.route('/generate-caption', methods=['POST'])
def generate_caption():
    data = request.get_json() or {}
    title = data.get('title')
    if not title:
        return jsonify({'error': 'title is required'}), 400
    try:
        caption = service.generate_instagram_caption(title)
        return jsonify({'caption': caption}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ai_content_bp.route('/generate-ad-copy', methods=['POST'])
def generate_ad_copy():
    data = request.get_json() or {}
    title = data.get('title')
    description = data.get('description')
    if not (title and description):
        return jsonify({'error': 'title and description are required'}), 400
    try:
        ad_copy = service.generate_ad_copy(title, description)
        return jsonify({'ad_copy': ad_copy}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
