from main import db
from models import  User
print(User.query.all())
Users=User.query.all()
for User in Users:
    print(User.Email)
selected_User=User.query.filter_by('username'='admin').first()
print(selected_User)

