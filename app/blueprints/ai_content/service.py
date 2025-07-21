import openai
from app.utils.encryption import decrypt_value
from app.models.api_key import APIKey

class AIContentService:

    def __init__(self):
        self.api_key = self._load_openai_key()

    def _load_openai_key(self):
        key = APIKey.get("openai")
        return decrypt_value(key)

    def generate_product_description(self, title: str) -> str:
        openai.api_key = self.api_key
        prompt = f"Write a luxury fashion product description for: {title}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()

    def generate_instagram_caption(self, title: str) -> str:
        openai.api_key = self.api_key
        prompt = f"Write a catchy Instagram caption for a luxury women's fashion item: {title}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9
        )
        return response.choices[0].message.content.strip()

    def generate_ad_copy(self, title: str, description: str) -> str:
        openai.api_key = self.api_key
        prompt = f"Create an engaging ad copy for a product titled '{title}' with the description: {description}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8
        )
        return response.choices[0].message.content.strip()
