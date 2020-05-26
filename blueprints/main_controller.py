"""
Author: Igor
Date: 2020.05.22
"""

from flask import Blueprint, render_template

main_controller = Blueprint("main_controller", __name__)


@main_controller.route('/')
def render_main_page():
    return render_template("mainpage/mainpage.html")
