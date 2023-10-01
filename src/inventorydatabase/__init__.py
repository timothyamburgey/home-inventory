from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "f99d17b2b2ffb29982555c1a73e629d7de9b8c834ab2dbe857edcc052474"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'

db = SQLAlchemy(app)
session = db.session

from inventorydatabase import routes