#--kind python:default
#--web true
#--param POSTGRES_URL $POSTGRES_URL

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass

class Message(Base):
    __tablename__ = "tbl_e2"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(100))

    person_id: Mapped[int] = mapped_column(ForeignKey("tbl_pers.id"))
    person: Mapped["Person"] = relationship(back_populates="texts")

class Person(Base):
    __tablename__ = "tbl_pers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    texts: Mapped[List[Message]] =relationship(back_populates="person", cascade="all, delete-orphan")

def get_engine(p_db_uri):
    db_uri=p_db_uri.replace('postgresql:','postgresql+psycopg:')
    engine = create_engine(db_uri, echo=True)
    Base.metadata.create_all(engine)
    return engine


def main(args):
    db_uri=args.get("POSTGRES_URL").replace('postgresql:','postgresql+psycopg:')
    engine = get_engine(db_uri)

    from sqlalchemy.orm import Session

    with Session(engine) as session:
        #...
        session.commit()


    return {'body':'ok pg1'}


def example_start(args):
    db_uri=args.get("POSTGRES_URL").replace('postgresql:','postgresql+psycopg:')
    engine = create_engine(db_uri, echo=True)
    Base.metadata.create_all(engine)


    from sqlalchemy.orm import Session

    with Session(engine) as session:
        spongebob = Person(
            name="spongebob",
            texts=[Message(text="spneg balbla")],
        )
        sandy = Person(
            name="sandy",
            texts=[
                Message(text="sandy txt1"),
                Message(text="sandy 2222"),
            ],
        )
        patrick = Person(name="patrick")

        session.add_all([spongebob, sandy, patrick])

        session.commit()


    return {'body':'ok pg1'}


from sqlalchemy.orm import Session
from sqlalchemy import select

def selectPerson(engine):
    session = Session(engine)
    qry = select(Person)#.where(Person.name.in_(["spongebob", "sandy"]))
    for p in session.scalars(qry):
        print(p)      
    return {'body':'ok pg1'}

def select_generic(engine, s_type):
    session = Session(engine)
    qry = select(s_type)#.where(Person.name.in_(["spongebob", "sandy"]))
    for p in session.scalars(qry):
        print(p)
    return {'body':'ok pg1'}


def selectPerson2(engine):
    session = Session(engine)
    persons=Person.query.all()

    for p in persons:
        print(p.name)
        
    return persons


def select_generic2(engine, s_type):
    session = Session(engine)
    list=s_type.query.all()
    return list