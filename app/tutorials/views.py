from flask import Blueprint

mod = Blueprint("tutorials", __name__, url_prefix="/tutorials")


@mod.route("/")
def tutorialindex():
    return "This feature is not implemented yet."
