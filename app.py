
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():

    return """
    <h1>Hello heroku</h1>
    """

@app.route('/upload', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json(silent=True)
    
    return """
    <h1>{cont}</h1>
    """.format(cont=content)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
