"""
Author: Igor
Date: 2020.05.30
"""

from children import db


class BaseService(object):
    """This class provides generic operations over
    all the typical ID-based entities."""
    app = None

    def __init__(self, app):
        self.app = app

    @classmethod
    def pre_check_automatic_id(cls, target_function):
        """Performs a pre-checks for an entity that has automatically generating ID,
        for example in case if ID is auto-incrementing. Currently the following checks
        are performing:
        1. checks whether the entity is None
        2. checks that ID is not set (it means the entity is already exists)
        """
        def wrapper(obj, entity):
            # Check that entity is provided
            if entity is None:
                raise ValueError('None object was provided to create new entity: {0}'.format(obj.__class__.__name__))

            # Check that this entity has no ID
            if entity.id is not None:
                raise ValueError('ID presented on creation of new entity: {0}'.format(obj.__class__.__name__))

            return target_function(obj, entity)
        return wrapper

    def create(self, entity):
        """Basic creation method, it does nothing special except adding the entity to
        session, committing it, refreshing the session ensuring the object is up to date
        and returning it back to caller.
        """
        db.session.add(entity)
        db.session.commit()
        db.session.refresh(entity)
        return entity

    def get_by_id(self, id):
        """TODO: implement it, for Lena"""
        pass


