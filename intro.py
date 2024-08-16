# We need to install the mysql connector package for python
# use pip install

import mysql.connector # importing the mysql connector that we just pip installed
from mysql.connector import Error # Importing the mysql Error package to deal with specific errors

# To establish a connection to our database, we're going to need some parameters first
db_name = 'ecom'
user = 'root' # select the specific database user
password = ''
host = '127.0.0.1' # localhost = 127.0.0.1

# Establish our connection
try:
    conn = mysql.connector.connect(
        database = db_name,
        user = user,
        password = password,
        host = host
    )

    if conn.is_connected():
        print("Connection to MySQL database successful!")

    cursor = conn.cursor() # creating a cursor to act as a middle man between Python and MySQL

    query = 'SELECT * FROM customer;'

    cursor.execute(query) # passing our query over to our cursor and executing it

    for row in cursor.fetchall():
        print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close() # ALWAYS BE SURE TO CLOSE YOUR CONNECTIONS WHEN YOU'RE FINISHED WITH A QUERY
        print("Connection successfully closed!")