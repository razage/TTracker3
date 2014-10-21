from os.path import abspath, dirname, join

_basedir = abspath(dirname(__file__))

SECRET_KEY = "Super_sekret"

SQLALCHEMY_DATABASE_URI = "sqlite:///"+join(_basedir, 'app.db')

CSRF_ENABLED = True
CSRF_SESSION_KEY = "Such_secure_much_safe_wow"


