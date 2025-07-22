from app.utils.openai_tools import gpt4_vision_generate_caption, gpt4_vision_generate_ad
from app.utils.helpers import validate_image_url


def generate_instagram_caption_from_image(image_url: str) -> str:
    if not validate_image_url(image_url):
        raise ValueError("Invalid image URL provided.")
    return gpt4_vision_generate_caption(image_url)


def generate_ad_copy_from_image(image_url: str) -> str:
    if not validate_image_url(image_url):
        raise ValueError("Invalid image URL provided.")
    return gpt4_vision_generate_ad(image_url)
