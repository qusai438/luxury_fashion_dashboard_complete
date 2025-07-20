from flask import Blueprint, request, jsonify
from .service import InventoryService

inventory_bp = Blueprint('inventory', __name__)
service = InventoryService()

@inventory_bp.route('/upload', methods=['POST'])
def upload_inventory():
    if 'file' not in request.files:
        return jsonify({'error': 'file missing'}), 400
    file = request.files['file']
    try:
        result = service.update_inventory(file.stream)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
