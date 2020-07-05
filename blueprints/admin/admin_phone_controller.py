"""
Authors: Igor, Lena
Date: 2020.06.23
"""

from flask import Blueprint, current_app, request, redirect
from config.security.admin_required import admin_required
from services.phone_service import PhoneService
from services.city_service import CityService
from views.admin_html_view import AdminHtmlView
from models.phone import Phone
from forms.phones_form import PhoneCreationForm, PhoneUpdateForm
from lib.mapping.object_mapping import map_objects

admin_phone_controller = Blueprint("admin_phone_controller", __name__)


@admin_phone_controller.route('/', methods=['post', 'get'])
@admin_required
def render_main_page():
    return (AdminHtmlView("admin/main_blocks/main_template.html")
            .set_title('Администраторский интерфейс &mdash; Добавление телефонов')
            .set_content('admin/phones_page/phones.html')
            .render())


@admin_phone_controller.route('/add/', methods=['post', 'get'])
@admin_required
def render_add_page():
    phone_service = PhoneService(current_app)
    city_service = CityService(current_app)

    phone_form = PhoneCreationForm()
    phone_form.id_city.choices = [(row.id, row.title) for row in city_service.get_all()]
    if request.method == 'POST' and phone_form.validate_on_submit():
        phone = Phone()
        map_objects(source=phone_form, destination=phone, suffix_of_source='data')
        phone_service.create(phone)
        return redirect('/admin/phones/')

    return (AdminHtmlView("admin/main_blocks/main_template.html")
            .set_title('Администраторский интерфейс &mdash; Добавление телефонов')
            .set_content('admin/phones_page/add_phone.html')
            .render(form=phone_form))


@admin_phone_controller.route('/edit/<id_phone>', methods=['post', 'get'])
@admin_required
def render_edit_page(id_phone):
    phone_service = PhoneService(current_app)
    city_service = CityService(current_app)

    current_phone = phone_service.get_by_id(id_phone)
    phone_form = PhoneUpdateForm()

    phone_form.id_phone.data = current_phone.id
    phone_form.id_city.choices = [(row.id, row.title) for row in city_service.get_all()]
    map_objects(source=current_phone, destination=phone_form, suffix_of_destination='data')

    return (AdminHtmlView("admin/main_blocks/main_template.html")
            .set_title('Администраторский интерфейс &mdash; Редактор телефонов')
            .set_content('admin/phones_page/edit_phone.html')
            .render(form=phone_form))


@admin_phone_controller.route('/do_edit/', methods=['post'])
@admin_required
def do_edit():
    city_service = CityService(current_app)
    phone_service = PhoneService(current_app)

    phone_form = PhoneUpdateForm()
    phone_form.id_city.choices = [(row.id, row.title) for row in city_service.get_all()]

    if request.method == 'POST' and phone_form.validate_on_submit():
        fields_to_update = dict()
        id_phone = phone_form.id_phone.data
        map_objects(source=phone_form,
                    destination=fields_to_update,
                    suffix_of_source='data',
                    keys_to_map=('id_city', 'phone', 'other_phones', 'description'))
        phone_service.update(id_phone, fields_to_update=fields_to_update)
        return redirect('/admin/phones/edit/' + str(id_phone))

    # We normally shouldn't be here, it means mostly that it was not a POST-method
    raise ValueError('Unknown method to access was used. POST is expected')
