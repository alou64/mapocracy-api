from models.Poll import Poll
from models.User import User
from models.Answer import Answer
from models.Vote import Vote
from models.VoterListPoll import VoterListPoll
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime
from sqlalchemy.orm import joinedload
from sqlalchemy import func


# def index():
#   return jsonify(Poll.query.all())


def answer_vote_count_coords(answers):
  return [{'id': answer.id, 'poll_id': answer.poll_id, 'content': answer.content, 'vote_count': Vote.query.filter(Vote.answer_id == answer.id).count(), 'coordinates': [[user.latitude, user.longitude] for user in User.query.with_entities(User.latitude, User.longitude).join(Vote, User.id == Vote.user_id).join(Answer, Vote.answer_id == Answer.id).filter(Vote.answer_id == answer.id).all()]} for answer in answers]


def test():
  poll = Poll.query.get(1)
  poo = answer_vote_count_coords(poll.answers)
  return jsonify(poo)


def create_poll():
  req = request.json

  poll = Poll(
    req['user_id'],
    req['category'],
    req['name'],
    req['region'],
    True if req['emaillist'] else False,
    req['description'],
    req['start_at'],
    req['end_at'],
    req['center'][1],
    req['center'][0],
    req['radius'],
    req['visibility']
  )

  db.session.add(poll)
  db.session.flush()

  for item in req['answers']:
    answer = Answer(poll.id, item)
    db.session.add(answer)

  if req['emaillist']:
    for item in req['emaillist']:
      voter_list_poll = VoterListPoll(item, poll.id)
      db.session.add(voter_list_poll)

  db.session.commit()

  user = User.query.get(req['user_id'])
  poll_dict = poll.as_dict()
  poll_dict['first_name'] = user.first_name
  poll_dict['last_name'] = user.last_name
  poll_dict['answers'] = answer_vote_count_coords(poll.answers)

  return jsonify(poll_dict)


def get_poll_by_id(id):
  poll = Poll.query.get(id)
  user = User.query.get(poll.user_id)


  poll_dict = poll.as_dict()
  poll_dict['first_name'] = user.first_name
  poll_dict['last_name'] = user.last_name
  poll_dict['answers'] = answer_vote_count_coords(poll.answers)

  return jsonify(poll_dict)


def filter_polls():
  q = Poll.query.filter(Poll.restriction == False)

  if request.args.get('time'):
    if request.args['time'] == 'current':
      q = q.filter(Poll.end_at >= datetime.now(), Poll.start_at <= datetime.now())
    else: # past
      q = q.filter(Poll.end_at < datetime.now())

  if request.args.get('region'):
    q = q.filter(Poll.region == request.args['region'])

  if request.args.get('category'):
    q = q.filter(Poll.category == request.args['category'])

  if request.args.get('order'):
    if request.args['order'] == 'popularity':
      subquery = db.session.query(Vote).with_entities(Vote.poll_id, func.count().label('popularity')).group_by(Vote.poll_id).subquery()
      q = q.join(subquery, Poll.id == subquery.c.poll_id).order_by(subquery.c.popularity.desc())
    elif request.args['order'] == 'new':
      q = q.order_by(Poll.created_at.desc())
    else: #old
      q = q.order_by(Poll.created_at.asc())


  res = []

  for poll in q.limit(9).all():
    user = User.query.get(poll.user_id)
    poll_dict = poll.as_dict()
    poll_dict['first_name'] = user.first_name
    poll_dict['last_name'] = user.last_name
    poll_dict['answers'] = answer_vote_count_coords(poll.answers)
    res.append(poll_dict)

  return jsonify(res)







  # return jsonify(
  #   [
  #     [
  #       poll,
  #       {
  #         'first_name': user.first_name,
  #         'last_name': user.last_name,
  #         'user_id': user.id
  #       },
  #       answer_vote_count_coords(poll.answers)
  #     ]
  #     for poll in q.limit(10).all()
  #       for user in
  #       [
  #         User.query.get(poll.user_id)
  #       ]
  #   ]
  # )
