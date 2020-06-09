"""
Author: Igor
Date: 2020.06.07
"""

from children import db
from exceptions.model_exceptions import ColumnValidationError
from sqlalchemy.orm import validates


class City(db.Model):
    """
    Represents a city (town, village) where all the other data is stored.
    """
    __tablename__ = 'cities'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(2), index=True, nullable=False, default="RU")
    region = db.Column(db.String(255), index=True, nullable=False)

    def __repr__(self):
        return "<City {0}>".format(self.id)

    @validates('title')
    def validate_title(self, key, title):
        if len(title) < 2:
            raise ColumnValidationError('City title is too short, at least two characters expected: {0}'.format(title))
        elif len(title) > 255:
            raise ColumnValidationError('City title is too long, max 255 characters allowed: {0}'.format(title))
        return title

    @validates('country')
    def validate_country(self, key, country):
        if len(country) != 2:
            raise ColumnValidationError('Country code should be in ISO 2-characters format,'
                                        ' for example FR or RU: {0}'.format(country))
        return country

    @validates('region')
    def validate_region(self, key, region):
        if len(region) < 2:
            raise ColumnValidationError('City region is too short, '
                                        'at least two characters expected: {0}'.format(region))
        elif len(region) > 255:
            raise ColumnValidationError('City region is too long, max 255 characters allowed: {0}'.format(region))
        return region
