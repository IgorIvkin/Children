from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    email = StringField("Email: ", validators=[Email(), DataRequired()], render_kw={"placeholder": "Введите свой email"})
    title = StringField("Имя: ", render_kw={"placeholder": "Придумайте имя"})
    password = PasswordField("Пароль: ", validators=[DataRequired()], render_kw={"placeholder": "Придумайте пароль"})

    submit = SubmitField("Зарегистрироваться")
