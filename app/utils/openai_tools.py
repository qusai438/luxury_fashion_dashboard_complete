import openai
import base64
import requests
from app.utils.api_keys import get_api_key

openai.api_key = get_api_key("openai")

def encode_image(image_url):
    response = requests.get(image_url)
    if response.status_code != 200:
        raise Exception("Failed to fetch image from URL.")
    return base64.b64encode(response.content).decode("utf-8")

def generate_caption_from_image(image_url):
    image_data = encode_image(image_url)
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "You are a luxury fashion marketing expert. Keep it concise and stylish."},
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}},
                    {"type": "text", "text": "Generate a high-end Instagram caption for this fashion product."}
                ]
            }
        ],
        max_tokens=150
    )
    return response.choices[0].message.content.strip()

def generate_ad_copy_from_image(image_url):
    image_data = encode_image(image_url)
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "system", "content": "You are a luxury brand ad copywriter. Create elegant and persuasive ad copy."},
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}},
                    {"type": "text", "text": "Write a polished ad copy for this luxury fashion item."}
                ]
            }
        ],
        max_tokens=250
    )
    return response.choices[0].message.content.strip()
