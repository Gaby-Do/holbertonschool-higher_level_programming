#!/usr/bin/python3
"""
7. All states via SQLAlchemy
lists all State objects from the database hbtn_0e_6_usa
use the module SQLAlchemy
code not executed when imported
"""


import sys
from model_state import Base, State
import sqlalchemy as db


if __name__ == "__main__":
    engine = db.create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.
            format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    conn = engine.connect()
    metadata = db.MetaData()
    states = db.Table('states', metadata, autoload=True, autoload_with=engine)
    query = db.select([states])
    ResultProxy = conn.execute(query)
    rows = ResultProxy.fetchall()
    for row in rows:
        print("{}: {}".format(row[0], row[1]))
