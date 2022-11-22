import os

from dotenv import load_dotenv
config_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file = config_file + '\config-dev.py'
load_dotenv(config_file)

import mysql.connector

conn = mysql.connector.connect(
  user=os.environ['DB_USERNAME'],
  password=os.environ['DB_PASSWORD'],
  host=os.environ['DB_CONN_HOSTNAME'],
  port=os.environ['DB_CONN_PORT'],
  database=os.environ['DB_NAME']
)

cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM post;')
res = cursor.fetchone()[0]
print(type(res))
conn.close()
