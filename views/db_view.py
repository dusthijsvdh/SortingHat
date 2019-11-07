# Handle blueprint garbage
from . import views

# Predefined modules.
from flask import redirect, url_for

# Our own modules.
from controllers import db_controller

# This route returns all records in json format.
@views.route("/db/get_records")
def get_records():
	return db_controller.get_records()

# This function returns one record as json.
@views.route("/db/get_record/<index>")
def get_record(index):
	return db_controller.get_record(index)

# This function adds a record with a specified name and then shows the record.
@views.route("/db/add_record/<name>")
def add_record(name):
	db_controller.add_record(name)
	return redirect(url_for("views.get_record", index = -1))

# This function updates a record and then shows the changed record.
@views.route("/db/update_record/<int:index>/<field>/<value>")
def update_record(index, field, value):
	db_controller.update_record(index, field, value)
	return redirect(url_for("views.get_record", index = index))