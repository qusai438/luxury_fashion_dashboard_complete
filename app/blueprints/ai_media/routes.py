from flask import Blueprint, request, jsonify
from .service import AIMediaService

ai_media_bp = Blueprint('ai_media', __name__)
service = AIMediaService()

@ai_media_bp.route('/ai/media/generate-image', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    try:
        image_path = service.generate_image(prompt)
        return jsonify({'image_url': image_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ai_media_bp.route('/ai/media/generate-variation', methods=['POST'])
def generate_variation():
    if 'image' not in request.files:
        return jsonify({'error': 'Image file is required'}), 400
    image = request.files['image']
    try:
        image_path = service.generate_variation(image.stream)
        return jsonify({'image_url': image_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
