from flask import Blueprint
<<<<<<< HEAD
from controllers.PollController import index, create_poll
||||||| 5f0f194
from controllers.PollController import index
=======
from controllers.PollController import index, create_poll, get_poll_by_id, get_poll_answers
>>>>>>> feature/routes

poll_bp = Blueprint('poll_bp', __name__)

poll_bp.route('/', methods=['GET'])(index)
<<<<<<< HEAD
poll_bp.route('/new', methods=['POST'])(create_poll)
||||||| 5f0f194
=======
poll_bp.route('/<int:id>', methods=['GET'])(get_poll_by_id)
poll_bp.route('/<int:id>/answer', methods=['GET'])(get_poll_answers)
poll_bp.route('/new', methods=['POST'])(create_poll)
>>>>>>> feature/routes
