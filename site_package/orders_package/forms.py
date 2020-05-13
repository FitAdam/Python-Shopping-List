from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    name = StringField('Product Name', validators=[
                       DataRequired(), Length(min=2, max=30)])
    category = SelectField('Category', [DataRequired()],
                        choices=[('1', '1'),
                                 ('2', '2'),
                                 ('3', '3'),
                                 ('4', '4'),
                                 ('5', '5'),
                                 ('6', '6')])

    quantity = SelectField('Ilość', [DataRequired()],
                        choices=[('1', '1'),
                                 ('2', '2'),
                                 ('3', '3'),
                                 ('4', '4'),
                                 ('5', '5'),
                                 ('6', '6')])
    
    submit = SubmitField('Add product')

