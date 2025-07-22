import requests
from app.utils.openai_tools import generate_caption_from_image, generate_ad_copy_from_image
from app.utils.shopify import get_product_image_url

class AdsGeneratorService:
    def generate_from_product(self, product_id):
        # Step 1: Get product image from Shopify
        image_url = get_product_image_url(product_id)
        if not image_url:
            raise Exception("No image found for this product.")

        # Step 2: Generate caption and ad content from image
        caption = generate_caption_from_image(image_url)
        ad_copy = generate_ad_copy_from_image(image_url)

        return {
            "image_url": image_url,
            "caption": caption,
            "ad_copy": ad_copy
        }
