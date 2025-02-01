import mysql.connector
from mysql.connector import Error

def connect_to_mysql(host, database, user, password):
    """ Connect to MySQL database and execute a simple query """
    connection = None  # Initialize the connection variable outside the try block
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database")

            # Fetch and print MySQL server info
            db_info = connection.get_server_info()
            print(f"MySQL Server version: {db_info}")

            # Create a cursor object to interact with the database
            cursor = connection.cursor()

            # Execute a simple query
            cursor.execute("SELECT * FROM `orders`;")
            records = cursor.fetchall()  # Fetch all records from the query
            print("Displaying the first few rows from the 'orders' table:")
            for row in records[:5]:  # Display only the first 5 rows for brevity
                print(row)

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        # Ensure the connection is properly closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Replace the following with your MySQL connection details
connect_to_mysql(
    host="34.171.34.164",
    database="ecommerce",   # Your MySQL database name
    user="root",            # Your MySQL user name
    password="hani"         # Your MySQL password
)
