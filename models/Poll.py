from app import db
from datetime import datetime

class Poll(db.Model):
  __tablename__ = 'poll'
  __table_args__ = {'schema': 'public'}

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('public.user.id'), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('public.category.id'), nullable=False)
  name = db.Column(db.String, nullable=False)
  # center = db.Column(db.String)
  # restriction = db.Column(db.String)
  description = db.Column(db.Text)
  created_at = db.Column(db.DateTime, nullable=False)
  start_at = db.Column(db.DateTime, nullable=False)
  end_at = db.Column(db.DateTime, nullable=False)
  # visibility = db.Column(db.Numeric)

  # list of answers for poll
  answers = db.relationship('Answer', cascade='all, delete')

  def __init__(self, user_id, category_id, name, description, start_at, end_at):
    self.user_id = user_id
    self.category_id = category_id
    self.name = name
    self.description = description
    self.created_at = datetime.now()
    self.start_at = start_at
    self.end_at = end_at
