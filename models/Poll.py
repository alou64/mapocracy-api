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
  category: str
  name: str
  region: str
  restriction: int
  description: str
  created_at: datetime
  start_at: datetime
  end_at: datetime
  visibility: str

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.String, db.ForeignKey('public.user.id', ondelete='CASCADE'), nullable=False)
  category = db.Column(db.String)
  name = db.Column(db.String, nullable=False)
  region = db.Column(db.String)
  restriction = db.Column(db.Integer, db.ForeignKey('public.voter_list.id', ondelete='CASCADE'))
  description = db.Column(db.Text)
  created_at = db.Column(db.DateTime, nullable=False)
  start_at = db.Column(db.DateTime, nullable=False)
  end_at = db.Column(db.DateTime, nullable=False)
  visibility = db.Column(db.String)

  # list of answers for poll
  answers = db.relationship('Answer', cascade='all, delete', lazy='joined')

  def __init__(self, user_id, category, name, region, restriction, description, start_at, end_at, visibility):
    self.user_id = user_id
    self.category = category
    self.name = name
    self.region = region
    self.restriction = None if not restriction else restriction
    self.description = description
    self.created_at = datetime.now()
    self.start_at = datetime.strptime(start_at, '%Y-%m-%d')
    self.end_at = datetime.strptime(end_at, '%Y-%m-%d')
    self.visibility = visibility
  # def __init__(self):
  #     self.start_at = datetime.strptime(self.start_at, '%Y-%m-%d')
  #     self.end_at = datetime.strptime(self.end_at, '%Y-%m-%d')
