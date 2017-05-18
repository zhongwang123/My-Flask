from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()

login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    from auth import auth
    app.register_blueprint(auth)

    from main import main
    app.register_blueprint(main)

    return app

