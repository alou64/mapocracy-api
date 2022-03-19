from models.User import User
from flask import Flask, request, jsonify, make_response
from app import db


def index():
  q = User.query.all()
  res = [x.serialize for x in q]
  return jsonify(res)
