#!/usr/bin/python3
"""Task: Print the first State object from the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    connect = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(connect, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    State = session.query(State).order_by(State.id).first()

    if State is None:
        print("Nothing")
    else:
        print("{}: {}".format(State.id, State.name))
