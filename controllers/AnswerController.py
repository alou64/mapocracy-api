from models.Answer import Answer
from flask import Flask, request, jsonify, make_response
from database import db


def index():
  return jsonify(Answer.query.all())


def create_answer():
  pass
