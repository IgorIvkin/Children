"""
Author: Igor, Lena
Date: 2020.05.30
"""

from children import create_app
from models.user import User
from services.user_service import UserService
from services.base_service import BaseService
import pytest


@pytest.fixture(scope='module')
def app():
    app = create_app(test_mode=True)
    yield app
    with app.app_context():
        user_service = UserService(app)
        user_service.delete_all()


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
    with app.app_context():
        user_service = UserService(app)
        with pytest.raises(ValueError, match=r"Login cannot be presented to update user*"):
            updated_user = user_service.update(id_entity=1, fields_to_update={'login': 'test3@example.com'})


def test_update_user_change_title_and_password(app):
    with app.app_context():
        user_service = UserService(app)
        user = User()
        user.login = 'tes4@example.com'
        user.password = 'test1'
        user.title = 'First title'
        user = user_service.create(user)
        new_title = 'Test title!'
        new_password = 'newpwd'
        updated_user = user_service.update(user.id, {'title': new_title, 'password': new_password})
        assert updated_user.title == new_title
        assert user_service.check_password_hash(user.password, new_password)


def test_delete_by_id(app):
    with app.app_context():
        user_service = UserService(app)
        user = User()
        user.login = 'test5@example.com'
        user.password = 'test1'
        user = user_service.create(user)
        user_service.delete_by_id(user.id)
        assert user_service.get_by_id(user.id) is None


def test_update_user_cannot_assign_bad_column(app):
    with app.app_context():
        user_service = UserService(app)
        user = User()
        user.login = 'tes4@example.com'
        user.password = 'test1'
        user = user_service.create(user)
        with pytest.raises(ValueError, match=r"Model definition does not have such key*"):
            updated_user = user_service.update(user.id, {'metadata': 'test'})


def test_create_base_service(app):
    with app.app_context():
        with pytest.raises(ValueError, match=r"You cannot instantiate an object of a class BaseService*"):
            service = BaseService(app)





