#class name flask and object is app and parameter is default python value __name__
#it takes program name as a value by default)
from flask import Flask
app = Flask(__name__)
#escape it is scureable way to take user input
from markupsafe import escape
#routing use to map the url to a function (/)means localhost or system default home url
#we can specify the routing path after the eg(/apton)
#decorator
@app.route('/') #(/)home url 
def hello():
    return 'hello good morning'
#by default it take user values by string
@app.route('/apton/<string>')
def apton(string):
    return 'welcome %s to apton'% string
#path is a data type u can give more input with /
@app.route('/user/<path:username>')
def show_post(username):
    return '<h1 style="text-align:center;"> user input </h1> your username is %s'% escape(username)
    

#create environment directory for project
#python3 -m venv flask =>to create vertual enviroment 
#pip install Flask    => to install Flask framework
#. flask/bin/activate => to activate flask
#export FLASK_APP=helloo.py 
#export FLASK_ENV=development => activate debug mode
#flask run => run the flsk app program 
