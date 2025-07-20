from flask import Blueprint, jsonify
from datetime import datetime
import random

analytics_bp = Blueprint("analytics", __name__, url_prefix="/api/analytics")

@analytics_bp.route("/overview", methods=["GET"])
def analytics_overview():
    now = datetime.utcnow()
    data = {
        "visits": random.randint(1500, 4000),
        "orders": random.randint(90, 250),
        "revenue": round(random.uniform(18000, 50000), 2),
        "conversion_rate": round(random.uniform(1.5, 3.9), 2),
        "top_country": random.choice(["Germany", "Sweden", "France", "Italy"]),
        "report_generated": now.isoformat()
    }
    return jsonify(data), 200

@analytics_bp.route("/social", methods=["GET"])
def analytics_social():
    data = {
        "likes": random.randint(100, 600),
        "comments": random.randint(20, 100),
        "reach": random.randint(1000, 5000),
        "clicks": random.randint(100, 700),
        "impressions": random.randint(2000, 9000)
    }

    suggestions = [
        "Post more during peak hours on weekends.",
        "Boost top-performing posts to increase reach.",
        "Use carousel ads to showcase multiple items."
    ]

    return jsonify({
        "metrics": data,
        "suggestions": suggestions
    }), 200
