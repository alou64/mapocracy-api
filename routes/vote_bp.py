from flask import Blueprint
from controllers.VoteController import index

vote_bp = Blueprint('vote_bp', __name__)

vote.route('/', methods=['GET'])(index)
