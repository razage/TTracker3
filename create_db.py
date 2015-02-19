from datetime import date

from app import db
from app.users.models import Technicians
from app.tickets.models import Os, Tickets


# Creating the tables
db.create_all()
db.session.commit()

# Predefined users
db.session.add(Technicians("admin@ttracker3.com", "Test", "User", "password", True, True))
db.session.add(Technicians("alaurent@ttracker2.com", "Andre", "Laurent", "password", False))
db.session.add(Technicians("bwright@ttracker2.com", "Brandon", "Wright", "password", False))
db.session.add(Technicians("ckrob@ttracker2.com", "Chris", "Krob", "password", False))
db.session.add(Technicians("fboterman@ttracker2.com", "Frederick", "Boterman", "password", False))
db.session.add(Technicians("jwilliams@ttracker2.com", "Jonathan", "Williams", "password", False))
db.session.add(Technicians("lglazman@ttracker2.com", "Les", "Glazman", "password", False))
db.session.add(Technicians("mlindberg@ttracker2.com", "Mike", "Lindberg", "password", False))
db.session.add(Technicians("plee@ttracker2.com", "Pete", "Lee", "password", False))
db.session.add(Technicians("rlarson@ttracker2.com", "Rob", "Larson", "password", False))
db.session.commit()


# Predefined Operating Systems
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

# Predefined Tickets
db.session.add(
    Tickets(date(2013, 9, 10), date(2013, 9, 24), "Fred Boterman", 3, "Windows XP", "Becky Bourque", 2183439832,
            "rebecca.bourque@witc.edu", "Computer won't power up properly.",
            "I found that when the power for the CPU is plugged into the motherboard, the computer will not power on. I tried another power source and found the the motherboard is faulty. \n\nI informed Becky of the problem and told her that some of the components are still usable in another computer."))
db.session.add(
    Tickets(date(2013, 9, 3), date(2013, 9, 16), "Jonathan Williams", 3, "Windows 7", "Senior Center", 7153943644, None,
            "Computer will not boot or show video on the monitor",
            "Tried new power supply, still reboot loops. After taking out all of the plugs on the motherboard except for the 24-pin and the Hard Drive, the conclusion was that the motherboard was corrupt. Swapped the hard drive into one of the extra computers that we had up here. Added an extra 2GB of RAM to the computer. The computer still reboot looped, but there was video, meaning the hard drive had to be rewritten. Booted into Windows PE and applying an image to the hard drive that is being used for all of the Senior Center Computers. Finished installing an image via ImageX and the computer is ready to go."))
db.session.commit()