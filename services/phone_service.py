"""
Author: Igor
Date: 2020.06.17
"""

from services.base_service import BaseService
from models.phone import Phone


class PhoneService(BaseService):
    """
    Provides basic methods to operate the phones.
    """

    def __init__(self, app):
        self.base_class = Phone
        super().__init__(app)

    def get_by_id_city(self, id_city, page=1, phones_per_page=50):
        """
        Returns the phones by defined city with possible pagination.
        By default the first page with first 50 results is assumed.
        """
        phones = (self.base_class.query
                  .filter_by(id_city=id_city)
                  .paginate(page=page, per_page=phones_per_page, error_out=False))
        return phones.items
