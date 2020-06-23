"""
Author: Igor
Date: 2020.06.07
"""

from flask import Blueprint
from config.security.admin_required import admin_required
from views.admin_html_view import AdminHtmlView

admin_main_controller = Blueprint("admin_main_controller", __name__)


@admin_main_controller.route('/')
@admin_required
def render_main_page():
    return (AdminHtmlView("admin/main_blocks/main_template.html")
            .set_title('Администраторский интерфейс &mdash; Главная страница')
            .set_content('admin/main_page/main_page.html')
            .render())
