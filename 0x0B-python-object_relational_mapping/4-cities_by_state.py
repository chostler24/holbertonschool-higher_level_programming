#!/usr/bin/python3
"""
4-cities_by_state.py
Lists all cities from db
"""
import MySQLdb
import sys


def city_lister():
    """function that lists cities"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    city_lister()
