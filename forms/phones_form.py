from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PhonesForm(FlaskForm):
    id_phone = StringField(render_kw={"hidden": "true"})
    city = SelectField("Город: ", coerce=int, validators=[DataRequired()])
    phone = StringField("Телефон: ", validators=[DataRequired()], render_kw={"placeholder": "Номер телефона"})
    other_phones = StringField("Дополнительный телефон: ", render_kw={"placeholder": "Дополнительный номер"})
    description = TextAreaField("Описание: ", validators=[DataRequired()], render_kw={"placeholder": "Описание"})
    submit = SubmitField("Добавить номер")
    submit_edit = SubmitField('Oбновить')
