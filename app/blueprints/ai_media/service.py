import os
import openai
from flask import current_app
from PIL import Image
import uuid

class AIMediaService:
    def __init__(self):
        openai.api_key = current_app.config['OPENAI_API_KEY']
        self.media_folder = os.path.join(current_app.root_path, '..', 'media')
        os.makedirs(self.media_folder, exist_ok=True)

    def generate_image(self, prompt: str) -> str:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        filename = f"{uuid.uuid4().hex}.png"
        image_path = os.path.join(self.media_folder, filename)
        self._download_image(image_url, image_path)
        return f"/media/{filename}"

    def generate_variation(self, image_stream) -> str:
        img = Image.open(image_stream)
        img = img.convert("RGBA")
        filename = f"{uuid.uuid4().hex}.png"
        input_path = os.path.join(self.media_folder, f"input_{filename}")
        img.save(input_path)

        response = openai.Image.create_variation(
            image=open(input_path, "rb"),
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        output_filename = f"variation_{filename}"
        output_path = os.path.join(self.media_folder, output_filename)
        self._download_image(image_url, output_path)
        return f"/media/{output_filename}"

    def _download_image(self, url, path):
        import requests
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
