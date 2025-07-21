from flask import Blueprint, render_template, request, redirect, url_for
from .forms import ImagePromptForm
from .utils import resize_image, is_supported_image
from ...services.ai_image_generator import generate_image_from_prompt
import base64

ai_media_bp = Blueprint("ai_media", __name__, url_prefix="/ai-media")

@ai_media_bp.route("/generate-image", methods=["GET", "POST"])
def generate_image():
    form = ImagePromptForm()
    generated_image_url = None

    if form.validate_on_submit():
        prompt = form.prompt.data
        image_file = form.image.data

        image_bytes = None
        if image_file and is_supported_image(image_file.filename):
            image_bytes = resize_image(image_file.read())

        result_image = generate_image_from_prompt(prompt, image_bytes)
        if result_image:
            encoded = base64.b64encode(result_image).decode("utf-8")
            generated_image_url = f"data:image/jpeg;base64,{encoded}"

    return render_template("ai_media/templates/image_generator.html", form=form, generated_image_url=generated_image_url)
