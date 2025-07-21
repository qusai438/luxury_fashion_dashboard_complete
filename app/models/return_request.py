from datetime import datetime
from app.extensions import db

class ReturnRequest(db.Model):
    __tablename__ = "return_requests"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    reason = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default="Pending")  # e.g., Pending, Approved, Rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "email": self.email,
            "reason": self.reason,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }
