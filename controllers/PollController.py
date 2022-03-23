from models.Poll import Poll
from models.Answer import Answer
from models.Vote import Vote
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import func


# def index():
#   return jsonify(Poll.query.all())


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
  q = Poll.query.get(id)
  return jsonify(q, q.answers)


def filter_polls():
  if not request.args:
    return jsonify(Poll.query.filter(Poll.restriction == None).all())

  if request.args['filter'] == 'current':
    return jsonify(
      Poll.query
        .filter(Poll.end_at >= datetime.now(), Poll.start_at <= datetime.now(), Poll.restriction == None)
        .order_by(Poll.start_at.desc())
        .all()
    )

  elif request.args['filter'] == 'past':
    return jsonify(
      Poll.query
        .filter(Poll.end_at < datetime.now(), Poll.restriction == None)
        .order_by(Poll.end_at.desc())
        .all()
      )

  elif request.args['filter'] == 'date':
    return jsonify(
      Poll.query
        .filter(Poll.restriction == None)
        .order_by(Poll.created_at.desc())
        .all()
      )


  subquery = db.session.query(Vote).with_entities(Vote.poll_id, func.count().label('popularity')).group_by(Vote.poll_id).subquery()
  return jsonify(
    Poll.query
      .join(subquery, Poll.id == subquery.c.poll_id)
      # .add_column(subquery.c.popularity)
      .filter(Poll.restriction == None)
      .order_by(subquery.c.popularity.desc())
      .all()
  )
