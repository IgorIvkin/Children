"""
Author: Igor
Date: 2020.05.30
"""

from services.base_service import BaseService
from models.user import User
from werkzeug.security import generate_password_hash


class UserService(BaseService):
    """This class provides generic operations over users."""
    app = None
    base_class = User

    def __init__(self, app):
        super().__init__(app)

    @BaseService.pre_check_automatic_id
    def create(self, entity: User):
        """Creates new user calculating a hash of his password. Password is mandatory.
        The function assumes the password given here in a form of plain string.
        """
        # Generate password hash on provided password
        if (entity.password is None) or \
           (entity.password == ''):
            raise ValueError('No password was provided on creation of new user')
        entity.password = self.produce_password_hash(entity.password)

        # Call parent's (BaseService) create method
        return super().create(entity)

    @classmethod
    def produce_password_hash(cls, password):
        """Calculates the hash of a given password using standard werkzeug.security
        function generate_password_hash. No special algorithm taken now, all values are default.
        """
        return generate_password_hash(password)
