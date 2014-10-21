from app import db
from werkzeug.security import generate_password_hash


class Technicians(db.Model):
    __tablename__ = "technicians"
    email = db.Column(db.String(50), primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(65), nullable=False)
    enrolled = db.Column(db.Boolean(), nullable=False)
    admin = db.Column(db.Boolean(), nullable=False)

    def __init__(self, email, f_name, l_name, password, enrolled=True, admin=False):
        self.email = email
        self.f_name = f_name
        self.l_name = l_name
        self.password = generate_password_hash(password)
        self.enrolled = enrolled
        self.admin = admin

    def isAdmin(self):
        return self.admin

    def isEnrolled(self):
        return self.enrolled

    def __repr__(self):
        return '<User %r>' % (self.f_name + ' ' + self.l_name)
