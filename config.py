import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ['DB_URI']

SQLALCHEMY_TRACK_MODIFICATIONS = False

# engine = create_engine(os.environ['DB_URI'])
# Session = sessionmaker(bind=engine)
