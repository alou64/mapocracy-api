from models.User import User
from flask import Flask, request, jsonify, make_response
from app import db


def index():
  q = User.query.all()
  return jsonify(q)

def get_user_by_id(user_id):
  q = User.query.filter_by(id=2).first()
  return jsonify(q)
