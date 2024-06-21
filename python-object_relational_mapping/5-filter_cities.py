#!/usr/bin/python3
"""Task: List all cities of a state"""
import MySQLdb
import sys

if __name__ == "__main__":
    connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    search = sys.argv[4].split(';')[0].strip("'")
    cur = connect.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name=%s \
                ORDER BY cities.id ASC", (search,)
                )
    qrows = cur.fetchall()
    cities = []
    for row in qrows:
        cities.append("{}".format(row[0]))
    print(", ".join(cities))
