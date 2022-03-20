from database import db
from dataclasses import dataclass

@dataclass
class Category(db.Model):
  __tablename__ = 'category'
  __table_args__ = {'schema': 'public'}

  id: int
  name: str

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)

  # list of votes for answer
  polls = db.relationship('Poll', cascade='all, delete')

  def __init__(self, name):
    self.name = name
