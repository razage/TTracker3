from functools import wraps

from flask import flash, redirect, session, url_for

from app import app


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'technician_name' not in session:
            flash("You need to be signed in to view this page.", app.config["ALERT_CATEGORIES"]['ERROR'])
            return redirect(url_for("home"))
        return f(*args, **kwargs)

    return decorated_function
