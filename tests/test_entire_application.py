"""
Author: Igor
Date: 2020.05.28
"""

from children import create_app
import pytest


@pytest.fixture(scope='module')
def app():
    app = create_app(test_mode=True)
    yield app


def test_environment_set(app):
    assert app.testing

