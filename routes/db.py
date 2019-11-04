from . import routes
from time import sleep
from excel_parser import parser
from flask import Flask, redirect, url_for

@routes.route("/db/get_record/<index>")
def get_record(index):
	records = parser.get_records("db.xlsx")
	return records[int(index)]

@routes.route("/db/add_record/<name>")
def add_record(name):
	sheet = parser.get_sheet("db.xlsx")
	parser.add_record(sheet, "db.xlsx", [name])
	sleep(1)
	return redirect(url_for("routes.get_record", index = -1))

@routes.route("/db/update_record/<int:index>/<field>/<value>")
def update_record(index, field, value):
	if field != "naam": value = int(value)
	sheet = parser.get_sheet("db.xlsx")

	record = parser.get_record(parser.get_records("db.xlsx"), index)
	record[field] = value
	new_record = parser.record_to_list(record)

	parser.update_record(sheet, "db.xlsx", index + 1, new_record)
	return "ok"
