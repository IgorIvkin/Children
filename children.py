"""
Authors: Igor, Elena
Date: 2020.05.22
"""

from flask import Flask, render_template
from config.application_setup import ApplicationSetup
from blueprints.main_controller import main_controller

app = Flask(__name__)
app.config.from_object(ApplicationSetup(app).get_config())
app.register_blueprint(main_controller)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 404
