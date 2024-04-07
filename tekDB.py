from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os


# Assuming the SSL certificate path is updated and correct
ssl_args = {'ssl': {'ca': './global-bundle.pem'}}


# Construct your connection string
connection_string = os.environ['DB_conn_string']


# Create the engine with the SSL arguments hjsf
engine = create_engine(connection_string, connect_args=ssl_args)

def loadjobfromDB():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result:
      jobs.append(row)
    print(type(jobs))
    return jobs





def load_job_fromDB(id):
  with engine.connect() as conn:
      result = conn.execute(
          text("SELECT * FROM jobs WHERE id = :val"),
          {'val': id}
      )
      rows = result.all()
      print("row type", type(rows))

      if not rows:
          return None
      else:
          first_row = rows[0]
          # Use the _asdict() method to convert RowProxy to a dict
          return first_row._asdict()




    