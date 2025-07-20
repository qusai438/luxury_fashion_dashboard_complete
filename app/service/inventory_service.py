class InventoryService:
    def __init__(self):
        self.inventory = {}

    def update_stock(self, sku: str, quantity: int):
        if not sku:
            raise ValueError("SKU is required")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.inventory[sku] = quantity
        return {"sku": sku, "quantity": quantity}

    def get_stock(self, sku: str):
        return {"sku": sku, "quantity": self.inventory.get(sku, 0)}

    def all_inventory(self):
        return self.inventory
