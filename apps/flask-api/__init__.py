from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from libs.server.data_access import db  # Import shared model definitions
from apps.flask_api.routes.route import api_bp
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app