from flask import Blueprint, jsonify
import random

recommendations_bp = Blueprint("recommendations", __name__, url_prefix="/api/recommendations")

@recommendations_bp.route("/products", methods=["GET"])
def get_recommendations():
    sample_products = [
        {"id": 101, "name": "Silk Blouse", "price": 149.99},
        {"id": 102, "name": "Luxury Handbag", "price": 899.99},
        {"id": 103, "name": "Elegant Heels", "price": 299.50},
        {"id": 104, "name": "Designer Sunglasses", "price": 199.00},
        {"id": 105, "name": "Classic Trench Coat", "price": 549.00}
    ]
    recommendations = random.sample(sample_products, k=3)
    return jsonify({"recommendations": recommendations}), 200
