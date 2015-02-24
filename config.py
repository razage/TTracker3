from os.path import abspath, dirname, join
from datetime import datetime

_basedir = abspath(dirname(__file__))

SECRET_KEY = "Super_sekret"

SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(_basedir, 'app.db')

# These configurations are used for my own purposes
ALERT_CATEGORIES = {"SUCCESS": "success", "INFO": "info", "ERROR": "danger"}

SITE_VERSION = "ALPHA"

FIRST_YEAR = 2012
CUR_YEAR = datetime.now().year
SEMESTERS = {'fall': (7, 8, 9, 10, 11, 12), 'spring': (1, 2, 3, 4, 5, 6)}

STATUSES = ("Unclaimed", "Repairing", "Waiting", "Complete")

TICKETSPERPAGE = 20