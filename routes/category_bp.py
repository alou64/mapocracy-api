from flask import Blueprint
from controllers.CategoryController import index

category_bp = Blueprint('vote_bp', __name__)

category.route('/', methods=['GET'])(index)
