from db_connection import connect_db, Error

def fetch_all_orders():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # select all orders
            query = "SELECT * FROM orders;"

            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


def fetch_order(customer_id, order_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM orders WHERE customer_id = %s AND id = %s;"

            cursor.execute(query, (customer_id, order_id))

            print(cursor.fetchone())

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

fetch_order(11, 20)