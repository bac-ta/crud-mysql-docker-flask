# importing libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating an instance of the flask app
app = Flask(__name__)

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:Silencer&&55@localhost/flask-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
