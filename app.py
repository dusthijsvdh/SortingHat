# Predifined 
from flask import Flask

# Our own packages
from routes import *
from excel_parser import parser

sheet = parser.get_sheet("db.xlsx")
parser.add_record(sheet, "db.xlsx", ["Joost", 1000, 0, 0, 0, 0.1, 0, 0, 0])
records = parser.get_records("db.xlsx")
record = parser.get_record(records, 0)

app = Flask(__name__)
app.register_blueprint(routes)
app.run()