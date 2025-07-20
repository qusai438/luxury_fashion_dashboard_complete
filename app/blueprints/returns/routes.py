from flask import Blueprint, request, jsonify
from .service import ReturnsService

returns_bp = Blueprint('returns', __name__)
service = ReturnsService()

@returns_bp.route('/request', methods=['POST'])
def request_return():
    data = request.get_json() or {}
    order_id = data.get('order_id')
    reason = data.get('reason')
    if not order_id or not reason:
        return jsonify({'error': 'order_id and reason are required'}), 400
    try:
        result = service.handle_return(order_id, reason)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
