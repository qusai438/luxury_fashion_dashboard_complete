from flask import Flask
from .config import Config
from .extensions import db, mail, socketio
from .tasks import make_celery
from .blueprints_loader import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    mail.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    
    # Register blueprints
    register_blueprints(app)

    # Celery
    celery = make_celery(app)

    return app, celery
