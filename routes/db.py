# Predefined modules.
from time import sleep
from flask import Flask, redirect, url_for

# Our own modules.
from . import routes
from excel_parser import parser

# This route returns all records in json format.
@routes.route("/db/get_records")
def get_records():
	records = parser.get_records("db.xlsx")
	return {"records": records}

# This function returns one record as json.
@routes.route("/db/get_record/<index>")
def get_record(index):
	records = parser.get_records("db.xlsx")
	return records[int(index)]

# This function adds a record with a specified name and then shows the record.
@routes.route("/db/add_record/<name>")
def add_record(name):
	sheet = parser.get_sheet("db.xlsx")
	parser.add_record(sheet, "db.xlsx", [name,0,0,0,0])
	sleep(0.2)
	return redirect(url_for("routes.get_record", index = -1))

# This function updates a record and then shows the changed record.
@routes.route("/db/update_record/<int:index>/<field>/<value>")
def update_record(index, field, value):
	if field != "naam": value = int(value)
	sheet = parser.get_sheet("db.xlsx")

	record = parser.get_record(parser.get_records("db.xlsx"), index)
	record[field] = value
	new_record = parser.record_to_list(record)

	parser.update_record(sheet, "db.xlsx", index + 1, new_record)
	
	redirect(url_for("routes.get_record", index = index))
