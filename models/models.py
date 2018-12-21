from flask import Flask
from sqlalchemy.exc import SAWarning

from flask_sqlalchemy import SQLAlchemy

APPLICATION = Flask(__name__)

APPLICATION.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vqntkxwnulxnhm:55ac12a8fb62914512c2b2320bd8cf0b9ec125b54d2a0fe4089d947e9ca37121@ec2-174-129-25-182.compute-1.amazonaws.com:5432/d9b2kbtnmn9grs"
APPLICATION.config['SQLALCHEMY_POOL_SIZE'] = 20
db = SQLAlchemy(APPLICATION)

class EMPLOYEEDATA(db.Model):
    __tablename__ = 'employeedata'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    number = db.Column(db.String(100))
    designation = db.Column(db.String(100))

    __table_args__ = (db.UniqueConstraint(
        email, number), {'extend_existing': True})


    def __repr__(self):
        return '(%r, %r, %r, %r)' % (self.email, self.name, self.number, self.designation)
    
    def __json__(self):
            return [self.email, self.name, self.number, self.designation]

