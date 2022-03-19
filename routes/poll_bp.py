from flask import Blueprint
from controllers.PollController import index

poll_bp = Blueprint('poll_bp', __name__)

poll.route('/', methods=['GET'])(index)
