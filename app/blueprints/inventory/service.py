import csv
from flask import current_app
import shopify
from ..notifications.service import NotificationService

class InventoryService:
    def __init__(self):
        self.notifier = NotificationService()
        self.low_stock_threshold = int(current_app.config.get('LOW_STOCK_THRESHOLD', 5))

    def update_inventory(self, stream):
        reader = csv.DictReader(stream.read().decode('utf-8').splitlines())
        results = {'updated': [], 'low_stock': [], 'errors': []}

        for row in reader:
            sku = row.get('sku')
            try:
                qty = int(row.get('quantity', 0))
            except ValueError:
                results['errors'].append({'sku': sku, 'error': 'invalid quantity'})
                continue

            try:
                product_variants = shopify.Variant.find(query={'sku': sku})
                if not product_variants:
                    raise Exception('SKU not found')
                variant = product_variants[0]
                inventory_item = shopify.InventoryLevel.set(
                    location_id=current_app.config['SHOPIFY_LOCATION_ID'],
                    inventory_item_id=variant.inventory_item_id,
                    available=qty
                )
                results['updated'].append({'sku': sku, 'quantity': qty})

                if qty == 0:
                    variant.product().published_at = None
                    variant.product().save()
                    self.notifier.send_dashboard(f"Product {sku} is out of stock and unpublished.")
                elif qty <= self.low_stock_threshold:
                    results['low_stock'].append({'sku': sku, 'quantity': qty})
                    self.notifier.send_dashboard(f"Low stock alert: {sku} has {qty} left.")

            except Exception as ex:
                current_app.logger.error(f"Failed to update SKU {sku}: {ex}")
        return results
