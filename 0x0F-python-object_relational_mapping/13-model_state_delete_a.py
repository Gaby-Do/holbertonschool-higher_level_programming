#!/usr/bin/python3
"""
13. Delete states
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
use the module SQLAlchemy
code not executed when imported
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.
            format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    adios = session.query(State).filter(State.name.like('%a%'))
    for state in adios:
        session.delete(state)
    session.commit()
    session.close()
