from flask import Flask, jsonify, render_template

app = Flask(__name__)
JOBS =[{
'id': 1,
'title': 'Data Analyst - Only Cloud',
'location': 'Bengaluru, India',
'salary': 'Rs. 10,00,000'
},
{
'id': 2,
'title': 'Data Scientist',
'location':'Delhi, India',
'salary': 'Rs. 15,00,000'
},
{
'id': 3,
'title': 'Frontend Engineer',
'location': 'Remote',
'salary': 'Rs. 12,00,000'
},
       {
       'id': 4,
       'title': 'AWS Engineer',
       'location': 'Remote',
       'salary': 'Rs. 12,00,000'
       }

]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs = JOBS, date = '03-31-2024')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)