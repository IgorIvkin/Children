"""
Author: Igor
Date: 2020.05.22
"""

from flask import Blueprint
from views.base_view import HTMLView

main_controller = Blueprint("main_controller", __name__)


@main_controller.route('/')
def render_main_page():
    return (HTMLView("main_blocks/main_template.html")
            .set_title('Главная страница')
            .set_header('main_blocks/main_header.html')
            .add_js('/js/test.js')
            .render())
