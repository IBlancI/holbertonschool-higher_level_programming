#!/usr/bin/python3
"""Task: List all states starting with 'N'"""
import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = connect.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    qrows = cur.fetchall()

    for row in qrows:
        print(row)
