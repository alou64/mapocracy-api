from models.Category import Category
from flask import Flask, request, jsonify, make_response
from database import db
# from config import Session
import json


def index():
  q = Category.query.all()
  return jsonify(q)

def create_category():
  category = Category(request.json['name'])
  db.session.add(category)
  db.session.commit()
  return jsonify(category)
