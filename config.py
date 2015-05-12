from datetime import datetime
from json import dump, load
from os.path import abspath, dirname, join
from random import SystemRandom

_basedir = abspath(dirname(__file__))
try:
    secrets = load(open(join(_basedir, 'secrets.json')))
except IOError:
    flask_key = ''.join([SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    secrets = {"flask_key": flask_key, "db_ip": "localhost", "db_port": 3306, "db_user": "", "db_password": "", "db_db": ""}
    dump(secrets, open(join(_basedir, 'secrets.json'), 'w'))

SECRET_KEY = secrets['flask_key']

SQLALCHEMY_DATABASE_URI = "sqlite:///" + join(_basedir, 'app.db')

# These configurations are used for my own purposes
ALERT_CATEGORIES = {"SUCCESS": "success", "INFO": "info", "ERROR": "danger"}

SITE_VERSION = "1.0.0rc1"

FIRST_YEAR = 2012
CUR_YEAR = datetime.now().year
SEMESTERS = {'fall': (7, 8, 9, 10, 11, 12), 'spring': (1, 2, 3, 4, 5, 6)}

STATUSES = ("Unclaimed", "Repairing", "Waiting", "Complete")

TICKETSPERPAGE = 20