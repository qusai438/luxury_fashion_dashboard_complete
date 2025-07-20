from flask import Blueprint, render_template

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/')
def orders():
    return render_template('orders.html')
