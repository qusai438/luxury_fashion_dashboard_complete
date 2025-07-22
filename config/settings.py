import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "..", "app.db"))
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.getenv("APP_SECRET_KEY", "supersecretkey")
APP_ENV = os.getenv("APP_ENV", "production")

# Mail
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv("SMTP_USERNAME")
MAIL_PASSWORD = os.getenv("SMTP_PASSWORD")
MAIL_DEFAULT_SENDER = os.getenv("SMTP_USERNAME")

# Celery
CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# OpenAI & Shopify (placeholder values)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY", "")
SHOPIFY_API_SECRET = os.getenv("SHOPIFY_API_SECRET", "")
