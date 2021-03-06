from app import db


class Os(db.Model):
    __tablename__ = "opsys"
    osname = db.Column(db.String(30), primary_key=True)
    enabled = db.Column(db.Boolean, nullable=False)
    tks = db.relationship("Tickets", backref="opsys")

    def __init__(self, osname, enabled=True):
        self.osname = osname
        self.enabled = enabled


class Tickets(db.Model):
    __tablename__ = "repairs"
    tid = db.Column(db.Integer(), primary_key=True)
    received = db.Column(db.Date(), nullable=False)
    returned = db.Column(db.Date(), default=None)
    technician = db.Column(db.String(30), db.ForeignKey("technicians.full_name"))
    status = db.Column(db.Integer(), nullable=False)
    os = db.Column(db.String(30), db.ForeignKey("opsys.osname"), nullable=False)
    cname = db.Column(db.String(30), default=None)
    cphone = db.Column(db.String(30), default=None)
    cemail = db.Column(db.String(30), default=None)
    problem = db.Column(db.Text(), default=None)
    workdone = db.Column(db.Text(), default=None)

    def __init__(self, received, returned, technician, status, os, cname, cphone, cemail, problem, workdone):
        self.received = received
        self.returned = returned
        self.technician = technician
        self.status = status
        self.os = os
        self.cname = cname
        self.cphone = cphone
        self.cemail = cemail
        self.problem = problem
        self.workdone = workdone