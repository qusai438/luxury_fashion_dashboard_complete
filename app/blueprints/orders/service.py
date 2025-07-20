import shopify
from flask import current_app

class OrdersService:
    def get_unfulfilled_orders(self):
        orders = shopify.Order.find(fulfillment_status='unfulfilled', financial_status='paid')
        result = []
        for order in orders:
            result.append({
                'id': order.id,
                'name': order.name,
                'email': order.email,
                'line_items': [{'title': item.title, 'quantity': item.quantity} for item in order.line_items]
            })
        return result

    def fulfill_order(self, order_id):
        order = shopify.Order.find(order_id)
        if not order:
            raise Exception("Order not found")

        fulfillment = shopify.Fulfillment({
            "order_id": order.id,
            "location_id": current_app.config['SHOPIFY_LOCATION_ID'],
            "tracking_number": None,
            "notify_customer": True,
            "line_items": order.line_items
        })

        if fulfillment.save():
            return {'status': 'fulfilled', 'order_id': order.id}
        else:
            raise Exception("Failed to fulfill order")
