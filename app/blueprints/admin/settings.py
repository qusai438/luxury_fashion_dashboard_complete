from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.extensions import db
from app.models.api_key import APIKey

settings_bp = Blueprint("settings", __name__, url_prefix="/admin/settings")

@settings_bp.route("/api-keys", methods=["GET", "POST"])
@login_required
def manage_api_keys():
    if not current_user.is_admin:
        flash("Access denied.", "danger")
        return redirect(url_for("dashboard.index"))

    if request.method == "POST":
        service = request.form.get("service_name", "").lower().strip()
        key = request.form.get("key_value", "").strip()

        if not service or not key:
            flash("Both fields are required.", "warning")
            return redirect(url_for("settings.manage_api_keys"))

        existing = APIKey.query.filter_by(service_name=service).first()
        if existing:
            existing.set_key(key)
            flash(f"Updated API key for '{service}'", "success")
        else:
            new_key = APIKey(service_name=service)
            new_key.set_key(key)
            db.session.add(new_key)
            flash(f"Added new API key for '{service}'", "success")

        db.session.commit()
        return redirect(url_for("settings.manage_api_keys"))

    keys = APIKey.query.all()
    return render_template("admin/settings.html", keys=keys)
