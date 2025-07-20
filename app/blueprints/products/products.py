from flask import Blueprint, render_template

products_bp = Blueprint('products', __name__)

@products_bp.route('/')
def list_products():
    return render_template('products.html')
