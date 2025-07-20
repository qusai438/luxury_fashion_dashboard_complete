from flask import Flask
from config import Config
from extensions import db, migrate, mail
from blueprints import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Register all blueprints
    register_blueprints(app)

    return app
