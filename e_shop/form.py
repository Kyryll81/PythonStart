from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name: StringField = StringField('Name', validators=[DataRequired()])
    price: FloatField = FloatField('Price', validators=[DataRequired()])
    stock: IntegerField = IntegerField('Stock', validators=[DataRequired()])
    submit: SubmitField = SubmitField('Save')