#!/usr/bin/python3
"""
5. All cities by state
Connects to database,
takes in the name of a state as an argument,
lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities\
        JOIN states ON cities.state_id=states.id\
        WHERE states.name=%s\
        ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    if len(rows) > 0:
        for i in range(len(rows)):
            if i < len(rows) - 1:
                print(rows[i][0], end=', ')
            else:
                print(rows[i][0])
    else:
        print()
    cur.close()
    db.close()
