import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")

if not APP_SECRET_KEY:
    raise ValueError("❌ APP_SECRET_KEY is missing from environment variables.")

fernet = Fernet(APP_SECRET_KEY.encode())

def encrypt_value(value: str) -> str:
    if not value:
        return ""
    return fernet.encrypt(value.encode()).decode()

def decrypt_value(value: str) -> str:
    if not value:
        return ""
    return fernet.decrypt(value.encode()).decode()
