import io
from PIL import Image

def resize_image(image_bytes, size=(512, 512)):
    image = Image.open(io.BytesIO(image_bytes))
    image = image.convert("RGB")
    image = image.resize(size)
    output = io.BytesIO()
    image.save(output, format='JPEG')
    output.seek(0)
    return output.read()

def is_supported_image(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))

def get_image_dimensions(image_bytes):
    image = Image.open(io.BytesIO(image_bytes))
    return image.size
