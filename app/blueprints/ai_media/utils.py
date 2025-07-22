import os
import base64
from io import BytesIO
from PIL import Image
from werkzeug.utils import secure_filename

TEMP_DIR = "temp"

def ensure_temp_dir():
    os.makedirs(TEMP_DIR, exist_ok=True)

def save_base64_image(data_url, filename=None):
    ensure_temp_dir()
    header, encoded = data_url.split(",", 1)
    image_data = base64.b64decode(encoded)
    image = Image.open(BytesIO(image_data)).convert("RGB")

    filename = secure_filename(filename or "upload.jpg")
    path = os.path.join(TEMP_DIR, filename)
    image.save(path, format="JPEG", quality=85)

    return path

def resize_image(path, max_size=(1080, 1080)):
    image = Image.open(path)
    image.thumbnail(max_size)
    image.save(path, format="JPEG", quality=90)
    return path
