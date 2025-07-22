from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..auth.utils import admin_required
from .service import AdsGeneratorService

ads_bp = Blueprint('ads', __name__)
generator = AdsGeneratorService()

@ads_bp.route('/generate-smart-ad', methods=['POST'])
@jwt_required()
@admin_required
def generate_smart_ad():
    data = request.get_json() or {}
    product_id = data.get("product_id")
    
    if not product_id:
        return jsonify({"error": "Missing product_id"}), 400

    try:
        result = generator.generate_from_product(product_id)
        return jsonify({"ad": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
