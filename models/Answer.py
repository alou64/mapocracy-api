from app import db
from Poll import Poll

class Answer(db.Model):
  __tablename__ = 'answer'
  __table_args__ = {'schema': 'public'}

  id = db.Column(db.Integer, primary_key=True)
  poll_id = db.Column(db.Integer, ForeignKey(Poll.id), nullable=False)
  content = db.Column(db.Text)
