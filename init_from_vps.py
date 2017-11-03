from flask import Flask,request
from flaskext.mysql import MySQL
from datetime import datetime
import json

mysql= MySQL()

app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

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
      content = ['a','ab','abc','abcd','abcde']
      return ','.join(content)

@app.route("/doc_check", methods=['GET', 'POST'])
def Authenticate():
    req = request.get_json(silent=True, force=True)
    doc = req.get("doctor")

    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * FROM doc_data WHERE doctor=%s", (doc))
    data = cursor.fetchone()
    if data is None:
      return "Enter Correct Doctor Name"
    else:
      return json.dumps(data)

@app.route("/insert_doc_data",  methods=['GET', 'POST'])
def insert_doc_data():
    req = request.get_json(silent=True, force=True)

    uid = int(req.get("id"))
    date_time = req.get("date_time")
    doctor = req.get("doctor")
    disease = req.get("disease")
    pres_link = req.get("pres_link")
    report_link = req.get("report_link")

    query = "INSERT INTO books (title,isbn) VALUES ('%d','%s','%s','%s','%s','%s')"
    args = (uid, date_time, doctor, disease, pres_link, report_link)

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute(query, args)
    conn.commit()
    data = cursor.fetchall()

    return json.dumps(data)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
