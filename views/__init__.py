from flask import Blueprint
views = Blueprint('views', __name__)

from .vraag_view import *
from .db_view import *