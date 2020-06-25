"""
Author: Igor
Date: 2020.06.23
"""

from flask import Blueprint, current_app, request, redirect
from config.security.admin_required import admin_required
from views.admin_html_view import AdminHtmlView
from forms.phones_form import PhonesForm
from services.phone_service import PhoneService
from services.city_service import CityService
from models.phone import Phone

admin_phone_controller = Blueprint("admin_phone_controller", __name__)


@admin_phone_controller.route('/', methods=['post', 'get'])
@admin_required
def render_main_page():
    phone_service = PhoneService(current_app)
    city_service = CityService(current_app)

    phone_form = PhonesForm()
    phone_form.city.choices = [(row.id, row.title) for row in city_service.get_all()]

    phone = Phone()

    if request.method == 'POST' and phone_form.validate_on_submit():
        phone.id_city = phone_form.city.data
        phone.phone = phone_form.phone.data
        phone.other_phones = phone_form.other_phones.data
        phone.description = phone_form.description.data
        phone_service.create(phone)
    return (AdminHtmlView("admin/main_blocks/main_template.html")
            .set_title('Администраторский интерфейс &mdash; Добавление телефонов')
            .set_content('admin/phones_page/phones.html')
            .render(form=phone_form))


@admin_phone_controller.route('/edit/<id_phone>', methods=['post', 'get'])
@admin_required
def render_edit_page(id_phone):
    phone_service = PhoneService(current_app)
    city_service = CityService(current_app)
    current_phone = phone_service.get_by_id(id_phone)

    phone_form = PhonesForm()
    phone_form.city.choices = [(row.id, row.title) for row in city_service.get_all()]
    phone_form.id_phone.data = current_phone.id
    phone_form.city.data = current_phone.id_city
    phone_form.phone.data = current_phone.phone
    phone_form.other_phones.data = current_phone.other_phones
    phone_form.description.data = current_phone.description

    return (AdminHtmlView("admin/main_blocks/main_template.html")
            .set_title('Администраторский интерфейс &mdash; Редактор телефонов')
            .set_content('admin/phones_page/edit_phone.html')
            .render(form=phone_form))


@admin_phone_controller.route('/edit/do_edit/', methods=['post', 'get'])
@admin_required
def do_edit():
    phone_service = PhoneService(current_app)
    fields_to_update = dict()
    if request.method == 'POST':
        id_phone = request.form.get('id_phone')
        fields_to_update['id_city'] = request.form.get('city')
        fields_to_update['phone'] = request.form.get('phone')
        fields_to_update['other_phones'] = request.form.get('other_phones')
        fields_to_update['description'] = request.form.get('description')
        phone_service.update(id_phone, fields_to_update=fields_to_update)

    return redirect('/admin/phones/edit/' + str(id_phone))
