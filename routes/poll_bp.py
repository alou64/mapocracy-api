from flask import Blueprint
from controllers.PollController import create_poll, get_poll_by_id, filter_polls, test, update_poll

poll_bp = Blueprint('poll_bp', __name__)

poll_bp.route('/', methods=['GET'])(filter_polls)
poll_bp.route('/test', methods=['GET'])(test)
poll_bp.route('/<int:id>', methods=['GET'])(get_poll_by_id)
poll_bp.route('/new', methods=['POST'])(create_poll)
poll_bp.route('/update', methods=['PUT'])(update_poll)
