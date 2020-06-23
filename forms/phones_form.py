from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PhoneForm(FlaskForm):

    city = SelectField("Город: ", validators=[DataRequired()])
    phone = StringField("Телефон: ", validators=[DataRequired()], render_kw={"placeholder": "Номер телефона"})
    other_phone = StringField("Дополнительный телефон: ", render_kw={"placeholder": "Дополнительный номер"})
    description = TextAreaField("Описание: ", validators=[DataRequired()], render_kw={"placeholder": "Описание"})
    submit = SubmitField("Добавить номер")

