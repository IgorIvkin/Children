"""
Author: Igor
Date: 2020.06.07
"""

from services.base_service import BaseService
from models.city import City


class CityService(BaseService):
    """This class provides a basic methods to obtain cities."""

    def __init__(self, app):
        self.base_class = City
        super().__init__(app)

    def get_by_title_like(self, title):
        """Returns a cities that are corresponding to title given in the parameter 'title'.
        Take a note that this function searches it in the form of %title% and it is case
        NON-sensitive"""
        filter_to_search = '%{}%'.format(title)
        cities = self.base_class.query.filter(City.title.ilike(filter_to_search)).all()
        return cities

