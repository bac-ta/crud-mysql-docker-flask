"""
Class user that mapping with "user" table
"""

from settings import *

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(10), nullable=False)

    def add_user(self, username, password, type):
        user = User(username=username, password=password, type=type)
        db.session.add(user)
        db.session.commit()

