from calendar import monthrange
from datetime import date

from flask import abort, Blueprint, flash, Markup, redirect, render_template, request, session, url_for
from sqlalchemy.orm.exc import NoResultFound

from app import app, db
from app.users.decorators import login_required
from .forms import TicketSubmitForm
from .models import Os, Tickets


mod = Blueprint('tickets', __name__, url_prefix="/tickets")

@mod.route('/')
@login_required
def redirtindex():
    return redirect(url_for('ticketindex', page=1))


@mod.route('/<int:page>/')
@login_required
def ticketindex(page):
    totalpages = int(db.session.query(Tickets).count() / app.config['TICKETSPERPAGE'])
    if totalpages is 0:
        totalpages = 1
    tickets = db.session.query(Tickets).limit(app.config['TICKETSPERPAGE']).offset(
        app.config['TICKETSPERPAGE'] * (page - 1))
    return render_template("tickets/ticketlist.html", title="Browse Tickets", tickets=tickets, cpage=page,
                           maxpage=totalpages)


@mod.route('/view/<int:tid>/')
@login_required
def viewticket(tid):
    try:
        ticket = db.session.query(Tickets).filter(Tickets.tid == tid).one()
    except NoResultFound:
        abort(404)
    return render_template("tickets/viewticket.html", title="Ticket #%s" % tid, ticket=ticket, tid=tid)


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
        data = [form.received.data, (None if form.returned.data == '' else form.returned.data), (None if form.status.data is 0 else session['technician_name']), form.status.data, form.os.data, (None if form.cname.data == '' else form.cname.data), (None if form.cphone.data == '' else form.cphone.data), (None if form.cemail.data == '' else form.cemail.data), (None if form.problem.data == '' else form.problem.data), (None if form.workdone.data == '' else form.workdone.data)]
        for i in range(len(data)):
            if data[i] is '':
                data[i] = None
        db.session.add(Tickets(*data))
        db.session.commit()
        flash("Your ticket has been added to the database!", app.config["ALERT_CATEGORIES"]['SUCCESS'])
        return redirect(url_for('tickets.ticketindex', page=1))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(Markup("<b>%s:</b> %s" % (getattr(form, field).label.text, error)),
                      app.config["ALERT_CATEGORIES"]['ERROR'])
    return render_template("tickets/submit.html", form=form, title="Submit a Ticket", page="tickets")


@mod.route('/edit/<int:tid>/', methods=["GET", "POST"])
@login_required
def editticket(tid):
    form = TicketSubmitForm(request.form)
    form.os.choices = [(o.osname, o.osname) for o in db.session.query(Os).filter(Os.enabled).order_by(Os.osname).all()]
    try:
        ticket = db.session.query(Tickets).filter(Tickets.tid == tid).one()
    except NoResultFound:
        flash("The ticket requested does not exist.", app.config["ALERT_CATEGORIES"]["ERROR"])
    if session['technician_name'] != ticket.technician:
        if not session['admin']:
            flash("You do not have permission to edit this ticket.", app.config["ALERT_CATEGORIES"]["ERROR"])
            return redirect(url_for('home'))
    if form.validate_on_submit():
        ticket.recieved = form.received.data
        ticket.returned = (None if form.returned.data == '' else form.returned.data)
        ticket.status = form.status.data
        if session['admin']:
            ticket.technician = (None if form.status.data == 0 else ticket.technician)
        else:
            ticket.technician = (None if form.status.data == 0 else session['technician_name'])
        ticket.os = form.os.data
        ticket.cname = (None if form.cname.data == '' else form.cname.data)
        ticket.cphone = (None if form.cphone.data == '' else form.cphone.data)
        ticket.cemail = (None if form.cemail.data == '' else form.cemail.data)
        ticket.problem = (None if form.problem.data == '' else form.problem.data)
        ticket.workdone = (None if form.workdone.data == '' else form.workdone.data)
        db.session.commit()
        flash(Markup("<b>Success!</b> Ticket #%s has been edited." % tid), app.config["ALERT_CATEGORIES"]["SUCCESS"])
        return redirect(url_for("tickets.viewticket", tid=tid))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(Markup("<b>%s:</b> %s" % (getattr(form, field).label.text, error)),
                      app.config["ALERT_CATEGORIES"]['ERROR'])
    form.os.data = ticket.os
    form.status.data = ticket.status
    form.problem.data = ticket.problem
    form.workdone.data = ticket.workdone
    return render_template("tickets/edit.html", form=form, title="Edit Ticket #%s" % tid, page="tickets", ticket=ticket)


@mod.route('/<semester>/<int:year>/')
@login_required
def semesterview(semester, year):
    semester = semester.lower()
    if semester not in app.config["SEMESTERS"]:
        abort(404)
    else:
        tickets = db.session.query(Tickets).filter(
            Tickets.received >= date(year, app.config["SEMESTERS"][semester][0], 1),
            Tickets.received <= date(year, app.config["SEMESTERS"][semester][5],
                                     monthrange(year, app.config["SEMESTERS"][semester][5])[1])).all()
        return render_template("tickets/semesterview.html", title="Tickets from %s %s" % (semester, year),
                               tickets=tickets)