"""
Author: Igor
Date: 2020.05.28
"""

import pytest
from children import create_app, db

"""
@pytest.fixture
def app():
    app = create_app(test_mode=True)
    yield app
"""


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def cli_runner(app):
    return app.test_cli_runner()



