# Predifined 
from flask import Flask

# Our own packages
from routes import *
from excel_parser import parser

sheet = parser.get_sheet("db.xlsx")
parser.add_record(sheet, ["Joost", 0, 0, 0, 0, "se"], "db.xlsx")
records = parser.get_records("db.xlsx")
print(parser.get_record(records, 0))

app = Flask(__name__)
app.register_blueprint(routes)
app.run()