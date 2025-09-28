import itertools

from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired


class RecordForm(FlaskForm):
    subject = StringField(
        'Subject',
        validators=[DataRequired()], 
        render_kw={"placeholder": "Enter subject"}
    )
    teacher = StringField(
        'Teacher',
        validators=[DataRequired()], 
        render_kw={"placeholder": "Enter teacher's name"}
    )
    grade = IntegerField(
        'Grade', 
        validators=[DataRequired()],
        render_kw={"placeholder": "Enter grade"}
    )
    date = StringField(
        'Date',
        validators=[DataRequired()],
        default=datetime.now().strftime("%Y-%m-%d")
    )
    submit = SubmitField('Save Grade')
