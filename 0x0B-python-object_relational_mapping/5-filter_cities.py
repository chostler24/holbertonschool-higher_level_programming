#!/usr/bin/python3
"""
5-filter_cities.py
List cities of state given as argument
"""
import MySQLdb
import sys


def city_lister():
    """function that lists cities of given state"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
        cities.state_id = states.id WHERE states.name LIKE BINARY \
            %(k)s GROUP BY cities.name", {'k': sys.argv[4]})
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()


if __name__ == "__main__":
    city_lister()
