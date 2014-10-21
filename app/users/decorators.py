from flask import flash, redirect, session, url_for
from functools import wraps
from app.constants import ALERT_CATEGORIES

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'technician_name' not in session:
            flash("You need to be signed in to view this page.", ALERT_CATEGORIES['ERROR'])
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return decorated_function
