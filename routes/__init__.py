from flask import Blueprint
routes = Blueprint('routes', __name__)

from .standard import *
from .db import *