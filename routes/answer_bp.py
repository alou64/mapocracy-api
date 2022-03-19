from flask import Blueprint
from controllers.AnswerController import index

answer_bp = Blueprint('answer_bp', __name__)

answer_bp.route('/', methods=['GET'])(index)
