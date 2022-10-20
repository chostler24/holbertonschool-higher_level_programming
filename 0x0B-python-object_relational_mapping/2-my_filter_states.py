#!/usr/bin/python3
"""
2-my_filter_states.py module
Takes argument and displays values where argument is matched
"""
import MySQLdb
import sys


def state_filter():
    """displays values in states where name is matched"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur=db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}' \
        ORDER BY id;".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    state_filter()
