from db_connection import connect_db, Error

def delete_order(order_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "DELETE FROM orders WHERE id = %s"

            cursor.execute(query, (order_id,))
            conn.commit()
            print(f"Order {order_id} was sucessfully deleted!!! Whoa!!")

        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

delete_order(22)