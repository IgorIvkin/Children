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

        # This test_mode variable comes from test setup, we are using pytest
        # framework and actively use its fixtures. So we pass test_mode=True
        # on creation of test application inside the tests.
        if test_mode:
            self.config = TestingConfiguration()
        else:
            self.config = BaseConfiguration()
        app.config.from_object(self.config)

    def get_config(self):
        return self.config
