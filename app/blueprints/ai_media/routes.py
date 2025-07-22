from flask import Blueprint, request, jsonify
from .utils import save_base64_image, resize_image
from .service import AIImageContentGenerator
from .schema import ImageGenerationRequestSchema

ai_media_bp = Blueprint("ai_media", __name__)
generator = AIImageContentGenerator()
schema = ImageGenerationRequestSchema()

@ai_media_bp.route("/ai-media/generate", methods=["POST"])
def generate_ai_media():
    try:
        data = schema.load(request.get_json() or {})
        image_path = save_base64_image(data["image_data"])
        resized_path = resize_image(image_path)

        content = generator.generate_ad_content_from_image(
            image_path=resized_path,
            style=data.get("style", "luxury"),
            language=data.get("language", "en")
        )

        return jsonify({"ad_content": content}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
