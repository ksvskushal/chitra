from flask import Flask,request
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def homepage():

    return """
    <h1>Hello heroku</h1>
    """

@app.route('/upload', methods=['GET', 'POST'])
def add_message():
    if request.method=='GET':
      return "This is GET"

    elif request.method == 'POST':  
      content = request.get_json(silent=True)
      return json.dumps(content)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
