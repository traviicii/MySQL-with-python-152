# Lecture Notes: SQL & Python

## Resources

[MySQL Connector Guide + Documentation](https://dev.mysql.com/doc/connector-python/en/)

## 1. Install and Establish Connection

### Install MySQL Connector

```bash
pip install mysql-connector-python
```

### Establich and Test connection
```python
import mysql.connector #importing the mysql connector library that we pip installed
from mysql.connector import Error # Allows us to handle MySQL errors

# Database connection Parameters
db_name = "ecom" #specifying
user = "root" #selecting our user
password = "" #grant access to db
host = "127.0.0.1" #setting host localhost == 127.0.0.1

#Establishing Connection
try:
    conn = mysql.connector.connect(
        database=db_name,
        user=user,
        password=password,
        host=host
    )

    cursor = conn.cursor() #Creating a cursor to act as the middle man between python and mysql

    query = "SELECT * FROM Customer;"

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    if conn.is_connected():
        print("Connected to MySQL Database")

except Error as e:
    print(f"Error: {e}")
finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close() #ALWAYS MAKE SURE YOU CLOSE YOUR CONNECTION WHEN DONE
        print("MySQL Connection Closed")
```

#### Now create a reusable connection function

**db_connection.py**
```python
import mysql.connector #importing the mysql connector library that we pip installed
from mysql.connector import Error

def connect_db():
    db_name = "ecomm_db" #specifying
    user = "root" #selecting our user
    password = "BAC146" #grant access to db
    host = "127.0.0.1" #setting host localhost == 127.0.0.1

    #Establishing Connection
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )

        if conn.is_connected():
            print("Connected to MySQL Database")
            return conn # Returning our connection to be used elsewhere

    except Error as e:
        print(f"Error: {e}")
        return None
   
```

## 2. Develop CRUD Functionality

### For Customer Table

#### Fetch All and Fetch by ID (Retrieve)

**customer_fetch.py**
```python
from db_connection import connect_db, Error

def fetch_all_orders():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all orders
            query = "SELECT * FROM Orders;"

            #Execute query
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()


def fetch_order(customer_id, order_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            #Select all orders
            query = "SELECT * FROM Orders WHERE customer_id = %s AND id = %s;"

            #Execute query
            cursor.execute(query, (customer_id, order_id))

            print(cursor.fetchall())
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() #DONT FORGET TO CLOSE THESE UP
            conn.close()
```

#### Add Customer (Create)

**customer_add.py**
```python
from db_connection import connect_db, Error
from customer_fetch import fetch_all_customers

def add_customer():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("What is your name? ").title()
            email = input("What is your email? ")
            phone = input("Phone: ")

            new_customer = (name, email, phone)

            query = "INSERT INTO Customer (customer_name, email, phone) VALUES (%s, %s, %s)"

            cursor.execute(query, new_customer)
            conn.commit() #fully commits the changes
            print(f"New Customer {name} added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
```

#### Update Customer (Update)

```python
from db_connection import connect_db, Error
from customer_fetch import fetch_all_customers

def update_customer_email(new_email, customer_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            email_update = (new_email, customer_id)

            query = "UPDATE Customer SET email = %s WHERE id = %s;" #Update query 

            cursor.execute(query, email_update)
            conn.commit() #Make sure to commit on update
            print("Successfully Changed Email!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def update_customer_phone(new_phone, customer_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            phone_update = (new_phone, customer_id)

            query = "UPDATE Customer SET phone = %s WHERE id = %s;" #Update query 

            cursor.execute(query, phone_update)
            conn.commit() #Make sure to commit on update
            print("Successfully Changed Phone!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def update_customer_name(new_name, customer_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name_update = (new_name, customer_id)

            query = "UPDATE Customer SET customer_name = %s WHERE id = %s;" #Update query 

            cursor.execute(query, name_update)
            conn.commit() #Make sure to commit on update
            print("Successfully Changed name!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
```
