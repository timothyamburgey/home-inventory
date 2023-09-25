from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float, Text, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
from database_classes import HomeItem

engin = create_engine('sqlite:///home_inventory.db', echo=True)
Session = sessionmaker(bind=engin)
session = Session()

response = session.query(HomeItem).all()
for item in response:
    print(item.item_name)