"""
Authors: Igor, Elena
Date: 2020.05.22
"""

from flask import Flask, render_template
from config.application_setup import ApplicationSetup


def create_app(test_config=None):
    app = Flask(__name__)
    with app.app_context():
        app_setup = ApplicationSetup(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    return app

