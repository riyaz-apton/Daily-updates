from main import db
from models import User
db.create_all()
admin=User(UserName="admin",Email="admin@ryz.com")
guest=User(UserName="guest",Email="guest@pkz.com")
db.session.add(admin)
db.session.add(guest)
db.session.commit()
