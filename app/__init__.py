from app.customfilters import statusname
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template("home.html", title="TicketTracker3", page="home")


from app.tickets.views import mod as ticketmod
from app.users.views import mod as usermod

app.register_blueprint(ticketmod)
app.register_blueprint(usermod)

app.jinja_env.filters['statusname'] = statusname