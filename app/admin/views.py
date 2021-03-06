from os.path import join

from flask import Blueprint, flash, Markup, redirect, render_template, request, session, url_for
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import generate_password_hash

from .decorators import admin_required
from .forms import *
from app import app, db
from app.tickets.models import Os
from app.users.models import Technicians


mod = Blueprint('admin', __name__, url_prefix="/admin")


@mod.route('/edithp/', methods=['GET', 'POST'])
@admin_required
def edithp():
    file = join('app', 'static', 'home.txt')
    form = EditHomepageForm(request.form)
    if form.validate_on_submit():
        f = open(file, 'w')
        f.write(form.bodytext.data)
        f.close()
        flash(Markup("<b>Success!</b> The homepage has been updated."), app.config['ALERT_CATEGORIES']['SUCCESS'])
        return redirect(url_for('home'))
    try:
        chp = open(file, 'r').read()
    except FileNotFoundError:
        chp = "Home.txt does not exist."
    form.bodytext.data = chp
    return render_template('admin/edithp.html', form=form, title="Edit Homepage")


@mod.route('/addos/', methods=['GET', 'POST'])
@admin_required
def addos():
    form = AddOSForm(request.form)
    if form.validate_on_submit():
        db.session.add(Os(form.osname.data))
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            os = db.session.query(Os).filter(Os.osname == form.osname.data).one()
            if not os.enabled:
                os.enabled = True
                db.session.commit()
        flash(Markup("The <b>%s</b> Operating System has been added to the database." % form.osname.data),
              app.config["ALERT_CATEGORIES"]["SUCCESS"])
        return redirect(url_for("home"))
    return render_template("admin/addos.html", form=form, title="Add an Operating System")


@mod.route('/remos/', methods=['GET', 'POST'])
@admin_required
def removeos():
    form = RemoveOSForm(request.form)
    form.osname.choices = [(o.osname, o.osname) for o in db.session.query(Os).order_by(Os.osname).all()]
    if form.validate_on_submit():
        try:
            os = db.session.query(Os).filter(Os.osname == form.osname.data).one()
        except NoResultFound():
            flash("This OS is not in the database.", app.config["ALERT_CATEGORIES"]["ERROR"])
            return redirect(url_for("home"))
        os.enabled = False
        db.session.commit()
        flash(Markup("Operating system <b>%s</b> has been removed." % form.osname.data),
              app.config["ALERT_CATEGORIES"]["SUCCESS"])
        return redirect(url_for("home"))
    return render_template("admin/removeos.html", form=form, title="Remove an Operating System")


@mod.route('/graduate/', methods=['GET', 'POST'])
@admin_required
def graduate():
    form = GraduateForm(request.form)
    form.techname.choices = [(u.full_name, u.full_name) for u in
                             db.session.query(Technicians).filter(Technicians.enrolled,
                                                                  Technicians.full_name != session[
                                                                      'technician_name']).order_by(
                                 Technicians.full_name)]
    if form.validate_on_submit():
        try:
            tech = db.session.query(Technicians).filter(Technicians.full_name == form.techname.data).one()
        except NoResultFound():
            flash("This user is not in the database.", app.config["ALERT_CATEGORIES"]["ERROR"])
            return redirect(url_for("home"))
        tech.enrolled = False
        db.session.commit()
        flash(Markup("Technician <b>%s</b> has been graduated." % form.techname.data),
              app.config["ALERT_CATEGORIES"]["SUCCESS"])
        return redirect(url_for("home"))
    return render_template("admin/graduate.html", form=form, title="Graduate a Technician")


@mod.route('/resetpwd/', methods=['GET', 'POST'])
@admin_required
def resetpwd():
    form = ResetTechPasswordForm(request.form)
    form.techname.choices = [(u.full_name, u.full_name) for u in
                             db.session.query(Technicians).filter(Technicians.enrolled,
                                                                  Technicians.full_name != session[
                                                                      'technician_name']).order_by(
                                 Technicians.full_name)]
    if form.validate_on_submit():
        tech = db.session.query(Technicians).filter(Technicians.full_name == form.techname.data).one()
        tech.password = generate_password_hash(form.password.data)
        db.session.commit()
        flash(Markup("User <b>%s's</b> password has been updated." % form.techname.data),
              app.config["ALERT_CATEGORIES"]["SUCCESS"])
        return redirect(url_for("home"))
    return render_template("admin/reset.html", form=form, title="Reset Technician's Password")


@mod.route('/semesterviews/')
@admin_required
def semesterviewindex():
    year = app.config["FIRST_YEAR"]
    years = []
    while year <= app.config["CUR_YEAR"]:
        years.append(year)
        year += 1
    return render_template("admin/semesterindex.html", title="Semester Index")