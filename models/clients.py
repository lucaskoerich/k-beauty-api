from flask_sqlalchemy import SQLAlchemy
from models import db

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def __init__(self, name, phone, gender):
        self.name = name
        self.phone = phone
        self.gender = gender
