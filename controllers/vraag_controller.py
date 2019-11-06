from controllers import excel_controller

# This cuntion checks if the awnser is given and adds the given points in the db.
def handle_antwoorden(antwoorden, index, form):
	# This loops through all of the awnsers in the awnsers list.
	for antwoord in antwoorden:
		# It checks if the awnser the user has given is the same as the awnser in the awnser list.
		if form == antwoord[0]:
			# If the awnser is the same it gets the sheet.
			sheet = excel_controller.get_sheet("db.xlsx")

			# Then it gets the record.
			record = excel_controller.get_record(excel_controller.get_records("db.xlsx"), index)

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