"""
Author: Igor
Date: 2020.05.28
"""

from children import db


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)

    def __repr__(self):
        return "<User {0}>".format(self.id)
