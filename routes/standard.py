# Predefined modules
from flask import render_template, redirect, request, url_for
import requests

# Our own routes
from excel_parser import parser
from . import routes
from routes import db

@routes.route("/", methods = ["GET", "POST"])
def home():
	if request.method == "POST" and request.form["name"] != "":
		name = request.form["name"]
		db.add_record(name)
		index = len(parser.get_records("db.xlsx")) - 1
		return redirect(url_for("routes.v1", index = index))
	else:
		return render_template("index.html")

@routes.route("/vraag/1/<int:index>", methods = ["GET", "POST"])
def v1(index):
	vraag = "Is dit een vraag?"
	antwoorden = [["Ja", 1000, "an"], ["Nee", 10, "ad"], ["Mischien", 1, "re"], ["Wellicht", 50, "on"], ["Aap", 2, "mc"]]

	if request.method == "POST":
		for antwoord in antwoorden:
			if request.form["antwoord"] == antwoord[0]:
				sheet = parser.get_sheet("db.xlsx")

				record = parser.get_record(parser.get_records("db.xlsx"), index)
				
				if record["punten_" + antwoord[2]] != "":
					record["punten_" + antwoord[2]] += antwoord[1]
				else: 
					record["punten_" + antwoord[2]] = antwoord[1]

				new_record = parser.record_to_list(record)

				parser.update_record(sheet, "db.xlsx", index + 1, new_record)

				return redirect(url_for("routes.v2", index = index))
		else:
			return render_template("vraag.html", vraag = vraag, antwoord1 = antwoorden[0][0], antwoord2 = antwoorden[1][0], antwoord3 = antwoorden[2][0], antwoord4 = antwoorden[3][0], antwoord5 = antwoorden[4][0])
	else:
		return render_template("vraag.html", vraag = vraag, antwoord1 = antwoorden[0][0], antwoord2 = antwoorden[1][0], antwoord3 = antwoorden[2][0], antwoord4 = antwoorden[3][0], antwoord5 = antwoorden[4][0])

@routes.route("/vraag/2/<int:index>", methods = ["GET", "POST"])
def v2(index):
	return "Vraag 2"

@routes.route("/vraag/3", methods = ["GET", "POST"])
def v3():
	return "Vraag 3"

@routes.route("/vraag/4", methods = ["GET", "POST"])
def v4():
	return "Vraag 4"

@routes.route("/uitslag")
def uitslag():
	return "Uitslag"
