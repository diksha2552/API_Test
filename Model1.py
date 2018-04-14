
from sqlalchemy import create_engine as ca
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker

engine = ca("postgresql+psycopg2://postgres:disk@2552@/Company_struct")
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
session = sessionmaker(bind=engine)
session = session()


class detail(Base):
    __tablename__ = 'details_empl'
    id_1 = Column(Integer, primary_key=True)
    name = Column(String)
    doj = Column(Integer)
    parent_id = Column(Integer)

    def __init__(self, id_1, name, doj, parent_id):
        self.id_1 = id_1
        self.name = name
        self.doj = doj
        self.parent_id = parent_id


Base.metadata.create_all(engine)
