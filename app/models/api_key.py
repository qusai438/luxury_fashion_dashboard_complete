from app.extensions import db
from cryptography.fernet import Fernet
import os

class APIKey(db.Model):
    __tablename__ = "api_keys"

    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(64), unique=True, nullable=False)
    encrypted_key = db.Column(db.Text, nullable=False)

    @staticmethod
    def get_fernet():
        secret = os.getenv("APP_SECRET_KEY")
        if not secret:
            raise Exception("APP_SECRET_KEY is not set")
        return Fernet(secret.encode())

    def set_key(self, raw_key: str):
        f = self.get_fernet()
        self.encrypted_key = f.encrypt(raw_key.encode()).decode()

    def get_key(self):
        f = self.get_fernet()
        return f.decrypt(self.encrypted_key.encode()).decode()
