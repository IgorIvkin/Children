"""
Author: Igor
Date 2020.05.28
"""

from flask import Flask
from blueprints.main_controller import main_controller


class BlueprintsSetup(object):
    app: Flask = None

    def __init__(self, app):
        self.app = app
        self.app.register_blueprint(main_controller)

