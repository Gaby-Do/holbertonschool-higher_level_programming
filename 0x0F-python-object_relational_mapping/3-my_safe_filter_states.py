#!/usr/bin/python3
"""
3. SQL Injection...
Connects to database,
takes in the name of a state as an argument and lists all cities of that state,
safe from MySQL injections!
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
            "SELECT * FROM states\
            WHERE name=%s\
            ORDER BY id ASC", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
