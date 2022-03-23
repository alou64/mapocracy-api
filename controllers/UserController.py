from models.User import User
from models.VoterList import VoterList
from models.VoterListMember import VoterListMember
from models.Poll import Poll
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime
import json


def index():
  return jsonify(User.query.all())


def get_user_by_email(user_id):
  return jsonify(User.query.get_or_404(user_id))


def create_user():
  user_id = request.json['email']

  if User.query.get(user_id):
    return make_response('User already exists', 400)

  user = User(user_id)

  db.session.add(user)
  db.session.commit()

  return jsonify(user)


def get_user_poll(user_id):
  if request.args['time'] == 'current':
    return jsonify(
      Poll.query
        .filter(Poll.user_id == user_id, Poll.end_at >= datetime.now())
        .all()
    )

  return jsonify(
    Poll.query
    .filter(Poll.user_id == user_id, Poll.end_at < datetime.now())
    .all()
  )


def get_user_invites(user_id):
  return jsonify(
    Poll.query
      .join(VoterList, Poll.restriction == VoterList.id)
      .join(VoterListMember, VoterList.id == VoterListMember.voter_list_id)
      .filter(VoterListMember.user_id == user_id)
      .all()
  )


def get_user_voter_list(user_id):
  return jsonify(
    {
      VoterList.id:
        [
          VoterListMember.user_id for VoterListMember in VoterList.voter_list_members
            ]
              for VoterList in VoterList.query
                .filter(VoterList.user_id == user_id)
                .all()
      }
  )


def update_user():
  req = request.json
  user = User.query.get(req['id'])

  user.first_name = req['first_name']
  user.last_name = req['last_name']
  user.longtitude = req['longtitude']
  user.latitude = req['latitude']
  user.age = req['age']
  user.gender = req['gender']
  user.ethnicity = req['ethnicity']
  user.industry = req['industry']
  user.religion = req['religion']
  user.income_range = req['income_range']
  user.education = req['education']
  user.marital_status = req['marital_status']
  user.veteran = req['veteran']

  db.session.commit()

  return jsonify(user)
