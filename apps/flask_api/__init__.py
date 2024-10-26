# apps/flask-api/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from libs.server.data_access.database import db  # Import db from database
from apps.flask_api.routes import api_bp
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app
