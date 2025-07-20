import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
    SHOPIFY_PASSWORD = os.getenv("SHOPIFY_PASSWORD")
    SHOPIFY_STORE_NAME = os.getenv("SHOPIFY_STORE_NAME")
    SHOPIFY_LOCATION_ID = os.getenv("SHOPIFY_LOCATION_ID")

    # Email
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    # Celery
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

    # Uploads
    MEDIA_FOLDER = os.path.join(os.getcwd(), "media")
    LOW_STOCK_THRESHOLD = os.getenv("LOW_STOCK_THRESHOLD", 5)

    # Sentry or error reporting can be added here if needed
