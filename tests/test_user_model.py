"""
Author: Igor
Date: 2020.05.30
"""

from models.user import User
from services.user_service import UserService
import pytest


def test_create_user(app):
    with app.app_context():
        user_service = UserService(app)
        user = User()
        user.login = 'test@example.com'
        user.password = 'test'
        user = user_service.create(user)
        assert user.id is not None


def test_create_user_fail_none_entity_provided(app):
    with app.app_context():
        user_service = UserService(app)
        with pytest.raises(ValueError, match=r"None object was provided to create new entity.*"):
            user = user_service.create(None)

