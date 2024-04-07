from flask import Flask, jsonify, render_template
from tekDB import loadjobfromDB, load_job_fromDB

app = Flask(__name__)

@app.route('/')
def hello_world():
  jobs = loadjobfromDB()
  return render_template('home.html', jobs=jobs, date='03-31-2024')


@app.route('/api/jobs')
def list_jobs():
  return jsonify()

@app.route('/jobs/<id>')
def show_job(id):
  jobs_id = load_job_fromDB(id)
  if not jobs_id:
    return "Not Found", 404
  return render_template('jobpage.html', job=jobs_id)
  


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

