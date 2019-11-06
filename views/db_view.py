# Handle blueprint garbage
from . import views

# Predefined modules.
from time import sleep
from flask import Flask, redirect, url_for

# Our own modules.
from controllers import excel_controller

# This route returns all records in json format.
@views.route("/db/get_records")
def get_records():
	records = excel_controller.get_records("db.xlsx")
	return {"records": records}

# This function returns one record as json.
@views.route("/db/get_record/<index>")
def get_record(index):
	records = excel_controller.get_records("db.xlsx")
	return records[int(index)]

# This function adds a record with a specified name and then shows the record.
@views.route("/db/add_record/<name>")
def add_record(name):
	sheet = excel_controller.get_sheet("db.xlsx")
	excel_controller.add_record(sheet, "db.xlsx", [name,0,0,0,0])
	sleep(0.2)
	return redirect(url_for("views.get_record", index = -1))

# This function updates a record and then shows the changed record.
@views.route("/db/update_record/<int:index>/<field>/<value>")
def update_record(index, field, value):
	if field != "naam": value = int(value)
	sheet = excel_controller.get_sheet("db.xlsx")

	record = excel_controller.get_record(excel_controller.get_records("db.xlsx"), index)
	record[field] = value
	new_record = excel_controller.record_to_list(record)

	excel_controller.update_record(sheet, "db.xlsx", index + 1, new_record)
	
	redirect(url_for("views.get_record", index = index))