"""
Author: Igor
Date: 2020.06.04
"""

from flask import Flask
from services.user_service import UserService


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

