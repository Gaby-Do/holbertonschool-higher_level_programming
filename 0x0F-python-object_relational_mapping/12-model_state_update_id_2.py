#!/usr/bin/python3
"""
10. Get a state
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
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
    state = session.query(State).filter(State.id == 2)\
        .update({State.name: "New Mexico"})
    session.commit()
    session.close()
