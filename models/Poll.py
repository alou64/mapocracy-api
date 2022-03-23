from database import db
from datetime import datetime
from dataclasses import dataclass
from sqlalchemy.orm import joinedload

@dataclass
class Poll(db.Model):
  __tablename__ = 'poll'
  __table_args__ = {'schema': 'public'}

  id: int
  user_id: str
  category_id: int
  name: str
  center: str
  restriction: int
  description: str
  created_at: datetime
  start_at: datetime
  end_at: datetime
  visibility: str

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.String, db.ForeignKey('public.user.id', ondelete='CASCADE'), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('public.category.id', ondelete='CASCADE'), nullable=False)
  name = db.Column(db.String, nullable=False)
  center = db.Column(db.String)
  restriction = db.Column(db.Integer, db.ForeignKey('public.voter_list.id', ondelete='CASCADE'))
  description = db.Column(db.Text)
  created_at = db.Column(db.DateTime, nullable=False)
  start_at = db.Column(db.DateTime, nullable=False)
  end_at = db.Column(db.DateTime, nullable=False)
  visibility = db.Column(db.String)

  # list of answers for poll
  answers = db.relationship('Answer', cascade='all, delete', lazy='joined')

  def __init__(self, user_id, category_id, name, center, restriction, description, start_at, end_at, visibility):
    self.user_id = user_id
    self.category_id = int(category_id)
    self.name = name
    self.center = center
    self.restriction = None if not restriction else restriction
    self.description = description
    self.created_at = datetime.now()
    self.start_at = datetime.strptime(start_at, '%Y-%m-%d')
    self.end_at = datetime.strptime(end_at, '%Y-%m-%d')
    self.visibility = visibility
