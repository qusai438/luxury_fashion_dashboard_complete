from app.extensions import openai_client

class AdGeneratorService:
    def __init__(self):
        self.model = "gpt-4"

    def generate_ad(self, product: dict) -> str:
        title = product.get("title", "Luxury Fashion Item")
        description = product.get("description", "")
        audience = product.get("audience", "fashion-conscious women")

        prompt = (
            f"Write a high-converting, luxury-style ad copy for a women's fashion product.\n"
            f"Product Title: {title}\n"
            f"Description: {description}\n"
            f"Target Audience: {audience}\n\n"
            f"The ad should sound elegant, persuasive, and suitable for Facebook and Instagram."
        )

        response = openai_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()
