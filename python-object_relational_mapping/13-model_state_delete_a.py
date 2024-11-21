#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter 'a' from the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # create the tables
    Base.metadata.create_all(engine)

    # get the states with names containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # print the output in the expected format
    for state in states_to_delete:
        print(f"{state.id}\t{state.name}")

    # delete the states
    for state in states_to_delete:
        session.delete(state)

    # commit the changes and close the session
    session.commit()
    session.close()
