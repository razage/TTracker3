from app import app, db
from .decorators import login_required
from flask import Blueprint, flash, Markup, redirect, render_template, request, session, url_for
from .forms import LoginForm, RegisterForm
from .models import Technicians
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

mod = Blueprint('users', __name__, url_prefix="/users")


@mod.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        technician = Technicians.query.filter_by(email=form.email.data).first()
        if technician and check_password_hash(technician.password, form.password.data):
            session['techid'] = technician.email
            session['technician_name'] = technician.full_name
            session['admin'] = technician.admin
            flash(Markup("Welcome <b>%s</b>" % session['technician_name']), app.config["ALERT_CATEGORIES"]['SUCCESS'])
            return redirect(url_for("home"))
        flash("Incorrect email or password.", app.config["ALERT_CATEGORIES"]['ERROR'])
    return render_template("users/login.html", form=form, title="Login", page="login")


@mod.route('/logout/')
@login_required
def logout():
    session.pop('techid', None)
    session.pop('technician_name', None)
    session.pop('admin', None)
    flash("You have successfully logged out.", app.config["ALERT_CATEGORIES"]['SUCCESS'])
    return redirect(url_for("home"))


@mod.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        technician = Technicians(form.email.data.lower(), form.firstname.data, form.lastname.data, form.password.data)
        try:
            db.session.add(technician)
            db.session.commit()
        except IntegrityError:
            flash("This email is already in use.", app.config["ALERT_CATEGORIES"]['ERROR'])
            return redirect(url_for("users.register"))
        flash(Markup("Welcome to the team <b>%s %s</b>" % (form.firstname.data, form.lastname.data)), app.config["ALERT_CATEGORIES"]['SUCCESS'])
        return redirect(url_for("home"))
    return render_template("users/register.html", form=form, title="Register", page="register")


