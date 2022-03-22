from models.VoterList import VoterList
from models.VoterListMember import VoterListMember
from flask import Flask, request, jsonify, make_response
from database import db


def index():
  return jsonify(VoterList.query.all())


def create_voter_list():
  req = request.json
  return
