from models.Vote import Vote
from models.User import User
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime


def index():
  if request.method == 'POST':
    req = request.json

    if not Vote.query.filter_by(user_id=req['user_id'], poll_id=req['poll_id']).first():
      vote = Vote(req['user_id'], req['poll_id'], req['answer_id'])
      db.session.add(vote)
      db.session.commit()
      return jsonify(vote)

    return make_response("Cannot vote twice", 403)

  return jsonify(Vote.query.all())
