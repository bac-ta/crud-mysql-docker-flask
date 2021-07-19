"""
Class user that mapping with "user" table
"""

from settings import *

db = db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(10), nullable=False)

    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_type(self):
        return self.type
