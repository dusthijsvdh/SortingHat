# Predifined 
from flask import Flask

# Our own packages
from views import *

# Define flask app
app = Flask(__name__)

# Add the blueprint routes
app.register_blueprint(views)

# Run the flask app on port 5000
app.run(debug = True)