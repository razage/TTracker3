from app import db
from app.constants import ALERT_CATEGORIES
from app.users.decorators import login_required
from .forms import TicketSubmitForm
from .models import Os
from flask import Blueprint, flash, redirect, render_template, request, session, url_for

mod = Blueprint('tickets', __name__, url_prefix="/tickets")


@mod.route('/')
@login_required
def ticketindex():
    pass


@mod.route('/search/', methods=["GET", "POST"])
@login_required
def search():
    pass


@mod.route('/submit/', methods=["GET", "POST"])
@login_required
def submitticket():
    form = TicketSubmitForm(request.form)
    form.os.choices = [(o.oid, o.osname) for o in db.session.query(Os).order_by(Os.osname).all()]
    if form.validate_on_submit():
        pass
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash("%s: %s" % (getattr(form, field).label.text, error), ALERT_CATEGORIES['ERROR'])
    return render_template("tickets/submit.html", form=form, title="Submit a Ticket", page="submit")