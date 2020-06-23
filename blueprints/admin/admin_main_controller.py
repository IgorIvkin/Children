"""
Author: Igor
Date: 2020.06.07
"""

from flask import Blueprint, current_app, request
from config.security.admin_required import admin_required
from views.admin_html_view import AdminHtmlView
from forms.phones_form import PhonesForm
from services.phone_service import PhoneService
from services.city_service import CityService
from models.phone import Phone

admin_main_controller = Blueprint("admin_main_controller", __name__)


@admin_main_controller.route('/')
@admin_required
def render_main_page():
    return (AdminHtmlView("admin/main_blocks/main_template.html")
            .set_title('Администраторский интерфейс &mdash; Главная страница')
            .set_content('admin/main_page/main_page.html')
            .render())


@admin_main_controller.route('/phones/', methods=['post', 'get'])
def render_main_page():
    phone_service = PhoneService(current_app)
    city_service = CityService(current_app)

    phone_form = PhonesForm()
    phone_form.city.choices = [(row.id, row.title) for row in city_service.get_all()]

    phone = Phone()

    if request.method == 'POST' and phone_form.validate_on_submit():
        phone.id_city = phone_form.city.data
        phone.phone = phone_form.phone.data
        phone.other_phones = phone_form.other_phone.data
        phone.description = phone_form.description.data
        phone_service.create(phone)
    return (AdminHtmlView("admin/main_blocks/main_template.html")
            .set_title('Администраторский интерфейс &mdash; Редактор телефонов')
            .set_content('admin/phones_page/phones.html')
            .render(form=phone_form))

