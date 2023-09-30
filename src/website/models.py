from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Float, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class InventoryItem(Base):
    __tablename__ = "Items"
    ID = Column("ID", Integer, primary_key=True)
    item = Column("Item", String(50))
    location = Column("Location", String(50))
    value = Column("Value", Float)

    def __init__(self, item, location, value):
        self.item = item
        self.location = location
        self.value = value

    def __repr__(self):
        return f"Item: {self.item}, Location: {self.location}, Value: {self.value}"

engin = create_engine("sqlite:///inventory.db", echo=True)
Base.metadata.create_all(bind=engin)

Session = sessionmaker(bind=engin)
session = Session()

