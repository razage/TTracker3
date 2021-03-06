from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(Form):
    email = StringField('Email Address', [DataRequired(), Email(message="Invalid email.")])
    password = PasswordField('Password', [DataRequired()])


class RegisterForm(Form):
    firstname = StringField('First Name', [DataRequired(), Length(min=1, max=30,
                                                                  message="Your first name must be within 2-30 characters.")])
    lastname = StringField('Last Name', [DataRequired(), Length(min=1, max=30,
                                                                message="Your last name must be within 2-30 characters.")])
    email = StringField('Email', [DataRequired(), Email(message="Invalid email.")])
    password = PasswordField('Password', [DataRequired(), Length(min=6, max=30,
                                                                 message="Your password must be within 6-30 characters.")])
    confirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password', message='Passwords must match.')])
