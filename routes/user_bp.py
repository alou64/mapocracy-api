from flask import Blueprint
from controllers.UserController import index, get_user_by_email, create_user, user_poll

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/<email>', methods=['GET'])(get_user_by_email)
user_bp.route('/<email>/poll', methods=['GET'])(user_poll)
user_bp.route('/new', methods=['POST'])(create_user)
