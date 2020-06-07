"""
Author: Igor
Date: 2020.06.07
"""

from flask import Blueprint, render_template, request, current_app, redirect
from models.user import User
from services.user_service import UserService
from flask_login import login_user

user_controller = Blueprint("user_controller", __name__)


@user_controller.route('/user/register/', methods=['post', 'get'])
def render_register_page():
    if request.method == 'POST':
        user_service = UserService(current_app)
        user = User()
        user.login = request.form.get('login')
        user.title = request.form.get('title')
        user.password = request.form.get('password')
        user_service.create(user)
        return redirect('/')

    return render_template("user/register.html")


@user_controller.route('/user/login/', methods=['post', 'get'])
def render_login_page():
    if request.method == 'POST':
        user_service = UserService(current_app)
        login = request.form.get('login')
        password = request.form.get('password')
        remember = request.form.get('remember')
        if remember is None:
            remember = False
        registered_user = user_service.get_by_login(login)
        if registered_user is not None:
            if user_service.check_password_hash(registered_user.password, password):
                login_user(registered_user, remember=remember)
                return redirect('/')

    return render_template("user/login.html")
