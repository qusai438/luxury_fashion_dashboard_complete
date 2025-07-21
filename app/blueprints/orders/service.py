import requests
import os

class OrdersService:
    def __init__(self):
        self.shop_url = os.getenv("SHOPIFY_STORE_URL")
        self.api_key = os.getenv("SHOPIFY_API_KEY")
        self.api_password = os.getenv("SHOPIFY_API_PASSWORD")

        if not all([self.shop_url, self.api_key, self.api_password]):
            raise EnvironmentError("Missing Shopify API credentials.")

        self.session = requests.Session()
        self.session.auth = (self.api_key, self.api_password)
        self.base_url = f"https://{self.shop_url}/admin/api/2023-07"

    def get_unfulfilled_orders(self):
        url = f"{self.base_url}/orders.json?status=open&financial_status=paid&fulfillment_status=unfulfilled"
        response = self.session.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get("orders", [])

    def fulfill_order(self, order_id):
        # Create a fulfillment for a given order
        url = f"{self.base_url}/orders/{order_id}/fulfillments.json"
        payload = {
            "fulfillment": {
                "location_id": self.get_primary_location_id(),
                "tracking_number": None,
                "notify_customer": True
            }
        }
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    def get_primary_location_id(self):
        url = f"{self.base_url}/locations.json"
        response = self.session.get(url)
        response.raise_for_status()
        locations = response.json().get("locations", [])
        if not locations:
            raise ValueError("No locations found in Shopify store.")
        return locations[0]["id"]
