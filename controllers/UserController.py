from models.User import User
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime


def index():
  q = User.query.all()
  print(q)
  return jsonify(q)

def get_user_by_email(email):
  q = User.query.filter_by(id=email).first()
  return jsonify(q)

def create_user():
<<<<<<< HEAD
  user = User(request.json['email'])
  db.session.add(user)
  db.session.commit()
  return jsonify(user)

def get_user_poll(email):
  user = User.query.filter_by(id=email).first()
  if request.args['time'] == 'current':
    # polls = [poll for poll in user.polls if y.end_at > datetime.now()]
    return jsonify([poll for poll in user.polls if poll.end_at > datetime.now()])
  return jsonify([poll for poll in user.polls if poll.end_at < datetime.now()])
||||||| 5f0f194
  content = request.json
  return content
=======
  user = User(request.json['email'])
  db.session.add(user)
  db.session.commit()
  return jsonify(user)

def get_user_poll(email):
  user = User.query.filter_by(id=email).first()
  if request.args['time'] == 'current':
    return jsonify([poll for poll in user.polls if poll.end_at > datetime.now()])
  return jsonify([poll for poll in user.polls if poll.end_at < datetime.now()])
>>>>>>> feature/routes
