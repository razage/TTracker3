from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template("home.html", title="TicketTracker3", page="home")

from app.users.views import users

app.register_blueprint(users)