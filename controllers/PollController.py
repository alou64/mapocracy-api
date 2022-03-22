from models.Poll import Poll
from models.Answer import Answer
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime
from sqlalchemy.orm import joinedload


def index():
  return jsonify(Poll.query.all())


def create_poll():
  req = request.json

  poll = Poll(
    req['user_id'],
    req['category_id'],
    req['name'],
    req['center'],
    req['restriction'],
    req['description'],
    req['start_at'],
    req['end_at'],
    req['visibility']
  )

  db.session.add(poll)
  db.session.flush()

  for item in req['answers']:
    answer = Answer(poll.id, item)
    db.session.add(answer)

  db.session.commit()

  return jsonify(poll, poll.answers)


def get_poll_by_id(id):
  q = Poll.query.filter_by(id=id).first()
  return jsonify(q, q.answers)


def get_poll_answers(id):
  q = Answer.query.filter_by(poll_id=id).all()
  return jsonify(q)
