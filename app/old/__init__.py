from flask import Blueprint

old = Blueprint('old', __name__)

from . import views