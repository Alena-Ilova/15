import os
import json
import psycopg2
from psycopg2.extras import DictCursor

POSTGRESQL_HOST = '10.129.0.25'

!env | grep POST

conn = psycopg2.connect(
    dbname='demo', 
    user=os.environ['POSTGRESQL_USER'],
    password=os.environ['POSTGRESQL_PASSWORD'], 
    host=POSTGRESQL_HOST
)
cur = conn.cursor()

query = 'SELECT * FROM seats LIMIT 5'

cur.execute(query)
records = cur.fetchall()
cur.close()
conn.close()

records

with psycopg2.connect(
    dbname='demo', 
    user=os.environ['POSTGRESQL_USER'],
    password=os.environ['POSTGRESQL_PASSWORD'], 
    host=POSTGRESQL_HOST
) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM seats LIMIT 5')
        records = cur.fetchall()


records
