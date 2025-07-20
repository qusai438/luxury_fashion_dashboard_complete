class RecommendationService:
    def get_related_products(self, product_id: str) -> list:
        # Placeholder logic — in real use, you'd query Shopify, vector search, or ML
        return [
            {"id": "prod_1002", "title": "Elegant Silk Dress", "price": 179},
            {"id": "prod_1003", "title": "Luxury Leather Handbag", "price": 320},
            {"id": "prod_1004", "title": "Minimalist Gold Earrings", "price": 89}
        ]
