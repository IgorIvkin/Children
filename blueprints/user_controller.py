"""
Author: Igor
Date: 2020.06.07
"""

from flask import Blueprint, render_template

user_controller = Blueprint("user_controller", __name__)


@user_controller.route('/user/register/')
def render_register_page():
    return render_template("mainpage/mainpage.html")


@user_controller.route('/user/login/')
def render_login_page():
    return render_template("mainpage/mainpage.html")
