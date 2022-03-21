from models.Poll import Poll
from models.Answer import Answer
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime


def index():
  q = Poll.query.all()
  return jsonify(q)

def create_poll():
  req = request.json
  poll = Poll(
    req['user_id'],
    int(req['category_id']),
    req['name'],
    req['center'],
    req['restriction'],
    req['description'],
    datetime.fromtimestamp(int(req['start_at'])),
    datetime.fromtimestamp(int(req['end_at'])),
    req['visibility']
  )
  db.session.add(poll)
  db.session.flush()
  for item in req['answers']:
    answer = Answer(poll.id, item)
    db.session.add(answer)
  db.session.commit()
  return jsonify(poll)


# datetime.fromtimestamp(int('1364694508'))
