"""
Author: Igor
Date: 2020.05.22
"""

from flask import Blueprint, render_template
from children import log

main_controller = Blueprint("main_controller", __name__)


@main_controller.route('/')
def render_main_page():
    log.warn('test')
    log.error('test error')
    log.debug('test debug')
    log.info('test info')
    return render_template("mainpage/mainpage.html")
