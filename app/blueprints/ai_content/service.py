import openai
from flask import current_app

class AIContentService:
    def __init__(self):
        openai.api_key = current_app.config['OPENAI_API_KEY']

    def generate_product_description(self, title: str) -> str:
        prompt = f"Write a detailed and luxurious product description for a women's fashion item: '{title}'."
        resp = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a creative and proficient copywriter for luxury fashion."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        return resp.choices[0].message.content.strip()

    def generate_instagram_caption(self, title: str) -> str:
        prompt = f"Generate a short and stylish Instagram caption with hashtags for a luxury women's fashion product titled '{title}':"
        resp = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        return resp.choices[0].message.content.strip()

    def generate_ad_copy(self, title: str, description: str) -> str:
        prompt = (
            f"Write a compelling and concise ad copy for a luxury women's fashion item.\n"
            f"Title: {title}\nDescription: {description}\nInclude a clear call to action."
        )
        resp = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )
        return resp.choices[0].message.content.strip()
