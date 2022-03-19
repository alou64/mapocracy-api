import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

user = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']
SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@mapocracy-db.postgres.database.azure.com/postgres?sslmode=require'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# engine = create_engine(f'postgresql://{user}:{password}@mapocracy-db.postgres.database.azure.com/postgres?sslmode=require')
# Session = sessionmaker(bind=engine)
