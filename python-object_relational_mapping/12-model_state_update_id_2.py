#!/usr/bin/python3
"""Task: Change the name of a State object from the database"""
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

    States = session.query(State).filter_by(id=2).first()
    if States is not None:
        States.name = "New Mexico"
        session.commit()
