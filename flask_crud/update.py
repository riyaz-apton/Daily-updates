from main import db
from models import User
guest =User.query.filter_by(username='guest').first()
guest.email="guestmohan.com"

db.secssion.commit()

