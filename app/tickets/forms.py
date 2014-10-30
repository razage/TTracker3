from flask_wtf import Form
from wtforms import BooleanField, DateField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired


class TicketSubmitForm(Form):
    takeownership = BooleanField('Take Ownership of this Ticket')
    received = DateField('Received', [DataRequired()])
    returned = DateField('Returned')

    os = SelectField('Operating System', choices=[])
    status = SelectField('Ticket Status', choices=[(1, "Repairing"), (2, "Awaiting Customer Pickup"), (3, "Complete")], coerce=int)

    cname = StringField('Customer Name')
    cphone = StringField('Customer Phone Number')
    cemail = StringField('Customer Email Address')

    problem = TextAreaField("Problem")
    workdone = TextAreaField("Work Done")