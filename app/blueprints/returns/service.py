import datetime
from uuid import uuid4

# قاعدة بيانات مؤقتة في الذاكرة (placeholder)
RETURNS_DB = []

class ReturnsService:
    def request_return(self, order_id: str, reason: str) -> dict:
        return_request = {
            "id": str(uuid4()),
            "order_id": order_id,
            "reason": reason,
            "status": "pending",
            "requested_at": datetime.datetime.utcnow().isoformat()
        }
        RETURNS_DB.append(return_request)
        return return_request

    def get_all_returns(self) -> list:
        return RETURNS_DB
