"""
Author: Igor
Date: 2020.05.22
"""

import os
from config.config import BaseConfiguration, TestingConfiguration

"""
This class is intended to build a starting application setup including:
 - configuration setup
"""


class ApplicationSetup(object):
    setup_mode = "common"
    config = None

    def __init__(self):
        self.setup_mode = os.environ.get("FLASK_SETUP_MODE", default="common")
        if self.setup_mode == "tests":
            self.config = TestingConfiguration()
        elif self.setup_mode == "common":
            self.config = BaseConfiguration()
        else:
            raise ValueError("Unknown mode of application setup: " + self.setup_mode)

    def get_config(self):
        return self.config
