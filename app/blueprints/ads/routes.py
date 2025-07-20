from flask import Blueprint, request, jsonify
from .service import AdGeneratorService

ads_bp = Blueprint("ads", __name__, url_prefix="/api/ads")
service = AdGeneratorService()

@ads_bp.route("/generate", methods=["POST"])
def generate_ad():
    data = request.get_json() or {}
    product = data.get("product")

    if not product or not isinstance(product, dict):
        return jsonify({"error": "Missing or invalid product data"}), 400

    try:
        ad = service.generate_ad(product)
        return jsonify({"ad_copy": ad}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
