from flask import Blueprint, request, jsonify
from .service import DropshipService

dropship_bp = Blueprint("dropship", __name__, url_prefix="/api/dropship")
service = DropshipService()

@dropship_bp.route("/import", methods=["POST"])
def import_products():
    data = request.get_json() or {}
    category = data.get("category")

    if not category:
        return jsonify({"error": "Missing category"}), 400

    try:
        imported = service.import_products_by_category(category)
        return jsonify({"imported": imported}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
