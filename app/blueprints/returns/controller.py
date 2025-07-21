from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.return_request import ReturnRequest

returns_bp = Blueprint('returns', __name__)

@returns_bp.route('/request', methods=['POST'])
def request_return():
    data = request.get_json() or {}
    order_id = data.get('order_id')
    email = data.get('email')
    reason = data.get('reason')

    if not order_id or not reason:
        return jsonify({'error': 'Missing order_id or reason'}), 400

    new_request = ReturnRequest(
        order_id=order_id,
        email=email,
        reason=reason
    )
    db.session.add(new_request)
    db.session.commit()

    return jsonify({'message': 'Return request submitted successfully'}), 201

@returns_bp.route('/all', methods=['GET'])
def list_returns():
    returns = ReturnRequest.query.order_by(ReturnRequest.created_at.desc()).all()
    return jsonify([r.to_dict() for r in returns]), 200

@returns_bp.route('/update/<int:return_id>', methods=['PUT'])
def update_return_status(return_id):
    data = request.get_json() or {}
    status = data.get('status')

    if status not in ['Pending', 'Approved', 'Rejected']:
        return jsonify({'error': 'Invalid status'}), 400

    r = ReturnRequest.query.get_or_404(return_id)
    r.status = status
    db.session.commit()
    
    return jsonify({'message': 'Return request updated successfully'}), 200
