from models.VoterListMember import VoterListMember
from flask import Flask, request, jsonify, make_response
from database import db


def index():
  return jsonify(VoterListMember.query.all())
