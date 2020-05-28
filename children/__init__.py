"""
Authors: Igor, Elena
Date: 2020.05.22
"""

from flask import Flask, render_template
from config.application_setup import ApplicationSetup
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_mode=False, instance_relative_config=False):
    app = Flask(__name__)

    # Init configuration (depending on environment, test, dev or production - production is not yet implemented)
    app_setup = ApplicationSetup(app, test_mode)
    db.init_app(app)

    # Init blueprints (they behave as controllers actually)
    from config.blueprints_setup import BlueprintsSetup
    blueprints_setup = BlueprintsSetup(app)

    # Init basic 404 Not Found error handler
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    return app

