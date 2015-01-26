from os.path import abspath, dirname, join

_basedir = abspath(dirname(__file__))

SECRET_KEY = "Super_sekret"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(_basedir, 'app.db')

# These configurations are used for my own purposes
ALERT_CATEGORIES = {"SUCCESS": "success", "INFO": "info", "ERROR": "danger"}
SITE_VERSION = "ALPHA"
STATUSES = ("Unclaimed", "Repairing", "Waiting", "Complete")


