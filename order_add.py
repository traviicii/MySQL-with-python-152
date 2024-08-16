from db_connection import connect_db, Error

def add_order(date, customer_id):
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            new_order = (date, customer_id)

            query = "INSERT INTO orders (order_date, customer_id) VALUES (%s, %s)"

            cursor.execute(query, new_order)
            conn.commit()
            print("Order sucessfully placed!!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

add_order("2024-06-27", 11)