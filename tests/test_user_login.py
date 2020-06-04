"""
Author: Igor
Date: 2020.06.04
"""

import pytest
from children import create_app
from services.user_service import UserService
from models.user import User
from flask_login import current_user, login_user


@pytest.fixture(scope='module')
def app():
    app = create_app(test_mode=True)
    yield app
    with app.app_context():
        user_service = UserService(app)
        user_service.delete_all()


def test_create_user_and_login(app):
    with app.test_request_context():
        # Create the user first with a given login and password
        user_service = UserService(app)
        user = User()
        user.login = 'test@example.com'
        user.password = 'pwd111'
        user.title = 'Test user'
        created_user = user_service.create(entity=user)
        assert created_user.id is not None

        # Now get this user by its ID
        user_from_db = user_service.get_by_login(login='test@example.com')
        assert user_from_db is not None
        assert user_from_db.title == 'Test user'

        # Compare passwords and login user in case everything is ok
        assert user_service.check_password_hash(hash_to_check=user_from_db.password, password_to_check='pwd111')
        login_user(user=user_from_db, remember=False)
        assert current_user.id == user_from_db.id

