from app import app
from flask import flash, redirect, session, url_for
from functools import wraps


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' in session and not session['admin']:
            flash("Only administrators can view this page.", app.config["STATUSES"]['ERROR'])
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return decorated_function