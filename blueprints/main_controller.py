"""
Author: Igor
Date: 2020.05.22
"""

from flask import Blueprint
from views.web_site_html_view import WebSiteHtmlView

main_controller = Blueprint("main_controller", __name__)


@main_controller.route('/')
def render_main_page():
    return (WebSiteHtmlView('main_blocks/main_template.html')
            .set_title('Папомамер &mdash; Главная страница')
            .set_content('main_page/main_page.html')
            .render())
