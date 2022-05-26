from flask import Flask
from flask.sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['sqlalchemy_database_url']='sqlite:///pkg.db'
db = SQLAlchemy(app)
@app.route("/")
def index():
    return "hello welcome to home"
if __name__=="__main__":
    app.run(debug=True)
