from database_classes import HomeItem
from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engin = create_engine('sqlite:///home_inventory.db', echo=True)
Session = sessionmaker(bind=engin)
session = Session()

@app.route("/")
def home():
    items = session.query(HomeItem).all()
    for item in items:
        print(item.id, item.item_name, item.item_description, item.value)
    return render_template("index.html", item_data=items)

@app.route("/add_item", methods=["POST", "GET"])
def add_item():
    return render_template("AddPage.html")

if __name__ == '__main__':
    app.run(debug=False)