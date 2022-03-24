from models.Vote import Vote
from models.User import User
from models.Poll import Poll
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime


def index():
  if request.method == 'POST':
    req = request.json
    poll = Poll.query.get(req['poll_id'])

    # check voter list
    if poll.restriction:
      pass

    # check location

    # check if user already voted
    if not Vote.query.filter_by(user_id=req['user_id'], poll_id=poll.id).first():
      vote = Vote(req['user_id'], poll.id, req['answer_id'])
      db.session.add(vote)
      db.session.commit()
      return jsonify(vote)

    return make_response("Cannot vote twice", 403)

  return jsonify(Vote.query.all())
