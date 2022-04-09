#!/usr/bin/python3
"""
1. Filter states
Connects to database hbtn_0e_0_usa
lists all states with a name starting with upper N
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
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    cur.close()
    db.close()
