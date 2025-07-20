import datetime
from uuid import uuid4

# في هذا المشروع الافتراضي سنخزن التقييمات في ذاكرة مؤقتة (يمكن استبدالها بقاعدة بيانات لاحقًا)
REVIEWS_DB = {}

class ReviewService:
    def save_review(self, product_id: str, rating: int, comment: str) -> dict:
        review = {
            "id": str(uuid4()),
            "product_id": product_id,
            "rating": rating,
            "comment": comment,
            "timestamp": datetime.datetime.utcnow().isoformat()
        }

        REVIEWS_DB.setdefault(product_id, []).append(review)
        return review

    def get_reviews_for_product(self, product_id: str) -> list:
        return REVIEWS_DB.get(product_id, [])
