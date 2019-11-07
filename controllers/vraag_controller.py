from controllers import excel_controller, db_controller, results_controller
from flask import redirect, url_for, render_template
from views import *
import json

def home(method, form):
	# Check if we got form data.
    if method == "POST" and form["name"] != "":
        # Check for the easter egg's.
        if form["name"].lower() == "harry potter":
            return redirect(url_for("views.uitslag", index = 0, uitslag = "Gryffindor!"))
        elif form["name"].lower() == "jesse" or form["name"].lower() == "ryan":
            return redirect(url_for("views.uitslag", index = 0, uitslag = "SSSAAAAANG!!!!!"))
        # If none of the easter-eggs is triggered, the code below will be called.
        else:
            # Get the name variable and add it to the database.
            name = form["name"]
            db_controller.add_record(name)
            # Get the index of the record in the db.
            index = len(excel_controller.get_records("db.xlsx")) - 1
            # Redirect to the first question with the index of the record in the db.
            return redirect(url_for("views.vraag", vraagGetal = 1, index = index))
    else:
        # If we havent got any form data we will render the home page.
        return render_template("index.html")
    
def vraag(vraagGetal, index, method, form):
    # First we open the file where all of the questions are stored as json
    with open("./static/vragen.json") as f:
        vragenDict = json.load(f)
    
    # Now we define the questions and the anwsers variables using the question number.
    vraag = vragenDict["vragen"][vraagGetal - 1]
    antwoorden = vragenDict["antwoorden"][vraagGetal - 1]

    # We check to see if there is form data.
    if method == "POST":
        # If there is form data we first define a variable with the value, the awnser that the user gave.
        form = form["antwoord"]
        # Now we run the function handle_antwoorden from the exel_parser module, this function returns a 1 if a good awnser is given and stored,
        if handle_antwoorden(antwoorden, index, form) == 1:
            # We check if this whas the last question.
            if vraagGetal != len(vragenDict["vragen"]):
                # If it whas not the last question we render the next question.
                return redirect(url_for("views.vraag", vraagGetal = vraagGetal + 1, index = index))
            else:
                # If it was the last question we results_controllerulate the result.
                percentages = results_controller.calculate(index)
                
                keys = [k for k in percentages[0]]
                specialisatie = keys[0]
                
                procent = int(percentages[0][specialisatie])
                
                # Get the sheet.
                sheet = excel_controller.get_sheet("db.xlsx")
                
                # Get the current record.
                record = excel_controller.get_record(index)
                
            	# Change the uitkomst in the dictionary.
                record["uitkomst"] = f"{percentages}" 
                
                # Transform the dictionary to a list.
                new_record = excel_controller.record_to_list(record)
                
                # Update the record
                excel_controller.update_record(sheet, "db.xlsx", index + 1, new_record)
                
                # Render the result page
                return redirect(url_for("views.uitslag", index = index, specialisatie = specialisatie, procent = procent))
        else:
            # If the form returned an error we rerender the question.
            return render_template("vraag.html", vraag = vraag, antwoord1 = antwoorden[0][0], antwoord2 = antwoorden[1][0], antwoord3 = antwoorden[2][0], antwoord4 = antwoorden[3][0], vraagGetal = vraagGetal, antwoorden = antwoorden)
    else: 	
        # Is there is no form data we render the question.
        return render_template("vraag.html", vraag = vraag, antwoord1 = antwoorden[0][0], antwoord2 = antwoorden[1][0], antwoord3 = antwoorden[2][0], antwoord4 = antwoorden[3][0], vraagGetal = vraagGetal, antwoorden = antwoorden)

# This cuntion checks if the awnser is given and adds the given points in the db.
def handle_antwoorden(antwoorden, index, form):
	# This loops through all of the awnsers in the awnsers list.
	for antwoord in antwoorden:
		# It checks if the awnser the user has given is the same as the awnser in the awnser list.
		if form == antwoord[0]:
			# If the awnser is the same it gets the sheet.
			sheet = excel_controller.get_sheet("db.xlsx")

			# Then it gets the record.
			record = excel_controller.get_record(index)

			# And finally it gets the points and adds them to the value record.
			if record["punten_" + antwoord[2]] != "":
				record["punten_" + antwoord[2]] += antwoord[1]
			else: 
				record["punten_" + antwoord[2]] = antwoord[1]

			# It then makes a new record with the new value.
			new_record = excel_controller.record_to_list(record)

			# Then it updates the db.
			excel_controller.update_record(sheet, "db.xlsx", index + 1, new_record)

			# It returns 1 which means it worked.
			return 1
	else:
		# If it couldn't find the awnser it returns 0
		return 0

def uitslag(index, specialisatie, procent):
    return render_template("uitslag.html", specialisatie = specialisatie, procent = procent)