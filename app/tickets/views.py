from app import db
from app.constants import ALERT_CATEGORIES
from app.users.decorators import login_required
from .forms import TicketSubmitForm
from .models import Os, Tickets
from flask import abort, Blueprint, flash, Markup, redirect, render_template, request, session, url_for
from sqlalchemy.orm.exc import NoResultFound

mod = Blueprint('tickets', __name__, url_prefix="/tickets")


@mod.route('/')
@login_required
def ticketindex():
    tickets = db.session.query(Tickets).all()
    return render_template("tickets/ticketlist.html", title="Browse Tickets", tickets=tickets)


@mod.route('/view/<int:tid>/')
@login_required
def viewticket(tid):
    try:
        ticket = db.session.query(Tickets).filter(Tickets.tid == tid).one()
    except NoResultFound:
        abort(404)
    return render_template("tickets/viewticket.html", title="Ticket #"+str(tid), ticket=ticket)


@mod.route('/search/', methods=["GET", "POST"])
@login_required
def search():
    return "This feature is not implemented yet."


@mod.route('/submit/', methods=["GET", "POST"])
@login_required
def submitticket():
    form = TicketSubmitForm(request.form)
    form.os.choices = [(o.osname, o.osname) for o in db.session.query(Os).filter(Os.enabled).order_by(Os.osname).all()]
    if form.validate_on_submit():
        data = [form.received.data, form.returned.data, (None if form.status.data is 0 else session['technician_name']),
                form.status.data, form.os.data, form.cname.data, form.cphone.data, form.cemail.data, form.problem.data,
                form.workdone.data]
        for i in range(len(data)):
            if data[i] is '':
                data[i] = None
        db.session.add(Tickets(*data))
        db.session.commit()
        flash("Your ticket has been added to the database!", ALERT_CATEGORIES['SUCCESS'])
        return redirect(url_for("home"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(Markup("<b>%s:</b> %s" % (getattr(form, field).label.text, error)), ALERT_CATEGORIES['ERROR'])
    return render_template("tickets/submit.html", form=form, title="Submit a Ticket", page="tickets")