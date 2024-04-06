from flask import Flask, jsonify, render_template
from tekDB import loadjobfromDB

app = Flask(__name__)

@app.route('/')
def hello_world():
  jobs = loadjobfromDB()
  return render_template('home.html', jobs=jobs, date='03-31-2024')


@app.route('/api/jobs')
def list_jobs():
  return jsonify()


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
