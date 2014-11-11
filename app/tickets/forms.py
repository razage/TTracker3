from flask_wtf import Form
from wtforms import BooleanField, DateField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired, Optional


class TicketSubmitForm(Form):
    received = DateField('Received', [DataRequired()])
    returned = DateField('Returned', [Optional()])

    os = SelectField('Operating System', coerce=int)
    status = SelectField('Ticket Status', choices=[(0, "Unclaimed"), (1, "Repairing"), (2, "Awaiting Customer Pickup"), (3, "Complete")], coerce=int)

    cname = StringField('Customer Name')
    cphone = StringField('Customer Phone Number')
    cemail = StringField('Customer Email Address')

    problem = TextAreaField("Problem")
    workdone = TextAreaField("Work Done")