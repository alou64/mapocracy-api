from models.User import User
from flask import Flask, request, jsonify, make_response
from database import db


def index():
  q = User.query.all()
  return jsonify(q)

def get_user_by_id(user_id):
  q = User.query.filter_by(id=user_id).first()
  return jsonify(q)

def create_user():
  content = request.json
  return content
