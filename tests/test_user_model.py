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


def test_get_by_id(app):
    with app.app_context():
        user_service = UserService(app)
        user = User()
        user.login = 'test@example.com'
        user.password = 'test'
        user = user_service.create(user)
        assert user_service.get_by_id(user.id).id == user.id and user_service.get_by_id(user.id).login == user.login


def test_update_user_cannot_change_login(app):
    # TODO: for Lena, be sure that we have at least 1 user here
    with app.app_context():
        user_service = UserService(app)
        with pytest.raises(ValueError, match=r"Login cannot be presented to update user*"):
            updated_user = user_service.update(1, {'login': 'test3@example.com'})


def test_update_user_change_title_and_password(app):
    # TODO: for Lena, be sure that password was changed here
    with app.app_context():
        user_service = UserService(app)
        updated_user = user_service.update(1, {'title': 'Test title!', 'password': 'newpwd'})
        assert updated_user.title == 'Test title!'



