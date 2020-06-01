"""
Author: Igor
Date: 2020.05.30
"""

from services.base_service import BaseService
from models.user import User
from werkzeug.security import generate_password_hash
from datetime import datetime


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

    def update(self, id_entity, fields_to_update: dict, fail_if_entity_not_exists=False):
        """Updates an existing user.
        Can fail in case if user was not found, this
        behaviour can be set with parameter fail_if_entity_not_exists=True.
        """
        # Generate password hash on provided password. We assume here that if password is
        # provided in fields_to_update then it means we have to set a new password.
        if (
                'password' in fields_to_update and
                (fields_to_update['password'] is not None) and
                (fields_to_update['password'] != '')
        ):
            fields_to_update['password'] = self.produce_password_hash(fields_to_update['password'])

        # We cannot change login of user
        if 'login' in fields_to_update and fields_to_update['login'] != '':
            raise ValueError('Login cannot be presented to update user, it is not possible to change login')

        # Set updated time to current date-time
        fields_to_update['updated'] = datetime.utcnow()

        # Call parent's (BaseService) update method
        return super().update(id_entity,
                              fields_to_update,
                              fail_if_entity_not_exists)

    @classmethod
    def produce_password_hash(cls, password):
        """Calculates the hash of a given password using standard werkzeug.security
        function generate_password_hash. No special algorithm taken now, all values are default.
        """
        return generate_password_hash(password)
