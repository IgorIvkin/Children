"""
Author: Igor
Date: 2020.06.17
"""

from children import db
from models.city import City
from exceptions.model_exceptions import ColumnValidationError
from sqlalchemy.orm import validates


class Phone(db.Model):
    """
    Represents an useful phone number with its description
    and additional phone numbers.
    """
    __tablename__ = 'phones'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    # Yes, we need an index here, we use PostgreSQL as our back-end and PG does not
    # create an index just for foreign keys, it creates the indices just for primary keys and
    # unique constraints
    id_city = db.Column(db.BigInteger, db.ForeignKey('cities.id'), nullable=False, index=True)
    # By default it is lazy loading, don't need to be changed for now
    city = db.relationship("City")
    phone = db.Column(db.String(255), index=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    other_phones = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<Phone {0}>".format(self.id)

    @validates('phone')
    def validate_phone(self, key, phone):
        if len(phone) < 2:
            raise ColumnValidationError('Phone is too short, at least two characters expected: {0}'.format(phone))
        elif len(phone) > 255:
            raise ColumnValidationError('Phone is too long, max 255 characters allowed: {0}'.format(phone))
        return phone

    @validates('description')
    def validate_description(self, key, description):
        if len(description) > 10000:
            raise ColumnValidationError('Phone description is too long, max 10 000 characters allowed')
        return description

    @validates('other_phones')
    def validate_other_phones(self, key, other_phones):
        if len(other_phones) > 10000:
            raise ColumnValidationError('Other phones is too long, max 10 000 characters allowed')
        return other_phones
