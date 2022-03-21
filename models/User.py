from database import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
  __tablename__ = 'user'
  __table_args__ = {'schema': 'public'}

  id: str
  first_name: str
  last_name: str
  longtitude: float
  latitude: float
  age: int
  gender: str
  ethnicity: str
  industry: str
  religion: str
  income_range: str
  education: str
  marital_status: str
  veteran: bool

  id = db.Column(db.String, primary_key=True)
  first_name = db.Column(db.String)
  last_name = db.Column(db.String)
  longtitude = db.Column(db.Numeric)
  latitude = db.Column(db.Numeric)
  age = db.Column(db.Integer)
  gender = db.Column(db.String)
  ethnicity = db.Column(db.String)
  industry = db.Column(db.String)
  religion = db.Column(db.String)
  income_range = db.Column(db.String)
  education = db.Column(db.String)
  marital_status = db.Column(db.String)
  veteran = db.Column(db.Boolean)

  # list of polls for user
  polls = db.relationship(
    'Poll',
    cascade='all, delete',
    order_by='desc(Poll.id)'
  )

  def __init__(self, email):
    self.id = email

  # @property
  # def serialize(self):
  #   return {
  #     'id': self.id,
  #     'first_name': self.first_name,
  #     'last_name': self.last_name,
  #     'email': self.email
  #   }
