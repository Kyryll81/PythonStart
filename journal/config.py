from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = environ['SQLALCHEMY_TRACK_MODIFICATIONS']
    SECRET_KEY = environ['SECRET_KEY']
    SWAGGER = {
    'title': 'Journal API',
    'uiversion': 3,
    'version': 1.0,
    'description': 'API documentation for journal',
}
