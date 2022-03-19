from flask import Blueprint
from controllers.UserController import index

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
