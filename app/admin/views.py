from .decorators import admin_required
from .forms import *
from app import app, db
from app.tickets.models import Os
from flask import abort, Blueprint, flash, Markup, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import generate_password_hash

mod = Blueprint('admin', __name__, url_prefix="/admin")


@mod.route('/edithp/', methods=['GET', 'POST'])
@admin_required
def edithp():
    return "This feature is not implemented yet."


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
        flash(Markup("The <b>%s</b> Operating System has been added to the database." % form.osname.data), app.config["ALERT_CATEGORIES"]["SUCCESS"])
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
            flash("This OS is not on the database.", app.config["ALERT_CATEGORIES"]["ERROR"])
            return redirect(url_for("home"))
        os.enabled = False
        db.session.commit()
        flash(Markup("Operating system <b>%s</b> has been removed." % form.osname.data), app.config["ALERT_CATEGORIES"]["SUCCESS"])
        return redirect(url_for("home"))
    return render_template("admin/removeos.html", form=form, title="Remove an Operating System")


@mod.route('/graduate/', methods=['GET', 'POST'])
@admin_required
def graduate():
    return "This feature is not implemented yet."


@mod.route('/resetpwd/', methods=['GET', 'POST'])
@admin_required
def resetpwd():
    return "This feature is not implemented yet."