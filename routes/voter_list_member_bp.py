from flask import Blueprint
from controllers.VoterListMemberController import index

voter_list_member_bp = Blueprint('voter_list_member_bp', __name__)

voter_list_member_bp.route('/', methods=['GET'])(index)
