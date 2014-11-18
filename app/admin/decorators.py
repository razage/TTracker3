from flask import flash, redirect, session, url_for
from functools import wraps
from app.constants import ALERT_CATEGORIES


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' in session and not session['admin']:
            flash("Only administrators can view this page.", ALERT_CATEGORIES['ERROR'])
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return decorated_function