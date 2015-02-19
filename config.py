from os.path import abspath, dirname, join
from datetime import datetime

_basedir = abspath(dirname(__file__))

SECRET_KEY = "Super_sekret"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(_basedir, 'app.db')

# These configurations are used for my own purposes
ALERT_CATEGORIES = {"SUCCESS": "success", "INFO": "info", "ERROR": "danger"}

SITE_VERSION = "ALPHA"

CUR_YEAR = datetime.now().year
SEMESTERS = {'Fall': (8, 9, 10, 11, 12), 'Spring': (1, 2, 3, 4, 5)}

STATUSES = ("Unclaimed", "Repairing", "Waiting", "Complete")

TICKETSPERPAGE = 20