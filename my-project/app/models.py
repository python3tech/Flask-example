#Create our database model
from app import app , db

class UserModel(db):
    __tablename__="Users Model"
    id = db.Column (db.Integer,primary_key=True)
    username=db.Column(db.string(80),nullable=False,unique=True)
    email = db.Column(db.string(120),unique=True)
    mobile_number = db.Column(db.Integer,)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email
