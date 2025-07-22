import openai
from app.utils.api_keys import get_api_key

def generate_ad_copy_from_image(image_url):
    openai.api_key = get_api_key("openai")
    
    prompt = f"""
You are a luxury fashion marketing expert. Analyze the following product image and generate high-converting Instagram ad copy. 
Use refined language suitable for elite fashion brands. Do not explain or introduce anything. Just return the ad copy.

Image URL: {image_url}
    """.strip()

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": [{"type": "text", "text": prompt}]}],
        temperature=0.8,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()


def generate_instagram_caption_from_image(image_url):
    openai.api_key = get_api_key("openai")
    
    prompt = f"""
You are a luxury fashion social media specialist. Generate a short, elegant Instagram caption for the product shown in this image. 
Use an exclusive tone. Include one popular luxury hashtag. No emojis.

Image URL: {image_url}
    """.strip()

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": [{"type": "text", "text": prompt}]}],
        temperature=0.7,
        max_tokens=200
    )

    return response.choices[0].message.content.strip()
