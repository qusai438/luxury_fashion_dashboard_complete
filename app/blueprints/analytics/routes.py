from flask import Blueprint, jsonify
from ..service import AnalyticsService

analytics_bp = Blueprint('analytics', __name__)
service = AnalyticsService()

@analytics_bp.route('/overview', methods=["GET"])
def get_overview():
    try:
        overview_data = service.get_overview_metrics()
        return jsonify({"overview": overview_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
