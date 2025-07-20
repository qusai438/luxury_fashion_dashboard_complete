from flask import Blueprint, jsonify, request
from ..service import CustomerService

customers_bp = Blueprint('customers', __name__)
service = CustomerService()

@customers_bp.route('/', methods=["GET"])
def list_customers():
    try:
        customers = service.get_all_customers()
        return jsonify({"customers": customers}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@customers_bp.route('/add', methods=["POST"])
def add_customer():
    data = request.get_json()
    if not data.get("name"):
        return jsonify({"error": "Missing name"}), 400

    try:
        customer = service.add_customer(data)
        return jsonify({"customer": customer}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
