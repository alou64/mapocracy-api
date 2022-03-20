from models.User import User
from flask import Flask, request, jsonify, make_response
from database import db


def index():
  q = User.query.all()
  return jsonify(q)

def get_user_by_email(email):
  q = User.query.filter_by(id=email).first()
  return jsonify(q)

def create_user():
  user = User(request.json['email'])
  db.session.add(user)
  db.session.commit()
  return jsonify(user)

def user_poll():
  pass
