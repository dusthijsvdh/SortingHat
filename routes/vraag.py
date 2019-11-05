# Predefined modules
from flask import render_template, redirect, request, url_for
import json

# Our own routes
from excel_parser import parser
from . import routes
from routes import db

@routes.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "POST" and request.form["name"] != "":
		name = request.form["name"]
		db.add_record([name, 0,0,0,0,0])
		index = len(parser.get_records("db.xlsx")) - 1
		return redirect(url_for("routes.vraag", vraagGetal = 1, index = index))
	else:
		return render_template("index.html")

@routes.route("/vraag/<int:vraagGetal>/<int:index>", methods = ["GET", "POST"])
def vraag(vraagGetal, index):
	with open("./routes/vragen.json") as f:
		vragenDict = json.load(f)
	
	vraag = vragenDict["vragen"][vraagGetal - 1]
	antwoorden = vragenDict["antwoorden"][vraagGetal - 1]

	if request.method == "POST":
		form = request.form["antwoord"]
		if parser.handle_antwoorden(antwoorden, index, form) == 1:
			if vraagGetal != len(vragenDict["vragen"]):
				return redirect(url_for("routes.vraag", vraagGetal = vraagGetal + 1, index = index))
			else:
				return redirect(url_for("routes.uitslag", index = index))
		else:
			return render_template("vraag.html", vraag = vraag, antwoord1 = antwoorden[0][0], antwoord2 = antwoorden[1][0], antwoord3 = antwoorden[2][0], antwoord4 = antwoorden[3][0])
	else: 	
		return render_template("vraag.html", vraag = vraag, antwoord1 = antwoorden[0][0], antwoord2 = antwoorden[1][0], antwoord3 = antwoorden[2][0], antwoord4 = antwoorden[3][0])

@routes.route("/uitslag/<index>")
def uitslag(index):
	return "Uitslag"
