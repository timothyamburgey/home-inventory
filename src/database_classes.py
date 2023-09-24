from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float, Text, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class HomeItem(Base):
    __tablename__ = 'home_items'

    id = Column(Integer, primary_key=True)
    item_name = Column(String(250), nullable=False)
    item_description = Column(String(250))
    value = Column(Float)

    def __init__(self, item_name="Default Name", item_description="", value=0.0):
        self.item_name = item_name
        self.item_description = item_description
        self.value = value

    def __repr__(self):
        return f"{self.item_name} (${self.value})"

engin = create_engine('sqlite:///home_inventory.db', echo=True)
Base.metadata.create_all(bind=engin)
