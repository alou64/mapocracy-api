from app import db

class Answer(db.Model):
  __tablename__ = 'answer'
  __table_args__ = {'schema': 'public'}

  id = db.Column(db.Integer, primary_key=True)
  poll_id = db.Column(db.Integer, db.ForeignKey('public.poll.id'), nullable=False)
  content = db.Column(db.Text)

  # list of votes for answer
  votes = db.relationship('Vote')
