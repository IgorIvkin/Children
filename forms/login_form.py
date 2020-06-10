from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from forms.validators.email import email


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[email()])
    password = PasswordField("Пароль: ", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня ")
    submit = SubmitField("Авторизоваться")
