# Predifined 
from flask import Flask

# Our own packages
from routes import *
from excel_parser import parser

print(parser.test())

app = Flask(__name__)
app.register_blueprint(routes)
app.run()