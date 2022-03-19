from app import db

class User(db.Model):
  __tablename__ = 'user'
  __table_args__ = {'schema': 'public'}

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False, unique=True)
  auth0_id = db.Column(db.String, nullable=False, unique=True)
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

  @property
  def serialize(self):
    return {
      'id': self.id,
      'first_name': self.first_name,
      'last_name': self.last_name,
      'email': self.email
    }
