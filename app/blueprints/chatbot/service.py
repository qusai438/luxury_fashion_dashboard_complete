from app.extensions import openai_client

class ChatbotService:
    def __init__(self):
        self.model = "gpt-4"

    def get_reply(self, message: str) -> str:
        system_prompt = (
            "You are a helpful and polite customer support agent for a luxury women's fashion brand. "
            "Always respond with elegance, professionalism, and warmth."
        )

        response = openai_client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.6,
            max_tokens=300
        )

        return response.choices[0].message.content.strip()
