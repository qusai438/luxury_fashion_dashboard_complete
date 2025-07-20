from flask import jsonify

class ProductService:
    def __init__(self):
        # في المشروع الكامل، يمكن هنا الربط مع قاعدة بيانات أو API خارجي
        self.products = []

    def get_all_products(self):
        return self.products

    def add_product(self, product):
        if not product.get("title"):
            raise ValueError("Product must have a title")
        self.products.append(product)
        return product
