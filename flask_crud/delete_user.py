from main import db
from models import User
guest =User.query.filter_by(UserName='guest').first()


db.session.Delete(guest)
db.session.commit()
