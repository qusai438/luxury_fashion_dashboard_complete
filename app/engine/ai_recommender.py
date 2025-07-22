import random
from .user_behavior_tracker import load_events

class AIRecommender:
    def __init__(self):
        self.events = load_events()

    def recommend_bundle(self, product_id: str, user_id: str = None):
        """
        Recommends a bundle of products related to the given product.
        """
        related_products = self._get_related_products(product_id)
        return {
            "main_product": product_id,
            "bundle": related_products[:3]
        }

    def recommend_upsell(self, product_id: str):
        """
        Recommends a more expensive alternative to the given product.
        """
        return {
            "original": product_id,
            "upsell": f"{product_id}_premium"
        }

    def recommend_cross_sell(self, product_id: str):
        """
        Recommends complementary products.
        """
        return [f"{product_id}_accessory_{i}" for i in range(1, 4)]

    def _get_related_products(self, product_id: str):
        """
        Dummy logic based on user behavior.
        """
        clicked_products = [e["metadata"].get("product_id") for e in self.events if e["event_type"] == "click"]
        suggestions = list(set(clicked_products) - {product_id})
        random.shuffle(suggestions)
        return suggestions
