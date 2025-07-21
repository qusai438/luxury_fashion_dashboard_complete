# app/blueprints_loader.py

from app.blueprints.inventory.routes import inventory_bp
from app.blueprints.email.routes import email_bp
from app.blueprints.ai_content.routes import ai_content_bp
from app.blueprints.ai_media.routes import ai_media_bp
from app.blueprints.video.routes import video_bp
from app.blueprints.chatbot.routes import chatbot_bp
from app.blueprints.livechat.routes import livechat_bp
from app.blueprints.analytics.routes import analytics_bp
from app.blueprints.marketing.routes import marketing_bp
from app.blueprints.recommendations.routes import recommendations_bp
from app.blueprints.orders.routes import orders_bp
from app.blueprints.dropship.routes import dropship_bp
from app.blueprints.reviews.routes import reviews_bp
from app.blueprints.returns.routes import returns_bp
from app.blueprints.ads.routes import ads_bp
from app.blueprints.admin.settings import settings_bp
from app.blueprints.admin.routes import admin_bp
from app.blueprints.smart_editor.routes import smart_editor_bp

def register_blueprints(app):
    app.register_blueprint(inventory_bp)
    app.register_blueprint(email_bp)
    app.register_blueprint(ai_content_bp)
    app.register_blueprint(ai_media_bp)
    app.register_blueprint(video_bp)
    app.register_blueprint(chatbot_bp)
    app.register_blueprint(livechat_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(marketing_bp)
    app.register_blueprint(recommendations_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(dropship_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(returns_bp)
    app.register_blueprint(ads_bp)
    app.register_blueprint(settings_bp)  # لوحة التحكم لإدارة مفاتيح API
    app.register_blueprint(admin_bp)
    app.register_blueprint(smart_editor_bp)
