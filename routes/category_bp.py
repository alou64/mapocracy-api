from flask import Blueprint
from controllers.CategoryController import index

category_bp = Blueprint('category_bp', __name__)

category_bp.route('/', methods=['GET'])(index)
