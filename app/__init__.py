from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os
from .config import config

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    config_name = os.environ.get('FLASK_ENV', 'default')
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    
    from .cli import create_admin, init_db_command
    app.cli.add_command(create_admin)
    app.cli.add_command(init_db_command)
    
    with app.app_context():
        db.create_all()
        from .models import init_db
        init_db()
    
    return app
