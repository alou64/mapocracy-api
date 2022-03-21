from flask import Blueprint
from controllers.PollController import index, create_poll

poll_bp = Blueprint('poll_bp', __name__)

poll_bp.route('/', methods=['GET'])(index)
poll_bp.route('/new', methods=['POST'])(create_poll)
