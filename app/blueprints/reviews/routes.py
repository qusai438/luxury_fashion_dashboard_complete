from flask import Blueprint, request, jsonify
from .service import ReviewService

reviews_bp = Blueprint("reviews", __name__, url_prefix="/api/reviews")
service = ReviewService()

@reviews_bp.route("/submit", methods=["POST"])
def submit_review():
    data = request.get_json() or {}
    product_id = data.get("product_id")
    rating = data.get("rating")
    comment = data.get("comment")

    if not product_id or rating is None or not comment:
        return jsonify({"error": "Missing product_id, rating, or comment"}), 400

    try:
        review = service.save_review(product_id, rating, comment)
        return jsonify({"review": review}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@reviews_bp.route("/product/<product_id>", methods=["GET"])
def get_reviews(product_id):
    try:
        reviews = service.get_reviews_for_product(product_id)
        return jsonify({"reviews": reviews}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
