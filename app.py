from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
  poo = {
    'poo': 'poop',
    'poo2': 'poop2'
  }
  return jsonify(poo)


if __name__ == '__main__':
   app.run()
