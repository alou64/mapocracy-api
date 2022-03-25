from flask import Blueprint
from controllers.VoteController import index, delete_vote

vote_bp = Blueprint('vote_bp', __name__)

vote_bp.route('/', methods=['GET', 'POST'])(index)
vote_bp.route('/<user_id>/<int:poll_id>', methods=['DELETE'])(delete_vote)
