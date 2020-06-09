"""
Authors: Igor, Elena
Date: 2020.05.22
"""

from flask import Flask, render_template
from config.application_setup import ApplicationSetup
from children.basic_logging import get_logger
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
log = get_logger("children")
migrate = Migrate()


def create_app(test_mode=False):
    app = Flask(__name__)

    # Init configuration (depending on environment, test, dev or production - production is not yet implemented)
    ApplicationSetup(app, test_mode)
    db.init_app(app)

    # Init migration manager for database
    migrate.init_app(app, db)

    # Init blueprints (they behave as controllers actually)
    from config.blueprints_setup import BlueprintsSetup
    BlueprintsSetup(app)

    # Init login manager and security setup for users of application
    login_manager.init_app(app)
    from config.security.security_setup import SecuritySetup
    security_setup = SecuritySetup(app)

    # Init user loader for login manager
    @login_manager.user_loader
    def load_user(id_user):
        return security_setup.get_user_service().get_by_id(int(id_user))

    # Init basic 404 Not Found error handler
    @app.errorhandler(404)
    def page_not_found(event):
        return render_template("errors/404.html"), 404

    return app
