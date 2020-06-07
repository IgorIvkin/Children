"""
Author: Igor
Date: 2020.06.04
"""

from flask import Flask, redirect
from services.user_service import UserService
from models.user import USER_TYPE_ADMIN
from flask_login import current_user


class SecuritySetup(object):
    """Intended to create basic security setup for application.
    This class is based on login_manager from flask-login.
    """
    def __init__(self, app: Flask):
        self.app = app
        self.user_service = UserService(self.app)

    def get_user_service(self) -> UserService:
        return self.user_service


def url_of_login_page():
    """Returns the URL of login page that
    forces user to be logged in.
    """
    return "/user/login/"


def admin_required(func):
    """This decorator function forces user to be logged in and to be
    an effective administrator. Otherwise it will redirect user to login page
    to approve his credentials.
    """
    def decorated_view(*args, **kwargs):
        if current_user is None:
            return redirect(url_of_login_page())
        elif not hasattr(current_user, 'is_anonymous'):
            raise ValueError("Current user exists but has no attribute 'is_anonymous' that is expected for user. "
                             "Check the following class: {0}".format(type(current_user)))
        elif current_user.is_anonymous:
            return redirect(url_of_login_page())
        elif not hasattr(current_user, 'type'):
            raise ValueError("Current user exists but has no attribute 'type' that is expected for user. "
                             "Check the following class: {0}".format(type(current_user)))
        elif current_user.type != USER_TYPE_ADMIN:
            return redirect(url_of_login_page())
        else:
            return func(*args, **kwargs)
    return decorated_view
