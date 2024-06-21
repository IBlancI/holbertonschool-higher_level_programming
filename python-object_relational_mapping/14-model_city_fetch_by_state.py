#!/usr/bin/python3
"""Task: Change the name of a State object from the database"""
import sys
from model_state import State, Base
from model_city import City
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
    Cities = session.query(City, State).filter(City.state_id == State.id).\
        order_by(City.id)

    for city, state in Cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
