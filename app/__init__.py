from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from os.path import join

from app.customfilters import statusname


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def home():
    f = open(join(app.root_path, 'static', 'home.txt'), 'r').read()
    return render_template("home.html", title="TicketTracker3", page="home", text=f)


@app.route('/about/')
def about():
    return render_template("about.html", title="About", page="about")


from app.admin.views import mod as adminmod
from app.tickets.views import mod as ticketmod
from app.tutorials.views import mod as tutorialmod
from app.users.views import mod as usermod

app.register_blueprint(adminmod)
app.register_blueprint(ticketmod)
app.register_blueprint(tutorialmod)
app.register_blueprint(usermod)

app.jinja_env.filters['statusname'] = statusname