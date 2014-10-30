from app import db
from app.users.models import Technicians
from app.tickets.models import Os

#Creating the tables
db.create_all()
db.session.commit()

#Predefined users
db.session.add(Technicians("admin@ttracker3.com", "Test", "User", "password", True, True))
db.session.commit()


#Predefined Operating Systems
db.session.add(Os("Debian"))
db.session.add(Os("Fedora"))
db.session.add(Os("OS X 10.0 Cheetah"))
db.session.add(Os("OS X 10.1 Puma"))
db.session.add(Os("OS X 10.2 Jaguar"))
db.session.add(Os("OS X 10.3 Panther"))
db.session.add(Os("OS X 10.4 Tiger"))
db.session.add(Os("OS X 10.5 Leopard"))
db.session.add(Os("OS X 10.6 Snow Leopard"))
db.session.add(Os("OS X 10.7 Lion"))
db.session.add(Os("OS X 10.8 Mountain Lion"))
db.session.add(Os("OS X 10.9 Mavericks"))
db.session.add(Os("OS X 10.10 Yosemite"))
db.session.add(Os("Other"))
db.session.add(Os("Red Hat"))
db.session.add(Os("Ubuntu"))
db.session.add(Os("Windows 7"))
db.session.add(Os("Windows 8"))
db.session.add(Os("Windows 10"))
db.session.add(Os("Windows Vista"))
db.session.add(Os("Windows XP"))
db.session.commit()


