# app/blueprints/__init__.py

from flask import Blueprint
from .main import main_bp
from .products import products_bp
from .orders import orders_bp
from .customers import customers_bp
from .analytics import analytics_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(orders_bp, url_prefix="/orders")
    app.register_blueprint(customers_bp, url_prefix="/customers")
    app.register_blueprint(analytics_bp, url_prefix="/analytics")
