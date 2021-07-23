from flask import Flask, render_template, jsonify
import database



app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html'), 200

@app.route('/search/<text>')
def search(text):
   results = database.search_title(text)
   return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)