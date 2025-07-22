from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_socketio import SocketIO
from celery import Celery
from dotenv import load_dotenv
import os

db = SQLAlchemy()
mail = Mail()
socketio = SocketIO(cors_allowed_origins="*")

celery = Celery(__name__, broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"))

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object("config.settings")

    db.init_app(app)
    mail.init_app(app)
    CORS(app)
    socketio.init_app(app)
    celery.conf.update(app.config)

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
