from flask import render_template, redirect
from . import routes

@routes.route("/", methods = ["GET", "POST"])
def home():
	return render_template("./views/index.html")

@routes.route("/vraag/1", methods = ["GET", "POST"])
def v1():
	return "Vraag 1"

@routes.route("/uitslag")
def uitslag():
	return "Uitslag"
