# Handle blueprint garbage
from . import views

# Predefined modules
from flask import render_template, redirect, request, url_for

# Our own controllers
from controllers import vraag_controller

# This route lands you on the home page. Here you can fill in your name and then the server will redirect to the questions page.
@views.route("/", methods = ["GET", "POST"])
def home():
    return vraag_controller.home(request.method, request.form)

# This route renders the questions
@views.route("/vraag/<int:vraagGetal>/<int:index>", methods = ["GET", "POST"])
def vraag(vraagGetal, index):
    return vraag_controller.vraag(vraagGetal, index, request.method, request.form)

# This route renders the result page
@views.route("/uitslag/<index>/<specialisatie>/<procent>")
def uitslag(index, specialisatie, procent):
    return vraag_controller.uitslag(index, specialisatie, procent)