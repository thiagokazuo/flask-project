from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate  # Adicione esta linha
from .models import db
from config import Config

login_manager = LoginManager()
migrate = Migrate()  # Adicione esta linha

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)
    app.config.from_pyfile('config.py', silent=True)

    db.init_app(app)
    migrate.init_app(app, db)  # Inicialize o migrate

    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    from .controllers import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
