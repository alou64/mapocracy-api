from flask import Blueprint
from controllers.UserController import index, get_user_by_email, create_user, get_user_poll, get_user_invites, get_user_voter_list

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/<email>', methods=['GET'])(get_user_by_email)
user_bp.route('/<email>/poll', methods=['GET'])(get_user_poll)
user_bp.route('/<email>/invites', methods=['GET'])(get_user_invites)
user_bp.route('/<email>/voterlist', methods=['GET'])(get_user_voter_list)
user_bp.route('/new', methods=['POST'])(create_user)
