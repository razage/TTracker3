from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from app.customfilters import statusname


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template("home.html", title="TicketTracker3", page="home")


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