from models.Category import Category
from flask import Flask, request, jsonify, make_response
from app import db
# from config import Session
import json


def index():
  q = Category.query.all()
  return jsonify(q)

# def index():
#   session = Session()
#   q = session.query(Category).all()
#   res = [json.dumps(x) for x in q]
#   return jsonify(res)
