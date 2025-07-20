import openai
import os
from flask import current_app
from werkzeug.utils import secure_filename
from datetime import datetime

class AIMediaService:
    def __init__(self):
        openai.api_key = current_app.config['OPENAI_API_KEY']
        self.media_dir = os.path.join(current_app.root_path, 'media')
        os.makedirs(self.media_dir, exist_ok=True)

    def generate_image(self, prompt: str) -> str:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        filename = self._save_image_from_url(image_url)
        return filename

    def generate_variation(self, image_bytes: bytes) -> str:
        response = openai.Image.create_variation(
            image=image_bytes,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        filename = self._save_image_from_url(image_url)
        return filename

    def _save_image_from_url(self, url: str) -> str:
        import requests
        r = requests.get(url)
        if r.status_code == 200:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = secure_filename(f"ai_image_{timestamp}.png")
            filepath = os.path.join(self.media_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(r.content)
            return f"/media/{filename}"
        else:
            raise Exception("Failed to download image from OpenAI")
