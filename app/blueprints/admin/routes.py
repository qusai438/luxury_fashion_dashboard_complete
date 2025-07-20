from flask import Blueprint, jsonify

admin_bp = Blueprint("admin", __name__, url_prefix="/api/admin")

@admin_bp.route("/status", methods=["GET"])
def system_status():
    return jsonify({
        "status": "OK",
        "message": "System is running smoothly",
        "uptime": "99.99%",
        "version": "1.0.0"
    }), 200
