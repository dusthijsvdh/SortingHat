from . import routes

@routes.route("/")
def home():
    return "Hello World"