"""
Author: Igor
Date: 2020.06.07
"""

from flask import Blueprint, render_template, request, current_app, redirect
from models.user import User
from services.user_service import UserService
from flask_login import login_user
from forms.login_form import LoginForm
from forms.register_form import RegisterForm


user_controller = Blueprint("user_controller", __name__)


@user_controller.route('/user/register/', methods=['post', 'get'])
def render_register_page():
    register_form = RegisterForm()
    user_service = UserService(current_app)
    user = User()
    if request.method == 'POST' and register_form.validate_on_submit():
        user.login = register_form.email.data
        user.title = register_form.title.data
        user.password = register_form.password.data

        user_service.create(user)
        return redirect('/')

    return render_template("user/register.html", form=register_form)


@user_controller.route('/user/login/', methods=['post', 'get'])
def render_login_page():
    login_form = LoginForm()
    if request.method == 'POST' and login_form.validate_on_submit():
        login = login_form.email.data
        password = login_form.password.data
        remember = login_form.remember.data

        user_service = UserService(current_app)
        registered_user = user_service.get_by_login(login)
        if registered_user is not None:
            if user_service.check_password_hash(registered_user.password, password):
                login_user(registered_user, remember=remember)
                return redirect('/')

    return render_template("user/login.html", form=login_form)


