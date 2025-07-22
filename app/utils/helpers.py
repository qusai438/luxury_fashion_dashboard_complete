import re


def validate_image_url(url: str) -> bool:
    """
    Checks if a given string is a valid image URL.
    """
    image_pattern = r'^https?:\/\/.*\.(?:png|jpg|jpeg|webp|gif|bmp)$'
    return bool(re.match(image_pattern, url.strip().lower()))
