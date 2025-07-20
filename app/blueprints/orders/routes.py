from flask import Blueprint, jsonify, request
from .service import OrdersService

orders_bp = Blueprint('orders', __name__)
service = OrdersService()

@orders_bp.route('/orders', methods=['GET'])
def list_orders():
    try:
        orders = service.get_unfulfilled_orders()
        return jsonify({'orders': orders}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@orders_bp.route('/orders/fulfill', methods=['POST'])
def fulfill_order():
    data = request.get_json()
    order_id = data.get('order_id')
    if not order_id:
        return jsonify({'error': 'Missing order_id'}), 400
    try:
        result = service.fulfill_order(order_id)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
