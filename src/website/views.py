from flask import Blueprint, render_template, request, flash, redirect, url_for

views = Blueprint("views", __name__, template_folder="templates")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/add")
@views.route("/add/")
def add_base():
    return render_template("addform.html")
@views.route("/delete")
@views.route("/delete/")
def delete_base():
    return redirect(url_for("views.home"))
@views.route("/update")
@views.route("/update/")
def update_base():
    return redirect(url_for("views.home"))
@views.route("/add/<int:ID>")
def add(ID):
    return f"<h1>Test {ID}</h1>"

@views.route("/delete/<int:ID>")
def delete(ID):
    return f"<h1>Test {ID}</h1>"

@views.route("/update/<int:ID>")
def update(ID):
    return f"<h1>Test {ID}</h1>"