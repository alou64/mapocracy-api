from models.User import User
from models.VoterList import VoterList
from models.VoterListMember import VoterListMember
from models.Poll import Poll
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime


def index():
  return jsonify(User.query.all())


def get_user_by_email(email):
  return jsonify(User.query.get_or_404(email))


def create_user():
  user = User(request.json['email'])

  db.session.add(user)
  db.session.commit()

  return jsonify(user)


def get_user_poll(email):
  if request.args['time'] == 'current':
    return jsonify(Poll.query.filter(Poll.user_id == email, Poll.end_at >= datetime.now()).all())

  return jsonify(Poll.query.filter(Poll.user_id == email, Poll.end_at < datetime.now()).all())


def get_user_invites(email):
  invites = Poll.query\
    .join(VoterList, Poll.restriction == VoterList.id)\
    .join(VoterListMember, VoterList.id == VoterListMember.voter_list_id)\
    .filter(VoterListMember.user_id == email)\
    .all()

  return jsonify(invites)


def get_user_voter_list(email):
  return jsonify({VoterList.id: [VoterListMember.user_id for VoterListMember in VoterList.voter_list_members] for VoterList in VoterList.query.filter(VoterList.user_id == email).all()})
