"""
Author: Lena
Date: 2020.06.20
"""


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length


class PhoneCreationForm(FlaskForm):
    id_city = SelectField("Город: ", coerce=int, validators=[DataRequired()])
    phone = StringField("Телефон: ",
                        validators=[DataRequired(), Length(min=2, max=255, message='Недопустимая длина номера телефона')],
                        render_kw={"placeholder": "Номер телефона"})
    other_phones = StringField("Дополнительный телефон: ", render_kw={"placeholder": "Дополнительный номер"})
    description = TextAreaField("Описание: ", validators=[DataRequired()], render_kw={"placeholder": "Описание"})

    submit = SubmitField('Добавить номер')


class PhoneUpdateForm(PhoneCreationForm):
    id_phone = StringField(validators=[DataRequired()], render_kw={'hidden': 'true'})
    submit_edit = SubmitField('Обновить')
