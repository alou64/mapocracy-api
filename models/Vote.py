from app import db

class Vote(db.Model):
  __tablename__ = 'vote'
  __table_args__ = {'schema': 'public'}

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, nullable=False)
  answer_id = db.Column(db.Integer, nullable=False)
  voted_at = db.Column(db.DateTime, nullable=False)
