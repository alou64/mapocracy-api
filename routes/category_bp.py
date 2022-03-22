from flask import Blueprint
from controllers.CategoryController import index, create_category

category_bp = Blueprint('category_bp', __name__)

category_bp.route('/', methods=['GET'])(index)
category_bp.route('/new', methods=['POST'])(create_category)
