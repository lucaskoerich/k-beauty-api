import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('CONNECTION_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SALT = os.environ.get('SALT')
