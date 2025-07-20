from flask import Blueprint, jsonify, request
from ..service import ProductService

products_bp = Blueprint('products', __name__)
service = ProductService()

@products_bp.route('/', methods=["GET"])
def list_products():
    try:
        products = service.get_all_products()
        return jsonify({"products": products}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@products_bp.route('/add', methods=["POST"])
def add_product():
    data = request.get_json()
    if not data.get("name"):
        return jsonify({"error": "Missing name"}), 400

    try:
        product = service.add_product(data)
        return jsonify({"product": product}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
