from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Use the provided database credentials and endpoint
user = 'admin'
password = 'fwelmlskfsdf'  # Use the correct password here
endpoint = 'tek-database-carrerwebsite.cbgq48ko0bmz.us-east-1.rds.amazonaws.com'
database_name = 'ghimireDB'

# Assuming the SSL certificate path is updated and correct
ssl_args = {'ssl': {'ca': './global-bundle.pem'}}
#ssl_args = {'ssl': {'ca': '/Macintosh HD/Users/tekghimire/Downloads/global-bundle.pem'}}

# Construct your connection string
connection_string = f"mysql+pymysql://{user}:{password}@{endpoint}/{database_name}"

# Create the engine with the SSL arguments hjsfadj 
#&&dsjfkjsdf 
engine = create_engine(connection_string, connect_args=ssl_args)

def loadjobfromDB():
  with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM jobs"))
    jobs = []
    for row in result:
      jobs.append(row)
    print(type(jobs))
    return jobs





