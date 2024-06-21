#!/usr/bin/python3
"""Task: List all states that contain the letter 'a'"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    connect = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=connect)
    session = Session()
    States = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()

    for state in States:
        print("{}: {}".format(state.id, state.name))
