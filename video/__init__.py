from flask import Flask
from .config import secret_key,database
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = database

from video import routes
