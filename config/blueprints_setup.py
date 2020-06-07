"""
Author: Igor
Date 2020.05.28
"""

from flask import Flask
from blueprints.main_controller import main_controller


class BlueprintsSetup(object):
    def __init__(self, app):
        self.app: Flask = app
        self.app.register_blueprint(main_controller)

