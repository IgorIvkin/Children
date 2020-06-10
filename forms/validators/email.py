"""
Author: Igor
Date: 2020.06.10
"""

import re
from wtforms import ValidationError


class Email(object):
    """
    This validator checks that a given string is an email.
    It is very simple validator and it assumes mostly that
    it will have a string that contains one character @ inside.
    """
    def __init__(self, error_message=None):
        if error_message is None:
            error_message = 'Wrong email address'
        self.error_message = error_message

    def __call__(self, form, field):
        email_to_check = field.data
        if not re.match(r'[\w.-]+@[\w.-]+(?:\.[\w]+)+', email_to_check):
            raise ValidationError(self.error_message)


email = Email
