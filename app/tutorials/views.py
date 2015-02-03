from flask import Blueprint, render_template

from app.admin.decorators import admin_required

mod = Blueprint("tutorials", __name__, url_prefix="/tutorials")


@mod.route("/")
def tutorialindex():
    return render_template("tutorials/tindex.html", title="Tutorial Index")


@mod.route('/register/')
def tutregister():
    return render_template("tutorials/tregister.html", title="Tutorial - Registration")


@mod.route('/login/')
def tutlogin():
    return render_template("tutorials/tlogin.html", title="Tutorial - Logging In")
