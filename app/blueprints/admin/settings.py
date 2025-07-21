from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.api_key import APIKey
from app.forms.api_keys_form import APIKeysForm
from app.utils.encryption import encrypt_value, decrypt_value
from app.extensions import db

settings_bp = Blueprint("settings", __name__, url_prefix="/admin/settings")

@settings_bp.route("/api-keys", methods=["GET", "POST"])
@login_required
def manage_api_keys():
    if not current_user.is_admin:
        flash("Access denied.", "danger")
        return redirect(url_for("dashboard.index"))

    form = APIKeysForm()

    # تحميل القيم من قاعدة البيانات (لفيها فك تشفير)
    if request.method == "GET":
        form.openai_key.data = decrypt_value(APIKey.get("openai"))
        form.shopify_key.data = decrypt_value(APIKey.get("shopify"))
        form.meta_key.data = decrypt_value(APIKey.get("meta"))
        form.smtp_key.data = decrypt_value(APIKey.get("smtp"))

    elif form.validate_on_submit():
        APIKey.set("openai", encrypt_value(form.openai_key.data))
        APIKey.set("shopify", encrypt_value(form.shopify_key.data))
        APIKey.set("meta", encrypt_value(form.meta_key.data))
        APIKey.set("smtp", encrypt_value(form.smtp_key.data))
        db.session.commit()
        flash("✅ API keys updated successfully.", "success")
        return redirect(url_for("settings.manage_api_keys"))

    return render_template("admin/api_keys.html", form=form)
