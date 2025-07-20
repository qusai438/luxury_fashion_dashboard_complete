from app.extensions import openai_client

class SmartEditorService:
    def __init__(self):
        self.model = "gpt-4"

    def generate_html_section(self, instruction: str) -> str:
        prompt = (
            f"Generate a clean, responsive HTML5 + Bootstrap 5 section for a luxury fashion e-commerce site.\n"
            f"The section should follow this instruction: \"{instruction}\".\n"
            f"Do not include <html>, <head>, or <body> tags — return only the section code.\n"
        )

        response = openai_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6,
            max_tokens=800
        )

        return response.choices[0].message.content.strip()
