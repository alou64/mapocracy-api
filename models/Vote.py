from app import db

# many to many association object
class Vote(db.Model):
  __tablename__ = 'vote'
  __table_args__ = {'schema': 'public'}

  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
  poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'), primary_key=True)
  answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)
  voted_at = db.Column(db.DateTime, nullable=False)
