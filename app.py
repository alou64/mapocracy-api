from flask import Flask, request, jsonify, _request_ctx_stack
from database import db
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

from AuthError import AuthError

import json
from six.moves.urllib.request import urlopen
from functools import wraps
from jose import jwt

from routes.answer_bp import answer_bp
from routes.poll_bp import poll_bp
from routes.user_bp import user_bp
from routes.vote_bp import vote_bp
from routes.voter_list_bp import voter_list_bp
from routes.voter_list_member_bp import voter_list_member_bp


AUTH0_DOMAIN='dev-as09egye.us.auth0.com'
API_AUDIENCE = 'https://mapocracy-api.azurewebsites.net'
ALGORITHMS = ['RS256']


app = Flask(__name__)
app.config.from_object('config')
app.url_map.strict_slashes = False

cors = CORS(app, origins='http://localhost:3000')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(answer_bp, url_prefix='/answer')
app.register_blueprint(poll_bp, url_prefix='/poll')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(vote_bp, url_prefix='/vote')
app.register_blueprint(voter_list_bp, url_prefix='/voterlist')
app.register_blueprint(voter_list_member_bp, url_prefix='/voterlistmember')



@app.errorhandler(AuthError)
def handle_auth_error(ex):
  response = jsonify(ex.error)
  response.status_code = ex.status_code
  return response



@app.route('/', methods=['GET'])
def index():
  return {'test': 'test'}

if __name__ == '__main__':
  app.run()
