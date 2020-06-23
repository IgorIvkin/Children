"""
Author: Igor
Date 2020.05.28
"""

from flask import Flask
from blueprints.main_controller import main_controller
from blueprints.user_controller import user_controller
from blueprints.admin.admin_main_controller import admin_main_controller


class BlueprintsSetup(object):
    def __init__(self, app):
        self.app: Flask = app
        self.app.register_blueprint(main_controller)
        self.app.register_blueprint(user_controller)

        # Admin controllers
        self.app.register_blueprint(blueprint=admin_main_controller,
                                    url_prefix='/admin')


