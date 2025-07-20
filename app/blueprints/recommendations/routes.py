from flask import Blueprint, jsonify, request
from .service import RecommendationService

recommendations_bp = Blueprint("recommendations", __name__, url_prefix="/api/recommendations")
service = RecommendationService()

@recommendations_bp.route("/product/<product_id>", methods=["GET"])
def get_recommendations(product_id):
    try:
        related = service.get_related_products(product_id)
        return jsonify({"related": related}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
