import pyexcel as pe

# This function gets the sheet and returns it.
def get_sheet(filename):
    sheet = pe.get_sheet(file_name = "./db/" + filename)
    return sheet
	
# This function gets all the  records.
def get_records(filename):
	records = pe.get_records(file_name = "./db/" + filename)
	return records

# This function gets one specific record.
def get_record(records, index):
    return records[index]

# This function adds a record to the db.
def add_record(sheet, filename, new_record):
    sheet.row += new_record
    sheet.save_as("./db/" + filename)

# This function updates a specified record in the db.
def update_record(sheet, filename, index, new_record):
    sheet.row[index] = new_record
    sheet.save_as("./db/" + filename)

# This function converts a record dict to a list.
def record_to_list(record):
	return [ v for v in record.values() ]

# This cuntion checks if the awnser is given and adds the given points in the db.
def handle_antwoorden(antwoorden, index, form):
	# This loops through all of the awnsers in the awnsers list.
	for antwoord in antwoorden:
		# It checks if the awnser the user has given is the same as the awnser in the awnser list.
		if form == antwoord[0]:
			# If the awnser is the same it gets the sheet.
			sheet = get_sheet("db.xlsx")

			# Then it gets the record.
			record = get_record(get_records("db.xlsx"), index)

			# And finally it gets the points and adds them to the value record.
			if record["punten_" + antwoord[2]] != "":
				record["punten_" + antwoord[2]] += antwoord[1]
			else: 
				record["punten_" + antwoord[2]] = antwoord[1]

			# It then makes a new record with the new value.
			new_record = record_to_list(record)

			# Then it updates the db.
			update_record(sheet, "db.xlsx", index + 1, new_record)

			# It returns 1 which means it worked.
			return 1
	else:
		# If it couldn't find the awnser it returns 0
		return 0