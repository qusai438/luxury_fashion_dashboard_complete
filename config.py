import os

class Config:
    # Core Flask config
    SECRET_KEY = os.getenv("APP_SECRET_KEY", "dev-secret")
    ENV = os.getenv("FLASK_ENV", "production")
    DEBUG = ENV == "development"

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///luxury_fashion.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail (for alerts, contact forms, verifications...)
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", MAIL_USERNAME)

    # Celery + Redis
    CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # OpenAI
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")

    # Shopify
    SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
    SHOPIFY_API_SECRET = os.getenv("SHOPIFY_API_SECRET")
    SHOPIFY_ACCESS_TOKEN = os.getenv("SHOPIFY_ACCESS_TOKEN")

    # Meta Ads
    META_ADS_TOKEN = os.getenv("META_ADS_TOKEN")
    META_BUSINESS_ID = os.getenv("META_BUSINESS_ID")

    # File Uploads
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads/")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    # Security
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    PREFERRED_URL_SCHEME = "https"

    # Optional flags
    ENABLE_API_KEY_UI = True
