import uuid
from app.extensions import dalle_client
from app.utils.media import generate_video_from_images

def generate_video_promo(product_info: dict) -> str:
    title = product_info.get("title", "Luxury Fashion")
    description = product_info.get("description", "")
    prompt = f"A luxurious, cinematic product showcase of a women's fashion item: {title}. {description}"

    image_urls = dalle_client.generate_images(prompt=prompt, n=4)
    video_id = str(uuid.uuid4())
    video_path = generate_video_from_images(image_urls, video_id)

    video_url = f"/static/generated_videos/{video_id}.mp4"
    return video_url
