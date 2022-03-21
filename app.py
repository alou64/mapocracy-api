from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


from database import db
from flask_migrate import Migrate
from flask_restless import APIManager


from flask_sqlalchemy import SQLAlchemy, BaseQuery

def _limit(self):
    return self.limit()

setattr(BaseQuery, '_limit', _limit)


from models.Answer import Answer
from models.Category import Category
from models.Poll import Poll
from models.User import User
from models.Vote import Vote

# from routes.answer_bp import answer_bp
# from routes.category_bp import category_bp
# from routes.poll_bp import poll_bp
# from routes.user_bp import user_bp
# from routes.vote_bp import vote_bp

app = Flask(__name__)
app.config.from_object('config')

db.app = app
db.init_app(app)
migrate = Migrate(app, db)

manager = APIManager(app, flask_sqlalchemy_db=db)

answer_blueprint = manager.create_api(Answer, methods=['GET', 'POST'], allow_functions=True)
category_blueprint = manager.create_api(Category, methods=['GET', 'POST'], allow_functions=True)
poll_blueprint = manager.create_api(Poll, methods=['GET', 'POST'], allow_functions=True)
user_blueprint = manager.create_api(User, methods=['GET', 'POST'], allow_functions=True)
vote_blueprint = manager.create_api(Vote, methods=['GET', 'POST'], allow_functions=True)




# app.register_blueprint(answer_bp, url_prefix='/answer')
# app.register_blueprint(category_bp, url_prefix='/category')
# app.register_blueprint(poll_bp, url_prefix='/poll')
# app.register_blueprint(user_bp, url_prefix='/user')
# app.register_blueprint(vote_bp, url_prefix='/vote')

@app.route('/', methods=['GET'])
def index():
  return {'test': 'test'}

if __name__ == '__main__':
  app.run()


# eval/answer?functions=[{"name":"count","field":"id"}]
# answer?filter[objects]=[{"limit":6,"name":"content","op":"==","val":"EDC"}]
# answer?filter[content]="EDC"
# answer?q={"single": false, "filters":[{"name":"content","op":"eq","val":"EDC"}]}
# api/eval/answer?functions=[{"name":"count","field":"id"},{"name":"avg","field":"age"}]
