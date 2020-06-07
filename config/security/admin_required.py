"""
Author: Igor
Date: 2020.06.07
"""

from flask import redirect
from config.security.security_setup import url_of_login_page
from models.user import USER_TYPE_ADMIN
from flask_login import current_user


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
