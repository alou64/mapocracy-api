from database import db
from app import app
from models.User import User
from models.Poll import Poll
from models.Vote import Vote
from models.VoterList import VoterList
from models.Answer import Answer
import datetime

import random
import names
import pandas as pd

AGE_MAX = 100
AGE_MIN = 18
LONGITUDE_MAX = -79.523
LONGITUDE_MIN = -79.638
LATITUDE_MAX = 43.689
LATITUDE_MIN = 43.663
POLL_RADIUS_MAX = 200
POLL_RADIUS_MIN = 100

def get_random_date(start, end, input_format, output_format):
    format = '%Y-%m-%d'
    stime = datetime.datetime.strptime(start, input_format)
    etime = datetime.datetime.strptime(end, input_format)
    td = etime - stime
    return (random.random() * td + stime).strftime(output_format)

def load_sample_values(filename):
  df = pd.read_csv(filename, delimiter=',')
  # remove nan values and return as dict
  return {df[column].name: [y for y in df[column] if not pd.isna(y)] for column in df}

def load_polls(filename):
  df = pd.read_csv(filename, delimiter=',')
  return df.groupby('Poll').apply(lambda s: s[['Answer', 'VoteWeight']].to_dict(orient='records')).to_dict()


def create_user(email):
  user = User(email)
  user.gender = random.choice(sample_values['Gender'])
  user.first_name = names.get_first_name(gender = user.gender.lower())
  user.last_name = names.get_last_name()
  user.longitude = random.uniform(LONGITUDE_MIN, LONGITUDE_MAX)
  user.latitude = random.uniform(LATITUDE_MIN, LATITUDE_MAX)
  user.age = random.randint(AGE_MIN,AGE_MAX)
  user.ethnicity = random.choice(sample_values['Ethnicity'])
  user.industry = random.choice(sample_values['Industry'])
  user.religion = random.choice(sample_values['Religion'])
  user.income_range = random.choice(sample_values['Income range'])
  user.education = random.choice(sample_values['Education'])
  user.marital_status = random.choice(sample_values['Marital status'])
  user.veteran = random.random() < 0.01

  return user

def create_poll(email, name):
  poll = Poll(
    email,
    random.choice(sample_values['Categories']),
    name,
    random.choice(sample_values['Regions']),
    False,
    None,
    get_random_date('2020-01-01','2021-01-01','%Y-%m-%d', '%Y-%m-%d'),
    get_random_date('2021-01-02','2022-01-01','%Y-%m-%d', '%Y-%m-%d'),
    random.uniform(LONGITUDE_MIN, LONGITUDE_MAX),
    random.uniform(LATITUDE_MIN, LATITUDE_MAX),
    random.randint(POLL_RADIUS_MIN, POLL_RADIUS_MAX),
    True)

  return poll



#load sample values for each property from csv file
sample_values = load_sample_values('dbsamplevalues.csv')
with app.app_context():
  db.drop_all()
  db.create_all()

  # create voters who will only vote on answers
  for v in range(0, 100):
    user = create_user(f'voter{v}@email.com')
    db.session.add(user)
    db.session.commit()

  for i in range(0, 100):
    # create user and poll owned by the user
    user = create_user(f'owner{i}@email.com')
    poll = create_poll(f'owner{i}@email.com', f'name{i}')

    # 50% chance to have a non-expired poll
    if(random.random() < 0.5):
      poll.end_at = get_random_date('2023-01-01','2024-01-01','%Y-%m-%d', '%Y-%m-%d')

    db.session.add(poll)
    db.session.add(user)
    db.session.flush()

    # create answers in range of 2-4 per poll
    num_of_answers = random.randint(2,4)
    answer_ids = []
    for j in range (0, num_of_answers):
      answer = Answer(poll.id, f'answer {j}')
      db.session.add(answer)
      db.session.flush()
      answer_ids.append(answer.id)

    # for each answer_id, generate a random weighting
    weighting = []
    for j in answer_ids:
      weighting.append(random.random())

    # generate a list of answer_ids to vote on with a random length
    answer_ids_to_vote_on = random.choices(answer_ids, weights=weighting, k=random.randint(50,100))

    # vote with random number of voters with a random weighting
    voter_num = 0
    for answer_id in answer_ids_to_vote_on:
      vote = Vote(f'voter{voter_num}@email.com', poll.id, answer_id)
      voter_num+=1
      db.session.add(vote)

  db.session.commit()