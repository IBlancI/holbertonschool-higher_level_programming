#!/usr/bin/python3
import MySQLdb
import sys

def main():
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        return

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        
        # Create a cursor object using cursor() method
        cursor = conn.cursor()

        # Execute SQL query
        cursor.execute("SELECT * FROM states ORDER BY id")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"MySQL Error {e}")
    finally:
        # Close cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
