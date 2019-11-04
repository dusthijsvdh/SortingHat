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