import os

class RenderConfig:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///instance/render.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email (if needed)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')

    # Mock mode for Render testing
    ENABLE_MOCK_MODE = os.environ.get("ENABLE_MOCK_MODE", "true").lower() == "true"
