from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp


class ContactForm(FlaskForm):
    name: StringField = StringField('Name', validators=[DataRequired()], 
                                    render_kw={'placeholder': 'Enter your name'})
    phone: StringField = StringField('Phone', 
                                     validators=[DataRequired(),
                                                 Regexp(r'^\+\d{10,15}$', message='Invalid phone number format.') # regex: phone number],
                                                ], 
                                     render_kw={'placeholder': 'Enter your phone number'})
    email: StringField = StringField('Email', validators=[DataRequired(), Email()], 
                                     render_kw={'placeholder': 'Enter your email'})
    submit: SubmitField = SubmitField('Submit')