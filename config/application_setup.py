"""
Author: Igor
Date: 2020.05.22
"""

from config.config import BaseConfiguration, TestingConfiguration


class ApplicationSetup(object):
    """This class is intended to build a starting application setup including:
     - configuration setup
    """
    def __init__(self, app, test_mode=False):
        self.setup_mode = "common"
        self.config = None
        
        if test_mode:
            self.config = TestingConfiguration()
        else:
            self.config = BaseConfiguration()
        app.config.from_object(self.config)

    def get_config(self):
        return self.config
