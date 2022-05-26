from main import db
class User(db.Model):
    ID = db.Column(db.Integer,primary_key=True,autoincrements=True)
    UserName = db.Coloumn(db.String(20),unique_key=True,nullable=False)
    Email =db.Column(db.String(80),unique_key=True, nullable=False)
#print default value of object
def __repr__(self):
    return '<User %r>' % self.UserName
