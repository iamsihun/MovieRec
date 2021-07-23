from flask import Flask, render_template, jsonify
import database

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html'), 200

@app.route('/search/<text>')
def search(text):
  try:
    results = database.search_title(text)
    print(results)
    return jsonify(results), 200
  except:
    return "", 404

@app.route('/insert', methods=['POST'])
def insert():
  title = ...
  overview = ...
  language = ...
  try:
    database.insert_movie(title, overview, language)
    return '', 200
  except:
    return '', 404

@app.route('/update/<id>/<new_title>', methods=['PUT'])
def update(id, new_title):
  try:
    database.update_movie_title(id, new_title)
    return '', 200
  except:
    return '', 404

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
  try:
    database.delete_movie(id)
    return '', 200
  except:
    return '', 404

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