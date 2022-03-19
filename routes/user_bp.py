from flask import Blueprint
from controllers.UserController import index, get_user_by_id, create_user

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/<int:user_id>', methods=['GET'])(get_user_by_id)
user_bp.route('/new', methods=['POST'])(create_user)
