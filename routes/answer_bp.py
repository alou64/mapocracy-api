from flask import Blueprint
from controllers.AnswerController import index

answer_bp = Blueprint('answer_bp', __name__)

answer.route('/', methods=['GET'])(index)
