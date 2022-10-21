#!/usr/bin/python3
"""
8-model_state_fetch_first.py module
lists all state objects from db
"""
import sys
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session1 = session()
    LA = State(name="Louisiana")
    session1.add(LA)
    session1.commit()
    print(LA.id)
    session1.close()
