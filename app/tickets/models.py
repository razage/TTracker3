from app import db


class Os(db.Model):
    __tablename__ = "opsys"
    osname = db.Column(db.String(30), primary_key=True)

    def __init__(self, osname):
        self.osname = osname


class Tickets(db.Model):
    __tablename__ = "repairs"
    tid = db.Column(db.Integer(), primary_key=True)
    received = db.Column(db.Timestamp(), nullable=False)
    returned = db.Column(db.Timestamp(), default=None)
    technician = db.Column(db.String(30), default=None)
    technician2 = db.Column(db.String(30), default=None)
    os = db.Column(db.String(30), default=None)
    cname = db.Column(db.String(30), default=None)
    cphone = db.Column(db.String(30), default=None)
    cemail = db.Column(db.String(30), default=None)
    problem = db.Column(db.Text(), default=None)
    workdone = db.Column(db.Text(), default=None)

    def __init__(self, received, returned, technician, technician2, os, cname, cphone, cemail, problem, workdone):
        self.received = received
        self.returned = returned
        self.technician = technician
        self.technician2 = technician2
        self.os = os
        self.cname = cname
        self.cphone = cphone
        self.cemail = cemail
        self.problem = problem
        self.workdone = workdone