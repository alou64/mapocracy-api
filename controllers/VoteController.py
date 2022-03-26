from models.Vote import Vote
from models.User import User
from models.Poll import Poll
from models.VoterList import VoterList
from models.VoterListPoll import VoterListPoll
from models.VoterListMember import VoterListMember
from flask import Flask, request, jsonify, make_response
from database import db
from datetime import datetime
from geopy.distance import geodesic
from auth0_decorators import *


@requires_auth
def index():
  if request.method == 'POST':
    req = request.json
    poll = Poll.query.get(req['poll_id'])
    user = User.query.get(req['user_id'])

    # check voter list
    if poll.restriction:
      q = VoterListMember.query.join(VoterList, VoterListMember.voter_list_id == VoterList.id).join(VoterListPoll, VoterList.id == VoterListPoll.voter_list_id).filter(VoterListPoll.poll_id == poll.id, VoterListMember.user_id == user.id).all()
      if not q:
        return make_response('User not authorized to vote in this poll', 403)

    # check location
    if geodesic((user.latitude, user.longitude), (poll.latitude, poll.longitude)).km > poll.radius:
      return('Cannot vote in this location', 403)

    # check if user already voted
    if not Vote.query.filter_by(user_id=user.id, poll_id=poll.id).first():
      vote = Vote(user.id, poll.id, req['answer_id'])
      db.session.add(vote)
      db.session.commit()
      return jsonify(vote)

    return make_response('Cannot vote twice', 403)

  return jsonify(Vote.query.all())


def delete_vote(user_id, poll_id):
  Vote.query.filter(Vote.user_id == user_id, Vote.poll_id == poll_id).delete()
  db.session.commit()

  return make_response('Success', 200)
