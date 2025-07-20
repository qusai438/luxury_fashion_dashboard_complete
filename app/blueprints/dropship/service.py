class DropshipService:
    def import_products_by_category(self, category: str) -> list:
        # Simulated product import logic — replace with actual API parsing logic (e.g. from BrandsGateway CSV or API)
        sample_products = [
            {"id": "SKU001", "title": "Slim Fit Jeans", "category": "pants"},
            {"id": "SKU002", "title": "Ankle Boots", "category": "shoes"},
            {"id": "SKU003", "title": "Leather Jacket", "category": "jackets"}
        ]

        imported = [p for p in sample_products if p["category"] == category.lower()]
        return imported
