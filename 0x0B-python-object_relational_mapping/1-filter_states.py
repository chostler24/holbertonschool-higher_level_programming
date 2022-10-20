#!/usr/bin/python3
"""
1-filter_states.py module
Lists all states starting with N from db hbtn_0e_0_usa
"""
import MySQLdb
import sys


def state_lister_n():
    """lists N states"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    state_lister_n()
