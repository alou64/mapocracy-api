from models.Answer import Answer
from flask import Flask, request, jsonify, make_response
from database import db


def index():
  q = Answer.query.all()
  return jsonify(q)


def create_answer():
  pass
