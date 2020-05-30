"""
Author: Igor
Date: 2020.05.30
"""

from children import db
from werkzeug.security import generate_password_hash


class BaseService(object):
    """This class provides generic operations over
    all the typical ID-based entities."""
    app = None

    def __init__(self, app):
        self.app = app

    def automatic_id_pre_check(self, entity):
        # Check that entity is provided
        if entity is None:
            raise ValueError('None object was provided to create new entity: {0}'.format(self.__class__.__name__))

        # Check that this entity has no ID
        if entity.id is not None:
            raise ValueError('ID presented on creation of new entity: {0}'.format(self.__class__.__name__))

        return True

    def create(self, entity):
        db.session.add(entity)
        db.session.commit()
        db.session.refresh(entity)
        return entity

