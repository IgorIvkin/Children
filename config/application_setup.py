"""
Author: Igor
Date: 2020.05.22
"""

import os
from config.config import BaseConfiguration, TestingConfiguration
from config.database_setup import DatabaseSetup


class ApplicationSetup(object):
    """This class is intended to build a starting application setup including:
     - configuration setup
    """
    setup_mode = "common"
    config = None
    database_setup = None
    blueprints_setup = None

    def __init__(self, app):
        # Prepare application config according to the environment variables
        self.setup_mode = os.environ.get("FLASK_SETUP_MODE", default="common")
        if self.setup_mode == "tests":
            self.config = TestingConfiguration()
        elif self.setup_mode == "common":
            self.config = BaseConfiguration()
        else:
            raise ValueError("Unknown mode of application setup: " + self.setup_mode)
        app.config.from_object(self.config)

        # Initialize database setup
        self.database_setup = DatabaseSetup(app)

        # Initialize blueprints (they represent controllers in some way)
        from config.blueprints_setup import BlueprintsSetup
        self.blueprints_setup = BlueprintsSetup(app)

    def get_config(self):
        return self.config
