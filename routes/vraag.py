# Predefined modules
from flask import render_template, redirect, request, url_for
import json

# Our own routes
from excel_parser import parser
from results import calc
from . import routes
from routes import db


@routes.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.form["name"] != "":
        if request.form["name"].lower() == "harry potter":
            return redirect(url_for("routes.uitslag", index=0, uitslag="Gryffindor!"))
        elif request.form["name"].lower() == "jesse" or request.form["name"].lower() == "ryan":
            return redirect(url_for("routes.uitslag", index=0, uitslag="SSSAAAAANG!!!!!"))
        else:
            name = request.form["name"]
            print(name)
            db.add_record([name, 0, 0, 0, 0, 0])
            index = len(parser.get_records("db.xlsx")) - 1
            return redirect(url_for("routes.vraag", vraagGetal=1, index=index))
    else:
        return render_template("index.html")


@routes.route("/vraag/<int:vraagGetal>/<int:index>", methods=["GET", "POST"])
def vraag(vraagGetal, index):
    with open("./routes/vragen.json") as f:
        vragenDict = json.load(f)

    vraag = vragenDict["vragen"][vraagGetal - 1]
    antwoorden = vragenDict["antwoorden"][vraagGetal - 1]

    if request.method == "POST":
        form = request.form["antwoord"]
        if parser.handle_antwoorden(antwoorden, index, form) == 1:
            print(f"vraag {index}, antwoord: {form}")
            if vraagGetal != len(vragenDict["vragen"]):
                return redirect(url_for("routes.vraag", vraagGetal=vraagGetal + 1, index=index))
            else:
                uitslag = calc.calculate(index)
                return redirect(url_for("routes.uitslag", index=index, uitslag=uitslag))
        else:
            return render_template("vraag.html", vraag=vraag, antwoord1=antwoorden[0][0], antwoord2=antwoorden[1][0], antwoord3=antwoorden[2][0], antwoord4=antwoorden[3][0])
    else:
        return render_template("vraag.html", vraag=vraag, antwoord1=antwoorden[0][0], antwoord2=antwoorden[1][0], antwoord3=antwoorden[2][0], antwoord4=antwoorden[3][0])

@routes.route("/uitslag/<index>/<uitslag>")
def uitslag(index, uitslag):
    return render_template("uitslag.html", uitslag=uitslag)
