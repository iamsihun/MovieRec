from flask import Flask, render_template, jsonify
import database

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html'), 200

@app.route('/login/username')
def login(username):
  ...

@app.route('/signup/username', methods=['POST'])
def signup(username):
  ...

@app.route('/search/<text>')
def search(text):
  try:
    results = database.search_title(text)
    return jsonify(results), 200
  except:
    return "", 404

@app.route('/addMovie/<movieID>', methods=['PUT'])
def addMovie(movieID):
  ...

@app.route('/deleteMovie<movieID>', methods=['DELETE'])
def deleteMovie(movieID):
  ...

@app.route('/aq1')
def aq1():
  try:
    results = database.advanced_query_1()
    return jsonify(results), 200
  except:
    return '', 404

@app.route('/aq2')
def aq2():
  try:
    results = database.advanced_query_2()
    return jsonify(results), 200
  except:
    return '', 404

if __name__ == '__main__':
  app.run(debug=True)