from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    name = StringField('Product Name', validators=[
                       DataRequired(), Length(min=2, max=30)])
    category = SelectField('Category', [DataRequired()],
                        choices=[('Beverages','Beverages'),('Bread/Bakery','Bread/Bakery'),('Vegetables','Vegetables'),('Dairy','Dairy'),('Dry/Baking Goods','Dry/Baking Goods'),('Meat','Meat'),('Fruits','Fruits'),('Cleaners', 'Cleaners'),('Paper Goods','Paper Goods'),('Personal Care','Personal Care'),('Other','Other')])

    quantity = SelectField('Quantity', [DataRequired()],
                        choices=[('1', '1'),
                                 ('2', '2'),
                                 ('3', '3'),
                                 ('4', '4'),
                                 ('5', '5'),
                                 ('6', '6')])
    
    submit = SubmitField('Add product')

