class MockConfig:
    DEBUG = True
    TESTING = True
    SECRET_KEY = "mock-secret"
    
    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///mock.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail
    MAIL_SERVER = "localhost"
    MAIL_PORT = 8025
    MAIL_DEFAULT_SENDER = "mock@example.com"
    MAIL_USERNAME = ""
    MAIL_PASSWORD = ""
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False

    # Celery + Redis
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

    # OpenAI, Shopify, Meta, وغيرها (تكون فارغة أو وهمية)
    OPENAI_API_KEY = "mock-key"
    SHOPIFY_API_KEY = "mock"
    SHOPIFY_API_SECRET = "mock"
    SHOPIFY_STORE_DOMAIN = "mock.myshopify.com"
    SHOPIFY_ACCESS_TOKEN = "mock"

    # Meta (فيسبوك وتيك توك)
    META_ADS_TOKEN = "mock"
    TIKTOK_API_TOKEN = "mock"

    # Cloudinary أو S3
    CLOUDINARY_URL = "mock"

    # Mock Mode مفعل
    MOCK_MODE = True
