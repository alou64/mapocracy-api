from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

from database import db

# from app import app, db
from flask_migrate import Migrate

from routes.answer_bp import answer_bp
from routes.category_bp import category_bp
from routes.poll_bp import poll_bp
from routes.user_bp import user_bp
from routes.vote_bp import vote_bp
app = Flask(__name__)
app.config.from_object('config')

# db = SQLAlchemy(app)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(answer_bp, url_prefix='/answer')
app.register_blueprint(category_bp, url_prefix='/category')
app.register_blueprint(poll_bp, url_prefix='/poll')
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(vote_bp, url_prefix='/vote')

@app.route('/', methods=['GET'])
def index():
  return {'test': 'test'}

if __name__ == '__main__':
  app.run()
