from flask_wtf import Form
from wtforms import PasswordField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length, Optional


class AddOSForm(Form):
    osname = StringField('Operating System Name', [DataRequired()])


class RemoveOSForm(Form):
    osname = SelectField('Operating System')


class GraduateForm(Form):
    techname = SelectField('Technician')


class ResetTechPasswordForm(Form):
    techname = SelectField('Technician')
    password = PasswordField('New Password', [DataRequired(), Length(min=6, max=30,
                                                                     message="Your password must be within 6-30 characters.")])
    confirm = PasswordField('Confirm New Password', [EqualTo('password', message="Your passwords must match.")])


class EditHomepageForm(Form):
    bodytext = TextAreaField('Edit Homepage', [Optional()])