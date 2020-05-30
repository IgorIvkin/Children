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

    def __init__(self, app):
        super().__init__(app)

    def create(self, entity: User):
        # Perform pre-checks for automatically generated ID
        super().automatic_id_pre_check(entity)

        # Generate password hash on provided password
        if (entity.password is None) or \
           (entity.password == ''):
            raise ValueError('No password was provided on creation of new user')
        entity.password = self.produce_password_hash(entity.password)

        return super().create(entity)

    def produce_password_hash(self, password):
        return generate_password_hash(password)
