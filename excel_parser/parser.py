import pyexcel as pe

# Functions regarding managing sheets

def get_sheet(filename):
    sheet = pe.get_sheet(file_name = "./db/" + filename)
    return sheet
	
# Functions regarding records

def get_records(filename):
	records = pe.get_records(file_name = "./db/" + filename)
	return records

def add_record(sheet, record, filename):
    sheet.row += record
    sheet.save_as("./db/" + filename)

def get_record(records, index):
    return records[index]
