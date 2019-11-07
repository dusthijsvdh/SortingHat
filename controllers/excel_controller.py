import pyexcel as pe

# This function gets the sheet and returns it.
def get_sheet(filename):
    sheet = pe.get_sheet(file_name = "./database/" + filename)
    return sheet
	
# This function gets all the  records.
def get_records(filename):
	records = pe.get_records(file_name = "./database/" + filename)
	return records

# This function gets one specific record.
def get_record(index):
    return get_records("db.xlsx")[index]

# This function adds a record to the db.
def add_record(sheet, filename, new_record):
    sheet.row += new_record
    sheet.save_as("./database/" + filename)

# This function updates a specified record in the db.
def update_record(sheet, filename, index, new_record):
    sheet.row[index] = new_record
    sheet.save_as("./database/" + filename)

# This function converts a record dict to a list.
def record_to_list(record):
	return [ v for v in record.values() ]