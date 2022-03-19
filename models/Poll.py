from app import db

class Poll(db.Model):
  __tablename__ = 'poll'
  __table_args__ = {'schema': 'public'}

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('public.user.id'), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('public.category.id'), nullable=False)
  name = db.Column(db.String, nullable=False)
  center = db.Column(db.String)
  restriction = db.Column(db.String)
  description = db.Column(db.Text)
  created_at = db.Column(db.DateTime, nullable=False)
  start_at = db.Column(db.DateTime, nullable=False)
  end_at = db.Column(db.DateTime, nullable=False)
  visibility = db.Column(db.Numeric)

  # list of answers for poll
  answers = db.relationship('Answer')
