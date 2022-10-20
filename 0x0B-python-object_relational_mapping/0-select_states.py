#!/usr/bin/python3
"""
0-select_states.py module
Lists all states from the db hbtn_0e_0_usa
"""
import MySQLdb
import sys


def state_lister():
    """function that lists states"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER by id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    state_lister()
