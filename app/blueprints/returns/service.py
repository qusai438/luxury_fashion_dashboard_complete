import shopify
from flask import current_app

class ReturnsService:
    def handle_return(self, order_id, reason):
        order = shopify.Order.find(order_id)

        if not order:
            raise Exception("Order not found")

        # Log return reason internally (could be saved to DB or sent to admin)
        return_note = f"Return requested: {reason}"

        # Optionally tag the order in Shopify
        order.tags += ",ReturnRequested"
        order.note = return_note

        if order.save():
            return {'success': True, 'message': 'Return request processed'}
        else:
            raise Exception("Failed to update order with return info")
