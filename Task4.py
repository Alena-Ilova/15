!pip install ipython-sql

%load_ext sql

!env | grep POST


import os
USER = os.environ['POSTGRESQL_USER']
PASSWORD = os.environ['POSTGRESQL_PASSWORD']
POSTGRESQL_HOST = '10.129.0.25'
DBASE_NAME = 'demo'


CONNECT_DATA = 'postgresql://{}:{}@{}/{}'.format(
    USER,
    PASSWORD,
    POSTGRESQL_HOST,
    DBASE_NAME
)

%%sql $CONNECT_DATA
    SELECT * FROM pg_database
    
%sql SELECT tablename AS table FROM pg_tables WHERE tablename !~ '^(pg_|sql_)'

result = %sql SELECT * FROM tickets * WHERE ticket_no = '0005432312164'

display(result)

print(result.keys)

result[0][0]

%%sql 
SELECT * 
FROM ticket_flights 
WHERE ticket_no = '0005432312164';