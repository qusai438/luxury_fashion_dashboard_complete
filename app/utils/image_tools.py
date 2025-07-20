import uuid
import os
import requests
from PIL import Image, ImageEnhance
from io import BytesIO

PROCESSED_IMG_DIR = "static/processed_images"
os.makedirs(PROCESSED_IMG_DIR, exist_ok=True)

def upscale_with_ai(image_url: str) -> str:
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    new_size = (image.width * 2, image.height * 2)
    upscaled = image.resize(new_size, Image.LANCZOS)

    filename = f"{uuid.uuid4()}_upscaled.jpg"
    path = os.path.join(PROCESSED_IMG_DIR, filename)
    upscaled.save(path, "JPEG")

    return f"/static/processed_images/{filename}"

def enhance_with_ai(image_url: str) -> str:
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    enhancer = ImageEnhance.Sharpness(image)
    enhanced = enhancer.enhance(2.0)

    filename = f"{uuid.uuid4()}_enhanced.jpg"
    path = os.path.join(PROCESSED_IMG_DIR, filename)
    enhanced.save(path, "JPEG")

    return f"/static/processed_images/{filename}"
