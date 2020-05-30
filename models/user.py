"""
Author: Igor
Date: 2020.05.28
"""

from children import db
from datetime import datetime

USER_TYPE_PLAIN = 1
USER_TYPE_ADMIN = 2


class User(db.Model):
    """Represents typical user of application.
    """
    __tablename__ = 'users'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_oauth = db.Column(db.String(255), nullable=True)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    created = db.Column(db.DateTime, nullable=False,default=datetime.utcnow())
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    status = db.Column(db.Boolean, nullable=False, default=True)
    type = db.Column(db.Integer, nullable=False, default=USER_TYPE_PLAIN)

    def __repr__(self):
        return "<User {0}>".format(self.id)
