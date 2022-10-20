#!/usr/bin/python3
"""
3-my_safe_filter_states.py
Displays values where argument is matched
"""
import MySQLdb
import sys


def safe_state_filter():
    """function that displays values where name matches argument"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %(state)s \
        ORDER BY id;", {'state': sys.argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    safe_state_filter()
