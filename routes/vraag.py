# Predefined modules
from flask import render_template, redirect, request, url_for
import json

# Our own routes
from excel_parser import parser
from results import calc
from . import routes
from routes import db

# This route lands you on the home page. Here you can fill in your name and then the server will redirect to the questions page.
@routes.route("/", methods = ["GET", "POST"])
def home():
    # Check if we got form data.
    if request.method == "POST" and request.form["name"] != "":
        # Check for the easter egg's.
        if request.form["name"].lower() == "harry potter":
            return redirect(url_for("routes.uitslag", index = 0, uitslag = "Gryffindor!"))
        elif request.form["name"].lower() == "jesse" or request.form["name"].lower() == "ryan":
            return redirect(url_for("routes.uitslag", index = 0, uitslag = "SSSAAAAANG!!!!!"))
        # If none of the easter-eggs is triggered, the code below will be called.
        else:
            # Get the name variable and add it to the database.
            name = request.form["name"]
            db.add_record(name)
            # Get the index of the record in the db.
            index = len(parser.get_records("db.xlsx")) - 1
            # Redirect to the first question with the index of the record in the db.
            return redirect(url_for("routes.vraag", vraagGetal = 1, index = index))
    else:
        # If we havent got any form data we will render the home page.
        return render_template("index.html")

# This route renders the questions
@routes.route("/vraag/<int:vraagGetal>/<int:index>", methods = ["GET", "POST"])
def vraag(vraagGetal, index):
    # First we open the file where all of the questions are stored as json
    with open("./routes/vragen.json") as f:
        vragenDict = json.load(f)
    
    # Now we define the questions and the anwsers variables using the question number.
    vraag = vragenDict["vragen"][vraagGetal - 1]
    antwoorden = vragenDict["antwoorden"][vraagGetal - 1]

    # We check to see if there is form data.
    if request.method == "POST":
        # If there is form data we first define a variable with the value, the awnser that the user gave.
        form = request.form["antwoord"]
        # Now we run the function handle_antwoorden from the exel_parser module, this function returns a 1 if a good awnser is given and stored,
        if parser.handle_antwoorden(antwoorden, index, form) == 1:
            # We check if this whas the last question.
            if vraagGetal != len(vragenDict["vragen"]):
                # If it whas not the last question we render the next question.
                return redirect(url_for("routes.vraag", vraagGetal = vraagGetal + 1, index = index))
            else:
                # If it was the last question we calculate the result.
                uitslag = calc.calculate(index)
                
                # Get the sheet.
                sheet = parser.get_sheet("db.xlsx")
                
                # Get the current record.
                record = parser.get_record(parser.get_records("db.xlsx"), index)
                
                # Change the uitkomst in the dictionary.
                record["uitkomst"] = uitslag
                
                # Transform the dictionary to a list.
                new_record = parser.record_to_list(record)
                
                # Update the record
                parser.update_record(sheet, "db.xlsx", index + 1, new_record)
                
                # Render the result page
                return redirect(url_for("routes.uitslag", index = index, uitslag = uitslag))
        else:
            # If the form returned an error we rerender the question.
            return render_template("vraag.html", vraag = vraag, antwoord1 = antwoorden[0][0], antwoord2 = antwoorden[1][0], antwoord3 = antwoorden[2][0], antwoord4 = antwoorden[3][0])
    else: 	
        # Is there is no form data we render the question.
        return render_template("vraag.html", vraag = vraag, antwoord1 = antwoorden[0][0], antwoord2 = antwoorden[1][0], antwoord3 = antwoorden[2][0], antwoord4 = antwoorden[3][0])

# This route renders the result page
@routes.route("/uitslag/<index>/<uitslag>")
def uitslag(index, uitslag):
    return render_template("uitslag.html", uitslag=uitslag)
