from flask_sqlalchemy import SQLAlchemy
from models import db

class Procedure(db.Model):
    __tablename__ = 'procedures'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Numeric(10, 2), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def __init__(self, name, value, duration):
        self.name = name
        self.value = value
        self.duration = duration
