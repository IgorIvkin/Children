"""
Author: Igor
Date: 2020.06.07
"""

from flask import Blueprint, render_template
from config.security.admin_required import admin_required

admin_main_controller = Blueprint("admin_main_controller", __name__)


@admin_main_controller.route('/')
@admin_required
def render_main_page():
    return render_template("admin/mainpage/mainpage.html")
