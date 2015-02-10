from flask import Blueprint, render_template

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


@mod.route('/browsetickets/')
def tutbrowsetickets():
    return render_template("tutorials/tbrowset.html", title="Tutorial - Browsing Tickets")