"""
Author: Igor
Date: 2020.06.17
"""

from children import create_app
from models.phone import Phone
from models.city import City
from services.phone_service import PhoneService
from services.city_service import CityService
import pytest


@pytest.fixture(scope='module')
def app():
    app = create_app(test_mode=True)
    yield app
    with app.app_context():
        phone_service = PhoneService(app)
        phone_service.delete_all()


def create_testing_city(app):
    with app.app_context():
        city_service = CityService(app)
        city = City()
        city.title = 'Пенза'
        city.title_with_preposition = 'в Пензе'
        city.region = 'Пензенская область'
        city.country = 'RU'
        created_city = city_service.create(city)
        return created_city.id


def test_get_phones(app):
    id_city = create_testing_city(app)
    assert id_city is not None

    with app.app_context():
        phone_service = PhoneService(app)
        phone = Phone()
        phone.id_city = id_city
        phone.phone = '+7-922-355-55-55'
        phone.description = 'Тестовый телефон'
        created_phone = phone_service.create(phone)
        assert created_phone.id is not None
        id_phone = created_phone.id

        # first check with default params of pagination, must be one telephone
        phones = phone_service.get_by_id_city(id_city)
        assert len(phones) == 1
        assert int(phones[0].id) == int(id_phone)
        # test lazy loading of city and check its title
        assert phones[0].city.title == 'Пенза'

        # now attempt to get second page of phones, should be empty
        phones2 = phone_service.get_by_id_city(id_city, page=2)
        assert len(phones2) == 0
