from app import db

class Category(db.Model):
  __tablename__ = 'category'
  __table_args__ = {'schema': 'public'}

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)

  # list of votes for answer
  polls = db.relationship('Poll')
