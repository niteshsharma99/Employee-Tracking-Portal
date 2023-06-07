# project/models.py

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    address = db.Column(db.String(255))
    phone = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    department = db.Column(db.String(50))
