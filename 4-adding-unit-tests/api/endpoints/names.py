from flask import Blueprint
from .util import identify_name

names_api = Blueprint('names_api', __name__)


@names_api.route('/names')
def get_name():
    name = identify_name("Brandon")
    return "works - "+name
