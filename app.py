from flask import Flask, request, jsonify, make_response
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
  conn = psycopg2.connect(
    host='mapocracy-db.postgres.database.azure.com',
    database='mapocracy_db',
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD']
    )
  return conn

conn = get_db_connection()
cur = conn.cursor()


@app.route('/')
@app.route('/<int:num>/<int:num2>')
def index(num=None, num2=None):
  if not (num and num2):
    poo = jsonify(poo='poo', poop='poop')
    return make_response(poo, 200)
  elif not num:
    return
  return jsonify(poo=num+num2)

@app.route('/poo/')
def poo():
  cur.execute('SELECT * FROM mapocracy.category;')
  poo = cur.fetchall()
  return jsonify(poo=poo)


if __name__ == '__main__':
   app.run()
