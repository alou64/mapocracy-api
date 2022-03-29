from models.User import User
from models.VoterList import VoterList
from models.VoterListMember import VoterListMember
from models.VoterListPoll import VoterListPoll
from models.Poll import Poll
from models.Vote import Vote
from models.Answer import Answer
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime
import json



def answer_vote_count_coords(answers):
  return [{'id': answer.id, 'poll_id': answer.poll_id, 'content': answer.content, 'vote_count': Vote.query.filter(Vote.answer_id == answer.id).count(), 'coordinates': [[user.latitude, user.longitude] for user in User.query.with_entities(User.latitude, User.longitude).join(Vote, User.id == Vote.user_id).join(Answer, Vote.answer_id == Answer.id).filter(Vote.answer_id == answer.id).all()]} for answer in answers]



def index():
  return jsonify(User.query.all())


def get_user_by_email(user_id):
  user = User.query.get(user_id)

  if not user:
    user = User(user_id)
    db.session.add(user)
    db.session.commit()

  return jsonify(user)



def create_user():
  user_id = request.json['email']

  if User.query.get(user_id):
    return make_response('User already exists', 400)

  user = User(user_id)

  db.session.add(user)
  db.session.commit()

  return jsonify(user)


def get_user_poll(user_id):
  q = Poll.query.filter(Poll.user_id == user_id)

  if request.args.get('time') == 'current':
    q = q.filter(Poll.user_id == user_id, Poll.end_at >= datetime.now())

  if request.args.get('time') == 'past':
    q = q.filter(Poll.user_id == user_id, Poll.end_at < datetime.now())

  res = []

  for poll in q.all():
    user = User.query.get(user_id)
    poll_dict = poll.as_dict()
    poll_dict['first_name'] = user.first_name
    poll_dict['last_name'] = user.last_name
    poll_dict['answers'] = answer_vote_count_coords(poll.answers)
    res.append(poll_dict)

  return jsonify(res)


def get_user_invites(user_id):
  polls = (Poll.query
    .join(VoterListPoll, Poll.id == VoterListPoll.poll_id)
    .join(VoterList, VoterListPoll.voter_list_id == VoterList.id)
    .join(VoterListMember, VoterList.id == VoterListMember.voter_list_id)
    .filter(VoterListMember.user_id == user_id)
    .all())

  res = []

  for poll in polls:
    user = User.query.get(user_id)
    poll_dict = poll.as_dict()
    poll_dict['first_name'] = user.first_name
    poll_dict['last_name'] = user.last_name
    poll_dict['answers'] = answer_vote_count_coords(poll.answers)
    res.append(poll_dict)

  return jsonify(res)


def get_user_voter_list(user_id):
  return jsonify({
    VoterList.id:
      [VoterListMember.user_id
        for VoterListMember in VoterList.voter_list_members]
          for VoterList in VoterList.query
            .filter(VoterList.user_id == user_id)
            .all()
  })


def update_user():
  req = request.json
  user = User.query.get(req['id'])

  for key, val in req.items():
    setattr(user, key, val)

  db.session.commit()

  return jsonify(user)
