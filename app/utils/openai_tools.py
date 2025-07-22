import openai
from app.utils.api_keys import get_api_key

openai.api_key = get_api_key("openai")


def gpt4_vision_generate_caption(image_url: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a luxury fashion marketing assistant. Generate an elegant, creative, and concise "
                    "Instagram caption based on the image. Avoid emojis and hashtags. Keep it classy."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": image_url}
                    }
                ]
            }
        ],
        max_tokens=150
    )
    return response.choices[0].message["content"].strip()


def gpt4_vision_generate_ad(image_url: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior advertising copywriter for luxury fashion. Analyze the image and generate a "
                    "short and powerful ad copy suitable for Meta Ads or Google Ads. Avoid clickbait. Keep the tone elegant."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": image_url}
                    }
                ]
            }
        ],
        max_tokens=200
    )
    return response.choices[0].message["content"].strip()
