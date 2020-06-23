"""
Author: Igor, Lena
Date: 2020.05.30
"""

from children import db


class BaseService(object):
    """This class provides generic operations over
        all the typical ID-based entities."""
    base_class = db.Model

    def __init__(self, app):
        self.app = app
        if self.base_class.__name__ == 'Model':
            raise ValueError('You cannot instantiate an object of a class BaseService. '
                             'Define some child and define attribute base_class for it.')
        self.model_columns = self.base_class.__table__.columns.keys()

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

    def update(self, id_entity, fields_to_update: dict, fail_if_entity_not_exists=True):
        existing_entity = self.get_by_id(id_entity)

        if existing_entity is not None:
            # Scroll all the items in fields to update and apply them to existing entity
            for key, value in fields_to_update.items():
                if value is not None:
                    if hasattr(existing_entity, key):
                        if self.__model_has_column__(key):
                            setattr(existing_entity, key, value)
                        else:
                            raise ValueError('Model definition does not have such key {0} presented to ' +
                                             'update the object ID {1} with class {2}'
                                             .format(key, id_entity, self.__class__.__name__))
                    else:
                        raise ValueError('No such attribute {0} presented to update the object ID {1} with class {2}'
                                         .format(key, id_entity, self.__class__.__name__))

            # Now add the updated entity to session and save it
            db.session.add(existing_entity)
            db.session.commit()
            db.session.refresh(existing_entity)
            return existing_entity
        else:
            # Show the ID and current class name in the exception if we need to fail
            if fail_if_entity_not_exists:
                raise ValueError("The entity with ID {0} doesn't presented to update with class {1}"
                                 .format(id_entity,
                                         self.__class__.__name__))
            return None

    def get_by_id(self, id_entity):
        # Return the object from db by id
        obj = self.base_class.query.filter_by(id=id_entity).first()
        return obj

    def get_all(self):
        all_data = db.session.query(self.base_class).all()
        return all_data

    def delete_by_id(self, id_entity, fail_if_entity_not_exists=False):
        # delete the object from db by id
        obj = self.get_by_id(id_entity)
        if obj is not None:
            db.session.delete(obj)
            db.session.commit()
        else:
            if fail_if_entity_not_exists:
                raise ValueError("The entity with ID {0} doesn't presented to delete with class {1}"
                                 .format(id_entity,
                                         self.__class__.__name__))

    def delete_all(self):
        db.session.query(self.base_class).delete()
        db.session.commit()

    def __model_has_column__(self, key):
        return key in self.model_columns
