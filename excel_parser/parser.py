import pyexcel as pe

# Functions regarding managing sheets

def get_sheet(filename):
    sheet = pe.get_sheet(file_name = "./db/" + filename)
    return sheet
	
# Functions regarding records

def get_records(filename):
	records = pe.get_records(file_name = "./db/" + filename)
	return records

def get_record(records, index):
    return records[index]

def add_record(sheet, filename, new_record):
    sheet.row += new_record
    sheet.save_as("./db/" + filename)

def update_record(sheet, filename, index, new_record):
    sheet.row[index] = new_record
    sheet.save_as("./db/" + filename)

def record_to_list(record):
	return [ v for v in record.values() ]

# Antwoorden

def handle_antwoorden(antwoorden, index, form):
	for antwoord in antwoorden:
		if form == antwoord[0]:
			sheet = get_sheet("db.xlsx")

			record = get_record(get_records("db.xlsx"), index)
				
			if record["punten_" + antwoord[2]] != "":
				record["punten_" + antwoord[2]] += antwoord[1]
			else: 
				record["punten_" + antwoord[2]] = antwoord[1]

			new_record = record_to_list(record)

			update_record(sheet, "db.xlsx", index + 1, new_record)

			return 1
	else:
		return 0