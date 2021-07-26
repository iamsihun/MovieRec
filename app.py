from flask import Flask, render_template, jsonify
import database

app = Flask(__name__)

# Loads Up Home Page:
@app.route('/')
def index():
  return render_template('index.html'), 200

# Creates a new user with the given username if the user doesn't already exists:
@app.route('/createUser/<username>', methods=['POST'])
def createUser(username):
  try:
    if database.createUser(username) is True:
      return "User successfully created!", 200
    else:
      return "User already exists.", 400
  except:
    return "Could not create user.", 404

# Deletes the given user if the user exists:
@app.route('/deleteUser/<username>', methods=['DELETE'])
def deleteUser(username):
  try:
    if database.deleteUser(username):
      return "User successfully deleted!", 200
    else:
      return "User doesn't exist", 400  
  except:
    return "Could not delete user.", 404

# Returns the movie list of the given user. Returns None if the user doesn't exist.
@app.route('/getMovieList/<username>')
def getMovieList(username):
  try:
    movieList = database.getMovieList(username)
    if movieList is None:
      return jsonify({}), 400
    else:
      return jsonify(movieList), 200
  except:
    return jsonify({}), 404

# Adds movie to given user's movie list if the user exists:
@app.route('/addMovie/<username>/<movieID>', methods=['PUT'])
def addMovie(username, movieID):
  try:
    if database.addMovie(username, movieID):
      return "Movie successfully added!", 200
    else:
      return "User doesn't exist.", 400
  except:
    return "Could not add movie.", 404

# Deletes the given movie from the given user's movie list if the user exists:
@app.route('/deleteMovie/<username>/<movieID>', methods=['DELETE'])
def deleteMovie(username, movieID):
  try:
    if database.deleteMovie(username, movieID):
      return "Movie successfully deleted!", 200
    else:
      return "User doesn't exist.", 400
  except:
    return "Could not delete movie.", 404

# Searches for all movies whose title has the given query as a substring:
@app.route('/search/<text>')
def search(text):
  try:
    results = database.search_title(text)
    return jsonify(results), 200
  except:
    return jsonify({}), 404

# Performs Advanced Query #1:
@app.route('/aq1')
def aq1():
  try:
    results = database.advanced_query_1()
    return jsonify(results), 200
  except:
    return jsonify({}), 404

# Performs Advanced Query #2:
@app.route('/aq2')
def aq2():
  try:
    results = database.advanced_query_2()
    return jsonify(results), 200
  except:
    return jsonify({}), 404

if __name__ == '__main__':
  app.run(debug=True)