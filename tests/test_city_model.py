"""
Author: Igor
Date: 2020.06.07
"""

from children import create_app
from models.city import City
from services.city_service import CityService
from exceptions.model_exceptions import ColumnValidationError
import pytest


@pytest.fixture(scope='module')
def app():
    app = create_app(test_mode=True)
    yield app
    with app.app_context():
        city_service = CityService(app)
        city_service.delete_all()


def test_city_get_with_title_part(app):
    with app.app_context():
        city_service = CityService(app)
        city = City()
        city.title = 'Пенза'
        city.region = 'Пензенская область'
        city.country = 'RU'
        city_service.create(city)

        cities_like_penza = city_service.get_by_title_like('Пенз')
        assert len(cities_like_penza) > 0

        cities_like_penza = city_service.get_by_title_like('пенз')
        assert len(cities_like_penza) > 0

        cities_like_zarechny = city_service.get_by_title_like('Заречный')
        assert len(cities_like_zarechny) == 0




