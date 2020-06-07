"""
Author: Igor
Date: 2020.05.28
"""

import re
from children import db
from exceptions.model_exceptions import ColumnValidationError
from datetime import datetime
from sqlalchemy.orm import validates

# User type - plain user
USER_TYPE_PLAIN = 1
# User type - administrator, has full access to application
USER_TYPE_ADMIN = 2


class User(db.Model):
    """Represents typical user of application.
    """
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_oauth = db.Column(db.String(255), unique=True, nullable=True)
    login = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    status = db.Column(db.Boolean, nullable=False, default=True)
    type = db.Column(db.Integer, nullable=False, default=USER_TYPE_PLAIN)

    def __repr__(self):
        return "<User {0}>".format(self.id)

    @property
    def is_active(self):
        return self.status is True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    @validates('login')
    def validate_login(self, key, login):
        if not re.match(r'[\w.-]+@[\w.-]+(?:\.[\w]+)+', login):
            raise ColumnValidationError('Wrong user login provided, an email is expected: {0}'.format(login))
        return login

    @validates('title')
    def validate_title(self, key, title):
        if len(title) < 2:
            raise ColumnValidationError('User title is too short, at least 2 characters expected: {0}'.format(title))
        elif len(title) > 255:
            raise ColumnValidationError('User title is too long, max 255 characters allowed: {0}'.format(title))
        return title
