from app.constants import STATUSES
from flask_wtf import Form
from wtforms import DateField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Optional


class TicketSubmitForm(Form):
    received = DateField('Received', [DataRequired()], format="%Y-%m-%d")
    returned = DateField('Returned', [Optional()], format="%Y-%m-%d")

    os = SelectField('Operating System')
    status = SelectField('Ticket Status', choices=[(idx, val) for idx, val in enumerate(STATUSES)], coerce=int)

    cname = StringField('Customer Name', [Optional()])
    cphone = StringField('Customer Phone Number', [Optional()])
    cemail = StringField('Customer Email Address', [Optional()])

    problem = TextAreaField("Problem", [Optional()])
    workdone = TextAreaField("Work Done", [Optional()])